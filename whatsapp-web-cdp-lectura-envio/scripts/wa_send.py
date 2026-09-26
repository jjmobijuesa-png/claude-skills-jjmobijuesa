# -*- coding: utf-8 -*-
"""
Envío ESTABLE con guardas (skill v1.1).
Uso:  python wa_send.py "<TARGET nombre exacto>" <archivo_mensaje.txt> ["<FORBID>"]
- Adjunta por CDP (requiere sesión viva; correr wa_connect.py antes).
- Verifica destinatario SOLO por la CABECERA (#main header).
- Nunca clica «Usar aquí». insert_text + Shift+Enter por línea. Enter para enviar.
- Verifica POST-envío leyendo el último message-out.
"""
import sys, time
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
if len(sys.argv)<3:
    print("uso: wa_send.py \"<TARGET>\" <archivo.txt> [\"<FORBID>\"]"); sys.exit(9)
TARGET=sys.argv[1]; MSGFILE=sys.argv[2]; FORBID=sys.argv[3] if len(sys.argv)>3 else ""
MSG=open(MSGFILE,encoding="utf-8").read().rstrip("\n").split("\n")
MARK=next((w for l in MSG for w in l.split() if any(c.isdigit() for c in w) and len(w)>4), "")  # marcador de verificación
HEADER_JS="""()=>{const h=document.querySelector('#main header')||document.querySelector('header');
  return h?(h.innerText||'').trim():'';}"""
CAJA_JS="""()=>{const W=innerWidth;
  for(const e of document.querySelectorAll('div[contenteditable="true"]')){const r=e.getBoundingClientRect();
    if(r.x>W*0.33 && r.y>innerHeight*0.65 && r.width>150) return {x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2)};}
  return null;}"""
OUT_JS="""()=>{const a=[...document.querySelectorAll('div.message-out')];return a.length?a[a.length-1].innerText:'';}"""
with sync_playwright() as p:
    br=p.chromium.connect_over_cdp("http://127.0.0.1:9222"); ctx=br.contexts[0]
    pg=next((pg for pg in ctx.pages if "web.whatsapp.com" in pg.url), None)
    if not pg: print("ABORTA: no hay pestaña WA. Corre wa_connect.py"); sys.exit(1)
    pg.bring_to_front(); time.sleep(1.2)
    if not pg.query_selector('#pane-side'):
        print("ABORTA: sesión no logueada (¿QR pendiente?). NO clico «Usar aquí»."); sys.exit(2)
    box=pg.query_selector('input[data-tab="3"]'); box.click(); time.sleep(0.4)
    pg.keyboard.press("Control+A"); pg.keyboard.press("Delete"); pg.keyboard.insert_text(TARGET); time.sleep(3.5)
    fila=None
    for f in pg.query_selector_all('#pane-side [role="row"]'):
        t=(f.inner_text() or "")
        if TARGET.lower() in t.lower() and (not FORBID or FORBID.lower() not in t.lower()): fila=f; break
    if not fila: print("ABORTA: no hallé la fila de", TARGET); sys.exit(3)
    r=fila.bounding_box(); pg.mouse.click(int(r['x']+r['width']*0.6), int(r['y']+r['height']/2)); time.sleep(5)
    head=pg.evaluate(HEADER_JS); print("CABECERA:", head.replace(chr(10)," ")[:60])
    if TARGET.lower() not in head.lower(): print("ABORTA: destinatario no confirmado en CABECERA"); sys.exit(4)
    if FORBID and FORBID.lower() in head.lower(): print("ABORTA: cabecera contiene FORBID"); sys.exit(5)
    caja=pg.evaluate(CAJA_JS)
    if not caja: print("ABORTA: sin caja de texto"); sys.exit(6)
    pg.mouse.click(caja['x'], caja['y']); time.sleep(0.5)
    for i,l in enumerate(MSG):
        if l: pg.keyboard.insert_text(l)
        if i<len(MSG)-1: pg.keyboard.press("Shift+Enter"); time.sleep(0.03)
    time.sleep(0.7); pg.keyboard.press("Enter"); print("Enter emitido"); time.sleep(4)
    out=pg.evaluate(OUT_JS)
    ok = (MARK and MARK in out) or (MSG[0][:20] in out)
    print("VERIFICACIÓN POST-ENVÍO:", "ENVIADO ✓" if ok else "NO CONFIRMADO — revisar en el teléfono", "| marcador:", MARK)
    sys.exit(0 if ok else 7)
