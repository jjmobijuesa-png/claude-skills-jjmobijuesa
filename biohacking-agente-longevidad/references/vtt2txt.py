# -*- coding: utf-8 -*-
"""Convierte VTT auto de YouTube a texto plano limpio (sin timestamps,
sin etiquetas <c>, sin líneas duplicadas por el efecto 'rolling')."""
import re, sys, glob
from pathlib import Path

def clean_vtt(path):
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    out = []
    for ln in lines:
        if "-->" in ln: continue
        if ln.strip() in ("WEBVTT","") : continue
        if ln.startswith(("Kind:","Language:")): continue
        ln = re.sub(r"<[^>]+>", "", ln)          # quita <c> y <00:00:00.000>
        ln = ln.strip()
        if not ln: continue
        if out and out[-1] == ln: continue       # dedup consecutivo
        out.append(ln)
    # dedup global de la ventana rodante: si una línea ya salió hace <=2, saltar
    final = []
    for ln in out:
        if ln in final[-3:]: continue
        final.append(ln)
    return " ".join(final)

for vid in sys.argv[1:]:
    # preferir es-orig si existe, si no es
    cand = f"{vid}.es-orig.vtt"
    if not Path(cand).exists(): cand = f"{vid}.es.vtt"
    txt = clean_vtt(cand)
    Path(f"{vid}.txt").write_text(txt, encoding="utf-8")
    print(f"{vid}: {len(txt)} chars -> {vid}.txt")
