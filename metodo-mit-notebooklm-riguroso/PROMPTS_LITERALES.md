# Prompts literales — copy & paste directo a NotebookLM

> Estos son los siete prompts en su forma exacta. Copiar uno por uno al
> chat del cuaderno *después* de cumplir el Paso 0 y el Paso 0.5 de
> `SKILL.md`.
>
> Sustituir `<DOMINIO>`, `<X>`, `<PERFIL>`, `<orden>`, `<tono>` antes de
> enviar.

---

## P1 — Modelos mentales

```
Basándote en todas las fuentes activas de este cuaderno,
identifica los CINCO modelos mentales fundamentales que
comparten todos los expertos en <DOMINIO>. No quiero un
resumen de cada fuente; quiero los marcos de pensamiento.
Para cada modelo dame: (1) nombre en una frase clara;
(2) explicación doctrinal; (3) citas de al menos dos
fuentes que lo respalden con título y sección; (4) un
ejemplo práctico de cómo este modelo cambia una decisión
real. Formato numerado 1–5.
```

---

## P2a — Desacuerdos: identificación

```
Identifica los puntos donde los expertos representados
en estas fuentes están en desacuerdo fundamental. Sólo
una lista enumerada — sin desarrollo todavía.
```

## P2b — Desacuerdos: desarrollo

```
De la lista anterior, desarrolla los tres desacuerdos
más relevantes. Para cada uno dame: (1) pregunta en
disputa formulada con precisión; (2) argumento más
fuerte de cada posición con cita de fuente; (3) por qué
este debate importa; (4) si existe consenso emergente o
si sigue abierto.
```

---

## P3 — Test de 10 preguntas

```
Genera 10 preguntas que expongan si alguien comprende
profundamente <DOMINIO> o sólo ha memorizado reglas y
datos. Las preguntas deben: requerir razonamiento, no
memoria; conectar conceptos de múltiples fuentes;
incluir situaciones donde la regla general falla;
distinguir entre quien repite consejos y quien
comprende los principios. Ordénalas de menor a mayor
dificultad. Para cada pregunta justifica por qué expone
comprensión profunda.
```

## P3.fallo — Plantilla de re-pregunta tras error

```
Explícame por qué mi respuesta a la pregunta <n> está
mal y qué concepto me falta dominar. Cita la fuente
exacta donde está el principio que estoy omitiendo.
```

---

## P4 — Conexiones ocultas y metamodelo (extra 1)

```
Analiza los cinco modelos mentales que identificaste
anteriormente. Dime: (1) dónde se solapan o se refuerzan
mutuamente; (2) dónde se contradicen o crean tensión;
(3) si existe un metamodelo que los englobe a todos.
Usa ejemplos concretos de las fuentes y cita cada uno.
```

---

## P5 — Vacíos y plan de estudio (extra 2)

```
Basándote en toda nuestra conversación y en las
respuestas que he dado al test de 10 preguntas, dime:
(1) mis tres mayores vacíos de comprensión; (2) para
cada vacío qué fuentes específicas de este cuaderno
debo estudiar; (3) qué conceptos debo dominar antes de
cubrir cada vacío; (4) un orden de estudio óptimo para
las próximas <X> horas.
```

---

> **Recordatorio de enfoque.** Cada artefacto se pide para revelar la
> *estructura mental* del corpus — los modelos, sus tensiones y el
> metamodelo que los engloba. Si el prompt no obliga a organizar la
> salida por modelos mentales, está mal redactado.

## P6a — Informe ejecutivo (Briefing Doc)

```
Genera un informe ejecutivo sobre <DOMINIO> basado en
todas las fuentes de este cuaderno con la estructura:
(1) resumen ejecutivo; (2) los cinco modelos mentales
clave — uno por sección; (3) el metamodelo que los
engloba; (4) los tres debates abiertos; (5) hoja de ruta
práctica de 10 pasos; (6) fuentes recomendadas por nivel.
Tono profesional pero accesible.
```

## P6b — Presentación

```
Estructura y crea una presentación sobre <DOMINIO> para
<PERFIL>. Diapositiva 1: el metamodelo en una frase.
Diapositivas 2–6: un modelo mental por slide con título y
3–4 puntos clave. Diapositivas 7–9: los tres desacuerdos
como "tensión productiva". Diapositiva final: hoja de
ruta. Orden sugerido: <orden>. Adapta los ejemplos a
<contexto>.
```

## P6c — Podcast

```
Usa la herramienta de podcast del Estudio para crear un
podcast sobre <DOMINIO>. El oyente es <PERFIL>. Organiza
el guión: (1) gancho — el problema; (2) un bloque por
modelo mental, ilustrado con un caso real y cita de
fuente; (3) un bloque sobre los desacuerdos; (4) cierre
con el metamodelo y una pregunta abierta. Tono <tono>.
Duración objetivo <minutos>.
```

## P6d — Video Overview

```
Usa la herramienta de video del Estudio para generar un
video resumen sobre <DOMINIO>. Apertura: el metamodelo
en pantalla con narración de una frase. Cuerpo: un
segmento por cada modelo mental con un esquema visual
sencillo. Cierre: las tres preguntas abiertas del debate.
Duración objetivo <minutos>. Tono <tono>.
```

## P6e — Mapa mental

```
Genera un mapa mental del corpus con esta arquitectura:
  • Nodo raíz: el metamodelo (una frase).
  • 5 nodos de primer nivel: los cinco modelos mentales.
  • Bajo cada modelo: las citas-puente que lo respaldan
    (mínimo dos fuentes por modelo).
  • 3 nodos transversales marcados como "tensión": los
    desacuerdos fundamentales, conectando los modelos
    que entran en conflicto.
  • Una rama lateral "vacíos detectados" con los puntos
    pendientes del plan de estudio.
```

## P6f — Guía de estudio

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

## P6g — Tarjetas didácticas (Flashcards)

```
Genera 30 tarjetas didácticas sobre <DOMINIO>:
  • 5 tipo "nombre del modelo ⇄ definición".
  • 10 tipo "cita-llave ⇄ fuente + modelo".
  • 10 tipo "situación práctica ⇄ qué modelo aplicar y
    por qué".
  • 5 tipo "tensión entre modelos X e Y ⇄ debate
    fundamental".
Etiqueta cada tarjeta con el modelo mental al que
pertenece. Formato CSV con columnas
front | back | tag_modelo.
```

## P6h — Cuestionario / Quiz

```
Genera un cuestionario de 15 preguntas sobre <DOMINIO>:
  • 5 conceptuales (un modelo mental por pregunta).
  • 5 de aplicación (escenario + elegir qué modelo
    aplica).
  • 5 de discriminación (dos modelos parecidos, ¿cuál
    aplica?).
Cada pregunta con 4 opciones, una correcta. Explica por
qué cada distractor es plausible pero incorrecto. Cita
la fuente que respalda cada respuesta correcta.
```

## P6i — FAQ

```
Genera 12 preguntas frecuentes sobre <DOMINIO>,
agrupadas en 5 secciones (una por modelo mental). Añade
al final una pregunta de cierre: "¿cuál es la idea más
grande detrás de todo esto?" cuya respuesta sea el
metamodelo. Respuestas de 3–4 frases máximo.
```

## P6j — Cronología

```
Genera una cronología de <DOMINIO> con hitos extraídos
de las fuentes. Para cada hito indica:
  • Fecha.
  • Descripción breve.
  • Fuente.
  • Modelo mental al que pertenece o que inaugura.
  • Si rompe con un modelo anterior, cuál.
```

## P6k — Infografía (estructura)

```
Diseña la estructura de una infografía A3 vertical sobre
<DOMINIO>. Bloques:
  • Titular: el metamodelo.
  • Cinco bloques principales: un modelo mental por
    bloque, con icono sugerido y dato-clave.
  • Tres flechas de tensión: los desacuerdos.
  • Pie: tres llamadas a acción derivadas del plan de
    estudio.
Devuelve la estructura como JSON con keys
titular | bloques | tensiones | pie.
```

## P6l — Informe personalizado (comodín)

```
Genera un informe personalizado sobre <DOMINIO> con
propósito <PROPOSITO>. Estructura libre. Requisitos no
negociables: (1) la primera línea enuncia el metamodelo;
(2) cada sección está anclada a uno de los cinco modelos
mentales; (3) el cierre vuelve al metamodelo y deja una
pregunta para el lector.
```
