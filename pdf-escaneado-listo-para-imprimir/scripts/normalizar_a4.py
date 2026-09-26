# normalizar_a4.py - deja TODAS las paginas de un PDF escaneado en un lienzo
# A4 identico, rasterizadas a un DPI uniforme y en JPEG de linea base.
#
# POR QUE: un PDF escaneado suele traer cada pagina con un tamano ligeramente
# distinto (595x842, 595x824, 587x843...). Algunas impresoras baratas, al
# recibir una pagina de medida no estandar, componen mal y expulsan la hoja a
# medias. Igualar el lienzo elimina esa variable de raiz, y de paso el peso
# baja mucho (imprime mas rapido, como un borrador).
#
#   python normalizar_a4.py <origen> <destino> [--dpi 150] [--calidad 70]
#                           [--gris] [--paginas 7,19] [--margen 0]
import os, argparse
import fitz

A4 = fitz.paper_rect("a4")          # 595.28 x 841.89 pt

ap = argparse.ArgumentParser()
ap.add_argument("origen")
ap.add_argument("destino")
ap.add_argument("--dpi", type=int, default=150)
ap.add_argument("--calidad", type=int, default=70)
ap.add_argument("--gris", action="store_true")
ap.add_argument("--paginas", default="")
ap.add_argument("--margen", type=float, default=0, help="margen en pt dentro del A4")
a = ap.parse_args()

src = fitz.open(a.origen)
nums = ([int(x) for x in a.paginas.split(",") if x.strip()]
        if a.paginas else list(range(1, src.page_count + 1)))

out = fitz.open()
cs = fitz.csGRAY if a.gris else fitz.csRGB
zoom = a.dpi / 72.0
m = a.margen
destino_rect = fitz.Rect(m, m, A4.width - m, A4.height - m)

print(f"Origen : {os.path.basename(a.origen)}")
print(f"Lienzo : A4 {A4.width:.0f} x {A4.height:.0f} pt  ({A4.width/72*2.54:.1f} x {A4.height/72*2.54:.1f} cm)")
print(f"Raster : {a.dpi} dpi, JPEG calidad {a.calidad}{', gris' if a.gris else ''}")
print()
print(f"{'PAG':>4}  {'TAMANO ORIGINAL':>18}  {'ESCALA':>7}  {'KB':>7}")

total = 0
for n in nums:
    p = src[n - 1]
    r = p.rect
    pm = p.get_pixmap(matrix=fitz.Matrix(zoom, zoom), colorspace=cs)
    jpg = pm.tobytes("jpeg", jpg_quality=a.calidad)

    nueva = out.new_page(width=A4.width, height=A4.height)
    # conservar proporcion: encajar dentro del area util, centrado
    esc = min(destino_rect.width / r.width, destino_rect.height / r.height)
    an, al = r.width * esc, r.height * esc
    x0 = (A4.width - an) / 2
    y0 = (A4.height - al) / 2
    nueva.insert_image(fitz.Rect(x0, y0, x0 + an, y0 + al), stream=jpg)

    kb = len(jpg) / 1024
    total += kb
    print(f"{n:>4}  {r.width:>8.0f} x {r.height:<7.0f}  {esc:>6.3f}  {kb:>7.0f}")

out.save(a.destino, deflate=True, garbage=3)
print()
print(f"Archivo: {a.destino}")
print(f"         {os.path.getsize(a.destino)/1024:.0f} KB, {out.page_count} paginas, "
      f"todas de {A4.width:.0f} x {A4.height:.0f} pt")

# verificacion: que ninguna pagina se salga del A4
chk = fitz.open(a.destino)
raros = [i + 1 for i in range(chk.page_count)
         if abs(chk[i].rect.width - A4.width) > 1 or abs(chk[i].rect.height - A4.height) > 1]
print("Verificacion: " + ("TODAS en A4 exacto" if not raros
                          else f"paginas fuera de medida: {raros}"))
chk.close()
src.close()
out.close()
