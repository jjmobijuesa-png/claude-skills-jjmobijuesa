# -*- coding: utf-8 -*-
"""
volcar_libro.py  —  Lee un .xlsx COMPLETO en UNA sola pasada y lo vuelca a disco.
Uso:
    python -I volcar_libro.py "<ruta.xlsx>" ["<salida.txt>"]

Por qué: cargar un libro grande (p. ej. 5-6 MB exportado de un ERP como XASS) es
lento (2-3 min). Hacerlo varias veces por lecturas parciales desperdicia crédito.
Esta utilidad lo carga DOS veces UNA sola vez (valores y fórmulas), vuelca TODAS
las hojas / celdas / filas / columnas / texto / fórmulas a un .txt y además imprime
un RESUMEN estructural. Después se analiza SObre el .txt (barato), sin recargar el xlsx.

Captura, por cada celda no vacía: coordenada | valor calculado | fórmula (si la hay).
Marca: encabezados, filas de TOTAL/SUBTOTAL/SALDO, y la columna de estado/observación.
"""
import sys, io, warnings
warnings.filterwarnings("ignore")
import openpyxl
from openpyxl.utils import get_column_letter

def main():
    if len(sys.argv) < 2:
        print("Uso: python -I volcar_libro.py <ruta.xlsx> [salida.txt]"); return 2
    path = sys.argv[1]
    out  = sys.argv[2] if len(sys.argv) > 2 else path.rsplit("\\",1)[-1].rsplit("/",1)[-1] + ".VOLCADO.txt"
    wbv = openpyxl.load_workbook(path, data_only=True)   # valores calculados
    wbf = openpyxl.load_workbook(path, data_only=False)  # fórmulas y texto crudo
    f = io.open(out, "w", encoding="utf-8")
    def w(s=""): f.write(str(s) + "\n")

    w("LIBRO: %s" % path)
    w("HOJAS (%d): %s" % (len(wbv.sheetnames), wbv.sheetnames))
    KW_TOT = ("total","subtotal","saldo","iva","ret ","neto")
    KW_EST = ("cancel","pendiente","procesad","autoriz","observaci","estado")
    resumen = []
    for name in wbv.sheetnames:
        wsv = wbv[name]; wsf = wbf[name]
        ncel = nfor = 0; tot_rows = []; est_cols = set(); max_r = wsv.max_row; max_c = wsv.max_column
        w("\n" + "="*90)
        w("HOJA: %s   dims=%s  filas=%d  cols=%d  oculta=%s" % (name, wsv.dimensions, max_r, max_c, wsv.sheet_state!="visible"))
        for r in range(1, max_r+1):
            rowtxt = []
            low_line = ""
            for c in range(1, max_c+1):
                vv = wsv.cell(r,c).value
                ff = wsf.cell(r,c).value
                if vv is None and (ff is None or ff==""):
                    continue
                ncel += 1
                col = get_column_letter(c)
                val = vv
                if isinstance(val,float): val = round(val,2)
                cell = "%s%d=%s" % (col, r, val)
                if isinstance(ff,str) and ff.startswith("="):
                    nfor += 1
                    cell += " {%s}" % ff            # fórmula entre llaves
                rowtxt.append(cell)
                low_line += " " + str(vv).lower() + " " + str(ff).lower()
                if any(k in str(vv).lower() for k in KW_EST): est_cols.add(col)
            if rowtxt:
                w("R%04d | %s" % (r, "  |  ".join(rowtxt)))
                if any(k in low_line for k in KW_TOT): tot_rows.append(r)
        resumen.append((name, max_r, max_c, ncel, nfor, tot_rows, sorted(est_cols)))
    w("\n" + "#"*90); w("RESUMEN ESTRUCTURAL")
    for name,mr,mc,nc,nf,tr,ec in resumen:
        w("  %-30s filas=%-4d cols=%-3d celdas=%-5d formulas=%-4d  filas_total/saldo=%s  col_estado=%s"
          % (name, mr, mc, nc, nf, tr[:20], ec))
    f.close()
    # eco corto a consola (para no gastar lectura del .txt completo)
    print("VOLCADO ->", out)
    for name,mr,mc,nc,nf,tr,ec in resumen:
        print("  %-30s celdas=%-5d formulas=%-4d total/saldo=%s estado=%s" % (name,nc,nf,tr[:12],ec))

if __name__ == "__main__":
    sys.exit(main() or 0)
