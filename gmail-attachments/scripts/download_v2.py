"""Descargador v2 robusto: espera UI real, screenshot diagnóstico, multi-selector.

Uso: python download_v2.py <profile_tag> <target_dir> <thread_id>
"""
import sys, re, os
from pathlib import Path
from playwright.sync_api import sync_playwright

os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def is_real(name):
    n = (name or "").lower().strip()
    if not n: return False
    if re.match(r"^image\d+\.(png|jpe?g|gif|bmp)$", n): return False
    return True

def main():
    profile_tag, target, tid = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
    target.mkdir(parents=True, exist_ok=True)
    profile_path = Path.home() / ".notebooklm" / f"browser_profile_{profile_tag}"

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_path), channel="msedge",
            headless=False, accept_downloads=True,
            viewport={"width": 1600, "height": 1000},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.set_default_timeout(60000)
        page.goto("https://mail.google.com/mail/u/0/#inbox", wait_until="load")
        # esperar UI real (no splash)
        for attempt in range(3):
            try:
                page.wait_for_selector('div[gh="cm"]', timeout=45000)
                print(f"UI cargada (intento {attempt+1})")
                break
            except Exception:
                page.reload(wait_until="load"); page.wait_for_timeout(6000)
        page.wait_for_timeout(3000)

        # navegar al thread
        page.evaluate(f"() => {{ window.location.hash = 'inbox/{tid}'; }}")
        page.wait_for_timeout(8000)

        # EXPANDIR todos los mensajes colapsados (los adjuntos están en el 1er msg colapsado)
        # Click en cada cabecera de mensaje colapsado por el remitente
        try:
            # Gmail: mensajes colapsados tienen clase .kQ o .kv; el sender está en span[email]
            expanded = page.evaluate(r"""() => {
                let n = 0;
                // Click en cada fila de mensaje colapsado (no la abierta)
                document.querySelectorAll('span[email]').forEach(s => {
                    const row = s.closest('.kQ, .kv, .gE, [role="listitem"]');
                    if (row) { row.click(); n++; }
                });
                return n;
            }""")
            print(f"Mensajes expandidos via JS: {expanded}")
        except Exception as e:
            print("expand JS fallo:", str(e)[:80])
        page.wait_for_timeout(2500)
        # Click directo sobre el remitente kdemera por si JS no expandió
        try:
            page.locator('text=kdemera@quevepalma.com').first.click(timeout=4000)
            print("Click en kdemera para expandir")
            page.wait_for_timeout(3000)
        except Exception:
            pass

        # scroll para forzar render de adjuntos
        page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2500)

        page.screenshot(path="C:/Users/datos/qvp_thread_debug.png", full_page=True)

        # Extraer TODOS los enlaces/atributos candidatos a descarga
        cand = page.evaluate(r"""() => {
            const out = [];
            // 1. anchors con download_url o view=att o disp=
            document.querySelectorAll('a').forEach(a => {
                const h = a.href || '';
                const du = a.getAttribute('download_url') || '';
                if (h.includes('view=att') || h.includes('disp=') || du) {
                    out.push({type:'a', href:h, download_url:du, text:(a.textContent||'').trim().slice(0,60)});
                }
            });
            // 2. spans/divs con download_url (chips de Gmail)
            document.querySelectorAll('[download_url]').forEach(el => {
                out.push({type:'dl', download_url: el.getAttribute('download_url'), text:(el.textContent||'').trim().slice(0,60)});
            });
            // 3. aria-label con 'Download'/'Descargar'
            document.querySelectorAll('[aria-label]').forEach(el => {
                const al = el.getAttribute('aria-label')||'';
                if (/download|descargar/i.test(al)) {
                    out.push({type:'aria', aria: al.slice(0,80), tag: el.tagName});
                }
            });
            return out;
        }""")
        print(f"Candidatos encontrados: {len(cand)}")
        for c in cand[:25]:
            print("  ", c)

        # download_url tiene formato "mime:filename:url"
        seen = set()
        for c in cand:
            du = c.get("download_url") or ""
            if not du or du in seen: continue
            seen.add(du)
            parts = du.split(":", 2)
            if len(parts) == 3:
                mime, fname, url = parts
                if not is_real(fname):
                    print(f"  skip {fname}"); continue
                try:
                    with page.expect_download(timeout=25000) as dl:
                        page.evaluate(r"""(u)=>{const a=document.createElement('a');a.href=u;a.click();a.remove();}""", url)
                    d = dl.value
                    dest = target / (fname or d.suggested_filename)
                    d.save_as(str(dest))
                    print(f"  -> DESCARGADO: {dest}")
                    page.wait_for_timeout(1500)
                except Exception as e:
                    print(f"  fallo {fname}: {str(e)[:120]}")

        ctx.close()

if __name__ == "__main__":
    main()
