# -*- coding: utf-8 -*-
"""
Agrupa los guardados de LinkedIn por concepto/tema y lista candidatos a skill/referencia.
Uso:  python clasificar_guardados.py
Lee:  E:\\vars\\var 5\\LinkedIn-guardados\\guardados.json
Crea: E:\\vars\\var 5\\LinkedIn-guardados\\analisis\\<ts>_clasificacion.md
"""
import json, re, datetime, unicodedata
from pathlib import Path

OUT = Path(r"E:\vars\var 5\LinkedIn-guardados")
AN = OUT / "analisis"; AN.mkdir(parents=True, exist_ok=True)
src = OUT / "guardados.json"
data = json.loads(src.read_text(encoding="utf-8")) if src.exists() else []

THEMES = {
    "finanzas-control": ["ebitda", "ratio", "flujo de caja", "margen", "rentabilidad", "bancab",
                          "cfo", "capital de trabajo", "dscr", "roe", "roa", "apalanc", "retiros",
                          "dividendo", "costos", "tesorer"],
    "ia-agentes": ["inteligencia artificial", " ia ", "llm", "agente", "prompt", "gpt", "claude",
                   "machine learning", "modelo", "copilot", "skill"],
    "blockchain-fintech": ["blockchain", "token", "rwa", "cripto", "dlt", "web3", "fintech",
                           "stablecoin", "smart contract"],
    "cognicion-metacognicion": ["mental", "cognitiv", "sesgo", "metacogn", "pensamiento", "hábito",
                                "neurocien", "decisi", "kahneman"],
    "liderazgo-estrategia": ["liderazgo", "estrategia", "gestión", "equipo", "poder", "negociaci",
                             "management", "ceo"],
    "empresa-familiar-pyme": ["empresa familiar", "pyme", "socio", "propietario", "sucesión", "familiar"],
    "juridico-legislativo": ["ley", "constituci", "reforma", "asamblea", "norma", "regulaci", "decreto"],
}

# 8-nov-2026: clasificacion INSENSIBLE A ACENTOS.
# Esta taxonomia existe por duplicado (aqui y en autoreflex_pipeline_linkedin.py)
# y las dos copias habian divergido por tildes: aqui "gestion", "habito" y
# "sucesion" llevaban acento y alla no. Mismo corpus, dos recuentos distintos,
# los dos escritos en artefactos: liderazgo 594 contra 550 (44 posts de
# diferencia, solo por "gestion") y cognicion 422 contra 407 (15, por "habito").
# Nadie lo noto. Pelando los acentos de AMBOS lados, las dos copias quedan
# equivalentes y el recuento es uno.
# 🚦 Siguen siendo dos copias: si se toca una, tocar la otra. Lo correcto seria
# un solo modulo compartido; pendiente de decision.
def _pelar(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "")
                   if unicodedata.category(c) != "Mn")


_THEMES_N = {k: [_pelar(w) for w in kws] for k, kws in THEMES.items()}


def classify(t):
    tl = " " + _pelar(t).lower() + " "
    hits = [k for k, kws in _THEMES_N.items() if any(w in tl for w in kws)]
    return hits or ["sin-clasificar"]

buckets = {}
for d in data:
    for th in classify(d.get("text", "")):
        buckets.setdefault(th, []).append(d)

ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
L = [f"# Clasificación de guardados LinkedIn (fedphd) — {ts}",
     f"Total capturado: **{len(data)}** posts · fuente `{src}`\n"]
for th in sorted(buckets, key=lambda k: -len(buckets[k])):
    L.append(f"## {th} — {len(buckets[th])}")
    for d in buckets[th][:40]:
        a = (d.get("author") or "?").strip()
        s = re.sub(r"\s+", " ", d.get("text", ""))[:150]
        u = d.get("url", "")
        L.append(f"- **{a}** · {s} … <{u}>")
    L.append("")
L.append("## Candidatos a skill / referencia (>=5 posts, excl. sin-clasificar)")
for th in sorted(buckets, key=lambda k: -len(buckets[k])):
    if th != "sin-clasificar" and len(buckets[th]) >= 5:
        L.append(f"- **{th}**: {len(buckets[th])} posts → aumentar skill existente o crear referencia/intereses-*.")
md = "\n".join(L)
(AN / f"{ts}_clasificacion.md").write_text(md, encoding="utf-8")
print(md[:1800])
print("\n-> guardado en", AN / f"{ts}_clasificacion.md")
