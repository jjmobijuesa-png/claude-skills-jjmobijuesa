# Volcado 01 de la PC — Agente integrado de estudios generales

> Escrito por la PC el 2026-09-28 (Guayaquil). Confirma el tema del hilo y corrige el marco
> provisional del espejo donde hacía falta. Solo rutas locales y conclusiones: sin documentos
> fuente, sin cifras de expedientes, sin datos personales ni financieros.

## 1. Tema confirmado

**Hipótesis (a) del marco, confirmada** — con una corrección de fondo: el sistema no está por
diseñarse, **está operando**. El hilo es el agente que sostiene el **Aula de Clases Magistrales**:
un programa de estudios generales de una hora diaria, con sus fuentes verificadas, sus páginas HTML
vivas y su espejo en NotebookLM.

Objetivo en una frase: **que Francisco estudie una hora al día sobre fuentes verificadas y que cada
unidad deje un entregable usable en un expediente real de la casa.**

Las hipótesis (b), (c) y (d) del marco no son alternativas: son partes. (b) el mantenimiento del
catálogo ya es rutina; (c) el anclaje a un expediente ya es la regla de todos los entregables;
(d) `tutor-mit-ecuablock` es una variante aplicada aparte, no este hilo.

## 2. Encuadre (paso 1) — ya ratificado, v2.0

| Campo | Valor |
|---|---|
| Materia | Formación general en 8 pilares, con la matemática como brecha declarada |
| Para qué | Discutir de igual a igual lo que ya se trabaja sin vocabulario formal (VAN, TIR, DSCR, sensibilidad, elasticidad) y sostener las defensas institucionales |
| Nivel de partida | Adulto con empresa, obra y familia; veinte años sin derivar |
| Carga | **1 hora diaria**, microciclos de 4 semanas = **24 h por microciclo**, **12 microciclos**, **288 h / 48 semanas** |
| Ritmo semanal | L–J núcleo · V expediente · S consolidación |
| Prueba de dominio | Un **entregable** por microciclo, anclado a un expediente real. Único filtro duro del año: la diagnóstica de precálculo del MC1 (80 % o se repite) |
| Orden | Los prerrequisitos son fijos; dentro de eso, «el orden lo manda el expediente que apremie» |

## 3. Estado de artefactos (verificado en disco hoy)

| Artefacto | Estado real | Ruta local |
|---|---|---|
| Catálogo de fuentes | **51 recursos** (no 50), v1.1, verificación HTTP del **2026-09-05** con `curl -L`, user-agent de navegador, timeout 12 s. Resultado: 42 vivas · 4 reemplazadas · **4 bloquean bots (403)** · 1 redirige. Más 2 en anexo fuera de la lista original. **9 pilares** (P1–P8 académicos + P9 «oficio financiero», que no es academia) | `E:\vars\var 5\Universidad-Abierta\catalogo-50-fuentes.json` · consulta con `consultar_universidad.py --query <tema>` |
| Programa | **v2.0 completo**, 12 microciclos con fuente única, prerrequisitos y entregable declarados uno por uno | `G:\Mi unidad\Clases-Magistrales-HTML\00-programa-y-catalogo\15-programa-estudios-generales.html` (38 KB) |
| Páginas del Aula | **30 HTML** (29 en 8 carpetas temáticas + `index.html`), reorganizadas el 13-sep-2026, enlaces relativos verificados sin roturas y contraste WCAG comprobado por cálculo | `G:\Mi unidad\Clases-Magistrales-HTML\` |
| PDF del Aula | **30 PDF** (33 MB) con las respuestas de recuperación activa desplegadas | `…\Clases-Magistrales-HTML\_pdf\<carpeta>\` + `manifiesto.json` |
| Cuaderno NotebookLM | **31 fuentes, todas `ready`** | ver §5 |

### Reparto de las páginas por carpeta

`00-programa-y-catalogo` 2 · `01-aprender-y-comunicar` 2 · `02-metodo-y-fuentes` 2 ·
`03-estrategia-y-negocios` 5 · `04-ia-y-sistemas` 3 · `05-matematica` 11 ·
`06-economia-y-finanzas` 3 · `07-proyectos-de-la-casa` 1.

### Los 12 microciclos y su cobertura en páginas

| MC | Título | Pilar · horas | ¿Tiene páginas? |
|---:|---|---|---|
| 1 | Método y reparación algebraica | Matemática · 24 h | **Sí** — maestra + 4 clases |
| 2 | Cálculo, a nivel de uso | Matemática · 24 h | **Sí** — maestra + 4 clases |
| 3 | Estadística y probabilidad aplicadas ⭐ | Matemática · 24 h (requiere M2) | **No** — hueco |
| 4 | Valoración y costo de capital | Finanzas · 24 h (M3) | No |
| 5 | Estados financieros y variaciones | Finanzas · 24 h (M4) | No |
| 6 | Evaluación de proyectos | Proyectos y fondos · 24 h (M4) | No |
| 7 | Gestión de proyectos y ruta crítica | Proyectos y fondos · 24 h (M6) | No |
| 8 | Redacción de propuestas y memorandos | Escritura · 24 h (M6) | No |
| 9 | Argumentación y exposición | Escritura · 24 h (M8) | No |
| 10 | Computación sobre los datos propios | Computación · 24 h (M3) | No |
| 11 | Economía política e instituciones ⭐ | Nuevo en la v2 · 24 h | No |
| 12 | Juicio, evidencia e identidad | Filosofía · 24 h (M9) | No |

**El hueco que manda:** el **MC3** es el único microciclo que el propio programa marca como «el más
importante del año», está habilitado (M2 ya tiene sus páginas) y no tiene material. Ahí está el
siguiente trabajo real del hilo.

## 4. Paso 3.5 — ponderación por evidencia (hecha el 2026-09-05)

Se midió en lugar de suponer, con tres fuentes locales independientes: 83 sesiones de trabajo
(427 MB de transcripciones, contando **ocurrencias**, no presencia), 9.739 bookmarks curados de X en
17 temas, y 7 buckets de LinkedIn. Resumen sin cifras de expedientes:

1. **La matemática es la brecha, no la demanda.** Es el dominio menos mencionado por un factor de
   veinte. Lectura correcta: no se pide lo que no se sabe pedir. Sube de 48 a **72 h** (3 microciclos).
2. **La computación estaba sobredimensionada por gusto del diseñador.** «Tecnología y programación»
   es el tema **menos curado** de diecisiete y el trabajo computacional real se delega en agentes.
   Baja de 72 a **24 h**; nand2tetris sale del currículo y queda como optativa en el catálogo.
3. **Faltaba lo más curado de todo.** Geopolítica y soberanía es el máximo absoluto de la curación y
   no aparecía en el plan. Entra como **MC11**, economía política e instituciones.

Detalle completo: `E:\vars\var 5\Universidad-Abierta\notas\2026-09-05_ponderacion-por-evidencia.md`.

## 5. Corpus NotebookLM ratificado (Paso 0 cumplido)

**Cuaderno:** «Aula de Clases Magistrales — MIT & Stanford» · id `97f4018b-8588-4b92-bd41-2cb5c82610f7`
· cuenta `mobijuesa360@gmail.com` · **31 fuentes, todas `ready`**, creado el 19-sep-2026.

Son los 30 PDF del Aula más una guía de uso. Los títulos llevan el prefijo de la carpeta temática
—`[06 Economía y finanzas] Lectura 01 · Entender bien el dinero`— para que el chat cite con contexto.
Grounding verificado con un `ask` real: devolvió respuestas correctas con citas `[n]`.

**El espejo ya puede aplicar el método MIT**: el Paso 0 no está pendiente, está cumplido. Lo que el
espejo no puede hacer es consultar el cuaderno (eso exige la PC); sí puede redactar las 3+2 preguntas
por unidad para que la PC las corra.

## 6. Archivo principal

- **En la PC (el que manda):** `G:\Mi unidad\Clases-Magistrales-HTML\00-programa-y-catalogo\15-programa-estudios-generales.html`.
  Es la fuente de verdad del encuadre, la malla, los prerrequisitos y los entregables.
- **En este canal (`archivos/`):** este volcado, hasta que exista `programa-mc03.md`, que pasará a ser
  el principal del hilo mientras se trabaje el MC3.

## 7. Bloqueantes: lo que solo puede hacer la PC

1. Escribir en `G:` (Drive) y leer `E:\vars\var 5\`.
2. Ejecutar los helpers: `consultar_universidad.py`, `reorganizar_aula.py`, `aula_a_pdf.py`
   (Playwright sobre **msedge headless**), `subir_aula_notebooklm.py`, la pasada de contraste de `a11y/`.
3. NotebookLM: cosechar la sesión, subir fuentes, `ask`. Cuenta `mobijuesa360@gmail.com`.
4. Edge con navegador logueado (CDP 9222) para las **4 fuentes que devuelven 403 a bots**.
5. OCR de PDF escaneados con `rapidocr-onnxruntime`.

## 8. Respuestas a las 7 preguntas del marco

1. **¿Es el programa de estudios generales?** Sí, hipótesis (a). Con la corrección de la §1: ya está
   operando, no por diseñar.
2. **¿Materia prioritaria?** **Matemática**, y dentro de ella el **MC3, estadística y probabilidad
   aplicadas**: es el siguiente por prerrequisito y el que el programa marca como el más importante
   del año.
3. **¿Qué expediente justifica el estudio?** Formación general, pero **ningún entregable es
   abstracto**: cada microciclo descarga en un expediente vivo de la casa (proyectos de vivienda,
   cartera, postulación a fondos multilaterales, cierre mensual). La regla escrita en el programa es
   que el orden lo manda el expediente que apremie.
4. **¿Se mantiene la hora diaria?** Sí: es el encuadre v2.0 ratificado — L–J núcleo, V expediente,
   S consolidación, 24 h por microciclo. Cambiarlo es decisión de Francisco.
5. **¿Qué prueba de dominio?** El **entregable** del microciclo, no un cuestionario: un artefacto que
   se pueda usar en el expediente. Único filtro duro: la diagnóstica del MC1 con 80 %.
6. **¿Qué puede adelantar el espejo sin la PC?** Redactar en `.md`: el sílabo del MC3, sus 4 clases,
   los problem sets **con solución**, las 3+2 preguntas del método MIT y el borrador de contenido de
   las páginas. También auditar la coherencia entre el programa y las skills, y verificar URL por HTTP
   salvo las 4 que dan 403. No puede: tocar `G:`, ejecutar los helpers, usar NotebookLM ni Edge.
7. **¿Dónde viven las HTML?** Canónicamente en `G:\Mi unidad\Clases-Magistrales-HTML` (8 carpetas
   temáticas, enlaces relativos, ninguna página en la raíz salvo `index.html`). Espejo en `_pdf\` y en
   el cuaderno de NotebookLM. **No se publican en la web.**

## 9. Siguiente paso propuesto y reparto

**Trabajo propuesto: el Microciclo 3 — Estadística y probabilidad aplicadas.** Fuente única del
programa: *OpenStax Introductory Statistics*; formalización con MIT 6.041 clases 1–8; verificador
Wolfram Alpha. Requiere M2, que ya está cubierto.

| Paso | Lado | Entregable |
|---|---|---|
| 1 | **Espejo** | `programa-mc03.md`: sílabo de 24 h en 4 semanas, con la clase maestra y 4 clases, prerrequisitos por sesión y el entregable declarado |
| 2 | **Espejo** | `mc03-problem-sets.md`: ejercicios con solución desarrollada, y las 3+2 preguntas del método MIT por clase |
| 3 | PC | Las 5 páginas HTML en la casa de estilo del Aula, en `05-matematica\`, más la tarjeta en `index.html` |
| 4 | PC | Pasada de contraste a11y, PDF con `aula_a_pdf.py` y subida al cuaderno con `subir_aula_notebooklm.py` |
| 5 | PC | Correr en NotebookLM las preguntas del método MIT sobre el corpus ampliado |

**Compuerta:** el paso 1 es contenido nuevo del Aula. Antes de que el espejo redacte, conviene el OK
de Francisco sobre el MC3 como siguiente microciclo (frente a saltar al MC4 o al MC11, que también
están habilitados por interés aunque no por prerrequisito).

**Regla de casa que el espejo debe respetar al redactar:** voz Francisco Duque, «usted»,
cortés-formal; **nunca `≈` ni `~`**; en un canal compartido, entregables descritos **sin cifras de
expedientes, ubicaciones, contactos ni cotizaciones exactas**.
