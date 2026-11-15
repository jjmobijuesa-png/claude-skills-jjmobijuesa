---
name: selector-modelo-claude-optimo
description: |
  ⭐ HABILIDAD DE EFICIENCIA PERMANENTE. Ante CADA nuevo prompt, tarea o
  indicación del usuario, evalúa cuál de los modelos Claude es el más
  apropiado — Haiku 5.5, Sonnet 5.5, Opus 5.5 o Fable 5.2 — y lo
  recomienda en UNA línea antes de trabajar, sólo si conviene cambiar
  del modelo actual.

  El criterio no es "el más barato" ni "el más potente": es el modelo
  cuya capacidad iguala la dificultad real de la tarea. Pagar Opus por
  renombrar archivos es desperdicio; usar Haiku para un dictamen
  jurídico es un error caro disfrazado de ahorro.

  Incluye enrutador heurístico (`sugerir_modelo.py`), tabla de
  capacidades y precios, la segunda palanca (nivel de `effort`), la
  doctrina de prompting de Fable (se le QUITA andamiaje), y la regla
  dura: **el agente recomienda, NUNCA cambia de modelo por su cuenta ni
  degrada por costo.**

trigger_phrases:
  - "qué modelo uso para esto"
  - "¿conviene Opus o Sonnet aquí?"
  - "cuál es el modelo más apropiado"
  - "esto es caro / optimiza el costo"
  - "haiku, sonnet, opus, fable"
  - (además: se evalúa en silencio ante CADA tarea nueva)

idioma_de_salida: español
nivel: permanente / transversal
dominio: eficiencia operativa del agente
metadata:
  version: 2.0
  fecha: 2026-11-13
  script: scripts/sugerir_modelo.py
  fuente_de_verdad: skill `claude-api` (nunca de memoria)
  relacionada:
    - eficiencia-generacion-respuestas
    - llave-maestra-autoaprendizaje-ia
    - doctrina-thorp-matematica-vs-multitud
    - prompting-opus-5-doctrina
    - cosechar-repositorios-de-agentes
---

# Skill `selector-modelo-claude-optimo`

## Doctrina

Cada tarea tiene una **dificultad real**; cada modelo tiene un **costo
por capacidad**. La eficiencia no es elegir siempre el más barato ni
siempre el más potente: es **hacer coincidir la capacidad con la
dificultad**. Un mismo día de trabajo puede pedir los cuatro modelos.

Aplica la lógica de [[doctrina-thorp-matematica-vs-multitud]]: la
decisión se toma por criterio explícito, no por costumbre ni por
impulso de «usar lo mejor porque sí».

## 🚦 Reglas duras (no negociables)

- 🚦 **El agente RECOMIENDA; el usuario DECIDE.** Nunca se cambia de
  modelo por cuenta propia, y **nunca se degrada por ahorrar costo** —
  esa es una decisión del dueño de la cuenta, no del agente.
- 🚦 **Nada de precios ni IDs de memoria.** Los modelos, precios y
  límites cambian. Antes de citarlos, **cargar la skill `claude-api`**
  (es su regla explícita: «never answer from memory»). La tabla de
  abajo es referencia con fecha, no verdad permanente.
- 🚦 **Silencio si el modelo actual ya es el correcto.** No molestar con
  una recomendación en cada turno — sólo hablar cuando cambiar aporta
  algo real. Coherente con [[eficiencia-generacion-respuestas]].
- 🚦 **Nunca cambiar de modelo a mitad de una tarea larga** sin avisar:
  se pierde la caché de prompt (los prefijos cacheados son por modelo)
  y se paga el prefijo completo de nuevo.
- 🚦 **Un indicador de la CLI no existe hasta que `claude --help` lo
  muestra.** Verificado el 13-nov-2026: un hilo viral recomendaba
  `claude --model opus --advisor fable`; **`--advisor` no existe**.
  Ver «Lo que la CLI sí ofrece».

## 🚦 Fable 5.2: ventana hasta el 16-nov-2026, techo del 50 % del plan

Confirmado por Francisco el **14-nov-2026**: este plan **sí** da acceso a
Fable, pero **sólo hasta el 16-nov-2026** y consumiendo **como máximo el 50 %
del plan**.

Por eso **«se reserva Fable para más adelante» dejó de ser consejo válido**: no
hay más adelante. Dentro de la ventana se gasta en lo que sólo Fable hace —el
atasco de semanas, la corrida autónoma de horas, el proyecto entero reescrito
de una pasada— y todo lo demás se queda en Opus 5.5, porque medio plan a
$8/$40 se agota rápido.

**Pasado el 16-nov-2026 esta sección caduca:** comprobar con `/model` en la
aplicación antes de volver a ofrecer Fable. La prueba por CLI anidada
(`claude --model fable ... -p`) responde «Not logged in» y no sirve.

## Las tres compuertas de Fable, y la cartera por hilo

Que una tarea sea difícil **no basta**. Pasan las tres o no pasa:

| # | Compuerta | Si falla |
|---|---|---|
| 1 | **Dificultad** — ¿excede de verdad a Opus 5.5? | Queda en Opus 5.5 |
| 2 | **Retención** — ¿el material puede quedar retenido 30 días? | **Prohibido** |
| 3 | **Ventana** — ¿están los insumos hoy? | No entra |

La compuerta 2 la gobierna [[gobernanza-datos-financieros-ia]], que es la
skill madre de qué dato sale y cuál no.

🚦 **La compuerta 2 no se negocia.** Fable exige retención de 30 días, así que
**nunca** recibe: cédulas ni nombres de personas naturales, escrituras o
certificados del expediente COAC, deuda personal, DSCR, cierres, los modelos de
Belén y San Sebastián con cifras reales, ni el Excel de flujo de caja.

**El rodeo que sí sirve:** cuando el trabajo es difícil pero el dato es
sensible, se le da **la estructura sin el dato**. Fable diseña el método o el
modelo en abstracto; Opus 5.5 lo rellena con las cifras reales en la máquina.

**Verde para Fable:** red de skills, matriz legislativa JRPFM, arquitectura
IBPP/EcuaLedger, marco de ingeniería de prompts, coherencia del libro Kleper.
**Ámbar, solo anonimizado:** arquitectura del CFO de 44 agentes ([[cfo-virtual-44-agentes]]), método del
motor de financiamiento, matriz de bancabilidad como instrumento.
**Rojo:** COAC, Belén, conciliación de cuentas (eso es Haiku 5.5: ver [[ahorro-de-tokens]]), flujo de
caja, ERP QVP (bloqueado), corpus de X y LinkedIn (es relogueo, no dificultad),
las 48 clases del Aula (es volumen, no dificultad).

**La prueba de una línea antes de lanzar:** «¿qué tiene esta tarea que Opus 5.5
no pueda?» Si no se contesta en una frase, no es de Fable.

Cartera completa, hilo por hilo, con el orden recomendado y los ejemplos de
prompt con andamiaje y sin andamiaje:
`references/cartera-fable-y-compuertas.md` (dentro de esta misma skill)

## Tabla de decisión — qué modelo para qué tarea

| Si la tarea es… | Modelo | Por qué |
|---|---|---|
| Clasificar, etiquetar, renombrar, extraer campos, contar, convertir formatos, triage de bandeja, trabajo en lote | **Haiku 5.5** | Es mecánica: no necesita criterio, necesita velocidad y volumen. **Hoy cuesta 1/40 de Opus y ya tiene 1M de contexto** |
| Redactar un correo o carta, resumir, traducir, generar un Word/Excel/PDF estándar, consultar el corpus curado, maquetar una landing | **Sonnet 5.5** | Calidad cercana a Opus en redacción y código, a la mitad del costo |
| Analizar finanzas (QVP, Mobijuesa), dictamen o memo jurídico, auditoría forense, valoración, depurar un fallo, construir o mejorar skills, código agéntico, sesión de varios pasos, decidir con criterio | **Opus 5.5** | Razonamiento profundo y autonomía larga. **Default de la casa y default documentado de Anthropic** |
| El problema que no se ha podido resolver, una corrida autónoma de horas, migrar o reescribir un proyecto entero de una sola vez | **Fable 5.2** | Techo de capacidad, el doble que Opus. 🚦 **Ventana hasta el 16-nov-2026, techo 50 % del plan**: no se reserva, se gasta o se pierde |

**Ante la duda → Opus 5.5.** Degradar es decisión explícita del
usuario, nunca silenciosa.

🚦 **Fable no es «Opus pero mejor».** Es el tope de dificultad, y su
prompting es distinto (ver abajo). Si la tarea cabe en Opus 5.5, Fable
sólo duplica la factura.

## Referencia de capacidades y precio

> Fuente: skill `claude-api`, caché **2026-11-03**, verificada el
> 13-nov-2026. Precios por millón de tokens (entrada / salida).
> **Referencia 1× = Opus 5.5.**

| Modelo | ID | Contexto | Precio | Relativo |
|---|---|---|---|---|
| **Haiku 5.5** | `claude-haiku-5-5` | 1M · salida 128K | **$0,10 / $0,50** (hasta 100K de prompt; $0,50 / $2,50 por encima) | **0,025×** |
| **Sonnet 5.5** | `claude-sonnet-5-5` | 1M · salida 128K | $2 / $10 · caché $0,10 | **0,5×** |
| **Opus 5.5** | `claude-opus-5-5` | 1M · salida 128K | $4 / $20 · caché $0,20 | **1× (referencia)** |
| **Fable 5.2** | `claude-fable-5-2` | 1M · salida 128K | $8 / $40 · caché $0,20 | **2×** |

Modo rápido: Opus 5.5 a $8 / $40 (2×) · Fable 5.2 a $16 / $80 (4×).

### Lo que cambió respecto de la v1 de esta skill (24-jul-2026)

Tres cosas que la v1 afirmaba y **hoy son falsas**:

1. **«Haiku es el único con 200K de contexto».** Haiku 5.5 tiene **1M**.
   Ya no se descarta por contexto; se descarta por criterio.
2. **«Haiku no admite `effort`».** Haiku 5.5 **sí** lo admite
   (`low` a `max`, **default `medium`**).
3. **Precio de Haiku.** Pasó de $1 / $5 a **$0,10 / $0,50**: de 0,2× a
   **0,025×**. El trabajo mecánico en lote es ahora casi gratis en
   comparación. Si algo se hacía a mano «porque Haiku salía caro», esa
   razón desapareció.

Y el default de la casa sube de Opus 4.8 a **Opus 5.5**, que además
**bajó** de $5 / $25 a $4 / $20.

## La segunda palanca: esfuerzo

Cambiar de modelo no es el único ajuste. El nivel de **esfuerzo**
(`low` → `medium` → `high` → `xhigh` → `max`) mueve calidad y costo
dentro del mismo modelo, **y su valor por defecto ya no es el mismo en
todos**:

| Modelo | Default | Cómo ajustarlo |
|---|---|---|
| **Haiku 5.5** | `medium` | `low` para lote puro |
| **Sonnet 5.5** | `high` | Niveles **recalibrados**: empezar en `medium` para código agéntico, `low` para conversación |
| **Opus 5.5** | **`medium`** | 🚦 Es un nivel **por debajo** del default de Opus 5. Para trabajo sensible, **subirlo a mano** |
| **Fable 5.2** | `high` | Empezar en `high`. `xhigh` **sólo donde se midió** una mejora; `max` para medir el techo |

🚦 **En Fable 5.2 el esfuerzo casi no cambia el largo de la respuesta.**
Si quiere algo corto o largo, **dígalo en el prompt**: subir o bajar
`effort` no lo hará.

## Prompting de Fable: se le QUITA andamiaje

El hallazgo que más dinero ahorra, y el menos intuitivo:

> **Los prompts escritos para modelos anteriores suelen ser demasiado
> prescriptivos en Fable y le BAJAN la calidad de salida.**

Es decir: pegarle a Fable el prompt afinado para Opus lo empeora. Hay
que quitarle los pasos numerados, las listas de comprobación y el
«primero haz A, luego B», y darle en cambio **la especificación
completa del resultado** para dejarlo correr. Mismo mecanismo ya
documentado para Opus 5 en [[prompting-opus-5-doctrina]], un grado más
pronunciado.

Dos consecuencias prácticas:

- Un turno de Fable puede durar **muchos minutos**. No es que se colgó.
- Fable exige **retención de datos de 30 días** (no funciona con
  retención cero) y **no tiene Priority Tier** (tampoco Opus 5.5,
  Sonnet 5.5 ni Haiku 5.5).

## Lo que la CLI sí ofrece (verificado 13-nov-2026)

```bash
claude --model fable|opus|sonnet|<id-completo>
claude --effort low|medium|high|xhigh|max
claude --fallback-model <lista,separada,por,comas>
claude --max-budget-usd <monto>        # sólo con --print
claude --autocompact auto|<100k-1M>
```

- `--fallback-model` acepta **lista**, y reintenta el principal al
  inicio de cada turno. Es la red de seguridad cuando el modelo de
  cabecera está saturado.
- `--max-budget-usd` es un **tope duro en dólares**, pero sólo en modo
  `--print`. Para una corrida larga desatendida es la única brida real.
- 🚦 **No existe `--advisor`.** El concepto «asesor» existe en la API
  (la herramienta advisor, con reglas de emparejamiento ejecutor y
  asesor), no como indicador de esta CLI.
- Los ajustes por modelo van en `~/.claude/settings.json` →
  `modelSettings` (este equipo ya tiene `claude-opus-5` con
  `autoCompactWindow`).

## Formato de la recomendación (cuando corresponde)

Una sola línea, antes de empezar, sin ceremonia:

> 💡 *Esto es redacción de documento — **Sonnet 5.5** lo hace igual de
> bien a la mitad del costo. ¿Cambio o sigo en Opus?*

Y si ya se está en el modelo correcto: **no se dice nada**.

## Enrutador heurístico (script)

```bash
"C:\Users\datos\.notebooklm-venv\Scripts\python.exe" "C:\Users\datos\.claude\skills\selector-modelo-claude-optimo\scripts\sugerir_modelo.py" "<texto de la tarea>"
```

Puntúa señales por palabras clave y cae a Opus cuando no hay señal
clara. 🚦 **Su diccionario `INFO` quedó en la generación anterior**
(Haiku 4.5 / Sonnet 5 / Opus 4.8 / Fable 5 y sus precios): sus
*veredictos* siguen sirviendo, sus *cifras* no. Actualizarlo es el
pendiente abierto de esta skill.

🚦 Es una **ayuda heurística, no un oráculo**: acierta el patrón obvio,
no juzga el contexto. Si la tarea suena simple pero el resultado se
firma o se envía a un tercero, sube un nivel.

## Aplicación a los frentes del usuario

| Frente | Modelo habitual |
|---|---|
| Triage de inbox, cosecha de bookmarks y LinkedIn, renombrado en lote, OCR en serie | **Haiku 5.5** |
| Correos a socios, informes Word/Excel, landing Vista al Río, actas | **Sonnet 5.5** |
| War Room QVP, Mobijuesa, EcuaLedger jurídico, EPACEM forense, construir skills, fondos BID/CAF | **Opus 5.5** |
| Un cierre de proyecto completo en una corrida, o un problema atascado hace semanas | **Fable 5.2** |

## Cómo cambiar de modelo

En la aplicación de escritorio el selector está en la **interfaz**
(`/model`), no por comando de terminal. 🚦 Una invocación anidada de
`claude` desde el Bash de una sesión **no hereda la sesión de la app**
(responde «Not logged in»): no sirve para probar si un modelo está
disponible en el plan. Para eso, abrir `/model` en la app.

## Cómo depurar si falla

- **Recomienda Haiku para algo delicado**: falta señal de criterio en
  el texto; añadir el verbo real (analiza, dictamina) o subir a mano.
- **Siempre dice Opus**: no hay palabras clave — normal; Opus es el
  default deliberado.
- **Precios desactualizados**: cargar `claude-api` y actualizar la
  tabla y el diccionario `INFO` del script.
- **Fable entrega peor que Opus en la misma tarea**: casi siempre es el
  prompt, no el modelo. Quitarle el andamiaje (ver arriba).

## Portabilidad (revisar el 20%)

La tabla de precios e IDs (cambia con cada lanzamiento), los defaults
de `effort` por modelo, los indicadores de la CLI, y los pesos de
`SENALES`. La doctrina (capacidad = dificultad; recomendar sin
degradar; verificar antes de citar) es estable.

## Relacionado

- [[eficiencia-generacion-respuestas]] — misma familia: no gastar de más.
- [[prompting-opus-5-doctrina]] — quitar andamiaje; Fable lo lleva más lejos.
- [[escalera-prompting-prueba-del-techo]] — el escalón es de la tarea, no del modelo:
  diagnosticarlo antes de elegir.
- [[doctrina-thorp-matematica-vs-multitud]] — decidir por criterio explícito.
- [[cosechar-repositorios-de-agentes]] — cómo tratar un anuncio de modelo que llega por un hilo viral.
- [[bucle-verificacion-garantia-vs-sugerencia]] — un indicador no existe hasta que `--help` lo muestra.
- [[llave-maestra-autoaprendizaje-ia]] — esta skill se evalúa en cada tarea.
