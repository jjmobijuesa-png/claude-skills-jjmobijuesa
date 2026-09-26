# -*- coding: utf-8 -*-
"""
Enrutador heurístico: dado un prompt/tarea, sugiere el modelo Claude
más apropiado (Haiku 4.5 / Sonnet 5 / Opus 4.8 / Fable 5).

Uso:
    python sugerir_modelo.py "texto del prompt o tarea"
    echo "texto" | python sugerir_modelo.py

Es una AYUDA heurística por palabras clave, no un oráculo. La decisión
final es del usuario; el agente nunca cambia de modelo por su cuenta.

Precios y capacidades: verificar SIEMPRE con la skill `claude-api`
antes de citarlos — cambian. Los de aquí son de referencia 2026-06-24.
"""
import sys, re
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# (modelo, peso, regex, motivo)
SENALES = [
    # --- HAIKU 4.5: mecánico, corto, alto volumen ---
    ("haiku", 3, r"\b(clasific|etiquet|renombr|list[ae]|cuent[ae]|contar|extrae|convert|mover|copiar|ordenar|filtrar)\w*", "tarea mecánica de transformación"),
    ("haiku", 3, r"\b(r[áa]pido|sencillo|simple|trivial|de una l[íi]nea|masivo|en lote|uno por uno)\b", "tarea explícitamente simple o de volumen"),
    ("haiku", 2, r"\b(triage|bandeja|inbox|s[íi]/no|sí o no|verdadero o falso|formato|reformate)\w*", "clasificación / formateo"),

    # --- SONNET 5: producción de contenido y documentos ---
    ("sonnet", 3, r"\b(redact|escrib|traduc|resum|reescrib|corrig|edita|formatea)\w*", "redacción o edición de contenido"),
    ("sonnet", 3, r"\b(correo|email|carta|informe|documento|word|docx|excel|xlsx|pdf|presentaci[óo]n|pptx|acta|memo)\b", "generación de documento estándar"),
    ("sonnet", 2, r"\b(consulta|busca en|revisa el corpus|qu[ée] tengo sobre|dame un resumen)\b", "consulta al corpus curado"),
    ("sonnet", 2, r"\b(landing|html|maqueta|dise[ñn]a la p[áa]gina|css)\b", "frontend / entregable visual"),

    # --- OPUS 4.8: razonamiento profundo y agentic ---
    ("opus", 4, r"\b(analiz|audit|diagnostic|investig|eval[úu]a|valora|forense|peritaje|dictamen)\w*", "análisis profundo / auditoría"),
    ("opus", 4, r"\b(estrategia|estrat[ée]gic|modelo financiero|flujo de caja|valoraci[óo]n|z-score|ebitda|margen|ratio)\w*", "análisis financiero o estratégico"),
    ("opus", 4, r"\b(jur[íi]dic|legal|normativ|ley|reglamento|art[íi]culo|reforma|contrato|convenio)\w*", "trabajo jurídico"),
    ("opus", 3, r"\b(depura|debug|arregla|repara|falla|error|no funciona|por qu[ée] falla)\w*", "depuración / diagnóstico técnico"),
    ("opus", 3, r"\b(skill|agente|pipeline|automatiz|orquest|script|refactor)\w*", "construcción de skills / agentes"),
    ("opus", 3, r"\b(varios pasos|multi-?paso|de punta a punta|end to end|todo el flujo|integra)\b", "tarea multi-paso encadenada"),
    ("opus", 2, r"\b(decide|recomienda|compara opciones|pros y contras|trade-?off|qu[ée] conviene)\b", "decisión con criterio"),

    # --- FABLE 5: lo más duro / autónomo largo ---
    ("fable", 5, r"\b(no (lo )?hemos podido|nadie ha logrado|el m[áa]s dif[íi]cil|imposible hasta ahora|se nos resiste)\b", "problema no resuelto, tope de dificultad"),
    ("fable", 5, r"\b(durante la noche|overnight|por horas|aut[óo]nom\w+ (largo|horas)|sin supervisi[óo]n|corrida larga)\b", "corrida autónoma de larga duración"),
    ("fable", 4, r"\b(el proyecto entero|todo el repositorio|migraci[óo]n completa|reescribe todo|de cero y completo)\b", "alcance total en una sola corrida"),
    ("fable", 3, r"\b(m[áa]xima capacidad|lo mejor que exista|el modelo m[áa]s potente|sin l[íi]mite de costo)\b", "se pide el tope explícitamente"),
]

# Señales que DESCARTAN Haiku (contexto grande: Haiku es 200K, el resto 1M)
CONTEXTO_GRANDE = re.compile(
    r"\b(todo el corpus|bookmarks|5\.?550|libro completo|transcripci[óo]n completa|"
    r"todos los (archivos|documentos|correos)|corpus entero|7\s?mb|expediente completo)\b", re.I)

INFO = {
    "haiku":  ("Haiku 4.5",  "claude-haiku-4-5",  "200K", "$1 / $5",        "0,2x Opus"),
    "sonnet": ("Sonnet 5",   "claude-sonnet-5",   "1M",   "$2 / $10 intro", "0,4x Opus (hasta 31-ago-2026)"),
    "opus":   ("Opus 4.8",   "claude-opus-4-8",   "1M",   "$5 / $25",       "1x (referencia)"),
    "fable":  ("Fable 5",    "claude-fable-5",    "1M",   "$10 / $50",      "2x Opus"),
}
ORDEN = ["haiku", "sonnet", "opus", "fable"]

def sugerir(texto):
    puntajes = {k: 0 for k in ORDEN}
    motivos = {k: [] for k in ORDEN}
    for modelo, peso, pat, motivo in SENALES:
        if re.search(pat, texto, re.I):
            puntajes[modelo] += peso
            if motivo not in motivos[modelo]:
                motivos[modelo].append(motivo)

    ctx_grande = bool(CONTEXTO_GRANDE.search(texto))
    if ctx_grande and puntajes["haiku"] > 0:
        puntajes["haiku"] = 0
        motivos["haiku"] = []

    # Sin señal clara -> Opus 4.8 (el default: nunca degradar por costo solo)
    if max(puntajes.values()) == 0:
        elegido, razon = "opus", ["sin señal clara — se mantiene el default Opus 4.8"]
    else:
        # empate: gana el más capaz (más a la derecha en ORDEN)
        top = max(puntajes.values())
        elegido = [m for m in ORDEN if puntajes[m] == top][-1]
        razon = motivos[elegido]

    nombre, mid, ctx, precio, rel = INFO[elegido]
    print(f"=== Sugerencia de modelo ===")
    print(f"  Tarea: {texto[:110]}{'...' if len(texto) > 110 else ''}\n")
    print(f"  >>> {nombre}   ({mid})")
    print(f"      contexto {ctx} · {precio} por 1M tok · costo {rel}")
    print(f"      Por qué: {'; '.join(razon)}")
    if ctx_grande:
        print(f"      ⚠ Corpus grande detectado: Haiku (200K) queda descartado por contexto.")
    print("\n  Puntajes:", ", ".join(f"{INFO[m][0]}={puntajes[m]}" for m in ORDEN))
    print("\n  Heurística por palabras clave — la decisión es del usuario.")
    print("  El agente NUNCA cambia de modelo por su cuenta ni degrada por costo.")
    return elegido

if __name__ == "__main__":
    txt = " ".join(sys.argv[1:]).strip() or sys.stdin.read().strip()
    if not txt:
        print(__doc__); sys.exit(1)
    sugerir(txt)
