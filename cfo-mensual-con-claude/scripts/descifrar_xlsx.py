# -*- coding: utf-8 -*-
"""Descifra una copia de trabajo de un .xlsx protegido con contrasena.
Uso: python descifrar_xlsx.py <archivo_cifrado.xlsx> <salida.xlsx> [password]
Requiere: pip install msoffcrypto-tool
Nota: 'Muchas Gracias 2026.xlsx' usa contrasena 2020 (OOXML cifrado, contenedor OLE2)."""
import sys, msoffcrypto, zipfile
def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    pwd = sys.argv[3] if len(sys.argv) > 3 else "2020"
    with open(src, "rb") as f:
        off = msoffcrypto.OfficeFile(f)
        off.load_key(password=pwd)
        with open(out, "wb") as g:
            off.decrypt(g)
    print("DESCIFRADO OK ->", out, "| ZIP valido:", zipfile.is_zipfile(out))
if __name__ == "__main__":
    main()
