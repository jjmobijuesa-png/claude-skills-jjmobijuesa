---
name: analisis-cognitivo-intervenciones-qvp
description: |
  Análisis de HABILIDADES BLANDAS y COGNICIÓN aplicado a las reuniones del comité / "cuarto de
  guerra" de Quevepalma (u otra organización). Toma una transcripción (Fathom, acta, audio→texto) y
  produce un diagnóstico del COMPORTAMIENTO de la reunión: cómo intervienen las personas, cómo se
  toman las decisiones, qué sesgos cognitivos aparecen y cómo se resuelven (o no) los problemas.
  No analiza las cifras (eso es de memoria-financiera) sino el FACTOR HUMANO: comunicación,
  participación, liderazgo/facilitación, inteligencia emocional, calidad de decisión y resolución de
  problemas. Se apoya en el cuaderno NotebookLM "Toma de Decisiones QVP" como marco de referencia.
  Entrega un informe con rúbrica/semáforos, evidencia citada (intervenciones) y recomendaciones.
  Triggers: "análisis cognitivo de la reunión", "habilidades blandas del comité", "cómo se toman las
  decisiones en QVP", "sesgos en la reunión", "resolución de problemas del cuarto de guerra",
  "análisis de intervenciones", "calidad de la facilitación / liderazgo de la reunión".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-16
  origen: cuaderno NotebookLM "Toma de Decisiones QVP" + transcripción comité (Fathom) + marcos Kahneman/Tversky
  relacionada: comite-cuarto-guerra-qvp, memoria-financiera-inteligenciada, neuro-oratoria-presentacion-persuasiva
---

# Skill `analisis-cognitivo-intervenciones-qvp`

Lee una reunión y la analiza como **comportamiento humano**, no como números. Responde: *¿quién habla
y cómo?, ¿se decide con datos o con anécdota?, ¿qué sesgos están operando?, ¿se resuelve el problema
o solo el síntoma?, ¿hay liderazgo y cierre?* Útil para mejorar la efectividad del comité (la propia
reunión SEM 24 se autodiagnosticó "ineficiente y sin liderazgo claro").

## 1. Fuentes
- **Transcripción** del comité: la trae [[comite-cuarto-guerra-qvp]] (correo "SEM xx" de Fathom).
  Ignorar las frases espurias en inglés de Fathom; analizar el contenido en español.
- **Marco de referencia:** cuaderno NotebookLM **"Toma de Decisiones QVP"** (cuenta
  mobijuesa360@gmail.com). Consultarlo con [[anthropic-skills:notebooklmskill]]:
  `notebooklm use <id>` → `notebooklm ask "¿qué modelo/criterios de toma de decisiones propone el
  cuaderno?"`. Integrar ese marco propio antes de aplicar los genéricos de abajo.
  *Fuentes del cuaderno (jun-2026): actas del comité (Sem 9/21/22), CoRT/Lateral Thinking de De Bono,
  EEFF, informes Panamá. Es el marco oficial de la empresa.*

## 1-bis. MARCO PROPIO del cuaderno "Toma de Decisiones QVP" (úsalo como lente principal)
La empresa decide con el lenguaje de **Edward de Bono + Kahneman + método MIT**. Evaluar las
intervenciones con estas herramientas (¿se usaron?, ¿faltaron?):

**A. Herramientas CoRT (de Bono):**
- **AGO** (Aims, Goals, Objectives) — ¿se definió el propósito/objetivo de la reunión (el **OEC**:
  Objetivo, Entregable, Criterio de éxito)?
- **CAF** (Consider All Factors) — ¿se consideraron todos los factores antes de decidir?
- **C&S** (Consequences & Sequels) — ¿se previeron consecuencias a corto/medio/largo plazo?
- **APC** (Alternatives, Possibilities, Choices) — ¿se generaron alternativas más allá de lo obvio?
- **FIP** (First Important Priorities) — ¿se priorizó lo esencial tras el análisis amplio?
- **OPV** (Other People's Views) — ¿se consideró la perspectiva de los demás interesados?

**B. Seis Sombreros para Pensar** (separar modos de pensamiento, evitar confrontación):
Blanco = datos/hechos · Rojo = emoción/intuición · Negro = riesgo/juicio crítico · Amarillo =
beneficios/optimismo · Verde = creatividad/alternativas (**PO**) · **Azul = control del proceso,
foco en el OEC y síntesis** (lo usa quien preside). Señal de alerta: una sola "voz" (p. ej. solo
sombrero negro) domina y bloquea la decisión.

**C. Pensamiento lateral / provocación (PO) + método MIT:**
- **PO / movimiento:** en fase creativa, prohibir el juicio inmediato y usar provocaciones para salir
  del patrón operativo rígido.
- **MIT:** mapear el **fenómeno** (modelo dinámico) antes de proponer soluciones; buscar el **"fulcro"**
  (punto de apoyo) donde un pequeño cambio estructural mueve el **Throughput**. Atacar la esencia, no el
  síntoma. (Conecta con [[metodo-mit-notebooklm-riguroso]].)

**D. Kahneman (Sistema 1/2):**
- Activar el **Sistema 2** con listas de control para frenar sesgos: **ilusión de validez**
  (proyecciones aspiracionales), **anclaje** en datos pasados, WYSIATI, falacia de planificación.
- **Pre-mortem:** asumir que el plan **ya fracasó** y enumerar por qué — revela riesgos que el
  optimismo oculta.

> Mapeo: las 8 dimensiones de §2 se **puntúan usando estas herramientas** (p. ej. "decisión sin C&S
> ni APC" = 🔴 en *Calidad de la decisión*; "el que preside no ejerció el sombrero Azul" = 🔴 en
> *Liderazgo*; "se ancló en la cifra de la semana pasada" = sesgo de anclaje).

## 2. Las 8 dimensiones del análisis (rúbrica 🟢🟡🔴)
1. **Participación e interacción** — mapa de quién interviene, dominancia vs. silencios,
   interrupciones, turnos, escucha activa. ¿Se invita a los expertos correctos por punto?
2. **Estilos de comunicación** — asertivo / pasivo / agresivo; claridad vs. divagación; uso de datos
   vs. relato; manejo del tiempo (temas críticos tratados con prisa).
3. **Calidad de la decisión** — ¿basada en evidencia o anécdota?, ¿estructurada o reactiva?,
   ¿consenso o imposición?, ¿se evalúan alternativas?, ¿la decisión es reversible y con dueño?
4. **Sesgos cognitivos (Kahneman/Tversky)** — anclaje, disponibilidad, confirmación, **WYSIATI**,
   **falacia de planificación**, aversión a la pérdida, sesgo del statu quo, exceso de confianza,
   descuento hiperbólico y **ruido** (variabilidad inconsistente). + sesgos de grupo: **pensamiento
   de grupo**, difusión de responsabilidad, sesgo de autoridad.
5. **Resolución de problemas** — ¿se define bien el problema?, ¿causa raíz vs. síntoma (5 porqués)?,
   ¿se generan opciones?, ¿criterios explícitos?, ¿se cierra con plan, dueño y fecha?
6. **Liderazgo y facilitación** — agenda, foco, rendición de cuentas, manejo de digresiones, cierre
   con compromisos. (La SEM 24 pidió justamente esto.)
7. **Inteligencia emocional y conflicto** — tono, tensión, validación, cómo se maneja el desacuerdo
   (p. ej. el debate cartera "gestionar vs. cumplir la meta").
8. **Métrica vs. realidad ("gestionar vs. la foto")** — *goal displacement* / ley de Goodhart:
   ajustar la meta para que "se vea bonita" en lugar de gestionar el problema real.

## 3. Patrones detectados en QVP (catálogo, ampliar por reunión)
- **"Gestionar vs. cumplir la foto":** bajar los días de cartera para que el % luzca mejor, en vez de
  dar visibilidad (debate SEM 24). → goal displacement + pérdida de información para decidir.
- **Falacia de planificación / WYSIATI / confirmación / ruido:** documentados en la auditoría forense
  de proyectos fallidos (sesgos de Kahneman) — vigilar su reaparición en las decisiones de inversión.
- **Liderazgo difuso:** múltiples presentaciones no coordinadas, sin un conductor que exija datos
  preparados (autodiagnóstico SEM 24).
- **Foco en el pasado:** se reporta lo ocurrido en vez de planificar (decidir hacia adelante).

## 4. Método (paso a paso)
1. Obtener la transcripción (skill del comité) y, si aplica, el marco del cuaderno NotebookLM.
2. Segmentar por **interventor** y por **punto de agenda**; marcar decisiones y desacuerdos.
3. Puntuar cada una de las 8 dimensiones con 🟢/🟡/🔴 y **citar la evidencia** (la intervención).
4. Señalar **sesgos** concretos con la frase que los delata.
5. Evaluar cada **problema tratado**: definición → causa raíz → alternativas → decisión → dueño/fecha.
6. Redactar **recomendaciones accionables** (de comportamiento, no de cifras) y, si se pide, un
   guion de mejora con [[neuro-oratoria-presentacion-persuasiva]].

## 5. Entregables
- **Informe de análisis cognitivo SEM xx** (md/PDF): rúbrica de 8 dimensiones con semáforos,
  evidencia citada, mapa de participación, catálogo de sesgos y plan de mejora.
- Opcional: **mapa de calor / radar** de las 8 dimensiones; ficha por interventor.
- Guardar en `WAR ROOM QVP\Actas\ANALISIS COGNITIVO SEM xx - QVP.*`.

## 6. Reglas
- **Constructivo, no punitivo.** Describir conductas y patrones, no etiquetar personas; el objetivo es
  mejorar la toma de decisiones del equipo.
- **Evidencia siempre:** cada juicio va con la intervención que lo respalda (cita textual breve).
- Separar claramente el **factor humano** (esta skill) del **análisis de cifras** (memoria-financiera).

## 7. Relación con otras skills
- `comite-cuarto-guerra-qvp` — provee la transcripción y el contexto de la reunión.
- `memoria-financiera-inteligenciada` — el "qué" (cifras); esta skill aporta el "cómo se decidió".
- `neuro-oratoria-presentacion-persuasiva` — convierte las recomendaciones en mejora de la exposición.
- `notebooklmskill` — consulta el cuaderno "Toma de Decisiones QVP" como marco propio.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
