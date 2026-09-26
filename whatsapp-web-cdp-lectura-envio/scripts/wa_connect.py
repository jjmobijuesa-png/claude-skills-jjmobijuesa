# -*- coding: utf-8 -*-
"""
Arranque ESTABLE de WhatsApp Web (skill v1.1) — ADJUNTAR primero, nunca robar sesión.
Uso:  python wa_connect.py
Salida: estado de la sesión. NUNCA clica «Usar aquí». Deja UNA sola pestaña WA.
Reglas: §0 (regla cero) y §2 del SKILL.md.
"""
import sys, time, subprocess, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
PROF=r"C:\Users\datos\.sas-agua-wa\browser_profile"
EDGE=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def port_up():
    try:
        urllib.request.urlopen("http://127.0.0.1:9222/json/version", timeout=4); return True
    except: return False

def launch():
    # matar SOLO los Edge de este perfil (nunca el Edge principal del usuario)
    subprocess.run(["powershell","-NoProfile","-Command",
        "Get-CimInstance Win32_Process -Filter \"Name='msedge.exe'\" | "
        "? { $_.CommandLine -like '*sas-agua-wa*' } | "
        "% { Stop-Process -Id $_.ProcessId -Force -EA SilentlyContinue }"],capture_output=True)
    time.sleep(2)
    subprocess.Popen([EDGE, f"--user-data-dir={PROF}","--remote-debugging-port=9222",
        "--no-first-run","--no-default-browser-check","--window-position=2200,2200",
        "--window-size=1300,950","https://web.whatsapp.com/"])
    for _ in range(15):
        time.sleep(2)
        if port_up(): return True
    return False

def cdp_connect(p, tries=6):
    last=None
    for _ in range(tries):
        try: return p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        except Exception as e: last=e; time.sleep(3)
    raise last

def main():
    if not port_up():
        print("9222 caido -> lanzando UNA instancia limpia del perfil dedicado...")
        if not launch(): print("ERROR: no levantó 9222"); return 2
        time.sleep(4)   # dar tiempo a que el endpoint CDP quede listo, no solo el puerto
    with sync_playwright() as p:
        br=cdp_connect(p)
        ctx=br.contexts[0]
        was=[pg for pg in ctx.pages if "web.whatsapp.com" in pg.url]
        # REGLA DE UNA SOLA PESTAÑA: cerrar duplicadas WA
        if len(was)>1:
            print(f"{len(was)} pestañas WA -> cerrando duplicadas, dejo una")
            for pg in was[1:]:
                try: pg.close()
                except: pass
            was=was[:1]
        if not was:
            pg=ctx.new_page(); pg.goto("https://web.whatsapp.com/"); time.sleep(8)
        else:
            pg=was[0]; pg.bring_to_front()
        time.sleep(3)
        body=pg.evaluate("()=>document.body.innerText")
        low=body.lower()
        if pg.query_selector('#pane-side'):
            n=len(pg.query_selector_all('#pane-side [role=\"row\"]'))
            print(f"ESTADO: LOGUEADO ✓  (chats visibles: {n})  -> listo para operar")
            return 0
        if "usar aquí" in low or "use here" in low:
            print("ESTADO: «abierto en otra ventana». NO clico «Usar aquí» (regla cero).")
            print("  -> Cerrando pestañas WA duplicadas y recargando esta.")
            pg.reload(); time.sleep(6)
            if pg.query_selector('#pane-side'): print("  recuperado ✓"); return 0
            print("  ABORTA: persiste. Avisar al usuario; NO robar la sesión."); return 3
        if "escanea" in low or "qr" in low or "scan" in low:
            print("ESTADO: pide QR. El usuario debe ESCANEAR una vez (dispositivo vinculado propio).")
            return 4
        print("ESTADO: desconocido. Primeras 120 chars:", body[:120].replace(chr(10)," "))
        return 5

if __name__=="__main__":
    sys.exit(main())
