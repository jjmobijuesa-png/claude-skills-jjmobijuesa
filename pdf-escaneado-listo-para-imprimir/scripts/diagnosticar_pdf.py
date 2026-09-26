# diagnosticar_pdf.py - revisa un PDF ESCANEADO antes de mandarlo a imprimir
# y senala las paginas que van a fallar.
#
# Reune las cuatro pruebas que hicieron falta el 2026-09-06 para entender por
# que dos paginas salian siempre a medias:
#
#   1. TAMANO DE PAGINA   <- la que resulto ser la causa
#   2. Peso del raster
#   3. Codificacion JPEG (linea base vs progresivo)
#   4. Integridad del flujo (marcador EOI y decodificacion completa)
#
#   python diagnosticar_pdf.py <pdf> [--paginas 3,5,7]
import sys, io, argparse, warnings, collections
import fitz

try:
    from PIL import Image, ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = False
    HAY_PIL = True
except ImportError:
    HAY_PIL = False

SOF = {0xC0: 'linea base', 0xC1: 'base ext', 0xC2: 'PROGRESIVO',
       0xC3: 'sin perdida', 0xC9: 'aritmetico', 0xCA: 'PROGRESIVO arit'}

# Medidas estandar en puntos (1 pt = 1/72 pulgada)
ESTANDAR = {'A4': (595, 842), 'Letter': (612, 792), 'Legal': (612, 1008),
            'A3': (842, 1191), 'A5': (420, 595)}
TOLERANCIA = 6      # pt


def tipo_jpeg(b):
    i, n = 2, len(b)
    while i < n - 1:
        if b[i] != 0xFF:
            i += 1
            continue
        m = b[i + 1]
        if m in SOF:
            return SOF[m]
        if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
            i += 2
            continue
        if i + 3 >= n:
            break
        i += 2 + ((b[i + 2] << 8) | b[i + 3])
    return '?'


def parecido_a(w, h):
    for nombre, (ew, eh) in ESTANDAR.items():
        if abs(w - ew) <= TOLERANCIA and abs(h - eh) <= TOLERANCIA:
            return nombre
    return None


ap = argparse.ArgumentParser()
ap.add_argument("pdf")
ap.add_argument("--paginas", default="")
a = ap.parse_args()

d = fitz.open(a.pdf)
nums = ([int(x) for x in a.paginas.split(",") if x.strip()]
        if a.paginas else list(range(1, d.page_count + 1)))

print(f"Documento: {a.pdf}")
print(f"Paginas  : {d.page_count}   (se revisan {len(nums)})")
print(f"PIL      : {'si' if HAY_PIL else 'NO - no se puede validar integridad'}")
print()
print(f"{'PAG':>4} {'TAMANO pt':>12} {'MEDIDA':>8} {'ROT':>4} {'MPIX':>6} "
      f"{'KB':>6} {'JPEG':>12} {'EOI':>5} {'DECODE':>9}")

tamanos = collections.Counter()
sospechosas = set()
filas = []

for n in nums:
    p = d[n - 1]
    r = p.rect
    w, h = round(r.width), round(r.height)
    tamanos[(w, h)] += 1
    med = parecido_a(w, h) or 'NO ESTANDAR'
    if med == 'NO ESTANDAR':
        sospechosas.add(n)

    px = by = 0
    tj = eoi = dec = '-'
    for im in p.get_images(full=True):
        info = d.extract_image(im[0])
        raw = info["image"]
        px += im[2] * im[3]
        by += len(raw)
        if info["ext"] == "jpeg":
            tj = tipo_jpeg(raw)
            eoi = 'si' if raw[-2:] == b"\xff\xd9" else 'NO'
            if 'PROGRESIVO' in tj or eoi == 'NO':
                sospechosas.add(n)
            if HAY_PIL:
                try:
                    img = Image.open(io.BytesIO(raw))
                    with warnings.catch_warnings():
                        warnings.simplefilter("error")
                        img.load()
                    dec = 'completa'
                except Exception:
                    dec = 'TRUNCADA'
                    sospechosas.add(n)
        else:
            tj = info["ext"]

    marca = '  <<<' if n in sospechosas else ''
    print(f"{n:>4} {w:>5} x {h:<4} {med:>8} {p.rotation:>4} {px/1e6:>6.2f} "
          f"{by/1024:>6.0f} {tj:>12} {eoi:>5} {dec:>9}{marca}")
    filas.append((n, w, h, med))

print()
print("=== TAMANOS PRESENTES ===")
for (w, h), c in tamanos.most_common():
    med = parecido_a(w, h) or 'NO ESTANDAR'
    aviso = '   <-- riesgo de recorte' if med == 'NO ESTANDAR' else ''
    print(f"   {w} x {h} pt = {w/72*2.54:.1f} x {h/72*2.54:.1f} cm   "
          f"{med:<12} {c:>3} pag{aviso}")

print()
if len(tamanos) > 1:
    print(f"AVISO: el documento mezcla {len(tamanos)} tamanos de pagina distintos.")
if sospechosas:
    print("PAGINAS DE RIESGO: " + ", ".join(str(x) for x in sorted(sospechosas)))
    print()
    print("SOLUCION: normalizar el lienzo antes de imprimir ->")
    print("   python normalizar_a4.py <origen> <destino> --dpi 150 --calidad 70 --gris")
else:
    print("Sin paginas de riesgo. Se puede imprimir tal cual.")
d.close()
