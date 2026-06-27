"""Descarga adjuntos reales de hilos Gmail via Playwright + Edge.

Uso:
    python download.py <profile_tag> <target_dir> <thread_id_1> [<thread_id_2> ...]

profile_tag: identificador del perfil Edge persistente (ej: 'jjm' para jjmobijuesa).
            El perfil debe estar autenticado: corre login.py una vez si no.

Ejemplo:
    python download.py jjm "C:/Users/u/Downloads" 19e7442d91139802 19e7431281f179d1
"""
import sys, re, time, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright


def is_real_attachment(name):
    n = (name or "").lower().strip()
    if not n: return False
    if re.match(r"^image\d+\.(png|jpe?g|gif|bmp)$", n): return False
    if re.match(r"^att\d+\.(png|jpe?g|gif)$", n): return False
    if n in ("noname",): return False
    return True


def force_download_url(href):
    """Replace any disp= parameter with disp=attd to force download (for PDFs)."""
    new = re.sub(r"&disp=[^&]*", "", href)
    return new + ("&disp=attd" if "?" in new else "?disp=attd")


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    profile_tag = sys.argv[1]
    target = Path(sys.argv[2])
    thread_ids = sys.argv[3:]
    target.mkdir(parents=True, exist_ok=True)

    profile_path = Path.home() / ".notebooklm" / f"browser_profile_{profile_tag}"
    if not profile_path.exists():
        print(f"Perfil no existe: {profile_path}. Corre login.py primero.")
        sys.exit(1)

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_path),
            channel="msedge",
            headless=False,
            accept_downloads=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.set_default_timeout(60000)
        page.goto("https://mail.google.com/mail/u/0/#inbox", wait_until="load")
        page.wait_for_timeout(5000)
        if "accounts.google.com" in page.url:
            print(f"Sesion no activa. Corre login.py con tag '{profile_tag}'.")
            ctx.close()
            sys.exit(1)

        for tid in thread_ids:
            print(f"\n=== Thread {tid} ===")
            page.evaluate(f"() => {{ window.location.hash = 'inbox/{tid}'; }}")
            page.wait_for_timeout(7000)

            links = page.evaluate(r"""() => {
                const out = [];
                document.querySelectorAll('a[href*="view=att"]').forEach(a => {
                    out.push({href: a.href, text: (a.textContent||'').trim().slice(0,80)});
                });
                return out;
            }""")
            print(f"  enlaces view=att: {len(links)}")

            for ln in links:
                if "disp=safe" not in ln["href"] and "disp=inline" not in ln["href"] and "disp=attd" not in ln["href"]:
                    continue
                # Try original first; if it's a PDF that opens preview, retry with forced disp
                for url_variant in [ln["href"], force_download_url(ln["href"])]:
                    try:
                        with page.expect_download(timeout=20000) as dl_info:
                            page.evaluate(r"""(href) => {
                                const a = document.createElement('a');
                                a.href = href; a.target = '_self';
                                document.body.appendChild(a); a.click(); a.remove();
                            }""", url_variant)
                        d = dl_info.value
                        name = d.suggested_filename
                        if not is_real_attachment(name):
                            print(f"    descartado: {name}")
                            d.delete()
                            break
                        dest = target / name
                        d.save_as(str(dest))
                        print(f"    -> {dest}")
                        page.wait_for_timeout(1500)
                        page.evaluate(f"() => {{ window.location.hash = 'inbox/{tid}'; }}")
                        page.wait_for_timeout(3000)
                        break
                    except Exception as e:
                        if "force" in url_variant or "attd" in url_variant:
                            print(f"    fallo: {str(e)[:100]}")
                        # else: try forced version next loop iteration
        ctx.close()


if __name__ == "__main__":
    main()
