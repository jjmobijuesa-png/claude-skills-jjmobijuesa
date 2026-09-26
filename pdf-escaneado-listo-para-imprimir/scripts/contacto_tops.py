# contacto_tops.py - hoja de contacto con la FRANJA SUPERIOR de varias paginas,
# etiquetada con el numero de pagina. Sirve para identificar contra el papel
# cual pagina salio mal, sin renderizar documentos enteros.
#
#   python contacto_tops.py <pdf> <salida.png> --paginas 3,5,7 --franja 0.30
import os, argparse
import fitz

ap = argparse.ArgumentParser()
ap.add_argument("pdf")
ap.add_argument("salida")
ap.add_argument("--paginas", required=True, help="lista separada por comas, 1-based")
ap.add_argument("--franja", type=float, default=0.30, help="fraccion superior de la pagina")
ap.add_argument("--cols", type=int, default=4)
ap.add_argument("--ancho", type=int, default=420, help="ancho en px de cada celda")
a = ap.parse_args()

nums = [int(x) for x in a.paginas.split(",") if x.strip()]
doc = fitz.open(a.pdf)

celdas = []
for n in nums:
    p = doc[n - 1]
    r = p.rect
    clip = fitz.Rect(r.x0, r.y0, r.x1, r.y0 + r.height * a.franja)
    zoom = a.ancho / r.width
    pm = p.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    celdas.append((n, pm))

cw = max(c[1].width for c in celdas)
ch = max(c[1].height for c in celdas)
etiqueta = 26
cols = a.cols
filas = (len(celdas) + cols - 1) // cols
W = cols * (cw + 8) + 8
H = filas * (ch + etiqueta + 8) + 8

salida = fitz.open()
pag = salida.new_page(width=W, height=H)
pag.draw_rect(fitz.Rect(0, 0, W, H), color=None, fill=(1, 1, 1))

for i, (n, pm) in enumerate(celdas):
    f, c = divmod(i, cols)
    x = 8 + c * (cw + 8)
    y = 8 + f * (ch + etiqueta + 8)
    pag.insert_text(fitz.Point(x + 4, y + 18), f"PAGINA {n}", fontsize=15,
                    fontname="hebo", color=(0.8, 0, 0))
    rect = fitz.Rect(x, y + etiqueta, x + pm.width, y + etiqueta + pm.height)
    pag.insert_image(rect, pixmap=pm)
    pag.draw_rect(rect, color=(0.6, 0.6, 0.6), width=0.8)

pag.get_pixmap(dpi=110).save(a.salida)
print(f"{a.salida}   ({len(celdas)} paginas, franja superior {a.franja:.0%})")
doc.close()
