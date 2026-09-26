# aligerar_pdf.py - reconstruye un PDF escaneado a menor resolucion.
#
# Para que sirve: con el driver generico IPP no se puede pedir "calidad
# borrador" (el driver rechaza psk:PageOutputQuality). El equivalente real es
# mandarle menos datos: rasterizar cada pagina a menos DPI y recomprimir en
# JPEG de linea base. Imprime MUCHO mas rapido y evita que la impresora se
# quede corta de memoria y expulse la hoja a medias.
#
#   python aligerar_pdf.py <origen> <destino> [--dpi 150] [--calidad 70]
#                          [--paginas 7,17,19] [--gris]
import sys, os, argparse
import fitz

ap = argparse.ArgumentParser()
ap.add_argument("origen")
ap.add_argument("destino")
ap.add_argument("--dpi", type=int, default=150)
ap.add_argument("--calidad", type=int, default=70)
ap.add_argument("--paginas", default="", help="1-based, separadas por comas; vacio = todas")
ap.add_argument("--gris", action="store_true", help="convertir a escala de grises")
a = ap.parse_args()

src = fitz.open(a.origen)
nums = ([int(x) for x in a.paginas.split(",") if x.strip()]
        if a.paginas else list(range(1, src.page_count + 1)))

out = fitz.open()
cs = fitz.csGRAY if a.gris else fitz.csRGB
zoom = a.dpi / 72.0
antes = total = 0

print(f"Origen : {os.path.basename(a.origen)}")
print(f"Destino: {a.dpi} dpi, JPEG calidad {a.calidad}"
      f"{', escala de grises' if a.gris else ''}")
print()
print(f"{'PAG':>4}  {'ORIGEN':>10}  {'NUEVO':>10}  {'REDUCE':>7}")

for n in nums:
    p = src[n - 1]
    r = p.rect
    orig_kb = sum(len(src.extract_image(im[0])["image"]) for im in p.get_images(full=True)) / 1024
    pm = p.get_pixmap(matrix=fitz.Matrix(zoom, zoom), colorspace=cs)
    jpg = pm.tobytes("jpeg", jpg_quality=a.calidad)
    nueva = out.new_page(width=r.width, height=r.height)
    nueva.insert_image(fitz.Rect(0, 0, r.width, r.height), stream=jpg)
    nuevo_kb = len(jpg) / 1024
    antes += orig_kb
    total += nuevo_kb
    pct = (1 - nuevo_kb / orig_kb) * 100 if orig_kb else 0
    print(f"{n:>4}  {orig_kb:>9.0f}K  {nuevo_kb:>9.0f}K  {pct:>6.0f}%")

out.save(a.destino, deflate=True, garbage=3)
print()
print(f"Total: {antes:.0f} KB  ->  {total:.0f} KB "
      f"({(1 - total/antes)*100:.0f}% menos)" if antes else "")
print(f"Archivo: {a.destino}  ({os.path.getsize(a.destino)/1024:.0f} KB, "
      f"{out.page_count} paginas)")
src.close()
out.close()
