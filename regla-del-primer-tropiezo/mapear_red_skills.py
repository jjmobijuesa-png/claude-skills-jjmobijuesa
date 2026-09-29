# -*- coding: utf-8 -*-
"""Extrae la RED REAL de skills: nodos, aristas ([[wikilinks]] + frontmatter `relacionada:`),
cubos (hubs), huérfanas y racimos. No inventa relaciones: las lee del corpus."""
import os, re, io, sys, json
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")

RAIZ = r"C:\Users\datos\.claude\skills"
SALIDA_MD = r"C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\skills_network.md"

def slug(s):
    # Conserva "_": las notas de memoria usan guion bajo y convertirlo en "-"
    # imprimía enlaces con la grafía equivocada (ver AUDITORIA_RED.md, PR #1).
    return re.sub(r"[^a-z0-9_\-]", "-", s.strip().lower()).strip("-")

nodos, texto = {}, {}
for d in sorted(os.listdir(RAIZ)):
    p = os.path.join(RAIZ, d, "SKILL.md")
    if not os.path.isdir(os.path.join(RAIZ, d)) or not os.path.exists(p):
        continue
    try:
        t = io.open(p, encoding="utf-8", errors="ignore").read()
    except Exception:
        continue
    nodos[slug(d)] = d
    texto[slug(d)] = t

aristas = defaultdict(set)
for s, t in texto.items():
    for m in re.findall(r"\[\[([^\]|#]+)", t):
        aristas[s].add(slug(m))
    fm = re.search(r"^relacionada:\s*(.+)$", t, re.M)
    if fm:
        for r in re.split(r"[,\n]", fm.group(1)):
            r = slug(r)
            if r: aristas[s].add(r)

reales = {s: {d for d in ds if d in nodos and d != s} for s, ds in aristas.items()}
rotos  = {s: sorted(d for d in ds if d not in nodos and d) for s, ds in aristas.items()}

entrantes = defaultdict(set)
for s, ds in reales.items():
    for d in ds: entrantes[d].add(s)

grado = {s: len(reales.get(s, set())) + len(entrantes.get(s, set())) for s in nodos}
hubs = sorted(nodos, key=lambda s: -grado[s])[:20]
huerfanas = sorted(s for s in nodos if grado[s] == 0)
solo_salida = sorted(s for s in nodos if reales.get(s) and not entrantes.get(s))

# racimos: componentes conexas del grafo no dirigido
vecinos = defaultdict(set)
for s, ds in reales.items():
    for d in ds:
        vecinos[s].add(d); vecinos[d].add(s)
vistos, racimos = set(), []
for s in nodos:
    if s in vistos: continue
    pila, comp = [s], []
    while pila:
        x = pila.pop()
        if x in vistos: continue
        vistos.add(x); comp.append(x)
        pila.extend(vecinos.get(x, set()) - vistos)
    racimos.append(sorted(comp))
racimos.sort(key=len, reverse=True)

L = []
L.append("# Red integrada de skills — mapa derivado del corpus\n")
L.append("> Generado por `mapear_red_skills.py`. **No es una lista: es un grafo.** Los nodos son")
L.append("> las skills de `~/.claude/skills/`; las aristas son los `[[wikilinks]]` y los")
L.append("> `relacionada:` que cada skill declara. Sirve para [[regla-del-primer-tropiezo]] §4:")
L.append("> la asociación análoga necesita saber qué está conectado con qué.\n")
L.append("**%d skills · %d aristas reales · %d racimos · %d huérfanas**\n"
         % (len(nodos), sum(len(v) for v in reales.values()), len(racimos), len(huerfanas)))

L.append("\n## Cubos (hubs) — por donde pasa el tráfico\n")
L.append("Si hay que entrar a la red por algún lado, es por aquí.\n")
L.append("| Skill | Grado | Sale hacia | Entra desde |")
L.append("|---|---:|---:|---:|")
for s in hubs:
    if grado[s] == 0: continue
    L.append("| `%s` | %d | %d | %d |" % (nodos[s], grado[s], len(reales.get(s, ())), len(entrantes.get(s, ()))))

L.append("\n## Racimos — las vecindades temáticas\n")
L.append("Un fallo en cualquier miembro de un racimo se busca primero en sus vecinos.\n")
for i, c in enumerate(racimos[:12], 1):
    if len(c) < 2: continue
    L.append("**Racimo %d (%d skills):** %s\n" % (i, len(c), ", ".join("`%s`" % nodos[x] for x in c)))

L.append("\n## Huérfanas — nadie las enlaza y ellas no enlazan a nadie\n")
L.append("Son capital muerto: existen pero la red no las alcanza. Candidatas a enlazar o a fusionar.\n")
for s in huerfanas:
    L.append("- `%s`" % nodos[s])

L.append("\n## Destinos fuera del repo (notas de memoria o enlaces rotos)\n")
L.append("Una nota de memoria o una skill que no existe. Comprobar en `memory/` antes de corregir.\n")
n = 0
for s in sorted(rotos):
    if rotos[s]:
        L.append("- `%s` → %s" % (nodos[s], ", ".join("[[%s]]" % r for r in rotos[s])))
        n += 1
    if n > 40: L.append("- …(recortado)"); break

io.open(SALIDA_MD, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("skills=%d aristas=%d racimos=%d huerfanas=%d" %
      (len(nodos), sum(len(v) for v in reales.values()), len(racimos), len(huerfanas)))
print("hubs:", ", ".join(nodos[s] for s in hubs[:8]))
print("->", SALIDA_MD)
