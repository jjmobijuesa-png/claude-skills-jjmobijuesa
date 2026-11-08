# -*- coding: utf-8 -*-
"""
Cosecha las publicaciones guardadas de LinkedIn (fedphd@gmail.com) conectandose por
CDP al Edge real (puerto 9222), haciendo scroll hasta capturarlas todas.
Uso:  python extraer_guardados.py [MAX_SCROLLS]
Salida: E:\\vars\\var 5\\LinkedIn-guardados\\guardados.json (+ snapshot fechado)
"""
import sys, json, datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

OUTDIR = Path(r"E:\vars\var 5\LinkedIn-guardados")
SNAP   = OUTDIR / "snapshots"
OUTDIR.mkdir(parents=True, exist_ok=True); SNAP.mkdir(exist_ok=True)
CDP = "http://localhost:9222"
URL = "https://www.linkedin.com/my-items/saved-posts/"
MAX_SCROLLS = int(sys.argv[1]) if len(sys.argv) > 1 else 150

EXTRACT_JS = r"""
() => {
  const out = []; const seen = new Set();
  const STATUS = /^(estado:|status:|•)/i;       // "Estado: localizable", bullets
  const anchors = Array.from(document.querySelectorAll(
    'a[href*="/feed/update/"], a[href*="/posts/"], a[href*="/pulse/"]'));
  for (const a of anchors) {
    const href = (a.href || '').split('?')[0];
    const m = href.match(/urn:li:activity:(\d+)/) || href.match(/activity-(\d+)/);
    const key = m ? m[1] : href;
    if (!href || seen.has(key)) continue;
    // subir hasta el contenedor <li> del item guardado
    let li = a;
    for (let i = 0; i < 16 && li.parentElement; i++) {
      li = li.parentElement;
      if (li.tagName === 'LI' && li.innerText && li.innerText.length > 120) break;
    }
    const lines = (li.innerText || '').split('\n').map(s => s.trim()).filter(Boolean);
    if (lines.length < 2) continue;
    seen.add(key);
    // autor = primera línea que no sea marcador de estado/bullet; quitar grado "• 2º"
    let author = '';
    for (const ln of lines.slice(0, 3)) { if (!STATUS.test(ln)) { author = ln; break; } }
    author = author.replace(/\s*•.*$/, '').replace(/\s+seguidores$/i, '').trim();
    const txt = (li.innerText || '').replace(/[ \t]+\n/g, '\n').trim().slice(0, 1600);
    out.push({ key, url: href, activity: m ? m[1] : null, author, text: txt });
  }
  return out;
}
"""

def run():
    captured, title = [], ""
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP)
        ctx = browser.contexts[0] if browser.contexts else browser.new_context()
        page = ctx.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(4000)
        title = page.title()
        last_h, stable = 0, 0
        for i in range(MAX_SCROLLS):
            page.mouse.wheel(0, 4200)
            page.wait_for_timeout(1200)
            for label in ("Show more results", "Ver más resultados", "Mostrar más resultados"):
                try:
                    btn = page.query_selector(f'button:has-text("{label}")')
                    if btn:
                        btn.click(); page.wait_for_timeout(1500)
                except Exception:
                    pass
            h = page.evaluate("document.body.scrollHeight")
            stable = stable + 1 if h == last_h else 0
            last_h = h
            if stable >= 4:
                break
        captured = page.evaluate(EXTRACT_JS)
        page.close()
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    payload = json.dumps(captured, ensure_ascii=False, indent=2)
    safe_title = title.encode("ascii", "replace").decode("ascii")

    # ── CANDADO ANTIPISADA (10-oct-2026) ───────────────────────────────────────
    # El corpus se vacio dos veces (17-ago y 10-oct) porque una corrida sin sesion
    # de LinkedIn escribia su resultado vacio sobre guardados.json. Desde ahora el
    # archivo bueno SOLO se sobrescribe si la cosecha es creible.
    destino = OUTDIR / "guardados.json"
    previos = 0
    if destino.exists():
        try:
            previos = len(json.loads(destino.read_text(encoding="utf-8")))
        except Exception:
            previos = 0

    muro = ("inicio de sesi" in safe_title.lower() or "sign in" in safe_title.lower()
            or "login" in safe_title.lower())
    # se acepta hasta un 20% de merma (el usuario puede haber desguardado posts)
    creible = bool(captured) and not muro and len(captured) >= previos * 0.8

    if creible:
        (SNAP / f"{ts}.json").write_text(payload, encoding="utf-8")
        destino.write_text(payload, encoding="utf-8")
        print(f"capturados {len(captured)} guardados -> {destino}  (previos: {previos})")
    else:
        rechazo = SNAP / f"{ts}_RECHAZADO.json"
        rechazo.write_text(payload, encoding="utf-8")
        print(f"capturados {len(captured)} | previos {previos}")
        print(f"NO SE SOBRESCRIBE guardados.json. Cosecha no creible -> {rechazo}")
        if muro:
            print("CAUSA: muro de autenticacion. Edge en 9222 no tiene sesion de fedphd@gmail.com.")
        elif not captured:
            print("CAUSA: 0 capturados. Revisa los selectores EXTRACT_JS.")
        else:
            print("CAUSA: merma superior al 20% frente al corpus previo.")
    print(f"page_title={safe_title!r}")

if __name__ == "__main__":
    run()
