# -*- coding: utf-8 -*-
"""
render_a4.py — HTML autocontenido -> PDF A4, con medicion de alto y control visual.

    python render_a4.py <fuente.html> <destino.pdf> [--sondas "1.320,00;80,42;DISEBAJ"]

Hace cuatro cosas que no son opcionales:
  1. mide el alto REAL de cada `.page` y lo compara con la caja util de 283,0 mm;
  2. cuenta las peticiones externas (debe ser 0: el HTML va autocontenido);
  3. renderiza cada pagina a PNG en ./verif para leerla a ojo;
  4. comprueba que las sondas aparecen en el texto del PDF, y audita cifras que
     se quedaron sin el signo de dolar (la mordida clasica de bash).

Requiere Playwright con Edge (channel msedge) y PyMuPDF. Solo Edge: regla de la casa.
"""
import argparse
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

CAJA_MM = 283.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fuente")
    ap.add_argument("destino")
    ap.add_argument("--sondas", default="", help="cadenas separadas por ';' que deben estar en el PDF")
    a = ap.parse_args()

    src = pathlib.Path(a.fuente).resolve()
    dst = pathlib.Path(a.destino)
    tmp = src.with_suffix(".pdf")
    verif = src.parent / "verif"
    verif.mkdir(exist_ok=True)

    from playwright.sync_api import sync_playwright

    ext = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(channel="msedge", headless=True)
        pg = b.new_page(viewport={"width": 1100, "height": 1600})
        pg.on("request", lambda r: ext.append(r.url) if not r.url.startswith("file:") else None)
        pg.goto(src.as_uri(), wait_until="networkidle", timeout=60000)
        pg.emulate_media(media="print")
        pg.wait_for_timeout(400)
        altos = pg.evaluate(
            "() => [...document.querySelectorAll('.page')]"
            ".map(e => e.getBoundingClientRect().height)")
        pg.pdf(path=str(tmp), format="A4", print_background=True,
               margin={"top": "8mm", "right": "9mm", "bottom": "6mm", "left": "9mm"})
        pg.close()
        b.close()

    ok = True
    for i, h in enumerate(altos, 1):
        mm = h / 96 * 25.4
        marca = "OK " if mm <= CAJA_MM else "SE PASA"
        if mm > CAJA_MM:
            ok = False
        print("hoja %d: %6.1f mm  (caja util %.1f mm)  %s" % (i, mm, CAJA_MM, marca))
    print("peticiones externas: %d %s" % (len(ext), "" if not ext else "<-- debe ser 0"))

    import fitz
    d = fitz.open(str(tmp))
    print("PDF: %d pagina(s), %.0f KB" % (len(d), tmp.stat().st_size / 1024))
    if len(d) != len(altos):
        print("AVISO: %d bloques .page pero %d paginas — algo desborda." % (len(altos), len(d)))
        ok = False
    txt = ""
    for i, pag in enumerate(d):
        txt += pag.get_text()
        pag.get_pixmap(matrix=fitz.Matrix(2.0, 2.0)).save(str(verif / ("pag%d.png" % (i + 1))))
    for s in [x.strip() for x in a.sondas.split(";") if x.strip()]:
        marca = "si" if s in txt else "NO ESTA"
        if s not in txt:
            ok = False
        print("  sonda '%s': %s" % (s, marca))
    huerfanas = re.findall(r"(?<![\$\d,.])\b\d{1,3},\d{2}\s+millones", txt)
    if huerfanas:
        print("AVISO: cifras sin signo de dolar delante: %s" % huerfanas)
        ok = False
    d.close()

    print("PNG de control en %s — leerlos a ojo antes de entregar." % verif)
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(tmp, dst)
        print("copiado -> %s" % dst)
    except PermissionError as e:
        print("PDF abierto en otra aplicacion, no se pudo copiar: %s" % e)
        ok = False
    print("\nRESULTADO: %s" % ("listo" if ok else "REVISAR los avisos de arriba"))


if __name__ == "__main__":
    main()
