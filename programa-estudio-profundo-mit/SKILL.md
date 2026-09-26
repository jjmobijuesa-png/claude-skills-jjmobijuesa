---
name: programa-estudio-profundo-mit
description: |
  FÁBRICA DE PROGRAMAS DE ESTUDIO PROFUNDO al modo MIT, y su entrega como HTML
  viva en el Aula de Clases Magistrales (`G:\Mi unidad\Clases-Magistrales-HTML`).

  Toma una materia («quiero dominar probabilidad», «necesito entender criptografía
  para EcuaLedger», «álgebra lineal para la IA») y devuelve un PROGRAMA con
  estructura de asignatura real: objetivos de aprendizaje verificables, secuencia
  de prerrequisitos, fuente única por unidad, problem sets con solución,
  evaluación, y calendario de adulto ocupado: por defecto UNA SESIÓN DIARIA DE 60
  MINUTOS en microciclos de 4 semanas (24 h cada uno).

  La diferencia con «una lista de cursos» es la exigencia de MIT: cada unidad
  termina en un ENTREGABLE que se puede calificar, no en «ver un video». Y el
  reparto de horas NO se hace por criterio del diseñador sino midiendo qué se
  trabaja y qué se cura de verdad en esta casa (paso 3.5).

trigger_phrases:
  - "arma un programa de estudio de X"
  - "quiero dominar X"
  - "sílabo de X"
  - "currículo MIT de X"
  - "programa de estudios generales"
  - "plan de estudio profundo"
  - "conviértelo en clase magistral HTML"
idioma_de_salida: español
nivel_madurez: aplicada
dominio: pedagogía / diseño curricular
metadata:
  version: 2.0
  fecha: "2026-09-05 — v2.0 el mismo dia; hora diaria y ponderacion por evidencia"
  catalogo: "E:\\vars\\var 5\\Universidad-Abierta\\catalogo-50-fuentes.json"
  salida_html: "G:\\Mi unidad\\Clases-Magistrales-HTML"
  salida_programas: "E:\\vars\\var 5\\Universidad-Abierta\\programas"
  agente: estudios-generales
  relacionada: universidad-abierta-catalogo, metodo-mit-notebooklm-riguroso, entrega-visual-html-vs-texto, memoria-aprendizaje-seis-reglas, winston-how-to-speak-mit
---

# Skill `programa-estudio-profundo-mit`

## Doctrina

Un curso no es una lista de videos. Un curso, en la tradición del MIT, es un **contrato**:
*si usted hace estas tareas en este orden, al final sabrá hacer estas cosas, y hay una manera
de comprobarlo.* Tres piezas hacen la diferencia y son las tres que las listas de internet
omiten:

1. **Problem sets con solución.** Sin ejercicios corregibles no hay aprendizaje, hay turismo.
   Por eso MIT OCW pesa más que cualquier plataforma comercial: publica los *psets* Y sus
   soluciones.
2. **Prerrequisito explícito.** El 90 % de los abandonos no son por falta de disciplina sino
   por saltarse un peldaño. El programa nombra el peldaño anterior y cómo repararlo.
3. **Entregable por unidad.** Cada semana termina en algo que existe fuera de la cabeza: un
   resumen de una página, un cálculo verificado en Wolfram, un script que corre, una
   explicación grabada en tres minutos.

Y una restricción del usuario que manda sobre todo: **es un adulto con empresa, obra y
familia**. El programa se diseña para 5-7 horas semanales, no para 40. Antes de aceptar un
programa se calcula el costo total en horas y se declara (regla de [[cuantificar-antes-de-pedir]]).

## Protocolo — de la materia al programa

> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

### Paso 1 — Encuadre (obligatorio, no omisible)
Antes de diseñar nada, fijar por escrito y hacer ratificar:

> 1. **Materia:** `<qué>`
> 2. **Para qué se estudia:** el expediente concreto que lo justifica (Belén, EcuaLedger,
>    QVP, el libro Kleper…). Si no hay expediente, decirlo: se estudia por formación general.
> 3. **Nivel de partida honesto:** qué se sabe hoy y qué se olvidó.
> 4. **Presupuesto de horas por semana y semanas totales.**
> 5. **Prueba de dominio:** cómo sabremos que se aprendió. Una frase.

Sin los cinco puntos no se avanza: un programa sin prueba de dominio es una lista de deseos.

### Paso 2 — Selección de fuentes (por catálogo, no por búsqueda)
Consultar [[universidad-abierta-catalogo]]:

```bash
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --query "<materia>"
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --mit
```

**Regla de Teach Yourself CS: una fuente principal por unidad, y solo una.** La segunda
fuente no es refuerzo, es dispersión. Se admite, además:
- **un complemento visual** (3Blue1Brown, HyperPhysics, PhET) que se ve ANTES del formalismo;
- **un verificador** (Wolfram Alpha, Desmos) para auditar resultados propios.

Si el catálogo no cubre la materia, verificar la fuente nueva por HTTP e incorporarla al
catálogo antes de usarla. Nunca al revés.

### Paso 3 — Malla y prerrequisitos
Usar la **secuencia MIT verificada** del catálogo (`--mit`) como columna vertebral cuando la
materia sea técnica. Cada unidad declara: prerrequisito, fuente única, complemento visual,
entregable y horas estimadas.

### Paso 3.5 — PONDERAR POR EVIDENCIA, no por criterio del diseñador ⭐ (v2.0)
**Antes de repartir horas, medir.** Un currículo diseñado a ojo reparte simétrico y se equivoca.
Tres mediciones locales, todas baratas:

- **Qué se trabaja de verdad:** ocurrencias por dominio en las sesiones —
  `grep -hoEi "<patrón>" ~/.claude/projects/*/*.jsonl | wc -l`.
  Contar ocurrencias, **nunca presencia**: la presencia satura al 100 % porque el prompt del sistema
  arrastra la memoria completa en cada sesión.
- **Qué se cura:** volúmenes de las skills `intereses-*` (X.com) y de los buckets `intereses-lkd-*`.
- **Qué está declarado vivo:** las entradas `project_*` de `MEMORY.md`.

Las cuatro lecturas que ordenan el reparto:

| Patrón | Lectura | Decisión |
|---|---|---|
| Alto en trabajo + alto en curación | El dominio manda | Súbele horas |
| Bajo en trabajo, alto en curación | Interés real sin cauce | Microciclo propio |
| Bajo en todo, pero estaba en el plan | Gusto del diseñador | **Sale** |
| Muy bajo en menciones pese a usarse a diario de forma implícita | **Brecha, no falta de demanda** | Súbele horas |

El último caso es el más difícil y el más importante: **no se pide lo que no se sabe pedir**. En esta
casa fue la matemática — 962 menciones frente a decenas de miles del resto, mientras se usan VAN,
TIR, DSCR y elasticidad todo el año sin el vocabulario formal para discutirlos.

Precedente completo con los números: `notas/2026-09-05_ponderacion-por-evidencia.md` en
`E:/vars/var 5/Universidad-Abierta/`.

### Paso 4 — Calendario de adulto: la hora diaria ⭐ (v2.0)
El formato por defecto de esta casa es **una sesión diaria de 60 minutos**, seis días por semana.
La frecuencia vence a la duración: seis contactos semanales producen seis consolidaciones, dos
producen dos — y una hora sobrevive a una semana de obra, tres horas seguidas no.

**Estructura invariable de la sesión** (la invariancia es la mitad del método):
- **0-5 min** recuperación de ayer, **a libro cerrado**;
- **5-45 min** núcleo: fuente única, una sola pasada, sin copiar;
- **45-55 min** un problema, hasta donde llegue;
- **55-60 min** tres líneas en un **único archivo continuo**, nunca uno nuevo por día.

**La semana:** L-M-X-J núcleo · V día del expediente (aplicar a un proyecto real) · S consolidación
y entregable · D vacío, no negociable.

**La unidad de planificación es el microciclo de 4 semanas = 24 h**, no el bloque de 12 semanas:
resiste mejor las interrupciones y permite reordenar sin romper prerrequisitos.

Reglas del formato diario:
- El problema **se deja a medias sin culpa** — encadenarlo tres días es normal y deseable (Zeigarnik).
- Si se pierde un día, **no se dobla la hora**: se corre el calendario. Doblar rompe el hábito, que
  es lo único que sostiene 48 semanas.
- Alternativa histórica (v1.0), válida si el usuario la prefiere: 6 h semanales en bloques de 2 h
  exposición + 2,5 h problemas + 1 h recuperación + 0,5 h entregable
  ([[memoria-aprendizaje-seis-reglas]]).

### Paso 5 — Protocolo de estudio de cada unidad
Cuando la unidad tenga corpus cerrado (PDF, transcripciones), aplicar
[[metodo-mit-notebooklm-riguroso]] con clausura de alcance. Cuando sea un curso vivo, el
ciclo semanal es: **ver → resolver → explicar → verificar**, donde *explicar* significa
producir tres minutos de exposición con la disciplina de [[winston-how-to-speak-mit]].

### Paso 6 — Entrega como HTML viva
El programa se entrega como página autocontenida en
`G:\Mi unidad\Clases-Magistrales-HTML`, siguiendo el patrón del Aula
([[entrega-visual-html-vs-texto]]) y registrándose en `index.html`.

## Patrón obligatorio de la HTML viva

Copiar la estructura de las clases existentes (`01-winston-how-to-speak.html` en adelante):

- **Un solo archivo**, sin dependencias externas, que abre sin conexión y se imprime.
- **Tokens de color en `:root`** con bloque `@media (prefers-color-scheme:dark)`. Rojo MIT
  `#A31F34` para el marco institucional; un color propio por clase.
- **Secciones canónicas**, en este orden:
  1. cabecera con badge, título y quién dicta;
  2. **la tesis en una frase** (por qué esta materia y no otra);
  3. mapa conceptual o malla de prerrequisitos (SVG inline, sin librerías);
  4. las unidades, cada una con fuente única enlazada, entregable y horas;
  5. **glosario** de los términos que hay que poder definir de memoria;
  6. **recuperación activa**: 8-12 preguntas con la respuesta plegada en `<details>`;
  7. **aplicación al expediente en curso** — el puente al negocio real;
  8. pie con fuentes, licencias y fecha de verificación.
- **Nada de datos sensibles** (cifras de caja, nombres de contraparte) en una página pensada
  para compartirse.
- **Contraste y despliegue, verificados con número (regla del 11-sep-2026):** letra siempre más
  oscura que los fondos; fondos vivos pero PASTEL; texto de acento con ratio ≥ 4,5 sobre tarjeta, fondo y
  pastel; `<summary>` con indicador explícito. Tras crear o editar cualquier página del Aula, ejecutar
  `python "E:/vars/var 5/Universidad-Abierta/a11y/reparar_contraste.py"` (idempotente, respalda la
  primera vez) y comprobar con `diagnostico_contraste.py`. Ningún acento vivo (`--a2`) como color de
  texto; ningún gradiente saturado con letra blanca en cabeceras.
- **Carpetas temáticas (regla del 13-sep-2026):** el Aula ya no es plana. Toda página nueva nace
  DENTRO de su carpeta (`00-programa-y-catalogo` · `01-aprender-y-comunicar` · `02-metodo-y-fuentes` ·
  `03-estrategia-y-negocios` · `04-ia-y-sistemas` · `05-matematica` · `06-economia-y-finanzas` ·
  `07-proyectos-de-la-casa`) y enlaza con rutas relativas (`../index.html`, `../05-matematica/…`).
  Su tarjeta se añade en el `index.html` de la raíz bajo el rótulo `.grp` de su carpeta, y su nombre
  se registra en `CARPETAS` de `E:\vars\var 5\Universidad-Abierta\reorganizar_aula.py`; correr ese
  script (idempotente, verifica que no quede ningún enlace roto) si la página se creó en la raíz.
  Nombres de archivo sin espacios.
- **Espejo en NotebookLM (regla del 19-sep-2026):** cada página del Aula tiene su PDF y vive como
  fuente en el cuaderno «Aula de Clases Magistrales — MIT & Stanford» (id `97f4018b`, cuenta
  mobijuesa360). Al crear o editar una página: (1) cosechar la sesión del CLI
  (`C:\Users\datos\war_room_tmp\cosechar_nlm.py`); (2) `python "E:/vars/var 5/Universidad-Abierta/aula_a_pdf.py" <fragmento>`
  (Edge headless, tema claro, respuestas desplegadas); (3) si la página ya estaba en el cuaderno,
  `notebooklm source delete-by-title "<título>" -n 97f4018b -y`; (4)
  `python "E:/vars/var 5/Universidad-Abierta/subir_aula_notebooklm.py" 97f4018b-8588-4b92-bd41-2cb5c82610f7 --solo <fragmento>`.
  Detalle y trampas en la memoria `reference_cuaderno_aula_clases_magistrales`.

## Compuertas 🚦

- **No prometer «dominar X en 48 horas».** Esa promesa es de la publicidad, no del MIT. El
  programa declara horas reales y el usuario decide.
- **No repartir horas por simetría ni por gusto.** Si el reparto no se puede defender con una de las tres mediciones, no está diseñado.
- **No apilar fuentes.** Si una unidad tiene tres fuentes principales, el diseño está mal.
- **No generar un programa sin entregables.** Si una unidad no termina en algo calificable,
  se reescribe.
- **No suplantar la prueba de dominio con la sensación de haber entendido.** La ilusión de
  fluidez es el enemigo: por eso las preguntas de recuperación activa son obligatorias.
- **Verificar cada URL antes de publicarla en la HTML.** Un enlace roto en una página que se
  comparte destruye la credibilidad de todo el material.

## Ejemplos de invocación

- «Ármame el programa de probabilidad que necesito para entender el modelo de riesgo de Belén.»
- «Quiero dominar álgebra lineal para poder discutir de IA sin asentir a ciegas. 6 h/semana.»
- «Convierte el programa de estudios generales en una clase magistral HTML y súbelo al Aula.»

## Relacionado

- Catálogo de fuentes: [[universidad-abierta-catalogo]]
- Estudio con corpus cerrado: [[metodo-mit-notebooklm-riguroso]]
- Memoria y repaso: [[memoria-aprendizaje-seis-reglas]]
- Formato de entrega: [[entrega-visual-html-vs-texto]]
- Exposición: [[winston-how-to-speak-mit]] · [[neuro-oratoria-presentacion-persuasiva]]
- Costo antes de comprometerse: [[cuantificar-antes-de-pedir]]
- Agente que lo ejecuta: `estudios-generales`
