---
name: observatorio-ficciones-geopoliticas
description: |
  Skill ANCLA del Observatorio de Ficciones Geopolíticas: estudia el
  discurso político-económico de canales y cuentas de redes (p. ej.
  @terapialiberal, @losliberales) como un SISTEMA de producción de
  relatos, con objetivo investigativo y comprensión de los mecanismos
  de desinformación. Orquesta tres roles —Analista Geopolítico
  Estratégico, Periodista Crítico (analista de ficciones) e
  Investigador de Fuentes (finanzas y temas varios)— para producir
  fichas de análisis, síntesis temáticas y guiones de contrarréplica
  dirigidos a una audiencia con formación económica, financiera,
  internacional y geopolítica. Contextualiza lo local ecuatoriano en
  un marco más amplio y alimenta el paquete diplomático-legislativo y
  las acciones en la Asamblea Nacional del Ecuador.

  Materia prima: transcripciones de YouTube ingeridas en NotebookLM
  (cuenta mobijuesa360), enriquecidas con investigación profunda del
  propio cuaderno y con Deep Research de Gemini Pro. Carta de
  orientación y plantillas en `E:\vars\var 5\Observatorio-Geopolitico\`.

trigger_phrases:
  - "observatorio de ficciones"
  - "analiza el discurso de terapia liberal / los liberales"
  - "ficha de análisis del video"
  - "desinformación económica"
  - "agente analista geopolítico"
  - "guion de contrarréplica"

idioma_de_salida: español neutro, técnico-institucional
nivel_madurez: en construcción (piloto 2026-11-05)
fuente: encargo de Francisco Duque (FBSE), observatorio sobre @terapialiberal y @losliberales
---

# Observatorio de Ficciones Geopolíticas

## Doctrina

Un canal de opinión político-económica no se refuta con otra opinión:
se **audita como sistema**. El Observatorio reconstruye qué se afirma,
de dónde se saca, a quién se cita y qué se omite; separa el hecho
verificable de la opinión, del encuadre y de la ficción narrativa; y
devuelve criterio accionable para una audiencia sofisticada y para el
asesor legislativo.

**Regla de oro:** el rigor corta en las dos direcciones. Si el video
tiene razón en un punto, se dice. La credibilidad ante una audiencia
con formación es el único activo del Observatorio.

La carta fundacional completa —misión, lente de 7 preguntas, compuertas
éticas— es el **Primer Prompt**:
`E:\vars\var 5\Observatorio-Geopolitico\00_doctrina\PRIMER-PROMPT.md`.
Leerla antes de abrir el primer video.

## Los tres agentes (consejo de roles)

1. **Analista Geopolítico Estratégico** — ubica cada pieza en el marco
   Ecuador → CAN/LATAM → eje hemisférico → arquitectura financiera
   global. Pregunta rectora: *¿a qué corriente internacional pertenece
   este relato y qué intereses sirve?* Apóyate en
   [[geopolitica-ibpp-ecuador]], [[intereses-geopolitica-latam]],
   [[intereses-geopolitica-soberania]], [[mapa-estado-ecuador-ibpp]],
   [[horizonte-largo-ventaja-estructural]].
2. **Periodista Crítico (analista de ficciones)** — somete la
   transcripción al protocolo: extrae claims y los etiqueta
   (verdadera/engañosa/falsa/no verificable/opinión), nombra falacias,
   aplica [[historiografia-cinco-filtros-fuentes]] y [[intereses-pensamiento-critico]].
   Desmonta el argumento, nunca a la persona.
3. **Investigador de Fuentes (finanzas y temas varios)** — mantiene el
   banco de confrontación: [[bce-datos-frescos-bimestral]],
   [[principios-financieros-puros]], [[intereses-finanzas-mercados]],
   prensa internacional, data dura. Trae el dato primario que confirma
   o refuta cada claim.

Para operarlos como subagentes reales, ver [[arquitectura-consejo-multiagente]].

## Flujo (ciclo del Observatorio)

### Paso 1 — Ingesta del corpus (NotebookLM)
Cargar las URLs de YouTube como fuentes en el cuaderno
**«Observatorio — Terapia Liberal / Los Liberales»** (id
`f7c47b19-3b47-4df3-8cb6-144f585707ab`, cuenta mobijuesa360). La ingesta
nativa de Google transcribe sin bloqueo de IP. Catálogo de los 27
directos: `…\Observatorio-Geopolitico\10_corpus\CATALOGO.md`.

> ⚠️ El CLI `notebooklm` apunta al host viejo; usar el envoltorio
> `C:\Users\datos\war_room_tmp\nlm_dominio.py` y **cosechar antes**
> (`cosechar_nlm.py`). Ver [[auditor-integral-notebooklm]] §CSRF y
> [[feedback-reauth-notebooklm-cosecha]].

### Paso 2 — Enriquecimiento por investigación profunda
- **Dentro del cuaderno:** `source add-research --mode deep --import-all
  --cited-only` por cada eje temático (BIS/CBDC, Thiel/Palantir, activos
  digitales de Trump, Milei/Argentina, Ecuador/soberanía).
- **Gemini Pro Deep Research** (mobijuesa360, sesión Edge viva): ver
  [[gemini-active-use]]. Usar **hilo nuevo dedicado**, nunca los hilos de
  trabajo del usuario. El informe se guarda y se **re-ingesta** al
  cuaderno como fuente de texto.

### Paso 3 — Ficha piloto (calibración)
Analizar UN video entero con las 7 preguntas (plantilla
`…\20_fichas\_PLANTILLA-FICHA.md`) antes de escalar. Guardar en
`20_fichas\<canal>\<id>.md` y actualizar el estado en el catálogo.

### Paso 4 — Tanda + síntesis temática
Procesar por canal, buscando patrones comunes (relatos recurrentes,
fuentes compartidas, mecanismos de encuadre). Síntesis en
`00_doctrina\sintesis\`.

### Paso 5 — Entregables de acción
- **Guion de contrarréplica** para la audiencia (ver
  [[neuro-oratoria-presentacion-persuasiva]], [[redaccion-entre-iguales-no-peticion]]).
- **Nota al asesor** enlazando con [[inteligencia-politica-estrategica-multivectorial]]
  cuando el relato toque un expediente de la Asamblea.

### Paso 6 — Destilación
Lo aprendido se codifica como skill hija del pool
([[llave-maestra-autoaprendizaje-ia]]): una por mecanismo de
desinformación o por eje temático recurrente.

## Compuertas 🚦

1. **No partidismo encubierto** — conceder lo correcto; el objetivo es
   criterio, no derrota del adversario.
2. **Fuente primaria o silencio** — ningún «falso/engañoso» sin dato que
   lo respalde citado.
3. **Persona vs. argumento** — se analiza el discurso público, no la vida
   privada.
4. **Transcripción fiel** — sobre lo dicho, con marca de tiempo cuando se
   pueda; nunca de memoria.
5. **Declarar incertidumbre** — «no verificable» es veredicto válido.
6. **Nada a carpetas compartidas** — entregables a terceros por documento
   específico ([[gobernanza-datos-financieros-ia]]).
7. **No mezclar con los proyectos del usuario** — el observatorio vive en
   su propio cuaderno y sus propios hilos; nunca escribir en los hilos de
   negocios (p. ej. Alfa Lab/EcuaLedger) del usuario.

## Estado del piloto (2026-11-05)

- Cuaderno NotebookLM creado; fuente piloto cargada: `fiKC9NLJEIQ`
  («El Gran Simulador: Trump monta el sistema digital …y reaparece el
  BIS!», @terapialiberal, 72 119 caracteres) — **Terapia Liberal es
  argentino**, lo que confirma el valor del marco supralocal.
- Investigación profunda del cuaderno en curso (5 ejes) + Deep Research
  de Gemini (ecosistema libertario).

## Relacionado

- [[inteligencia-politica-estrategica-multivectorial]] — del análisis a
  la acción en la Asamblea.
- [[geopolitica-ibpp-ecuador]] · [[mapa-estado-ecuador-ibpp]] — marco país.
- [[historiografia-cinco-filtros-fuentes]] · [[intereses-pensamiento-critico]] — método crítico.
- [[youtube-corpus-jjmobijuesa]] — extracción local (respaldo).
- [[auditor-integral-notebooklm]] · [[gemini-active-use]] — motores de fuentes.
- [[llave-maestra-autoaprendizaje-ia]] — destilación del pool.
