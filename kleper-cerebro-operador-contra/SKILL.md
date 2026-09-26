---
name: kleper-cerebro-operador-contra
description: |
  Réplica del CEREBRO DEL OPERADOR (Kleper): no un archivo que recuerda,
  sino un cerebro que **DISCUTE CONTIGO**. Destilada del artículo de X
  «Obsidian: A Vault That Argues Back» (@Nazik2053, 29-jul-2026) y del
  clip `21 X.mp4` (grafo de conocimiento + lienzo de razonamiento con
  aristas etiquetadas que termina en lista de acciones).

  Tesis: todos los «segundos cerebros» hacen lo mismo — detectan
  duplicados, revelan patrones, marcan hilos abandonados. **Ninguno
  discrepa contigo.** Eso deja fuera la única función que evita
  decisiones malas.

  > «El mejor argumento contra tu última decisión ya está en tu archivo.
  > Lo escribiste hace ocho meses y lo olvidaste.»

  Distingue dos capas: la capa **DO** (qué encaja: extraer, indexar,
  vincular — que el usuario YA tiene con
  [[agente-local-autoreflexivo-bookmarks]]) y la capa **CONTRA** (qué NO
  encaja, y ambas partes salieron de ti): abogado del diablo,
  contradicciones internas, polinización entre dominios, y el
  **«yo fantasma»** — el usuario de hace seis meses debatiendo con el de
  hoy. Esta skill aporta la capa que falta.

trigger_phrases:
  - "cerebro de Kleper / réplica de mi cerebro"
  - "que me discuta / que me contradiga"
  - "abogado del diablo de esta decisión"
  - "capa CONTRA / pasada contraria"
  - "qué pensaba yo antes de esto"
  - "revisa si me estoy contradiciendo"
  - "yo fantasma"

idioma_de_salida: español
nivel: maestra / arquitectura cognitiva
dominio: memoria y decisión asistida
metadata:
  version: 1.0
  fecha: 2026-07-29
  fuentes:
    - https://x.com/Nazik2053/status/2082370975132225737 (artículo «Obsidian: A Vault That Argues Back»)
    - "E:\\vars\\var 9 FBSE\\...\\Adm Alfa Lab\\21 X.mp4 (17 s: grafo + lienzo de razonamiento)"
    - "E:\\vars\\var 9 FBSE\\...\\Adm Alfa Lab\\IA alfa lab by Patrick Winston.mp4 (46 min, SIN audio; ya destilado en [[winston-representacion-restricciones-ia]])"
  transcripcion_articulo: references/obsidian_vault_argues_back.md
  relacionada:
    - agente-local-autoreflexivo-bookmarks
    - graph-engineering-memoria-agentes
    - winston-representacion-restricciones-ia
    - doctrina-thorp-matematica-vs-multitud
    - selector-modelo-claude-optimo
    - auditoria-cognitiva-reflexiva
    - metodo-hamming-preguntas-fundamentales
---

# Skill `kleper-cerebro-operador-contra`

## La tesis

> «Todos los que construyen un segundo cerebro construyen lo mismo.
> Detecta duplicados, revela patrones, marca hilos abandonados.
> **Lo que ninguno hace es discrepar contigo.**»
>
> «Tus notas no son neutrales. Contienen varias versiones de ti, cada
> una con conclusiones distintas. El tú de 2023 pensaba X. El tú de hace
> seis meses pensaba lo contrario. Los dos siguen ahí. **Ninguno le
> habla al otro**, porque tú eras el único que sostenía la conversación.»

Kleper es esa conversación **sostenida por el sistema y no por ti**.

## Dos capas: DO y CONTRA

| Capa **DO** (qué encaja) | Capa **CONTRA** (qué NO encaja) |
|---|---|
| extraer ideas | abogado del diablo del contraargumento más fuerte |
| encontrar patrones | sacar a la luz contradicciones entre tus propias notas |
| vincular notas relacionadas | polinizar conceptos de dominios sin relación |
| resucitar trabajo viejo | **«yo fantasma»**: tú de hace 6 meses debatiendo con el de hoy |

🚦 **Tu situación real:** ya tienes la capa DO funcionando
([[agente-local-autoreflexivo-bookmarks]], `intereses-*`,
`linkedin-guardados-fedphd`: cosechan, clasifican, destilan skills).
**Lo que falta es CONTRA.** Esta skill no reemplaza nada: le pone la
otra mitad.

### Validación externa: el «Committee» (cosechado de OpenExecutive, 2026-08-30)
El proyecto **OpenExecutive** (8 agentes ejecutivos, Apache 2.0) implementa
exactamente esta capa con otro nombre: un **Committee** que ejecuta un **pase de
revisión adversarial** — los agentes **se critican entre sí antes** de que la
salida llegue al usuario. Es validación cruzada, **no consenso automático**.
Confirma que la capa CONTRA no es un lujo: es la pieza que separa un consejo útil
de una máquina de multiplicar confianza.

Y la crítica más aguda que recibió ese proyecto (Alejandro Téllez, LinkedIn) es
**la razón de ser de esta skill**:
> «Repartir la dirección entre ocho agentes basados en **el mismo modelo**: la
> diversidad funcional puede ser solo aparente… pueden **compartir errores de
> origen**. La tensión entre funciones no es un obstáculo; también es un
> **mecanismo de control**.»

🚦 **Consecuencia operativa:** varios agentes del mismo modelo **no** son varias
opiniones. Para que CONTRA sea real hay que **diseñar** la discrepancia:
① rol explícitamente adversarial, ② **sin contexto compartido** con quien produjo
la tesis, ③ preferiblemente **otro modelo o parámetros distintos**, ④ trazabilidad
de quién validó qué. Ver el patrón completo en
[[arquitectura-consejo-multiagente]].

## Por qué un bucle y no una pestaña de chat

> «Ya puedes abrir Claude, pegar una nota y escribir "argumenta en
> contra". Funciona **una vez**. Cierras la pestaña y el argumento se
> detiene.»

El valor aparece cuando el argumento **corre solo**. La fricción que el
archivo se creó para eliminar —encontrar notas— se sustituye por la
fricción sobre la que se quedó callado: **encontrar contradicciones**.

## El campo que lo desbloquea todo: `supuesto`

En la ingesta (Loop 1) cada nota registra, además de su contenido, un
campo de **AFIRMACIÓN** y un campo de **SUPUESTO**.

> «Sin él, las contradicciones parecen desacuerdos. Con él, parecen
> **discusiones sobre premisas**. Dos notas que parecen chocar
> normalmente descansan sobre supuestos distintos: haz explícito el
> supuesto y la discusión se vuelve tratable.»

Esto es Winston puro: **una representación que expone la restricción**
([[winston-representacion-restricciones-ia]]). El supuesto es la
restricción oculta; escribirlo la vuelve operable.

## LOOP 1 — ingesta con etiquetas de argumento (especificación literal)

```
TRIGGER: new note added or existing note edited
STEPS:
  1. Read the note
  2. Extract the core claim being made
  3. Identify the assumption behind that claim
  4. Add three fields to frontmatter:
     ---
     claim: [what the note asserts]
     assumption: [what must be true for the claim to hold]
     ready_for_contra: false
     ---
  5. If the assumption is unclear, flag the note for review
VERIFY: every processed note has claim and assumption filled
STOP:   verify passes, or flag after 2 retries
```

🚦 **Son TRES campos, no dos.** `ready_for_contra: false` es la
compuerta: una nota no entra al Loop 2 hasta que **tú** la marcas en
`true`. Sin ese campo el bucle argumenta contra material a medio cocinar.

Equivalente en español para el vault del usuario:
```yaml
---
claim: "El inventario congelado se descongela bajando precio 8%."
assumption: "La demanda es elástica al precio en este segmento."
ready_for_contra: false
contexto: "Mobijuesa · bodegas · jul-2026"
fecha: 2026-07-29
---
```

## LOOP 2 — el bucle contrario (especificación literal)

`TRIGGER: every 6 hours`

```
STEPS:

Pass 1 - steelman:
  Pick 5 notes at random. For each, write the strongest
  counterargument using material from other notes in the
  vault. Save as: [note-title]-contra.md

Pass 2 - contradictions:
  Compare assumption fields across all notes. Find pairs
  where one note's assumption conflicts with another
  note's claim. Log the collision in memory/CONTRA.md
  with direct quotes from both notes.

Pass 3 - cross-domain:
  Pick one technical note and one personal or
  philosophical note. Force an analogy between them.
  Record it in memory/BRIDGES.md.

Pass 4 - ghost self:
  Load all notes older than 6 months on the same topic
  as any note edited in the last 14 days. Write a short
  paragraph in the voice of past-you reacting to
  current-you. Save to memory/GHOST.md.

VERIFY: each pass writes at least one entry.
        Pass 2 collisions include real quotes.
        Pass 4 uses only quotes from old notes.
STOP:   all four passes complete, or a pass logs and moves on
```

**Los cuatro archivos de salida son la arquitectura**, no un detalle:

| Pasada | Salida | Modelo |
|---|---|---|
| 1 · steelman | `[titulo-nota]-contra.md` (uno por nota) | fuerte |
| 2 · contradicciones | `memory/CONTRA.md` (bitácora de choques) | económico |
| 3 · entre dominios | `memory/BRIDGES.md` (puentes) | fuerte |
| 4 · yo fantasma | `memory/GHOST.md` (voz del pasado) | fuerte |

Detalles que cambian el resultado y son fáciles de perder:
- Pasada 1: **5 notas al azar**, no las que te convienen.
- Pasada 2: compara `assumption` de una contra `claim` de otra — **no
  claim contra claim**. El choque vive entre premisa y afirmación.
- Pasada 3: fuerza el cruce **una nota técnica × una personal o
  filosófica**. El azar es el mecanismo.
- Pasada 4: **solo** notas de más de 6 meses, y solo sobre temas que
  tocaste en los **últimos 14 días**. Es el pasado interpelando lo que
  estás moviendo AHORA.

> «La Pasada 4 es la que cambia cómo usas el archivo. Leer al tú del
> pasado decirle al tú del futuro que estás racionalizando **se siente
> distinto** que leer una lista de ideas parecidas.»

## PRUEBA MANUAL — el prompt que va PRIMERO (literal)

El artículo es explícito: antes de programar nada, correr esto en un
solo chat contra notas reales. **Si lo que vuelve te hace repensar algo,
el bucle se gana el calendario. Si no, no se automatiza.**

```
Read every note in [folder].

For each note:
1. Extract the core claim
2. Find one other note where the assumption conflicts
   with this claim
3. Write the steelman of the opposite position, using
   direct quotes from both notes

Success criteria (strict, no soft passes):
- every steelman quotes both notes directly
- every contradiction pair identifies the assumption gap
- no vague "you might reconsider X" output

LOOP PROTOCOL, repeat every turn:
1. PLAN   - state the single next step
2. DO     - produce or improve the output
3. VERIFY - score 1-10 on each criterion, be brutally honest
4. DECIDE - if every criterion is 8+, print "FINAL" and stop

Begin. Run the loop until FINAL.
```

🚦 **El `LOOP PROTOCOL` es la pieza más transferible del artículo** y
sirve mucho más allá de este caso: PLAN → DO → VERIFY (puntuar 1-10,
brutalmente honesto) → DECIDE (si todo ≥8, imprimir «FINAL» y parar).
Es un arnés de autoverificación con **criterio de parada explícito** —
lo contrario de «mejóralo un poco más» infinito. Los criterios de éxito
son **estrictos y sin aprobados blandos**: prohibido el «podrías
reconsiderar X» genérico; cada steelman **cita literalmente ambas
notas**.

## Reparto de modelos (usa [[selector-modelo-claude-optimo]])
El artículo lo dice igual que tu doctrina: **capacidad = dificultad.**
- **Modelo fuerte** (Opus/Fable): abogado del diablo, polinización, yo
  fantasma — requieren juicio.
- **Modelo económico** (Haiku/Sonnet): etiquetar, indexar, parsear,
  detectar contradicciones, extraer citas.
- «No gastas el modelo caro en revisar un nombre de archivo.»

## 🚦 Compuertas (las reglas duras)

- 🚦 **NUNCA fusionar automáticamente las contradicciones.**
  «Un abogado del diablo es una **sugerencia, no un veredicto**. El
  bucle expone, **tú decides**.» El fallo concreto que advierte el autor:
  fusionará dos notas sobre «dejar a un cliente malo» que en realidad
  eran **dos clientes distintos**, y perderás el razonamiento que hacía
  correctas a ambas en su momento.
- 🚦 **Dos notas que se contradicen no están necesariamente
  equivocadas**: pueden ser de contextos, restricciones o fases
  distintas.
- 🚦 **Probarlo a mano ANTES de automatizar.** Correr la pasada en un
  chat contra notas reales varias veces. «Si lo que vuelve realmente te
  hace repensar algo, el bucle se gana el calendario. **Si no, no lo
  automatices.**»
- 🚦 **No programar todo el día uno.** «Un bucle corriendo contra tres
  notas alucinará conexiones y te entrenará a ignorar la salida.» Ese es
  el modo de fallo más caro: no es el error, es **perder la confianza**.
- 🚦 **Curar ≠ firmar** (doctrina de la casa): que Kleper exponga una
  contradicción no la convierte en verdad ni en decisión.

## Orden de construcción (no negociable)

1. **Loop 1 primero** (ingesta con `afirmacion` + `supuesto`). Dejar que
   el archivo acumule **al menos 3 semanas** de material: el bucle
   necesita contra qué argumentar.
2. **Pasada 2 (contradicciones) a mano**, unas cuantas veces. Si los
   choques te sorprenden → programarla.
3. **Pasada 4 (yo fantasma)**. Necesita **~3 meses** de historia.
   «El yo fantasma en un archivo joven es solo adivinar.»
4. **Pasadas 1 y 3 al final.** «Son las divertidas, pero solo aterrizan
   cuando hay masa crítica.»

## PASOS A SEGUIR (plan de ejecución para este computador)

Estado real a 2026-07-29: **nada de esto está construido todavía.** Solo
existe la doctrina (este archivo) y la fuente. La secuencia es:

| # | Paso | Quién | Bloquea a |
|---|---|---|---|
| **0** | **Elegir la carpeta-vault del piloto** (decisión del usuario) | usuario | todo |
| **1** | **Prueba manual** con el prompt `LOOP PROTOCOL` sobre esa carpeta. Sin automatizar nada | agente | 2 |
| **2** | **Veredicto honesto**: ¿te hizo repensar algo? Si NO → se detiene aquí y no se automatiza | usuario | 3 |
| **3** | Construir **Loop 1** (script que añade `claim`/`assumption`/`ready_for_contra` al frontmatter) | agente | 4 |
| **4** | Dejar **≥3 semanas** acumulando material etiquetado | tiempo | 5 |
| **5** | **Pasada 2** (contradicciones) a mano, varias veces. Si los choques sorprenden → programar | agente | 6 |
| **6** | **Pasada 4** (yo fantasma) — necesita **~3 meses** de historia | tiempo | 7 |
| **7** | **Pasadas 1 y 3** (steelman + entre dominios) al final | agente | — |
| **8** | Programar Loop 2 cada 6 h (Tarea programada de Windows) | agente | — |

**Candidatos a vault del piloto** (el paso 0 es tuyo):
- `E:\vars\var 8\...\Proyeccion Financiera\` — decisiones de Mobijuesa
  bodegas: pocas notas pero **decisiones vivas con supuestos explícitos**
  (la renta de 4,50 USD/m² marcada como «a validar» es un `assumption`
  de libro).
- Actas del comité QVP — muchas semanas, ideal para Pasada 2.
- `E:\vars\var 5\X-com guardados\analisis\` — ya tiene análisis
  acumulados del pipeline DO.

🚦 **No empezar por el corpus de 5.550 bookmarks.** No son *tus*
afirmaciones: son material curado de terceros («curar ≠ firmar»). El
yo-fantasma solo funciona sobre notas donde **tú** afirmaste algo.

## Costo (del artículo)
Loop 1 corre una vez por cambio de nota (modelo económico, fracción de
centavo, no recurrente). Loop 2 son 4 pasadas cada 6 h = **16 pasadas
al día ≈ el precio de un café**. «Si el bucle atrapa una sola
contradicción que detiene una decisión mala, se paga un año de sí mismo
en una tarde.»

## La mecánica visual (del clip `21 X.mp4`)
17 segundos que muestran el resultado bien hecho:
1. Un **grafo de conocimiento** donde el nodo de la decisión concentra
   las aristas (ver [[graph-engineering-memoria-agentes]]).
2. Un **lienzo de razonamiento** donde la afirmación se descompone en
   bloques numerados y **cada arista lleva etiqueta con el POR QUÉ del
   enlace** (no solo «se relaciona con»).
3. Termina en **resumen → lista de acciones ejecutables**.

Lección: la arista etiquetada es lo que convierte un mapa bonito en un
cerebro. Un enlace sin razón es decoración.

## Aplicación a los frentes reales del usuario
- **QVP / cuarto de guerra**: antes de cada comité, Pasada 2 sobre las
  actas — ¿el comité se está contradiciendo entre semanas?
- **Mobijuesa / bodegas**: Pasada 4 sobre los supuestos de renta
  (el 4,50 USD/m² que quedó marcado como «a validar»).
- **EcuaLedger / fondos BID-CAF**: Pasada 1 antes de postular — el
  contraargumento más fuerte a la propuesta, con material propio.
- **EPACEM forense**: Pasada 2 es literalmente el «olfato Madoff» de
  [[doctrina-thorp-matematica-vs-multitud]] institucionalizado.

## El cierre del artículo (vale citarlo entero)
> «Tu mejor asesor no es Claude. Es **tú de hace ocho meses**, todavía
> escribiendo en tu archivo, esperando que algo traduzca lo que
> escribiste a un idioma que el tú de hoy sí escuche.
> **El bucle es ese traductor.**»

## Relacionado
- [[agente-local-autoreflexivo-bookmarks]] — la capa DO que ya existe.
- [[graph-engineering-memoria-agentes]] — el grafo como memoria permanente.
- [[winston-representacion-restricciones-ia]] — el supuesto como restricción expuesta.
- [[doctrina-thorp-matematica-vs-multitud]] — disenso contra el consenso.
- [[selector-modelo-claude-optimo]] — reparto fuerte/económico por pasada.
- [[metodo-hamming-preguntas-fundamentales]] · [[auditoria-cognitiva-reflexiva]].
