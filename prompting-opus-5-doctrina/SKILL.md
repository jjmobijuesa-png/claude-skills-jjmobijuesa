---
name: prompting-opus-5-doctrina
description: |
  Doctrina de PROMPTING para Claude Opus 5, destilada de la guía oficial
  de Anthropic (platform.claude.com/.../prompting-claude-opus-5).
  Aplica cuando el modelo activo es **Opus 5** (`claude-opus-5`) o al
  escribir prompts/system prompts destinados a Opus 5.

  Tesis central y contraintuitiva: la mayor parte de la doctrina es
  **QUITAR andamiaje**, no añadirlo. Opus 5 ya se autoverifica, se
  autocorrige y completa tareas enteras solo; las instrucciones que
  funcionaban en 4.x («doble-chequea», «verifica al final», «usa un
  subagente para revisar», «no pienses») ahora SOBRAN o hacen daño
  (sobre-verificación, fuga de tags, más costo sin mejor calidad).

  El otro eje: Opus 5 por defecto responde MÁS LARGO, narra más,
  delega más y expande el alcance. Se controla con instrucciones
  explícitas de concisión, cadencia y alcance (bloques listos abajo),
  no bajando el esfuerzo (el esfuerzo controla cuánto PIENSA, no cuánto
  DICE).

trigger_phrases:
  - "prompting para Opus 5"
  - "cómo le hablo a Opus 5"
  - "Opus 5 responde muy largo / narra demasiado"
  - "Opus 5 se sale del alcance / sobre-verifica"
  - "migrar mi prompt de Opus 4.8 a Opus 5"
  - "system prompt para Opus 5"

idioma_de_salida: español
nivel: aplicada
dominio: prompting / operación del modelo
metadata:
  version: 1.0
  fecha: 2026-07-24
  fuente: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
  modelo: claude-opus-5
  relacionada:
    - selector-modelo-claude-optimo
    - eficiencia-generacion-respuestas
    - llave-maestra-autoaprendizaje-ia
    - agentic-ai-hitchhiker-guide
---

# Skill `prompting-opus-5-doctrina`

## Qué cambia en Opus 5 (vs Opus 4.8)

Opus 5 rinde bien de entrada con los prompts que ya funcionaban en 4.8.
Los ajustes que casi siempre hacen falta salen de estos rasgos nuevos:

| Rasgo de Opus 5 | Consecuencia práctica |
|---|---|
| Responde **más largo** por defecto | Pedir concisión explícita (bajar el esfuerzo NO acorta lo visible) |
| **Narra más** durante trabajo agéntico | Definir cadencia de avisos |
| **Se autoverifica** solo | QUITAR instrucciones de verificación (causan sobre-verificación) |
| **Se autocorrige** solo | QUITAR «doble-chequea / re-verifica» |
| **Delega en subagentes** con facilidad | Poner tope/criterio de delegación |
| **Expande el alcance** de la tarea | Acotar el alcance explícitamente |
| Escribe **archivos más largos** en disco | Calibrar longitud de entregables |
| **1M de contexto** (default y máximo) | Instrucción/tool-calling estables en toda la ventana |
| **Pensamiento ON por defecto**; desactivarlo solo con effort ≤ `high` | Ver sección «thinking desactivado» |

## 🚦 La doctrina del QUITAR (lo más importante)

- 🚦 **Quita las instrucciones de verificación** («incluye un paso final
  de verificación», «usa un subagente para verificar»). En Opus 5
  causan sobre-verificación → tokens desperdiciados, cero mejora.
- 🚦 **Quita los «doble-chequea» / «re-verifica antes de responder».**
  Se compounden con su autocorrección nativa: más costo, igual calidad.
- 🚦 **Quita el andamiaje del harness** que añade pasos separados de
  verificación.
- 🚦 **En revisión de código, quita «solo reporta lo grave / sé
  conservador».** Opus 5 obedece literal y reporta MENOS. Pídele que
  reporte TODO y filtra en un paso aparte. (Aprovecha su alta precisión
  y recall — combina con [[doctrina-thorp-matematica-vs-multitud]]:
  cobertura primero, filtrado después.)
- 🚦 **Quita cualquier regla de «no pienses / no razones».** Aumenta la
  fuga de tags `<thinking>` en la salida visible.

## Bloques de prompt listos (canónicos, en inglés como los valida la guía)

> **System prompt base ya ensamblado** (los bloques combinados, inglés +
> español, con los condicionales marcados) →
> [`references/system_prompt_base_opus5.md`](references/system_prompt_base_opus5.md).
> Se pueden adaptar al español; el sentido es lo que importa. Positivos
> («haz esto así») funcionan mejor que negativos («no hagas»).

**Concisión (producto conversacional multi-turno):**
```
Keep responses focused, brief, and concise. Keep disclaimers and caveats short, and spend most of the response on the main answer. When asked to explain something, give a high-level summary unless an in-depth explanation is specifically requested.
```
En system prompt largo, además, cerca del final:
```
<tone_preference>
Keep outputs reasonably concise.
</tone_preference>
```

**Cadencia de avisos de progreso (bajar la narración):**
```
Before your first tool call, say in one sentence what you're about to do. While working, give a brief update only when you find something important or change direction. When you finish, lead with the outcome: your first sentence should answer "what happened" or "what did you find," with supporting detail after it.
```

**Longitud de entregables escritos a disco:**
```
Match the length of written documents to what the task needs: cover the substance, but do not pad with filler sections, redundant summaries, or boilerplate.
```

**Acotar alcance (tareas estrechas):**
```
Deliver what was asked, at the scope intended. Make routine judgment calls yourself, and check in only when different readings of the request would lead to materially different work. If the request seems mistaken or a better approach exists, say so in a sentence and continue with the task as asked rather than quietly narrowing, widening, or transforming it. Finish the whole task, and stop short of actions that are clearly beyond what was asked.
```

**Tope de subagentes (cargas sensibles a costo):**
```
Delegate to a subagent only for large tasks that are genuinely independent and parallelizable, such as a wide multi-file investigation. Do not delegate work you can finish yourself in a handful of tool calls, and do not use subagents to verify or double-check your own work. If one subagent can complete the task, use one rather than several, and keep spawn counts low.
```

**Narración de autocorrección (solo lo que cambia algo):**
```
Only correct an earlier statement when the error would change the user's code, conclusions, or decisions. State corrections plainly and briefly, then continue the task. For slips that change nothing for the user, make the fix and move on without noting it.
```

**Con thinking DESACTIVADO (mitiga los dos artefactos):**
```
When you use a tool, you may say a brief sentence first. If no tool can express what the user asked for, say so instead of guessing. Do not include internal or system XML tags in your response.
```

## Esfuerzo (effort) en Opus 5

- Default = `high`. **Usar `low`/`medium` con liberalidad** como palanca
  principal de costo/latencia donde la calidad aguante; subir a `xhigh`
  para código y agentic exigentes. Reejecutar un barrido de effort sobre
  tus propios evals si venías de 4.x.
- **El effort controla cuánto PIENSA, no cuánto DICE.** Para acortar la
  respuesta visible → instrucción de concisión, no bajar effort.
- **Visión**: dar herramientas para recortar/verificar imágenes rinde
  más que subir el pensamiento.
- **Thinking desactivado**: solo se puede a effort ≤ `high`. Para casi
  todo, **thinking ON a `low` supera a thinking OFF** al mismo costo.

## Thinking desactivado — dos artefactos a vigilar
1. **Tool calls como texto**: escribe la llamada en el texto visible en
   vez de un bloque `tool_use`; la llamada nunca corre y contamina el
   historial. Frecuente en cargas con muchas búsquedas.
2. **Tags XML internos** (`<thinking>`) en la salida. Empeora si el
   system prompt tiene una regla de «no pienses». No nombrar los tags
   por su nombre (menos efectivo que la regla general del bloque).
Mitigación primaria de ambos: **mantener thinking ON y controlar costo
con effort bajo.**

## Cuándo usar Opus 5 en este ecosistema
Es el nuevo tope Opus para **código agéntico difícil, refactors
multi-archivo, trabajo de punta a punta y coordinación de subagentes**.
Darle la especificación COMPLETA de una vez y dejarlo correr. Ver
[[selector-modelo-claude-optimo]] para elegir entre Opus 5 y el resto.

## 🚦 Compuertas
- 🚦 **Precio/ID/capacidades exactas de Opus 5: verificar en la skill
  `claude-api` / Models API**, no de memoria (la caché de `claude-api`
  a 2026-06-24 aún no lo listaba). ID conocido: `claude-opus-5`.
- 🚦 Estos patrones son para cuando el modelo activo es Opus 5; en 4.8
  aplica su propia guía.

## Relacionado
- [[selector-modelo-claude-optimo]] — cuándo elegir Opus 5.
- [[eficiencia-generacion-respuestas]] — misma familia: no gastar de más.
- [[doctrina-thorp-matematica-vs-multitud]] — code review: cobertura y luego filtro.
- [[llave-maestra-autoaprendizaje-ia]] — esta skill nació de destilar la guía oficial.
