# -*- coding: utf-8 -*-
"""Compara G:\\Mi unidad\\var 9 FBSE\\CCEATI con su copia E:\\vars\\var 9 FBSE\\CCEATI (solo lectura)."""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
G, E = r"G:\Mi unidad\var 9 FBSE\CCEATI", r"E:\vars\var 9 FBSE\CCEATI"
X = lambda p: "\\\\?\\" + p
def inv(root):
    out = {}
    for dp, dn, fn in os.walk(X(root)):
        rel = os.path.relpath(dp, X(root))
        for n in fn:
            if n.lower() == "desktop.ini" or n.startswith("~$"): continue
            st = os.stat(os.path.join(dp, n))
            out[os.path.normpath(os.path.join(rel, n))] = (st.st_size, st.st_mtime)
    return out
g, e = inv(G), inv(E)
solo_g = sorted(set(g) - set(e)); solo_e = sorted(set(e) - set(g))
dif = sorted(k for k in set(g) & set(e) if g[k][0] != e[k][0])
print(f"G: {len(g)} archivos | E: {len(e)} archivos | solo en G: {len(solo_g)} | solo en E: {len(solo_e)} | distinto tamaño: {len(dif)}")
from collections import Counter
top = lambda k: k.split(os.sep)[0] if os.sep in k else "(raíz)"
print("solo en E: por carpeta superior:", dict(Counter(top(k) for k in solo_e)))
print("solo en G: por carpeta superior:", dict(Counter(top(k) for k in solo_g)))
print("--- solo en G:"); [print("  ", k) for k in solo_g]
print("--- solo en E: (fuera del ZZ)"); [print("  ", k) for k in solo_e if not k.startswith("ZZ Archivo")]
print("--- distinto tamaño:"); [print("  ", k, g[k][0], e[k][0], "G más nuevo" if g[k][1] > e[k][1] else "E más nuevo") for k in dif]
json.dump({"solo_g": solo_g, "solo_e": solo_e, "dif": dif}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_comparar_ge.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("--- carpetas de primer nivel de var 9 FBSE en G:", sorted(os.listdir(X(r"G:\Mi unidad\var 9 FBSE"))))
