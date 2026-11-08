# -*- coding: utf-8 -*-
"""Lee la respuesta ya generada de un hilo de Perplexity con el perfil jjmobijuesa y la guarda en texto. Uso: leer_hilo_perplexity.py <url> <salida>"""
import sys, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright
URL, OUT = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(r"C:\Users\datos\.notebooklm\browser_profile_jjm", channel="msedge", headless=False,
                                               args=["--window-position=-2400,-2400", "--window-size=1200,900"])
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    pg.goto(URL, wait_until="domcontentloaded", timeout=60000)
    previo, estable = "", 0
    for _ in range(40):
        time.sleep(4)
        t = pg.evaluate("() => document.body.innerText")
        estable = estable + 1 if t == previo else 0
        previo = t
        if estable >= 3 and "En curso" not in t: break
    txt = ""
    for sel in ['div.prose', '[class*="prose"]', 'main']:
        els = pg.query_selector_all(sel)
        if els:
            txt = "\n\n".join(e.inner_text() for e in els)
            if len(txt) > 300: break
    enlaces = pg.evaluate("() => [...new Set([...document.querySelectorAll('a[href^=\"http\"]')].map(a => a.href).filter(h => !h.includes('perplexity.ai')))]")
    open(OUT, "w", encoding="utf-8").write(txt + "\n\nFUENTES\n" + "\n".join(enlaces))
    print(len(txt), "caracteres |", len(enlaces), "enlaces")
    ctx.close()
