# Marco provisional — Agente integrado de estudios generales

> ⚠️ **Hipótesis del espejo, no el tema real.** Lo redactó el espejo en la nube (2026-09-28 21:57,
> Guayaquil) sin volcado de la PC y a partir de las skills candidatas de `ESTADO.md`.
> **El tema real lo confirma la PC** en su primer volcado. Si la PC lo contradice, prevalece la PC.
> Este archivo solo contiene resúmenes y punteros; no contiene datos personales ni financieros.

## 1. De qué podría tratar el hilo (según las skills)

Tres de las cinco skills declaran `agente: estudios-generales`, así que el hilo es casi con
seguridad el **agente que ejecuta ese sistema**:

| Skill | Papel en el sistema | Ruta local (PC) |
|---|---|---|
| `universidad-abierta-catalogo` | **Biblioteca**: 50 fuentes abiertas verificadas por HTTP, en 8 pilares (P1 método … P8 herramientas), y la malla MIT con sus URL. Responde «¿de dónde lo saco?» | `E:\vars\var 5\Universidad-Abierta\catalogo-50-fuentes.json` + `consultar_universidad.py` |
| `programa-estudio-profundo-mit` (v2.0) | **Fábrica de programas**: encuadre → fuentes por catálogo → malla y prerrequisitos → ponderación por evidencia (paso 3.5) → hora diaria en microciclos de 4 semanas (24 h) → HTML viva | Programas en `E:\vars\var 5\Universidad-Abierta\programas`; HTML en `G:\Mi unidad\Clases-Magistrales-HTML` |
| `metodo-mit-notebooklm-riguroso` | **Método de estudio de cada unidad**: 3 preguntas + 2 extras sobre un corpus de NotebookLM **ratificado** (Paso 0 no omisible) | Transcripción en `C:\Users\datos\.notebooklm-extractos\` |
| `intereses-educacion-aprendizaje` | **Evidencia de interés**: 917 bookmarks de X curados. Sirve de insumo para ponderar horas (paso 3.5), no como fuente de estudio («curar no es estudiar») | `E:\vars\var 5\X-com guardados\` |
| `tutor-mit-ecuablock` | **Variante aplicada** a un expediente (EcuaBlock, 5 audiencias). Probablemente periférica, salvo que el hilo sea preparar a Francisco en ese expediente | Cuaderno NotebookLM «EcuaBlock - IBPP» |

**Hipótesis principal:** diseñar y poner en marcha un **programa de estudios generales** para
Francisco (adulto con empresa, obra y familia), con 1 h diaria y un entregable calificable por
unidad. Las fuentes saldrían del catálogo, el estudio seguiría el método MIT-NotebookLM y la
entrega sería una HTML viva en el Aula de Clases Magistrales.

**Hipótesis alternativas:**
- (b) Mantener el propio sistema: re-verificar las 50 fuentes, ampliar el catálogo y corregir skills.
- (c) Un programa de una materia concreta ligada a un expediente (EcuaLedger, Belén, QVP, libro Kleper…).
- (d) Preparación en el expediente EcuaBlock con `tutor-mit-ecuablock`.

## 2. Qué debe volcar la PC (primer volcado)

En `ESTADO.md` y en resúmenes `.md` dentro de `archivos/`. **Solo rutas locales y
conclusiones, nunca el documento fuente.**

1. **Tema confirmado**: cuál de las hipótesis (o cuál otra) y el objetivo en una frase.
2. **Encuadre del paso 1**, si ya existe: materia, para qué, nivel de partida, horas por
   semana y semanas, prueba de dominio.
3. **Estado de artefactos** (existe / versión / fecha):
   - `catalogo-50-fuentes.json`: número de fuentes y fecha de la última verificación HTTP;
   - carpeta `programas/`: qué programas hay y en qué microciclo van;
   - `Clases-Magistrales-HTML`: qué HTML existen y cuál está en `index.html`.
4. **Resultado del paso 3.5 (ponderación)**, si se hizo: la tabla de pilares con su peso y la
   decisión de horas, **en resumen**.
5. **Corpus NotebookLM ratificado**, si lo hay: cuaderno, etiquetas y lista nominal de fuentes
   (solo títulos). El espejo no puede aplicar el método MIT sin ese Paso 0.
6. **Razonamiento en curso** y **siguiente paso exacto**.
7. **Archivo principal**: cuál es y su ruta local.
8. **Bloqueantes de la PC**: lo que solo la PC puede hacer (helpers Python en `E:\`,
   Google Drive `G:\`, navegador Edge para los 4 sitios que devuelven 403 a bots, NotebookLM).

## 3. Preguntas abiertas para Francisco

1. ¿El hilo es el **programa de estudios generales** (hipótesis principal) o otra cosa?
2. ¿Hay una **materia prioritaria** o se empieza por la formación general de los 8 pilares?
3. ¿Qué **expediente** justifica el estudio (EcuaLedger, Belén, QVP, Kleper, EcuaBlock) o
   ninguno (formación general)?
4. ¿Se mantiene la **1 h diaria** (L–J núcleo, V expediente, S consolidación) o cambia?
5. ¿Qué **prueba de dominio** acepta como evidencia de aprendizaje?
6. ¿Qué parte puede avanzar el **espejo en la nube** sin la PC? Por ejemplo: redactar sílabos,
   problem sets y la HTML en borrador dentro del repo, verificar URL por HTTP, preparar las
   preguntas MIT.
7. ¿Las HTML finales viven solo en `G:\` o también se publican (artifact o repo)?

## 4. Propuesta de estructura de trabajo

**Reparto PC ⇄ nube**
- **PC:** todo lo que toca `E:\`, `G:\`, NotebookLM y Edge. Ejecuta helpers, consulta el
  catálogo, guarda las HTML finales y ratifica corpus.
- **Espejo:** trabajo de texto. Redacta sílabos, unidades, problem sets con solución, preguntas
  MIT y borradores de HTML como `.md` en `archivos/`. También verifica fuentes por HTTP desde
  la nube, sin los 4 sitios 403, y hace las revisiones de coherencia entre skills.

**Carpeta `archivos/` propuesta** (todo `.md`):
```
archivos/
├── marco-estudios-generales.md   # este archivo (provisional)
├── encuadre.md                   # paso 1 ratificado por Francisco
├── ponderacion-pilares.md        # paso 3.5: resumen de la medición y reparto de horas
├── programa-<materia>.md         # ARCHIVO PRINCIPAL propuesto: malla, unidades, horas
├── microciclo-01.md              # 4 semanas × sesiones, entregable por unidad
└── punteros-pc.md                # rutas locales de catálogo, programas, HTML y cuadernos
```

**Secuencia**
1. PC: primer volcado y confirmación del tema.
2. Francisco responde las preguntas 1–5 → `encuadre.md`.
3. Ponderación (paso 3.5): la mide la PC y el resumen queda en `ponderacion-pilares.md`.
4. Malla y fuentes por catálogo (una fuente por unidad) → `programa-<materia>.md`.
5. Microciclo 1 con entregables → `microciclo-01.md`.
6. PC: HTML viva en `Clases-Magistrales-HTML` e `index.html`.
7. Estudio diario: el método MIT-NotebookLM se aplica por unidad, con el corpus ratificado.

**Compuertas:** sin horas declaradas no hay programa; no se promete «dominar en 48 h»;
no se cita una fuente fuera del catálogo o sin verificar; no se aplica el método MIT sin el Paso 0.
