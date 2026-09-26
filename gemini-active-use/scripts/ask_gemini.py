# -*- coding: utf-8 -*-
"""
Gemini en modo ACTIVO via Playwright + perfil Edge persistente logueado.
Robusto v3 (2026-08-25): confirma CUENTA, puede ABRIR un hilo por titulo,
ENVIA con boton (o Enter) y confirma el submit por URL, y LEE la respuesta
del panel de conversacion (no el sidebar). Canal de archivos: G:\\Mi unidad.

Uso:  python ask_gemini.py "mensaje" [slug]
Env:
  GEM_PROFILE   = edge (mobijuesa360, DEFAULT) | jjm | fedphd
  GEM_OPEN_TITLE= subcadena del titulo de un hilo del sidebar a abrir antes de escribir
  GEM_URL       = URL de hilo a continuar (prioridad sobre OPEN_TITLE)
  GEM_THREAD    = .txt donde persistir/leer la URL del hilo (se reutiliza si existe)
  GEM_WAIT      = seg max de espera de respuesta (default 130)
  GEM_HEADLESS  = 1 headless (default 0 headed fuera de pantalla)
Salida: imprime ACCOUNT / THREAD_URL / RESPUESTA y guarda .md en Gemini-consultas.
"""
import sys, time, os
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

PROFILES = {
    "edge":   r"C:\Users\datos\.notebooklm\browser_profile_edge",
    "jjm":    r"C:\Users\datos\.notebooklm\browser_profile_jjm",
    "fedphd": r"C:\Users\datos\.notebooklm\browser_profile_fedphd",
}
PROF_KEY = os.environ.get("GEM_PROFILE","edge").strip().lower()
PROF     = PROFILES.get(PROF_KEY, PROFILES["edge"])
OUTDIR   = r"E:\vars\var 5\Gemini-consultas"
OPEN_T   = os.environ.get("GEM_OPEN_TITLE","").strip()
GEM_URL  = os.environ.get("GEM_URL","").strip()
THREAD_F = os.environ.get("GEM_THREAD","").strip()
WAIT     = int(os.environ.get("GEM_WAIT","130"))
HEADLESS = os.environ.get("GEM_HEADLESS","0")=="1"
QUERY    = sys.argv[1] if len(sys.argv)>1 else "Confirma en una linea que operas como coprocesador."
SLUG     = sys.argv[2] if len(sys.argv)>2 else "consulta"
os.makedirs(OUTDIR, exist_ok=True)

target="https://gemini.google.com/app"
if GEM_URL: target=GEM_URL
elif THREAD_F and os.path.exists(THREAD_F):
    try:
        s=open(THREAD_F,encoding="utf-8").read().strip()
        if s.startswith("http"): target=s
    except Exception: pass

def detect_accounts(pg):
    try:
        return pg.evaluate(r"""()=>{const s=new Set();
          document.querySelectorAll('[aria-label],[title],[alt]').forEach(e=>{
            const t=(e.getAttribute('aria-label')||'')+' '+(e.getAttribute('title')||'')+' '+(e.getAttribute('alt')||'');
            const m=t.match(/[a-z0-9._%+-]+@gmail\.com/ig); if(m)m.forEach(x=>s.add(x.toLowerCase()));});
          const b=document.body.innerText.match(/[a-z0-9._%+-]+@gmail\.com/ig); if(b)b.forEach(x=>s.add(x.toLowerCase()));
          return [...s];}""") or []
    except Exception: return []

def open_thread(pg, title):
    try:
        items=pg.query_selector_all('[data-test-id="conversation"], div.conversation, [role="button"], a, div[role="listitem"]')
        for it in items:
            try: t=(it.inner_text() or "").strip()
            except Exception: t=""
            if t and title.lower() in t.lower() and len(t)<80:
                it.click()
                for _ in range(22):
                    time.sleep(0.7)
                    if "/app/" in pg.url: return True
                return True
    except Exception: pass
    return False

def find_editor(pg):
    for sel in ['div.ql-editor[contenteditable="true"]','rich-textarea div[contenteditable="true"]','div[contenteditable="true"]','textarea']:
        try:
            el=pg.query_selector(sel)
            if el and el.is_visible(): return el,sel
        except Exception: pass
    return None,None

def click_send(pg):
    for s in ['button[aria-label*="Enviar"]','button[aria-label*="Send"]','button.send-button',
              'button[mattooltip*="Enviar"]','button[aria-label*="enviar" i]']:
        try:
            e=pg.query_selector(s)
            if e and e.is_visible() and e.is_enabled(): e.click(); return True
        except Exception: pass
    return False

def count_turns(pg):
    try: return len(pg.query_selector_all('message-content'))
    except Exception: return 0

def last_response(pg):
    for s in ['model-response message-content','message-content','model-response','[data-test-id="conversation-turn"]']:
        try:
            els=pg.query_selector_all(s)
            if els:
                t=els[-1].inner_text()
                if t and len(t)>20: return t
        except Exception: pass
    return ""

with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(PROF, channel="msedge", headless=HEADLESS,
        args=["--window-position=2200,2200","--window-size=1300,950","--disable-blink-features=AutomationControlled"])
    pg=ctx.pages[0] if ctx.pages else ctx.new_page(); pg.set_default_timeout(45000)
    pg.goto(target, wait_until="domcontentloaded", timeout=60000); time.sleep(8)
    accts=detect_accounts(pg)
    print("PROFILE:",PROF_KEY,"| ACCOUNT(s):", ", ".join(accts) if accts else "(no detectada)")

    if OPEN_T and "/app/" not in pg.url:
        ok=open_thread(pg, OPEN_T)
        print("OPEN_THREAD['%s']:"%OPEN_T, ok, "->", pg.url[:90])
        time.sleep(3)
    print("URL antes de escribir:", pg.url[:90])

    box,sel=find_editor(pg)
    if not box:
        shot=os.path.join(os.environ.get("TEMP","."),"_gemini_state.png")
        try: pg.screenshot(path=shot)
        except Exception: pass
        print("NO_INPUT — login/consent requerido. Screenshot:",shot); ctx.close(); sys.exit(1)
    print("INPUT:",sel)

    before=count_turns(pg)
    box.click(); time.sleep(0.4)
    try: pg.keyboard.insert_text(QUERY)
    except Exception: pg.keyboard.type(QUERY, delay=4)
    time.sleep(0.8)
    if not click_send(pg): pg.keyboard.press("Enter")
    # confirmar submit: aumenta el nro de turnos o cambia la URL
    submitted=False
    for _ in range(20):
        time.sleep(1)
        if count_turns(pg)>before or "/app/" in pg.url: submitted=True; break
    print("SUBMIT_OK:", submitted, "| turns:", before, "->", count_turns(pg))

    last=""; stable=0; t0=time.time()
    while time.time()-t0<WAIT:
        time.sleep(4)
        cur=last_response(pg)
        stable=stable+1 if len(cur)==len(last) and len(cur)>0 else 0
        last=cur
        if stable>=2 and len(cur)>60: break
    answer=last or last_response(pg)

    final=pg.url
    if THREAD_F and "/app/" in final:
        try: open(THREAD_F,"w",encoding="utf-8").write(final)
        except Exception: pass
    print("THREAD_URL:", final)
    print("\n===== RESPUESTA (ultimo turno del modelo) =====\n"+(answer[:4500] if answer else "(vacia)"))
    fn=os.path.join(OUTDIR, time.strftime("%Y-%m-%d_%H%M%S")+f"_{SLUG}.md")
    with open(fn,"w",encoding="utf-8") as f:
        f.write(f"# Consulta Gemini — {SLUG}\n- Fecha: {time.strftime('%Y-%m-%dT%H:%M')}\n"
                f"- Perfil: {PROF_KEY} | Cuenta(s): {', '.join(accts)}\n- Hilo: {final}\n"
                f"- Mensaje: {QUERY}\n\n## Respuesta\n\n"+(answer or "(vacia)"))
    print("\nGUARDADO ->",fn)
    ctx.close()
