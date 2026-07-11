# -*- coding: utf-8 -*-
"""
Agrupa los guardados de LinkedIn por concepto/tema y lista candidatos a skill/referencia.
Uso:  python clasificar_guardados.py
Lee:  E:\\vars\\var 5\\LinkedIn-guardados\\guardados.json
Crea: E:\\vars\\var 5\\LinkedIn-guardados\\analisis\\<ts>_clasificacion.md
"""
import json, re, datetime
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

def classify(t):
    tl = " " + (t or "").lower() + " "
    hits = [k for k, kws in THEMES.items() if any(w in tl for w in kws)]
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
