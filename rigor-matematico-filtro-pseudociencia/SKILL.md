---
name: rigor-matematico-filtro-pseudociencia
description: >-
  Distingue MATEMÁTICA REAL de vocabulario matemático usado como adorno
  (esotérico, conspirativo o de marketing) y fija el orden de rigor
  lógica→matemática→ciencia. Invocar ante cualquier afirmación con números,
  «fórmulas», modelos o estadística antes de citarla, invertir o decidir.
trigger_phrases:
  - "¿esto es matemática de verdad?"
  - "verifica esta fórmula / este dato"
  - "suena científico pero"
  - "rigor matemático"
  - "filtrar pseudociencia"
  - "minar matemáticas del corpus"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: fundamentos / pensamiento crítico
fuente:
  - "Minería propia del corpus de bookmarks @fdc_ec (5.561 textos, 2026-08-07) con scripts/minar_matematica.py"
  - "Bookmarks citados en el cuerpo (URL canónica de cada uno)"
---

## Acerca de mí (cargar al arrancar)
Leer `...\memory\user_role.md` + `MEMORY.md`. Hermana de
[[doctrina-thorp-matematica-vs-multitud]] (confía en las matemáticas, no en la
multitud), [[winston-representacion-restricciones-ia]] (la representación
correcta expone las restricciones), [[metodo-hamming-preguntas-fundamentales]]
(¿por qué funciona y dónde deja de funcionar?) y [[wolfram-forensic-engine]]
(verificación numérica dura). Sirve al **Pilar VII (Gerko)** y al anclaje
obligatorio de toda ecuación del Alfa Lab a las 17 de Stewart
([[project_alfalab_uteq]]).

## Hallazgo que origina esta skill (medido, no supuesto)
Sobre los **5.561 bookmarks** de @fdc_ec: **234** contienen vocabulario
matemático, pero al filtrar por contenido verificable quedan **~23 rigurosos**
frente a **~29 que usan el vocabulario como adorno** místico o conspirativo
(Matrix, geometría sagrada, 666, activación del ADN, numerología).

**Y la asimetría de alcance es el dato importante:**

| | Ejemplo | Alcance |
|---|---|---|
| Pseudomatemática | «descubrió la Matrix» (@thedarshakrana) | **❤ 25.202** |
| Matemática real | «sigue el álgebra, no la interpretación» (@mathelirium) | ❤ 1.695 |
| Matemática real | guía de tests estadísticos (@RaziaAliani) | ❤ 491 |
| Matemática real | Tibshirani / Lasso (@probnstat) | ❤ 218 |

> **La pseudomatemática viraliza ~15× más que la matemática real.** Eso es la
> confirmación empírica, en el propio archivo del usuario, de la doctrina Thorp:
> *cuando la multitud dice una cosa y las matemáticas dicen otra, confía en las
> matemáticas* — porque la multitud premia sistemáticamente lo que **suena**
> matemático sobre lo que **es** matemático.

## Doctrina central — los tres filtros
1. **Orden de aprendizaje (clásico).** Primero **lógica** (da el método), luego
   **matemática** (no requiere experiencia ni trasciende la imaginación), luego
   **ciencias naturales**. Quien salta a la conclusión sin lógica, no está
   haciendo matemática. — <https://x.com/AHomelyHouse/status/1996385782295069080>
2. **Sigue el álgebra, no la interpretación.** «La mecánica cuántica tiene fama
   de mística sobre todo porque la gente se salta las reglas y salta a las
   interpretaciones. Aquí hacemos lo contrario: partimos de las reglas, seguimos
   el álgebra, y dejamos que la imagen sea el cálculo.»
   — <https://x.com/mathelirium/status/2006351810940768310>
   *Regla operativa:* si un texto usa términos matemáticos pero **no hay un
   cálculo que se pueda rehacer**, es adorno.
3. **Falsabilidad y falacias.** Toda afirmación cuantitativa debe decir dónde
   **dejaría** de ser cierta (Hamming). Repasar falacias lógicas frecuentes:
   <https://x.com/KnowledgeOfOld/status/2033457903261069480>

## Qué NO hacer / compuertas 🚦
- 🚦 **No confundir alcance con validez.** Likes/RT no son evidencia: en este
  corpus correlacionan **inversamente** con el rigor.
- 🚦 **No citar un bookmark como fuente matemática** sin verificar el cálculo
  aparte (usar [[wolfram-forensic-engine]]). **Curar ≠ firmar**: tener un
  bookmark no implica que el usuario lo suscriba ([[feedback_uso_bookmarks_archivo]]).
- 🚦 **No descalificar por el tema, sino por el método.** Un texto sobre física
  cuántica puede ser riguroso; uno sobre finanzas puede ser puro humo. El
  criterio es *¿se puede rehacer el cálculo?*, no la etiqueta del asunto.
- 🚦 **No `Read` el `bookmarks.json`** (7 MB) — usar siempre
  `scripts/minar_matematica.py` ([[eficiencia-generacion-respuestas]]).
- 🚦 **No inventar bookmarks ni métricas.** Solo lo que devuelve el script.
- 🚦 **No presentar este filtro como juicio sobre creencias personales del
  usuario.** Distingue *afirmación verificable* de *creencia*; la creencia es
  legítima, pero no entra como dato en un informe de negocio o técnico.

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Aislar la afirmación** cuantitativa concreta (número, fórmula, modelo).
2. **Filtro 1 — lógica:** ¿la conclusión se sigue de las premisas? ¿hay falacia?
3. **Filtro 2 — cálculo rehacible:** ¿puedo reproducir el número? Si no hay
   datos ni método, se marca **adorno**, no matemática.
4. **Filtro 3 — falsabilidad:** ¿bajo qué condición sería falsa? Si no hay
   ninguna, no es una afirmación científica.
5. **Verificar** lo que sobreviva con [[wolfram-forensic-engine]].
6. **Anclar** (si es para el Alfa Lab) la ecuación a una de las 17 de Stewart.
7. **Reportar** con URL canónica y el veredicto: *riguroso · adorno · ruido*.

Para minar un corpus:
```bash
python "C:\Users\datos\.claude\skills\rigor-matematico-filtro-pseudociencia\scripts\minar_matematica.py" --top 30
```
```bash
python "C:\Users\datos\.claude\skills\rigor-matematico-filtro-pseudociencia\scripts\minar_matematica.py" --pseudo --top 20
```

## El núcleo matemático aprovechable del corpus (lo que SÍ hay)
- **Estadística aplicada:** guía de elección de test (Z, T…) —
  <https://x.com/RaziaAliani/status/2002276588038336525> · Tibshirani/**Lasso**
  y modelos dispersos — <https://x.com/probnstat/status/1966249316617748610>
- **Forma cerrada / sucesiones:** fórmula de **Binet** para Fibonacci —
  <https://x.com/scievision369/status/2021057876576608383>
- **IA matemática:** **RoPE** (rotary positional encoding) —
  <https://x.com/tslaming/status/2012374751982092501> · formalización de la
  neurona artificial — <https://x.com/antoniolupetti/status/2041155213776892240>
- **Cognición cuantitativa:** Kahneman, Sistema 1 vs Sistema 2 —
  <https://x.com/JaynitMakwana/status/2053028240013561885> · fallas
  epistemológicas humano-LLM —
  <https://x.com/ValerioCapraro/status/2003457899805233538>

## HUECO detectado del corpus (brecha abierta)
El archivo **no tiene base matemática formal**: falta álgebra lineal seria,
probabilidad rigurosa, optimización, teoría de grafos y criptografía
demostrativa — justo lo que exigen el **Pilar VII (Gerko / $X^TX$)** y el
**Ecuador Quantitative Cryptography Lab**. Además, la taxonomía de
`analizar_temas.py` **no tiene un tema «matemáticas»**, por eso el router
genérico devuelve blockchain/finanzas/pensamiento-crítico.
**Acciones sugeridas:** (a) añadir el tema `matematicas` a la taxonomía;
(b) alimentar el corpus desde fuentes formales (MIT OCW 6.034 ya archivado,
cuaderno NotebookLM «Math» id `00a993be`, Stewart) en vez de X.

## Cómo depurar si falla
- ¿Devuelve 0 rigurosos? Revisar que los regex no lleven grupos de captura con
  `findall` (usar `finditer`+`group(0)`) — ese fue el bug original.
- ¿Demasiado ruido? Subir el umbral `nr >= 3` en `analizar()`.
- ¿Corpus distinto? Pasar `--corpus <ruta.json>` con campos `text`, `url`,
  `author_handle`, `metrics`.

## Portabilidad (revisar el 20% al reusar)
Cambian: ruta del corpus y el esquema de campos. Los tres filtros y los
diccionarios de subdominio son estables y portables.

## Reuso (no empezar de cero)
Componer con [[doctrina-thorp-matematica-vs-multitud]],
[[metodo-hamming-preguntas-fundamentales]], [[wolfram-forensic-engine]],
[[winston-representacion-restricciones-ia]] y [[consulta-bookmarks-fdc-ec]].

## Ejemplos de invocación
- «¿Esta fórmula que me pasaron es matemática real o marketing?»
- «Mina las matemáticas de mis bookmarks y dime qué sirve.»
- «Antes de citar esto en el informe CAF, pásalo por el filtro de rigor.»
