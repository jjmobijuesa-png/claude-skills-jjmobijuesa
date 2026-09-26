# -*- coding: utf-8 -*-
"""
Perplexity en modo ACTIVO vía Playwright + perfil Edge logueado (jjmobijuesa).
Uso:  python ask_perplexity_playwright.py "mi pregunta"  [slug-opcional]
Método PRIMARIO (verificado 2026-07-12): evita la extensión Claude-in-Chrome,
que bloquea la navegación a perplexity.ai. Navega directo con el perfil
persistente ya logueado.
"""
import sys, time, os
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
PROF=r"C:\Users\datos\.notebooklm\browser_profile_jjm"
OUTDIR=r"E:\vars\var 5\Perplexity-consultas"
QUERY=sys.argv[1] if len(sys.argv)>1 else "Hola"
SLUG=sys.argv[2] if len(sys.argv)>2 else "consulta"
os.makedirs(OUTDIR, exist_ok=True)
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(PROF, channel="msedge", headless=False,
        args=["--window-position=2200,2200","--window-size=1280,900","--disable-blink-features=AutomationControlled"])
    pg=ctx.pages[0] if ctx.pages else ctx.new_page(); pg.set_default_timeout(45000)
    pg.goto("https://www.perplexity.ai/", wait_until="domcontentloaded", timeout=60000); time.sleep(6)
    print("TITLE:",pg.title()[:60],"| URL:",pg.url[:60])
    box=None
    for sel in ['textarea[placeholder]','div[contenteditable="true"]','textarea']:
        try:
            el=pg.query_selector(sel)
            if el and el.is_visible(): box=el; print("input:",sel); break
        except: pass
    if not box:
        print("NO_INPUT — login/captcha; re-loguear a la vista del usuario."); pg.screenshot(path=os.path.join(os.environ.get("TEMP","."),"_pplx_state.png")); ctx.close(); sys.exit(1)
    box.click(); time.sleep(0.5); pg.keyboard.type(QUERY, delay=8); time.sleep(0.6); pg.keyboard.press("Enter")
    print("query enviada, esperando streaming...")
    last=""; stable=0; t0=time.time()
    while time.time()-t0 < 90:
        time.sleep(4)
        try: txt=pg.evaluate("() => document.body.innerText")
        except: txt=""
        stable=stable+1 if len(txt)==len(last) else 0; last=txt
        if stable>=2: break
    answer=""
    for sel in ['div.prose','[class*="prose"]','main']:
        try:
            els=pg.query_selector_all(sel)
            if els:
                answer="\n\n".join(e.inner_text() for e in els[-3:])
                if len(answer)>300: break
        except: pass
    if not answer: answer=last
    links=pg.evaluate("""() => [...document.querySelectorAll('a[href^=\"http\"]')].map(a=>a.href)""")
    cites=[]
    for l in links:
        if 'perplexity.ai' not in l and l not in cites: cites.append(l)
    cites=cites[:15]
    print("\n===== RESPUESTA =====\n"+answer[:4000]); print("\n===== FUENTES =====")
    for c in cites: print(" -",c)
    fn=os.path.join(OUTDIR, time.strftime("%Y-%m-%d")+f"_{SLUG}.md")
    with open(fn,"w",encoding="utf-8") as f:
        f.write(f"# Consulta Perplexity — {SLUG}\n- Fecha: {time.strftime('%Y-%m-%dT%H:%M')}\n- Pregunta: {QUERY}\n- URL del hilo: {pg.url}\n- Fuentes citadas:\n")
        for c in cites: f.write(f"  - {c}\n")
        f.write("\n## Respuesta\n\n"+answer)
    print("\nGUARDADO ->",fn); ctx.close()
