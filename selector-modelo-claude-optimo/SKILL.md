---
name: selector-modelo-claude-optimo
description: |
  ⭐ HABILIDAD DE EFICIENCIA PERMANENTE. Ante CADA nuevo prompt, tarea o
  indicación del usuario, evalúa cuál de los modelos Claude es el más
  apropiado — Haiku 4.5, Sonnet 5, Opus 4.8 o Fable 5 — y lo recomienda
  en UNA línea antes de trabajar, sólo si conviene cambiar del modelo
  actual.

  El criterio no es "el más barato" ni "el más potente": es el modelo
  cuya capacidad iguala la dificultad real de la tarea. Pagar Opus por
  renombrar archivos es desperdicio; usar Haiku para un dictamen
  jurídico es un error caro disfrazado de ahorro.

  Incluye enrutador heurístico (`sugerir_modelo.py`), tabla de
  capacidades y precios, la segunda palanca (nivel de `effort` y modo
  rápido), y la regla dura: **el agente recomienda, NUNCA cambia de
  modelo por su cuenta ni degrada por costo.**

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
  version: 1.0
  fecha: 2026-07-24
  script: scripts/sugerir_modelo.py
  fuente_de_verdad: skill `claude-api` (nunca de memoria)
  relacionada:
    - eficiencia-generacion-respuestas
    - llave-maestra-autoaprendizaje-ia
    - doctrina-thorp-matematica-vs-multitud
    - memoria-financiera-inteligenciada
---

# Skill `selector-modelo-claude-optimo`

## Doctrina

Cada tarea tiene una **dificultad real**; cada modelo tiene un **costo
por capacidad**. La eficiencia no es elegir siempre el más barato ni
siempre el más potente: es **hacer coincidir la capacidad con la
dificultad**. Un mismo día de trabajo puede pedir los cuatro modelos.

Aplica la lógica de [[doctrina-thorp-matematica-vs-multitud]]: la
decisión se toma por criterio explícito, no por costumbre ni por
impulso de "usar lo mejor porque sí".

## 🚦 Reglas duras (no negociables)

- 🚦 **El agente RECOMIENDA; el usuario DECIDE.** Nunca se cambia de
  modelo por cuenta propia, y **nunca se degrada por ahorrar costo** —
  esa es una decisión del dueño de la cuenta, no del agente.
- 🚦 **Nada de precios ni IDs de memoria.** Los modelos, precios y
  límites cambian. Antes de citarlos, **cargar la skill `claude-api`**
  (es su regla explícita: "never answer from memory"). La tabla de
  abajo es referencia con fecha, no verdad permanente.
- 🚦 **Silencio si el modelo actual ya es el correcto.** No molestar con
  una recomendación en cada turno — sólo hablar cuando cambiar aporta
  algo real. Coherente con [[eficiencia-generacion-respuestas]]
  (entregar sólo el delta).
- 🚦 **Nunca cambiar de modelo a mitad de una tarea larga** sin avisar:
  se pierde la caché de prompt (los prefijos cacheados son por modelo)
  y se paga el prefijo completo de nuevo.

## Tabla de decisión — qué modelo para qué tarea

| Si la tarea es… | Modelo | Por qué |
|---|---|---|
| Clasificar, etiquetar, renombrar, extraer campos, contar, convertir formatos, triage de bandeja, trabajo en lote | **Haiku 4.5** | Es mecánica: no necesita criterio, necesita velocidad y volumen |
| Redactar un correo o carta, resumir, traducir, generar un Word/Excel/PDF estándar, consultar el corpus curado, maquetar una landing | **Sonnet 5** | Calidad cercana a Opus en redacción y código, a una fracción del costo |
| Analizar finanzas (QVP, Mobijuesa), dictamen o memo jurídico, auditoría forense, valoración, depurar un fallo, construir/mejorar skills, sesión agéntica de varios pasos, decidir con criterio | **Opus 4.8** | Razonamiento profundo + autonomía larga. **Default de la casa** |
| **Código agéntico difícil**, refactor multi-archivo, feature de punta a punta, coordinar subagentes, revisión de código de alta precisión | **Opus 5** (`claude-opus-5`) | Nuevo tope Opus para lo agéntico/código. Darle la especificación COMPLETA y dejarlo correr. Prompting propio → [[prompting-opus-5-doctrina]] |
| El problema que no se ha podido resolver, una corrida autónoma de horas, migrar/reescribir un proyecto entero de una sola vez | **Fable 5** | Techo de capacidad histórico. Se paga el doble que Opus: se reserva |

**Ante la duda → Opus 4.8** (default de la casa; degradar es decisión
explícita del usuario, nunca silenciosa). **Para código agéntico duro
sube a Opus 5**; su prompting cambia (responde/narra/delega más y se
autoverifica solo → se le QUITA andamiaje): ver [[prompting-opus-5-doctrina]].
🚦 Precio/posición exacta de Opus 5 vs Fable 5: confirmar en `claude-api`
(la caché a 2026-06-24 aún no listaba Opus 5).

## Referencia de capacidades y precio

> Fuente: skill `claude-api`, caché **2026-06-24**. **Verificar antes
> de citar.** Precios por millón de tokens (entrada / salida).

| Modelo | ID | Contexto | Precio | Costo relativo |
|---|---|---|---|---|
| **Haiku 4.5** | `claude-haiku-4-5` | **200K** · salida 64K | $1 / $5 | **0,2×** |
| **Sonnet 5** | `claude-sonnet-5` | 1M · salida 128K | $3 / $15 — **intro $2 / $10 hasta 31-ago-2026** | **0,4×** hoy |
| **Opus 4.8** | `claude-opus-4-8` | 1M · salida 128K | $5 / $25 | 1× (referencia) |
| **Fable 5** | `claude-fable-5` | 1M · salida 128K | $10 / $50 | **2×** |

Diferencias que importan al elegir:

- **Haiku 4.5 es el único con 200K de contexto** (los otros tienen 1M).
  Para corpus grandes (bookmarks, un libro, un expediente completo) se
  descarta por contexto, no por capacidad.
- **Sonnet 5 está en precio introductorio hasta el 31-ago-2026** — hoy
  cuesta el 40% de Opus. Es la mejor relación calidad/precio del
  momento para producción de documentos.
- **Fable 5** tiene un perfil distinto: razonamiento siempre activo,
  turnos que pueden durar muchos minutos, clasificadores de seguridad
  que pueden rechazar temas de biología/ciberseguridad, y **exige
  retención de datos de 30 días** (no funciona con retención cero).
  No es "Opus pero mejor": es una herramienta para el tope de
  dificultad.

## La segunda palanca: esfuerzo y velocidad

Cambiar de modelo no es el único ajuste. Dentro de Opus 4.8 / Sonnet 5
/ Fable 5 existe el nivel de **esfuerzo** (`low` → `medium` → `high` →
`xhigh` → `max`; el default es `high`):

- Bajar a `medium` en trabajo rutinario ahorra tokens y tiempo sin
  perder calidad perceptible.
- Subir a `xhigh` es lo recomendado para lo más duro de código y
  trabajo agéntico.
- **Haiku 4.5 no admite `effort`** (da error): es la generación previa.

Y en Claude Code existe el **modo rápido** (`/fast`), disponible en
Opus 4.8/4.7: el mismo Opus con salida más veloz, a precio premium.
No degrada a un modelo menor.

## Formato de la recomendación (cuando corresponde)

Una sola línea, antes de empezar, sin ceremonia:

> 💡 *Esto es redacción de documento — **Sonnet 5** lo hace igual de bien
> al 40% del costo. ¿Cambio o sigo en Opus?*

Y si ya se está en el modelo correcto: **no se dice nada**.

## Enrutador heurístico (script)

```bash
"C:\Users\datos\.notebooklm-venv\Scripts\python.exe" "C:\Users\datos\.claude\skills\selector-modelo-claude-optimo\scripts\sugerir_modelo.py" "<texto de la tarea>"
```

Puntúa señales por palabras clave, descarta Haiku si detecta corpus
grande, y cae a Opus 4.8 cuando no hay señal clara. Verificado con
tareas reales del usuario: lote mecánico → Haiku; correo + informe →
Sonnet; flujo de caja QVP → Opus; "no lo hemos podido resolver, déjalo
toda la noche sobre el proyecto entero" → Fable.

🚦 Es una **ayuda heurística, no un oráculo**: acierta el patrón obvio,
no juzga el contexto. Si la tarea suena simple pero el resultado se
firma o se envía a un tercero, sube un nivel.

## Aplicación a los frentes del usuario

| Frente | Modelo habitual |
|---|---|
| Triage de inbox, cosecha de bookmarks/LinkedIn, renombrado en lote | Haiku 4.5 |
| Correos a socios, informes Word/Excel, landing Vista al Río, actas | Sonnet 5 |
| War Room QVP, Mobijuesa, EcuaLedger jurídico, EPACEM forense, construir skills, fondos BID/CAF | Opus 4.8 |
| Un cierre de proyecto completo en una corrida, o un problema atascado hace semanas | Fable 5 |

## Cómo cambiar de modelo
En esta aplicación, el selector de modelo está en la **interfaz de la
app** (no por comando de terminal). El modo rápido se alterna con
`/fast` sobre Opus 4.8.

## Cómo depurar si falla
- **Recomienda Haiku para algo delicado**: falta señal de criterio en
  el texto; añadir el verbo real (analiza/dictamina) o subir a mano.
- **Siempre dice Opus**: no hay palabras clave — normal; Opus es el
  default deliberado.
- **Precios desactualizados**: cargar `claude-api` y actualizar la
  tabla + el diccionario `INFO` del script.

## Portabilidad (revisar el 20%)
La tabla de precios/IDs (cambia con cada lanzamiento), la fecha de fin
del precio introductorio de Sonnet 5, y los pesos de `SENALES`. La
doctrina (capacidad = dificultad; recomendar sin degradar) es estable.

## Relacionado
- [[eficiencia-generacion-respuestas]] — misma familia: no gastar de más.
- [[doctrina-thorp-matematica-vs-multitud]] — decidir por criterio explícito.
- [[llave-maestra-autoaprendizaje-ia]] — esta skill se evalúa en cada tarea.
