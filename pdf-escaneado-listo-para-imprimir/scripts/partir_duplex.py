# partir_duplex.py - parte un PDF en las dos pasadas de duplex manual,
# con el orden YA HORNEADO dentro de cada archivo (Ley 2 de la skill:
# no depender de ningun ajuste del driver ni de la app).
#
#   python partir_duplex.py <origen.pdf> <carpeta_salida> [--prefijo NOMBRE]
#                           [--pares-orden asc|desc] [--calibrar]
#
# Genera:
#   <prefijo>-1-IMPARES-asc.pdf      paginas 1,3,5...  en orden ascendente
#   <prefijo>-2-PARES-<orden>.pdf    paginas 2,4,6...  en el orden indicado
#   Con --calibrar, ademas: cal-p1.pdf, cal-p2.pdf y los PNG de referencia.

import sys, os, argparse
import fitz

ap = argparse.ArgumentParser()
ap.add_argument("origen")
ap.add_argument("salida")
ap.add_argument("--prefijo", default="")
ap.add_argument("--pares-orden", choices=["asc", "desc"], default="desc")
ap.add_argument("--calibrar", action="store_true")
ap.add_argument("--desde", type=int, default=1,
                help="primera pagina del documento a incluir (1-based). "
                     "Sirve para continuar un juego ya empezado sin reimprimir.")
a = ap.parse_args()

os.makedirs(a.salida, exist_ok=True)
src = fitz.open(a.origen)
n = src.page_count
pref = a.prefijo or os.path.splitext(os.path.basename(a.origen))[0][:20].strip()

print(f"Origen : {os.path.basename(a.origen)}")
print(f"Paginas: {n}   ->  {(n + 1) // 2} hojas a doble cara")

# tamanos, para detectar mezclas (Ley 3)
tam = {}
for i in range(n):
    r = src[i].rect
    k = (round(r.width), round(r.height))
    tam[k] = tam.get(k, 0) + 1
print("Tamanos presentes (pt):")
for k, v in sorted(tam.items(), key=lambda x: -x[1]):
    print(f"   {k[0]} x {k[1]}  =  {k[0]/72*2.54:.1f} x {k[1]/72*2.54:.1f} cm   ({v} pag)")

desde0 = max(0, a.desde - 1)
if desde0:
    print(f"\nContinuando desde la pagina {a.desde} (las anteriores ya estan impresas)")

# ---- PASADA 1: impares, ascendente ----
imp = fitz.open()
impares = [i for i in range(desde0, n) if (i + 1) % 2 == 1]
for i in impares:
    imp.insert_pdf(src, from_page=i, to_page=i)
f1 = os.path.join(a.salida, f"{pref}-1-IMPARES-asc.pdf")
imp.save(f1)
print(f"\n[1] {os.path.basename(f1)}  ->  {imp.page_count} paginas "
      f"({impares[0]+1}..{impares[-1]+1} impares, ascendente)")

# ---- PASADA 2: pares ----
par = fitz.open()
pares = [i for i in range(desde0, n) if (i + 1) % 2 == 0]
if a.pares_orden == "desc":
    pares = list(reversed(pares))
for i in pares:
    par.insert_pdf(src, from_page=i, to_page=i)
f2 = os.path.join(a.salida, f"{pref}-2-PARES-{a.pares_orden}.pdf")
par.save(f2)
orden_txt = "descendente" if a.pares_orden == "desc" else "ascendente"
print(f"[2] {os.path.basename(f2)}  ->  {par.page_count} paginas "
      f"(pares, {orden_txt}: empieza en la {pares[0]+1})")

# ---- Calibracion: una sola hoja ----
if a.calibrar:
    for idx, nombre in ((0, "cal-p1"), (1, "cal-p2")):
        d = fitz.open()
        d.insert_pdf(src, from_page=idx, to_page=idx)
        ruta = os.path.join(a.salida, f"{nombre}.pdf")
        d.save(ruta)
        png = os.path.join(a.salida, f"{nombre}.png")
        src[idx].get_pixmap(dpi=90).save(png)
        print(f"[cal] {nombre}.pdf  +  {nombre}.png   (pagina {idx+1})")

src.close()
print("\nListo.")
