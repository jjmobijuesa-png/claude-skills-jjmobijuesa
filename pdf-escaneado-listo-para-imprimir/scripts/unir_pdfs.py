# unir_pdfs.py - une varios PDF en uno, EN EL ORDEN DADO.
# Sirve para armar las dos tandas del duplex manual cuando cada documento es
# una hoja: tanda 1 con todos los frentes, tanda 2 con todos los reversos en
# el MISMO orden (la bandeja de esta impresora alimenta en ascendente).
#
#   python unir_pdfs.py <destino.pdf> <a.pdf> <b.pdf> ...
import sys, os
import fitz

destino = sys.argv[1]
fuentes = sys.argv[2:]
out = fitz.open()
for f in fuentes:
    d = fitz.open(f)
    out.insert_pdf(d)
    print(f"   + {os.path.basename(f):<22} {d.page_count} pag")
    d.close()
out.save(destino, deflate=True, garbage=3)
print(f"\n{destino}")
print(f"   {out.page_count} paginas, {os.path.getsize(destino)/1024:.0f} KB")
med = {(round(out[i].rect.width), round(out[i].rect.height)) for i in range(out.page_count)}
print(f"   medidas: {med}   " + ("TODAS IGUALES" if len(med) == 1 else "OJO: MEZCLA DE TAMANOS"))
out.close()
