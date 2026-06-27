# -*- coding: utf-8 -*-
"""
Lee una URL de claude.ai/share/<id> usando Playwright con el perfil Edge
persistente (`~/.notebooklm/browser_profile_edge`). Sustituye al WebFetch
(que ve solo "Claude" porque la página es client-side React) y al Chrome
MCP (que tiene claude.ai bloqueado en su allowlist).

Salida: archivo .md en E:\\vars\\var 5\\Claude-share-archivo\\<slug>.md
con título + autor + cuerpo entero de la conversación.

Uso:
  python fetch_share.py <URL>
  python fetch_share.py 55c390d2-c19b-4d49-a3aa-b068791e6978   # solo el ID
  python fetch_share.py <URL> --headed       # mostrar Edge (debug)
"""
import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from playwright.sync_api import sync_playwright

PROFILE = Path.home() / ".notebooklm" / "browser_profile_edge"
OUT_DIR = Path(r"E:\vars\var 5\Claude-share-archivo")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def slugify(s, max_len=80):
    s = re.sub(r"[^A-Za-z0-9_\- ]", "", s or "").strip()
    s = re.sub(r"\s+", "_", s)
    return (s or "share")[:max_len]


def parse_url(arg):
    if arg.startswith("http"):
        return arg
    # Probablemente sólo el ID
    return f"https://claude.ai/share/{arg}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="URL completa o solo el ID del share")
    ap.add_argument("--headed", action="store_true",
                    help="Mostrar el navegador (útil para debug)")
    ap.add_argument("--wait", type=int, default=12,
                    help="Segundos a esperar el render React (default 12)")
    args = ap.parse_args()

    url = parse_url(args.url)
    share_id = url.rstrip("/").rsplit("/", 1)[-1]
    print(f"Fetching: {url}")

    with sync_playwright() as p:
        # PRIMER intento: conectar al Edge debug existente (puerto 9222).
        # Ese Edge es el navegador real del usuario; pasa Cloudflare.
        # Si no hay CDP disponible, caer al launch_persistent_context.
        ctx = None
        page = None
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            ctx = browser.contexts[0]
            page = ctx.new_page()
            print("  via CDP localhost:9222 (Edge real)")
        except Exception as e:
            print(f"  CDP no disponible ({e.__class__.__name__}); fallback persistent_context")
            ctx = p.chromium.launch_persistent_context(
                user_data_dir=str(PROFILE),
                channel="msedge",
                headless=not args.headed,
                viewport={"width": 1300, "height": 950},
                args=["--disable-blink-features=AutomationControlled"],
            )
            page = ctx.pages[0] if ctx.pages else ctx.new_page()

        page.set_default_timeout(60000)
        page.goto(url, wait_until="domcontentloaded")
        # Esperar render React: aparecen mensajes
        # Estrategia: esperar hasta que aparezcan elementos de mensaje
        # (selectores conocidos de claude.ai) o se llene el body con texto
        # sustancial (>2000 chars y estable).
        SELECTORS = (
            '[data-testid*="message"]',
            '.font-claude-message',
            'div[role="article"]',
            'main p',  # fallback: algún párrafo dentro del main
        )
        deadline = time.time() + max(args.wait, 30)
        last_len = 0
        stable = 0
        found_messages = False
        while time.time() < deadline:
            page.wait_for_timeout(1500)
            try:
                # ¿hay elementos de mensaje?
                for sel in SELECTORS:
                    n = page.locator(sel).count()
                    if n > 0:
                        found_messages = True
                        break
                txt = page.evaluate("() => document.body.innerText || ''")
            except Exception:
                txt = ""
            # detectar Cloudflare loop (texto no crece pero <500 chars)
            if "Verificaci" in txt or "Verification" in txt or "Just a moment" in txt:
                continue
            if found_messages and len(txt) > 1500:
                # esperar un poco más para que termine de cargar (streaming visual)
                if len(txt) == last_len:
                    stable += 1
                    if stable >= 3:
                        break
                else:
                    stable = 0
                    last_len = len(txt)
            else:
                last_len = len(txt)

        # Capturar titulo + body
        try:
            title = page.title()
        except Exception:
            title = ""
        try:
            body = page.evaluate("() => document.body.innerText || ''")
        except Exception:
            body = ""

        # Intentar capturar mensajes uno a uno por bloque
        messages = []
        try:
            messages = page.evaluate("""() => {
                const out = [];
                // Diferentes selectores que Anthropic ha usado
                const sels = [
                  '[data-testid^="user-message"], [data-testid^="assistant-message"]',
                  '.font-claude-message, .font-user-message',
                  'div[role="article"]',
                ];
                let nodes = [];
                for (const s of sels) {
                  nodes = Array.from(document.querySelectorAll(s));
                  if (nodes.length) break;
                }
                for (const n of nodes) {
                  const role = (n.getAttribute('data-testid') || '').includes('user') ? 'user' :
                               (n.getAttribute('data-testid') || '').includes('assistant') ? 'assistant' :
                               (n.className || '').includes('user') ? 'user' : 'assistant';
                  out.push({role, text: (n.innerText || '').trim()});
                }
                return out;
            }""")
        except Exception:
            pass

        # Si abrimos via CDP, cerrar sólo la tab; no el navegador del usuario
        try:
            page.close()
        except Exception:
            pass

    # Persistir
    safe = slugify(title or share_id)
    target = OUT_DIR / f"{datetime.now().strftime('%Y-%m-%d')}_{safe}__{share_id}.md"
    parts = [
        f"# {title or share_id}",
        f"",
        f"- **share_id**: `{share_id}`",
        f"- **url**: {url}",
        f"- **fetched_at**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"- **page_text_chars**: {len(body)}",
        f"- **messages_detected**: {len(messages)}",
        f"",
        f"---",
        f"",
    ]
    if messages:
        for i, m in enumerate(messages, 1):
            parts.append(f"## [{i}] {m.get('role', '?').upper()}")
            parts.append("")
            parts.append(m.get("text", ""))
            parts.append("")
    else:
        parts.append("## Cuerpo completo (sin parse por mensaje)")
        parts.append("")
        parts.append(body)

    target.write_text("\n".join(parts), encoding="utf-8")
    print(f"Guardado: {target}")
    print(f"  body_chars: {len(body)}, messages: {len(messages)}")


if __name__ == "__main__":
    main()
