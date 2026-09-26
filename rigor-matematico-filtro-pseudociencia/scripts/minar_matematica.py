# -*- coding: utf-8 -*-
"""Minero + filtro de RIGOR MATEMATICO sobre un corpus de textos.

Uso por defecto: bookmarks de X.com de @fdc_ec.
  python minar_matematica.py                 # resumen + top rigurosos
  python minar_matematica.py --pseudo        # muestra los de uso esoterico
  python minar_matematica.py --top 40
  python minar_matematica.py --corpus <ruta.json>

Separa TRES cosas que se confunden:
  1. matematica REAL (teorema/ecuacion/probabilidad con contenido verificable)
  2. vocabulario matematico usado como ADORNO esoterico o conspirativo
  3. ruido: la palabra aparece de paso en un texto de otro tema

Salida: conteos por subdominio, autores recurrentes y top con URL canonica.
NUNCA inventa contenido: solo reporta lo que esta en el corpus.
"""
import argparse, collections, io, json, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

CORPUS_DEF = r"E:\vars\var 5\X-com guardados\bookmarks.json"

SUB = {
 "fundamentos/logica": r"\b(l[oó]gica|logic|axiom[ao]s?|teorema|theorem|demostraci[oó]n|proof|deducci[oó]n|falacias? l[oó]gicas?|teor[ií]a de conjuntos|set theory)\b",
 "algebra/geometria": r"\b([aá]lgebra|algebra|algebraic|geometr[ií]a|geometry|topolog[ií]a|topology|matri(z|ces)|matrix|matrices|vector(es)?|eigen\w*|tensor(es)?)\b",
 "calculo/analisis": r"\b(c[aá]lculo (diferencial|integral)|calculus|derivad[ao]s?|derivative|integral(es)?|ecuaci[oó]n diferencial|differential equation)\b",
 "probabilidad/estadistica": r"\b(probabilidad|probability|estad[ií]stica|statistic(s|al)?|bayes\w*|gauss\w*|varianza|variance|desviaci[oó]n est[aá]ndar|correlaci[oó]n|correlation|regresi[oó]n|regression|monte ?carlo|valor esperado|expected value|z-?test|t-?test|lasso)\b",
 "optimizacion/juegos": r"\b(optimizaci[oó]n|optimization|programaci[oó]n lineal|linear programming|gradient descent|descenso de gradiente|teor[ií]a de juegos|game theory|nash|kelly criterion|criterio de kelly)\b",
 "grafos/redes": r"\b(teor[ií]a de grafos|graph theory|grafos?|graphs?|aristas?|edges?|dag\b|directed acyclic)\b",
 "criptografia": r"\b(criptograf[ií]a|cryptograph\w*|hash(ing)?|sha-?256|curva el[ií]ptica|elliptic curve|zero.?knowledge|zk-?snark|post.?cu[aá]ntic\w*|post.?quantum|lattice|ret[ií]cul[ao]s|rsa\b)\b",
 "finanzas cuantitativas": r"\b(quant\w*|cuantitativ[ao]s?|black.?scholes|volatilidad|arbitraje|arbitrage|sharpe|value at risk|high.?frequency|hft|market making|xtx|gerko|medallion|simons)\b",
 "IA matematica": r"\b(red(es)? neuronal(es)?|neural net\w*|neurona artificial|backprop\w*|transformer|embedding(s)?|rope\b|rotary positional|perceptr[oó]n|activation function|funci[oó]n de activaci[oó]n)\b",
 "verificacion formal": r"\b(verificaci[oó]n formal|formal verification|formal methods|m[eé]todos formales|coq|lean prover|tla\+|model checking|invariante)\b",
 "matematica general": r"\b(matem[aá]tic[ao]s?|mathematic(s|al)?|maths?\b|n[uú]meros? primos?|prime numbers?|fibonacci|binet|n[uú]mero [aá]ureo|golden ratio|ian stewart)\b",
}
COMP = {k: re.compile(v, re.I) for k, v in SUB.items()}

# uso NO riguroso del vocabulario (esoterico / conspirativo / pseudociencia)
PSEUDO = re.compile(
 r"\b(matrix|ascensi[oó]n|ascension|chakra|k[aá]rmic\w*|karma|despertar espiritual|spiritual awakening|666|geometr[ií]a sagrada|sacred geometry|sint[eé]rgic\w*|akash\w*|vibraci[oó]n(es)? (alta|elevada)|frecuencia del amor|5d\b|arconte|reptilian\w*|illuminati|new age|activaci[oó]n del adn|dna activation|numerolog[ií]a|astrolog[ií]a|tarot|portal energ\w*)\b", re.I)

# marcadores de contenido verificable
RIGOR = re.compile(
 r"\b(teorema|theorem|demostraci[oó]n|proof|lema|corolario|axiom\w*|paper|arxiv|preprint|peer.?review|ecuaci[oó]n|equation|f[oó]rmula|formula|algoritmo|algorithm|derivad[ao]|integral|matri(z|ces)|matrix|eigen\w*|probabilidad|probability|bayes|regresi[oó]n|regression|varianza|distribuci[oó]n|z-?test|t-?test|lasso|teor[ií]a de juegos|game theory|nash|kelly|black.?scholes|fibonacci|binet|primos?|c[aá]lculo|calculus|[aá]lgebra|algebra|topolog\w*|grafos?|graph theory|criptograf\w*|cryptograph\w*|hash|elliptic|zero.?knowledge|post.?quantum|lattice|verificaci[oó]n formal|formal verification|neural net|backprop|transformer|gradient|estad[ií]stic\w*|statistic\w*|falacia\w*|fallac\w*)\b", re.I)


def cargar(ruta):
    d = json.load(io.open(ruta, encoding="utf-8"))
    return d.get("bookmarks", d) if isinstance(d, dict) else d


def analizar(bl):
    rig, pse = [], []
    for b in bl:
        if b.get("tombstone"):
            continue
        t = (b.get("text") or "")
        if not t:
            continue
        subs = {k: len(c.findall(t)) for k, c in COMP.items() if c.search(t)}
        if not subs:
            continue
        nr = len(set(m.group(0).lower() for m in RIGOR.finditer(t)))
        np_ = len(set(m.group(0).lower() for m in PSEUDO.finditer(t)))
        m = b.get("metrics") or {}
        rec = {"h": b.get("author_handle"), "u": b.get("url"),
               "d": (b.get("created_at") or "")[:16],
               "l": m.get("like_count") or m.get("favorite_count") or 0,
               "t": re.sub(r"\s+", " ", t)[:340],
               "nr": nr, "np": np_, "subs": subs}
        if np_ >= 1 and np_ >= nr:
            pse.append(rec)
        elif nr >= 2:
            rig.append(rec)
    rig.sort(key=lambda x: (-x["nr"], -x["l"]))
    pse.sort(key=lambda x: -x["l"])
    return rig, pse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default=CORPUS_DEF)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--pseudo", action="store_true")
    a = ap.parse_args()

    bl = cargar(a.corpus)
    rig, pse = analizar(bl)
    print(f"Corpus: {len(bl)} textos")
    print(f"RIGUROSOS: {len(rig)}   |   VOCABULARIO MATEMATICO USADO COMO ADORNO: {len(pse)}\n")

    cnt = collections.Counter()
    for h in rig:
        for k in h["subs"]:
            cnt[k] += 1
    print("== SUBDOMINIOS CON CONTENIDO VERIFICABLE ==")
    for k, v in cnt.most_common():
        print(f"  {v:4}  {k}")

    objetivo = pse if a.pseudo else rig
    titulo = "USO ESOTERICO / NO RIGUROSO" if a.pseudo else "TOP RIGUROSOS"
    print(f"\n== {titulo} ==")
    for i, h in enumerate(objetivo[:a.top], 1):
        print(f"\n{i}. @{h['h']} · rigor {h['nr']} · pseudo {h['np']} · ❤{h['l']} · {h['d']}")
        print(f"   subs: {', '.join(h['subs'])}")
        print(f"   {h['t'][:260]}")
        print(f"   → {h['u']}")


if __name__ == "__main__":
    main()
