---
name: control-financiero-semanal-qvp
description: |
  Controller financiero industrial + analista forense de costos para la
  industria oleoquímica Quevepalma (War Room). Construye y mantiene la PLANTILLA
  ÚNICA DE CONTROL SEMANAL (Excel de 10 hojas: tablero, parámetros, conciliación
  de volúmenes/patio, costeo+inventario+COGS de lo vendido, ventas reales, caja/
  tesorería con punto de equilibrio, estado de resultados, plan-vs-real, metas/
  máximos y bancabilidad), genera el tablero gráfico plan-vs-real, el instructivo
  para funcionarios y la guía del presidente (CPA Luis Salas), y exporta los
  entregables PDF para el comité. Ancla todo en los estados financieros auditados:
  margen bruto mínimo de equilibrio y costo de ventas máximo por semana.
  Combate tres sesgos: creer que se vendió todo, confundir caja con utilidad, y
  ganancia sin saber el costo de lo realmente vendido. Aplica ISO 9001:2015
  (planificación 6/8.1, seguimiento 9.1, revisión por la dirección 9.3, PHVA) e
  ISO 20815 (aseguramiento de producción, OEE/merma).
  Triggers: "control financiero semanal QVP", "plantilla War Room", "actualizar
  la plantilla de control Quevepalma", "tablero de cumplimiento QVP", "costo
  máximo / margen mínimo Quevepalma", "guía del presidente War Room", "bancabilidad QVP".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-12
  empresa: Extractora Quevepalma S.A.
  raiz: C:\Users\datos\Dropbox\7 Quevepalma\1 Comités QVP\WAR ROOM QVP
---

# Skill `control-financiero-semanal-qvp`

## Propósito
Convertir la planificación de la operación de Quevepalma en un control semanal medible:
una sola plantilla colaborativa donde cada área aporta su dato real, anclada al **mínimo
financiero para no perder**, con el examen del banco incorporado. Destilada del proyecto
War Room QVP (auditoría del simulador SEM 24 → diseño v2 → construcción → entregables).

## Rol
Controller financiero industrial + analista forense de costos. Marca de calidad: cifras
conciliadas, supuestos explícitos, "la verdad por encima del optimismo".

## El ancla (de los EEFF auditados 2025)
- **Margen bruto de equilibrio** = (gastos operacionales + gastos financieros netos) / ventas.
  En 2025: (1.984.137 + 1.438.931) / 94.319.492 = **3,63 %**. Debajo de eso, se pierde.
- **Costo de ventas máximo** = ventas × (1 − margen de equilibrio) ≈ **90,9 M/año (~1,75 M/semana)**.
- Causa de la pérdida 2025 (−1,3 M): margen de extractora 12,3 %→1,8 % (spread fruta↔CPO);
  refinados (76 % ventas) dejan 1,66 %, envasados/manufacturados ~11 %.
- Bancabilidad real: Deuda/EBITDA 3,56 🔴, EBITDA/Intereses 1,08 🔴, % deuda CP 70 % 🔴.

## Estructura de la plantilla (10 hojas)
PORTADA_TABLERO · PARAMETROS · A_OPERACION_VOLUMENES (patio diario, merma, 800 t/24 h) ·
B_PRODUCCION_COSTEO (inventario PT + COGS de lo vendido) · C_VENTAS (ventas reales ≠ producción) ·
D_CAJA_TESORERIA (necesidad + punto de equilibrio en caja + ciclo de conversión + proyección 3 sem) ·
E_RESULTADOS (P&L + throughput + Deuda/EBITDA + DSCR) · F_PROY_REAL (comprado/producido/vendido) ·
G_METAS_MAXIMOS (máximos por rubro, semáforos 3 %/5 %) · H_BANCABILIDAD (4 bloques del banco).

Convención: celdas amarillas = entrada; blancas = fórmula; semáforos verde/amarillo/rojo.

## Cómo regenerar (scripts en `scripts/`)
1. `build_plantilla.py` — construye la PLANTILLA UNICA CONTROL SEMANAL QVP.xlsx (openpyxl).
2. `build_docs.py` — genera el INSTRUCTIVO (funcionarios) y la GUÍA DEL PRESIDENTE (python-docx) y los exporta a PDF (Word COM).
3. `build_entregables.py` — exporta la plantilla a PDF (Excel COM), el tablero HTML a PDF (Edge headless), copia a Entregables\ y arma el PAQUETE COMITÉ.
4. El tablero gráfico es `Tableros\TABLERO_CUMPLIMIENTO_QVP.html` (autocontenido, SVG/CSS).

Requisitos: Excel + Word instalados (COM), Python con openpyxl, pypdf, pywin32, python-docx,
pymupdf. PDF de Excel/Word vía COM (no hay poppler/pandoc).

## Marco normativo (confirmado en instructivo y guía)
- **ISO 9001:2015**: 6.1/6.2 planificación; 8.1 control operacional; **9.1 seguimiento y medición**
  (KPIs/semáforos); **9.3 revisión por la dirección** (= la reunión del War Room); 10 mejora (planes
  de acción); ciclo **PHVA**.
- **ISO 20815**: aseguramiento de la producción (disponibilidad/confiabilidad, OEE, merma),
  planificación y seguimiento (conciliación compra-producción-ventas).

## Insumos del proyecto (carpeta `Analisis\`)
diagnostico-simulador-SEM24.md · esquema-plantilla-unica.md (v2) · revision-esquema-v2.md ·
integracion-informes-financieros-2025-2026.md · referencias-linkedin-flujo-caja.md (R1–R16) ·
fuente-perplexity-planificacion-produccion.md.

## Pendiente del proyecto
Objetivo 2: análisis transversal + gráficos de auditorías 2009–2025. Y, en cada uso semanal,
reemplazar las celdas amarillas con el dato real de la semana.

## Citas ancla para la guía del presidente (CPA Luis Salas)

Doctrina externa para citar textualmente al directorio cuando se justifica el régimen de margen
mínimo 3,63 % y el costo de ventas máximo semanal:

> **«Los bancos no financian historias; financian capacidad de pago.»**
> — Walter Zevallos Bustamante, LinkedIn `activity-7472136518502010880` (R21 / [[reference-ebitda-bancabilidad-walterzevallos]]).
> Caso real: +40 % crecimiento de ventas con costos subiendo más rápido, margen en reducción,
> EBITDA bajo presión y caja limitada → cuatro señales presentes simultáneamente en QVP 2024–2025.

> **«EBITDA es para comparativas; OCF es para supervivencia.»**
> — Síntesis de Jordi Altimira, LinkedIn `activity-7472573800476340224` (R25 / [[reference-tipos-flujo-caja-jordialtimira]]).
> Regla práctica derivada para la PLANTILLA ÚNICA: agregar columna **OCF mensual** además de la
> caja contable; pregunta obligatoria en cualquier negociación de financiamiento: *"¿qué
> entiende usted por flujo de caja libre?"* antes de firmar.

Ambas refuerzan la hoja **H_BANCABILIDAD** y la **GUÍA DEL PRESIDENTE**; conviene incluirlas
literalmente en la introducción del documento entregable para fijar el marco ante el comité.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
