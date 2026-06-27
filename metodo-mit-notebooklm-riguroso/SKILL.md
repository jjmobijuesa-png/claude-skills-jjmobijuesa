---
name: metodo-mit-notebooklm-riguroso
description: |
  Aplica de manera RIGUROSA y PASO A PASO la metodología "MIT student"
  para dominar una materia en tiempo récord usando NotebookLM. La fuente
  primaria de la metodología es el video alojado en el cuaderno
  "EcuaBlock - IBPP", etiqueta "Herramientas IA" (transcripción
  verificada en C:\Users\datos\.notebooklm-extractos\MIT_video_transcript.txt).

  REGLA DE INVOCACIÓN INNEGOCIABLE: la skill NO se ejecuta sobre un
  cuaderno completo, ni sobre etiquetas múltiples, ni sobre fuentes
  genéricas. Antes de aplicar cualquier paso, esta skill OBLIGA a
  confirmar de forma explícita y por escrito con el usuario:
    1) el cuaderno objetivo (notebook_id),
    2) la(s) etiqueta(s) que delimitan el corpus,
    3) la lista nominal de fuentes incluidas en el corpus,
    4) el alcance excluido (qué NO entra).
  Sólo cuando el usuario haya ratificado los cuatro puntos anteriores,
  la skill avanza al Paso 1. Si el usuario omite la ratificación,
  la skill se detiene y vuelve a preguntar.

  Esta skill NO suplanta a `tutor-mit-ecuablock`. Aquella es una skill
  pedagógica multi-audiencia (Pleno, Comisión, Presidencia, Prensa,
  Asesores). Esta es un protocolo de aprendizaje profundo —
  estrictamente fiel al video MIT — con clausura de alcance.

trigger_phrases:
  - "aplica la metodología MIT"
  - "aplica el método MIT a este cuaderno"
  - "ejecuta el protocolo MIT riguroso"
  - "aplica la skill metodo-mit-notebooklm-riguroso"
  - "método MIT NotebookLM"
  - "7 pasos MIT NotebookLM"

source_of_truth: |
  Video original: cuaderno EcuaBlock - IBPP, etiqueta "Herramientas IA".
  Transcripción verbatim: C:\Users\datos\.notebooklm-extractos\MIT_video_transcript.txt
  Cita literal de control (apertura): "un estudiante de la MIT dominó
  una asignatura en tan solo 48 horas; a sus compañeros les llevó 5 meses…
  la diferencia: tres preguntas que le hizo a NotebookLM".
  Cita literal de control (cierre): "ahora ya conocemos su historia…
  hay que ir un paso más allá de lo que él hizo… dos proms extra…".

idioma_de_salida: español neutro académico

---

# Metodología MIT — NotebookLM (protocolo riguroso)

## PASO 0 — CLAUSURA DE ALCANCE (obligatorio, no omisible)

Antes de ejecutar cualquier paso, formular textualmente al usuario el
siguiente bloque y esperar su ratificación expresa:

> **Confirmación de corpus a someter al método MIT**
>
> Voy a aplicar la metodología MIT-NotebookLM **únicamente** sobre el
> siguiente corpus. Por favor confirma o corrige cada punto antes de
> que avance:
>
> 1. **Cuaderno objetivo:** `<nombre>` (`notebook_id: <id>`).
> 2. **Etiqueta(s) que delimitan el corpus:** `<etiqueta_1>`,
>    `<etiqueta_2>`…
> 3. **Lista nominal de las N fuentes incluidas:**
>    - F1: `<título de fuente>`
>    - F2: `<título de fuente>`
>    - …
>    - FN: `<título de fuente>`
> 4. **Alcance excluido (lo que NO entra):** etiquetas/fuentes que se
>    omiten en este ejercicio.
>
> Confirma con **"corpus ratificado"** o indica las correcciones.

Si el usuario responde "corpus ratificado" → avanzar al Paso 1.
Si el usuario indica correcciones → reformular la lista y volver a
pedir ratificación. **No avanzar bajo ninguna otra forma de respuesta.**

---

## PASO 0.5 — CONFIGURACIÓN PREVIA DEL CHAT DE NOTEBOOKLM

Conforme al video fuente, antes de la primera pregunta:

1. Abrir el cuaderno ratificado en `notebooklm.google.com/notebook/<id>`.
2. Acceder a **Configuración del chat** (engranaje superior derecho del
   panel de chat).
3. Comportamiento: **Predeterminado** (NO usar "Guía de aprendizaje" —
   el video lo descarta expresamente).
4. Longitud de respuesta: **Más larga** (el video lo recomienda para
   exhaustividad; la variante "más cortas" es sólo para grabación de
   video).
5. Guardar.
6. **Aislar el corpus**: en el panel de fuentes, desmarcar todo lo que
   no pertenezca al corpus ratificado en el Paso 0. Sólo deben quedar
   marcadas con check las N fuentes confirmadas.

---

## PASO 1 — IDENTIFICACIÓN DE MODELOS MENTALES

Prompt literal a enviar al chat de NotebookLM:

```
Basándote en TODAS las fuentes activas de este cuaderno
(N fuentes ratificadas), identifica los CINCO modelos
mentales fundamentales que comparten todos los expertos
en el campo de <DOMINIO>.

No quiero un resumen de cada fuente. Quiero los marcos
de pensamiento. Para CADA modelo mental dame:

  1. Nombre del modelo en una frase clara.
  2. Explicación doctrinal (en qué consiste).
  3. Citas de AL MENOS DOS fuentes que lo respalden,
     indicando título de fuente y, si es posible, sección.
  4. Un ejemplo práctico de cómo este modelo cambia una
     decisión real.

Devuelve el resultado en formato numerado 1–5.
```

Al recibir la respuesta, guardar `modelos_mentales.md` en el folder de
trabajo. Verificar que cada modelo cumpla los 4 elementos. Si falta
alguno, repreguntar.

---

## PASO 2 — DESACUERDOS FUNDAMENTALES

Prompt literal:

```
Ahora muéstrame los TRES puntos donde los expertos
representados en estas fuentes están en desacuerdo
fundamental. Para CADA desacuerdo dame:

  1. La pregunta en disputa formulada con precisión.
  2. El argumento más fuerte de cada posición, con cita
     de fuente.
  3. Por qué este debate importa (impacto práctico).
  4. Si existe consenso emergente o si el debate sigue
     abierto.
```

Variante recomendada del video: hacerlo en **dos turnos** — primero
pedir la mera identificación de los puntos, luego solicitar el
desarrollo. Guardar `desacuerdos.md`.

---

## PASO 3 — TEST DE COMPRENSIÓN PROFUNDA

Prompt literal:

```
Genera 10 preguntas que expongan si alguien comprende
profundamente <DOMINIO> o sólo ha memorizado reglas y
datos. Las preguntas deben:

  1. Requerir razonamiento, no memoria.
  2. Conectar conceptos de MÚLTIPLES fuentes de este
     cuaderno.
  3. Incluir situaciones donde la regla general falla.
  4. Distinguir entre quien repite consejos y quien
     comprende los principios.

Ordénalas de menor a mayor dificultad. Para cada
pregunta, justifica por qué expone comprensión profunda.
```

**Protocolo de respuesta del estudiante:**

- El usuario (o yo, si actúo como aprendiz) responde una por una.
- Ante cada fallo, pedir literalmente a NotebookLM:
  ```
  Explícame por qué mi respuesta a la pregunta <n> está
  mal y qué concepto me falta dominar. Cita la fuente
  exacta donde está el principio que estoy omitiendo.
  ```
- Guardar `test_comprension_<DOMINIO>.md` con preguntas, respuestas y
  correcciones.

---

## PASO 4 — CONEXIONES OCULTAS Y METAMODELO (prom extra 1)

Prompt literal:

```
Analiza los cinco modelos mentales que identificaste
anteriormente e identifica:

  1. Dónde se solapan o se refuerzan mutuamente.
  2. Dónde se contradicen o crean tensión.
  3. Si existe un METAMODELO que los englobe a todos.

Usa ejemplos concretos de las fuentes de este cuaderno
para ilustrar cada conexión. Cita la fuente exacta para
cada ejemplo.
```

Guardar `metamodelo.md`. El metamodelo es el entregable de mayor valor
de toda la secuencia.

---

## PASO 5 — VACÍOS Y PLAN DE ESTUDIO (prom extra 2)

**Requisito previo:** el aprendiz debe haber respondido el test del
Paso 3.

Prompt literal:

```
Basándote en toda nuestra conversación y en las
respuestas que he dado a las 10 preguntas del test,
dime:

  1. ¿Cuáles son mis tres mayores vacíos de comprensión?
  2. Para cada vacío, ¿qué fuentes específicas de este
     cuaderno debo estudiar?
  3. ¿Qué conceptos debo dominar antes de cubrir cada
     vacío?
  4. Sugiéreme un orden de estudio óptimo para las
     próximas <X> horas.
```

Guardar `plan_estudio.md`.

---

## PASO 6 — ARTEFACTOS DE ESTUDIO (catálogo completo NotebookLM)

> **Enfoque doctrinal — confirmado y vinculante.**
> El propósito de toda esta secuencia NO es producir resúmenes ni
> "saber el tema". Es **ver los mapas o esquemas mentales detrás de
> las fuentes**: cómo agrupan la información, qué jerarquía operan,
> qué tensiones reprimen, y — sobre todo — cómo cada uno de esos
> mapas es parte de algo más grande (el metamodelo del Paso 4).
>
> Cada artefacto que se pida al panel de Estudio debe diseñarse para
> *revelar la estructura* del conocimiento, no para repetir su
> contenido. Si una salida no expone los modelos mentales y su
> ensamblaje, está mal pedida.

Generar en el chat (no directamente en el panel de Estudio — el video
aclara que el chat orquesta automáticamente el agente del Studio).
Cada subsección define: **qué es**, **para qué sirve dentro del
método MIT**, **cómo ayuda a ver los esquemas mentales**, y el
**prompt literal**.

---

### 6a. Informe ejecutivo (Briefing Doc)

**Qué es.** Documento estructurado de 5–10 páginas que sintetiza el
corpus en lenguaje profesional. Es el artefacto "de oficina".

**Para qué sirve.** Llevar el conocimiento a un decisor que no leerá
las fuentes pero debe actuar sobre ellas.

**Cómo expone la estructura mental.** El informe debe organizarse
por *modelos mentales* (no por fuente), y reservar una sección para
el *metamodelo* y los *debates abiertos*. Así el lector ve la
arquitectura, no la sumatoria.

```
Genera un informe ejecutivo sobre <DOMINIO> basado en
todas las fuentes de este cuaderno con la siguiente
estructura:
  1. Resumen ejecutivo.
  2. Los cinco modelos mentales clave (uno por sección).
  3. El metamodelo que los engloba.
  4. Los tres debates abiertos.
  5. Hoja de ruta práctica (10 pasos).
  6. Fuentes recomendadas por nivel.
Tono: profesional pero accesible.
```

---

### 6b. Presentación / slide deck

**Qué es.** Conjunto de diapositivas (típicamente 12–20) con título
+ 3–4 viñetas cada una y notas del orador.

**Para qué sirve.** Exposición oral. Comunicación a grupos.

**Cómo expone la estructura mental.** La primera diapositiva *no*
es agenda — es el **metamodelo en una imagen**. Cada modelo mental
ocupa su slide. Los desacuerdos van como bloque "tensión productiva".

```
Estructura y crea una presentación sobre <DOMINIO> para
<PERFIL_DEL_OYENTE>. Diapositiva 1: el metamodelo en una
sola frase. Diapositivas 2–6: un modelo mental por slide,
con título y 3–4 puntos clave. Diapositivas 7–9: los tres
desacuerdos como "tensión productiva". Diapositiva final:
hoja de ruta. Adapta los ejemplos al contexto <regional>.
```

---

### 6c. Podcast / Audio Overview

**Qué es.** Conversación generada entre dos voces que dialogan sobre
las fuentes; duración hasta ~30 minutos.

**Para qué sirve.** Repaso pasivo (transporte, ejercicio). Excelente
para fijar los modelos mentales por exposición repetida.

**Cómo expone la estructura mental.** Pedir explícitamente que el
podcast **organice el guión por modelos mentales y termine con el
metamodelo** — sin esa instrucción produce charlas planas.

```
Usa la herramienta de podcast del Estudio para crear un
podcast sobre <DOMINIO>. El oyente es <PERFIL>. Organiza
el guión así: (1) un gancho que plantee el problema;
(2) un bloque por modelo mental — explicado con un caso
real; (3) un bloque sobre los desacuerdos; (4) un cierre
que enuncie el metamodelo y deje una pregunta abierta.
Tono <tono>. Duración objetivo <minutos>.
```

(El video advierte que en versiones recientes a veces hay que pedir
explícitamente *"usa la herramienta de podcast del Estudio"* para que
el agente la invoque.)

---

### 6d. Video Overview / Resumen en video

**Qué es.** Video corto (3–10 min) con narración + diapositivas
animadas generado por el Studio.

**Para qué sirve.** Comunicación asincrónica visual, compartible por
mensajería.

**Cómo expone la estructura mental.** El video debe abrir con el
metamodelo y luego mostrar **un esquema visual por modelo mental**.

```
Usa la herramienta de video del Estudio para generar un
video resumen sobre <DOMINIO>. Apertura: el metamodelo
en pantalla con narración de una frase. Cuerpo: un
segmento por cada modelo mental, con un esquema visual
sencillo. Cierre: las tres preguntas abiertas del debate.
Duración objetivo <minutos>. Tono <tono>.
```

---

### 6e. Mapa mental (Mind Map)

**Qué es.** Diagrama jerárquico interactivo que el Studio genera
expandiendo nodo a nodo el contenido de las fuentes.

**Para qué sirve.** Es el **artefacto central** de esta skill,
porque es el que literalmente *muestra la estructura*. Aquí el
método MIT alcanza su máxima expresión visual.

**Cómo expone la estructura mental.** El nodo raíz **debe ser el
metamodelo**, no el nombre del dominio. Los nodos de primer nivel
son los cinco modelos mentales. Los desacuerdos van como
"nodos-tensión" coloreados distinto.

```
Genera un mapa mental del corpus con esta arquitectura:
  • Nodo raíz: el metamodelo (una frase).
  • 5 nodos de primer nivel: los cinco modelos mentales.
  • Bajo cada modelo: las citas-puente que lo respaldan
    (mínimo 2 fuentes por modelo).
  • 3 nodos transversales marcados como "tensión": los
    desacuerdos fundamentales, conectando los modelos
    que entran en conflicto.
  • Una rama lateral "vacíos detectados" con los puntos
    pendientes del Paso 5.
```

---

### 6f. Guía de estudio (Study Guide)

**Qué es.** Documento didáctico con objetivos de aprendizaje,
preguntas-guía por sección y ejercicios.

**Para qué sirve.** Autoestudio estructurado por capas de
profundidad.

**Cómo expone la estructura mental.** Cada sección debe estar
anclada a un modelo mental. Los ejercicios deben *hacer aparecer*
las conexiones entre modelos, no repetir definiciones.

```
Genera una guía de estudio sobre <DOMINIO> con esta
estructura por cada uno de los cinco modelos mentales:
  1. Objetivo de aprendizaje del modelo.
  2. Lectura obligatoria (fuentes específicas).
  3. Tres preguntas guía que detecten comprensión.
  4. Un ejercicio que conecte este modelo con otro del
     metamodelo.
Cierra con un módulo final dedicado al metamodelo.
```

---

### 6g. Tarjetas didácticas (Flashcards)

**Qué es.** Pares pregunta-respuesta optimizados para repetición
espaciada (estilo Anki).

**Para qué sirve.** Memorización quirúrgica de los anclajes —
nombres de modelos, citas-llave, fechas, cifras críticas.

**Cómo expone la estructura mental.** Las flashcards deben venir
**agrupadas por modelo mental** y etiquetar explícitamente la capa:
*"capa 1: nombre del modelo"*, *"capa 2: cita-llave"*, *"capa 3:
conexión con otro modelo"*. Sin esa estratificación son trivia
suelta.

```
Genera 30 tarjetas didácticas sobre <DOMINIO>,
distribuidas así:
  • 5 tarjetas tipo "nombre del modelo ⇄ definición".
  • 10 tarjetas tipo "cita-llave ⇄ fuente + modelo".
  • 10 tarjetas tipo "situación práctica ⇄ qué modelo
    aplicar y por qué".
  • 5 tarjetas tipo "tensión entre modelos X e Y ⇄
    debate fundamental".
Etiqueta cada tarjeta con el modelo mental al que
pertenece.
```

---

### 6h. Pruebas / Cuestionarios (Quiz)

**Qué es.** Test de opción múltiple, verdadero/falso o respuesta
breve, autoevaluable.

**Para qué sirve.** Verificación rápida del Paso 3 (test de
comprensión profunda) en formato cerrado.

**Cómo expone la estructura mental.** Cada pregunta debe traer un
distractor que represente la *aplicación incorrecta de otro modelo
mental*. Eso obliga al estudiante a diferenciar marcos, no
contenidos.

```
Genera un cuestionario de 15 preguntas sobre <DOMINIO>
con esta composición:
  • 5 preguntas conceptuales (un modelo mental por
    pregunta).
  • 5 preguntas de aplicación (escenario + elegir qué
    modelo aplica).
  • 5 preguntas de discriminación (dos modelos
    parecidos, ¿cuál aplica?).
Para cada pregunta incluye 4 opciones, una correcta, y
explica brevemente por qué cada distractor es plausible
pero incorrecto. Cita la fuente que respalda la
respuesta correcta.
```

---

### 6i. Preguntas frecuentes (FAQ)

**Qué es.** Listado de Q&A breves, formato divulgativo.

**Para qué sirve.** Comunicación externa, atender consultas
recurrentes, base de FAQ para web o redes.

**Cómo expone la estructura mental.** Pedir que las preguntas se
agrupen por modelo mental. Una pregunta final debe ser:
*"¿cuál es la idea más grande detrás de todo esto?"* — y la
respuesta es el metamodelo.

```
Genera 12 preguntas frecuentes sobre <DOMINIO>,
agrupadas en 5 secciones (una por cada modelo mental).
Añade al final una pregunta de cierre: "¿cuál es la
idea más grande detrás de todo esto?" cuya respuesta sea
el metamodelo. Respuestas de 3–4 frases máximo.
```

---

### 6j. Cronología (Timeline)

**Qué es.** Línea de tiempo con hitos extraídos de las fuentes.

**Para qué sirve.** Cuando el dominio tiene componente histórico,
normativo o procesal (típico en el trabajo legislativo).

**Cómo expone la estructura mental.** Cada hito se etiqueta con el
**modelo mental al que pertenece o que inaugura**. Así la línea
deja de ser una sucesión de fechas y pasa a ser la **evolución de
los marcos de pensamiento**.

```
Genera una cronología de <DOMINIO> con hitos extraídos
de las fuentes. Para cada hito indica:
  • Fecha.
  • Descripción breve.
  • Fuente.
  • Modelo mental al que pertenece o que inaugura.
  • Si rompe con un modelo anterior, indica cuál.
```

---

### 6k. Infografía / panel visual

**Qué es.** Pieza visual estática (poster, panel, lámina) con
jerarquía gráfica. NotebookLM puede entregar la estructura; la
pieza final se compone con la skill `infografia-creativa-ecuador-digital`.

**Para qué sirve.** Comunicación masiva, redes sociales, paneles
institucionales.

**Cómo expone la estructura mental.** La infografía debe ser un
**plano de los modelos mentales** — no un poster decorativo. El
metamodelo arriba como titular, los cinco modelos como bloques
mayores, los desacuerdos como flechas de tensión.

```
Diseña la estructura de una infografía A3 vertical sobre
<DOMINIO>. Bloques:
  • Titular: el metamodelo.
  • Cinco bloques principales: un modelo mental por
    bloque, con icono sugerido y dato-clave.
  • Tres flechas de tensión: los desacuerdos.
  • Pie: tres llamadas a acción derivadas del plan de
    estudio.
Devuélveme la estructura como JSON o tabla para pasar al
diseñador.
```

---

### 6l. Informe personalizado (Custom Report)

**Qué es.** Documento de formato libre que el usuario define con un
prompt abierto. Es el "comodín" del Studio.

**Para qué sirve.** Salidas no previstas en los templates
anteriores: dossier para un ministro, opinión legal, memorial,
position paper.

**Cómo expone la estructura mental.** Cualquiera sea el formato,
el informe personalizado debe **abrir con el metamodelo y cerrar
con el metamodelo** — es la firma estructural de la skill.

```
Genera un informe personalizado sobre <DOMINIO> con el
siguiente propósito: <PROPOSITO>. Estructura libre.
Requisitos no negociables: (1) la primera línea enuncia
el metamodelo; (2) cada sección está anclada a uno de
los cinco modelos mentales; (3) el cierre vuelve al
metamodelo y deja una pregunta para el lector.
```

---

### 6m. Otras salidas emergentes del Studio

El Studio de NotebookLM amplía periódicamente su catálogo. Cuando
aparezca una salida nueva (formularios, hojas de trabajo,
explicadores en una página, etc.), aplicar siempre la misma regla:

> **La salida debe revelar la estructura mental del corpus, no su
> superficie.** Si no expone los modelos mentales, el metamodelo y
> las tensiones, está mal pedida.

---

## ENTREGABLE FINAL DE LA SKILL

Carpeta de trabajo `metodo-mit-<DOMINIO>-<fecha>/` con:

```
00_corpus_ratificado.md
01_configuracion_chat.md
02_modelos_mentales.md
03_desacuerdos.md
04_test_comprension.md
05_metamodelo.md
06_plan_estudio.md
07a_informe_ejecutivo.md
07b_presentacion.pptx
07c_podcast.mp3
07d_video_overview.mp4
07e_mapa_mental.png      (o export interactivo)
07f_guia_estudio.md
07g_flashcards.csv       (importable a Anki)
07h_cuestionario.md
07i_faq.md
07j_cronologia.md
07k_infografia_estructura.json
07l_informe_personalizado.md
```

Y un `INDEX.md` que enlace todo y resuma en 1 página los hallazgos.
El `INDEX.md` debe arrancar con el **metamodelo** como titular —
nunca con el nombre del dominio.

---

## ENFOQUE DOCTRINAL (confirmación expresa)

Esta skill **no** persigue producir resúmenes ni demostrar cobertura
de las fuentes. Su único propósito es:

> **Volverse experto comprendiendo los mapas o esquemas mentales que
> hay detrás de las fuentes**, para mirar más profundamente *cómo
> agrupan la información* y para *mirarlos como parte de algo más
> grande* — el metamodelo.

Operativamente, ese enfoque se traduce en tres compromisos
no negociables:

1. **Estructura sobre contenido.** Toda salida se evalúa por la
   estructura mental que revela, no por la cantidad de información
   que repite.
2. **Modelos como unidad atómica.** Los modelos mentales identificados
   en el Paso 1 son la unidad de organización de todos los
   entregables posteriores; no la "fuente", no el "tema", no el
   "capítulo".
3. **Metamodelo como techo.** Toda salida abre o cierra (o ambos)
   anclada al metamodelo del Paso 4. Un entregable sin metamodelo
   está incompleto.

---

## CRITERIOS DE FIDELIDAD AL VIDEO FUENTE Y AL ENFOQUE

Esta skill se considera correctamente aplicada cuando:

- [x] Se respetaron los 5 pasos originales (modelos / desacuerdos /
      test / metamodelo / plan de estudio) en su orden y con sus
      prompts literales.
- [x] Se incorporaron los **dos proms extra** del video
      (conexiones-metamodelo + vacíos-plan de estudio) que el video
      explícitamente atribuye al "creador del contenido", no al
      estudiante MIT original.
- [x] Se generaron los **artefactos del catálogo 6a–6l** que
      correspondan al uso pedido, cada uno organizado por modelos
      mentales y anclado al metamodelo.
- [x] El corpus se limitó EXCLUSIVAMENTE a las fuentes ratificadas en
      el Paso 0.
- [x] Toda respuesta de NotebookLM se archivó con cita a fuente.
- [x] El `INDEX.md` final abre con el metamodelo como titular.

---

## CONTRAINDICACIONES

No usar esta skill cuando:

- El usuario quiere un resumen rápido (usar lectura directa).
- El usuario quiere un memorial pedagógico multi-audiencia (usar
  `tutor-mit-ecuablock`).
- El corpus no está consolidado en NotebookLM (subir primero las
  fuentes — usar skills `perplexity-extractor` o `notebooklm-reorganize`).
- El usuario no ha ratificado el alcance (volver al Paso 0).

---

## TRAZABILIDAD

Esta skill registra el linaje:

- Fuente primaria: video YouTube transcripto en
  `MIT_video_transcript.txt`.
- Verificación de la transcripción: realizada el 2026-05-31.
- Skill complementaria: `tutor-mit-ecuablock` (uso pedagógico).
- Integración: cuaderno `0bdb495d-9cb9-4781-ae61-9661bbbebc16`
  (EcuaBlock - IBPP), etiqueta "Herramientas IA".
