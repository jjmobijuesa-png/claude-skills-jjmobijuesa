"""Envia un correo Gmail con adjuntos via Playwright.

Uso:
    python send.py \
        --profile <tag> \
        --to "a@x.com,b@y.com" \
        --subject "Asunto..." \
        --body-file body.txt \
        [--attach path1 --attach path2 ...]

El perfil debe estar autenticado al Gmail desde el cual se envia.
"""
import argparse, time, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", required=True, help="tag del perfil Edge (~/.notebooklm/browser_profile_<tag>)")
    ap.add_argument("--to", required=True, help="destinatarios separados por coma")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--body-file", required=True)
    ap.add_argument("--attach", action="append", default=[], help="ruta de adjunto (repetible)")
    return ap.parse_args()


def main():
    args = parse_args()
    profile = Path.home() / ".notebooklm" / f"browser_profile_{args.profile}"
    body = Path(args.body_file).read_text(encoding="utf-8")
    emails = [e.strip() for e in args.to.split(",") if e.strip()]

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(profile),
            channel="msedge",
            headless=False,
            accept_downloads=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.set_default_timeout(60000)
        page.goto("https://mail.google.com/mail/u/0/#inbox", wait_until="load")
        page.wait_for_timeout(5000)

        # 1. Compose
        page.locator('div[gh="cm"]').first.click()
        page.wait_for_timeout(3500)

        # 2. To — type each email + Enter to commit chip
        page.locator(
            'input[role="combobox"][aria-label*="To"], input[role="combobox"][aria-label*="Para"]'
        ).first.click()
        page.wait_for_timeout(400)
        for em in emails:
            page.keyboard.type(em)
            page.wait_for_timeout(300)
            page.keyboard.press("Enter")
            page.wait_for_timeout(500)

        # 3. Subject — force-click to bypass any autocomplete overlay
        subj = page.locator('input[name="subjectbox"]').first
        subj.click(force=True)
        page.wait_for_timeout(500)
        subj.fill(args.subject)

        # 4. Body — Tab to focus, then JS-insert with createElement (TrustedHTML-safe)
        page.keyboard.press("Tab")
        page.wait_for_timeout(900)
        page.evaluate(r"""(text) => {
            let target = document.activeElement;
            if (!target || !target.isContentEditable) {
                for (const d of document.querySelectorAll('div[role="dialog"]')) {
                    const ed = d.querySelector('div[contenteditable="true"][aria-label]');
                    if (ed) { target = ed; break; }
                }
            }
            if (!target || !target.isContentEditable) return 'NO TARGET';
            target.focus();
            while (target.firstChild) target.removeChild(target.firstChild);
            for (const ln of text.split('\n')) {
                const div = document.createElement('div');
                if (ln.trim() === '') div.appendChild(document.createElement('br'));
                else div.appendChild(document.createTextNode(ln));
                target.appendChild(div);
            }
            target.dispatchEvent(new InputEvent('input', {bubbles: true}));
            return 'OK';
        }""", body)
        page.wait_for_timeout(1500)

        # 5. Attach (a single set_input_files supports multiple paths)
        if args.attach:
            file_inputs = page.locator('input[type="file"]')
            for idx in range(file_inputs.count() - 1, -1, -1):
                try:
                    file_inputs.nth(idx).set_input_files(args.attach)
                    break
                except Exception:
                    continue
            # Espera adaptativa por tamaño (base 15s + ~10 KB/s conservador)
            total_bytes = sum(Path(a).stat().st_size for a in args.attach if Path(a).exists())
            wait_ms = max(15000, 3000 + total_bytes // 100)
            wait_ms = min(wait_ms, 180000)  # cap a 3 min
            print(f"  Esperando upload de {len(args.attach)} adjuntos ({total_bytes/1024:.0f} KB) — {wait_ms/1000:.0f}s")
            page.wait_for_timeout(wait_ms)

        # 6. Send (try Spanish + English labels, then Ctrl+Enter)
        sent = False
        for sel in [
            'div[role="button"][aria-label^="Enviar"]',
            'div[role="button"][aria-label^="Send"]',
            'div[role="button"][data-tooltip^="Enviar"]',
            'div[role="button"][data-tooltip^="Send"]',
        ]:
            try:
                page.locator(sel).first.click(timeout=5000, force=True)
                sent = True
                break
            except Exception:
                continue
        if not sent:
            page.keyboard.press("Control+Enter")

        page.wait_for_timeout(8000)

        # 7. Verify in Sent
        page.goto("https://mail.google.com/mail/u/0/#sent", wait_until="load")
        page.wait_for_timeout(5000)
        body_txt = page.evaluate("() => document.body.innerText.slice(0, 5000)")
        if args.subject[:30] in body_txt:
            print("ENVIADO CONFIRMADO en Sent.")
        else:
            print("AVISO: no se confirma en Sent al primer barrido. Revisar manualmente.")

        time.sleep(3)
        ctx.close()


if __name__ == "__main__":
    main()
