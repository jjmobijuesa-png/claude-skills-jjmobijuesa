# ver_propietario.py - para cada PDF de una carpeta, dice cuantas paginas tiene,
# si es escaneado o texto, y extrae las lineas donde aparece un nombre de
# propietario / contribuyente / solicitante.
import sys, os, re
import fitz

carpeta = sys.argv[1]
CLAVES = re.compile(r'(propietario|contribuyente|solicitante|apellidos|nombres|'
                    r'duque|villavicencio|cede.o)', re.IGNORECASE)

for f in sorted(os.listdir(carpeta)):
    if not f.lower().endswith(".pdf"):
        continue
    ruta = os.path.join(carpeta, f)
    d = fitz.open(ruta)
    tot_txt = 0
    tot_img = 0
    lineas = []
    for i in range(d.page_count):
        p = d[i]
        t = p.get_text()
        tot_txt += len(t.strip())
        tot_img += len(p.get_images())
        for ln in t.splitlines():
            ln = ln.strip()
            if ln and CLAVES.search(ln):
                lineas.append(f"p{i+1}: {ln}")
    tipo = "TEXTO" if tot_txt > 200 else ("ESCANEADO" if tot_img else "vacio")
    print(f"--- {f}")
    print(f"    {d.page_count} pag | {tipo} | {tot_txt} chars | {tot_img} img")
    if lineas:
        for ln in lineas[:8]:
            print(f"      {ln}")
    elif tipo == "ESCANEADO":
        print("      (escaneado: el nombre esta en la imagen, no en texto)")
    print()
    d.close()
