---
name: comite-cuarto-guerra-qvp
description: |
  Procesa la reunión semanal del COMITÉ EJECUTIVO / "CUARTO DE GUERRA" de Extractora Quevepalma
  (control de toda la operación y su planificación), grabada por Fathom IA y enviada por correo
  desde <mailbox-reuniones>@<empresa-B>.com con asunto "SEM xx". Convierte la transcripción/resumen en:
  (1) ACTA estructurada, (2) TABLERO DE COMPROMISOS / action items con responsable y fecha,
  (3) lista de RIESGOS y DECISIONES, y (4) insumos para alimentar la PLANTILLA ÚNICA de control
  semanal. Sigue el ciclo operativo Ventas → Refinería → Extractora → Compra de fruta → Flujo de
  caja, y vigila los indicadores recurrentes: brecha producción-vs-ventas, margen semanal realizado
  vs. objetivo, recuperación de cartera (método "−4 días"), flujo de caja proyectado a 3 semanas,
  TEA y costo por tonelada (con transporte).
  Triggers: "acta del cuarto de guerra", "comité ejecutivo QVP", "reunión SEM", "procesar la
  reunión de Fathom", "resultados de la semana / proyección de la semana", "tablero de compromisos
  QVP", "correo reunionesqp".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-15
  origen: reunión SEM 24 (Fathom) + correo <mailbox-reuniones>@<empresa-B>.com
  relacionada: control-financiero-semanal-qvp, memoria-financiera-inteligenciada, neuro-oratoria-presentacion-persuasiva
---

# Skill `comite-cuarto-guerra-qvp`

Convierte cada comité semanal (el "cuarto de guerra") en **acta + compromisos + riesgos + insumos
para la plantilla**, de forma comparable semana a semana.

## 1. Cómo acceder a la fuente
- El comité lo graba **Fathom IA**; el correo llega a `jjmobijuesa@gmail.com` desde
  **`<mailbox-reuniones>@<empresa-B>.com`** con asunto **"SEM xx"**.
- **Leerlo por Gmail MCP** (`search_threads` → `get_thread` FULL_CONTENT). El campo `plaintextBody`
  trae el **resumen de Fathom + action items + la transcripción literal**. Si el hilo excede el
  límite, guardarlo a archivo y extraer `plaintextBody` con Python.
- ⚠️ La página `fathom.video/share/...` es una SPA: **WebFetch da error** (no renderiza). Usa el
  correo, que ya contiene todo. Búsqueda: `from:<mailbox-reuniones>@<empresa-B>.com subject:"SEM"`.
- La transcripción de Fathom intercala frases espurias en inglés ("Fathom, Reuniones QP…");
  **ignóralas**: el contenido válido es el español y el bloque "Action Items".
- **Adjuntos de trabajo** (acta previa .docx, deck .pptx, COSTEO PROY/REAL .xlsx, planificación,
  compra de fruta, inventario): el Gmail MCP da solo metadatos → **descárgalos con la skill
  [[gmail-attachments]]**, método ZIP: `download_all_zip.py jjm "...\WAR ROOM QVP\Adjuntos SEM xx"
  <thread_id>`. Léelos luego con openpyxl/python-pptx/python-docx. (SEM 24: 9 adjuntos verificados.)

## 2. Agenda oficial del comité (orden a respetar)
1. Filosofía empresarial + **OEC** (objetivo específico del comité).
2. **Resultados de la semana anterior:** compra de fruta → proceso de extracción → refinación →
   análisis throughput → ventas → flujo de efectivo real → recuperación de cartera.
3. **Proyecciones de la semana actual:** compras de fruta → simulador throughput → flujo proyectado
   a 3 semanas → plan de ventas → plan de producción de refinería (conciliado con ventas) → plan de
   extractora (conciliado con refinería y compra de fruta) → presupuesto de costos y gastos.
4. Firmas del acta de la semana anterior.
5. Evaluación de planes de acción/proyectos previos → definición de los nuevos.

## 3. Mejora del proceso (acordado en SEM 24)
La reunión era ineficiente, desestructurada y sin liderazgo claro. Acciones:
- **Centralizar** en UNA sola plantilla/deck consolidado (es la PLANTILLA ÚNICA de
  `control-financiero-semanal-qvp`; el deck con `neuro-oratoria-presentacion-persuasiva`).
- **Agenda estricta** por el ciclo operativo: Ventas → Refinería → Extractora → Compra de fruta →
  Flujo de caja (planificar, no solo reportar el pasado).
- **Exigir rendición de cuentas:** datos preparados antes de la reunión; el líder dirige.

## 4. Indicadores recurrentes a extraer cada semana
| Indicador | Qué vigilar |
|---|---|
| Brecha producción-vs-ventas | capacidad (~$2,0M) − plan de ventas; cerrar la brecha |
| Margen semanal realizado | % real vs. objetivo y vs. equilibrio 3,6 % |
| Recuperación de cartera | método **"−4 días"** (visibilidad de lo por vencer), no "lunes a lunes" |
| Flujo de caja a 3 semanas | alertas de pagos grandes (p. ej. crédito de importación) |
| TEA (tasa de extracción) | tendencia por planta (Quevedo / Río Coca) |
| Costo por tonelada | con asignación correcta de **transporte** |
| Giro de producto | exportar CPO vs. refinar para local (lo que deje más margen) |

## 5. Salida (entregables que produce)
- **Acta SEM xx** (markdown/PDF): filosofía/OEC, resultados, proyecciones, decisiones, riesgos.
- **Tablero de compromisos:** acción · responsable · fecha · estado (abierto/cerrado), comparable
  semana a semana (carry-over de lo no cerrado).
- **Insumos a la plantilla:** valores reales de fruta/TEA/ventas/cartera/caja para `PARAMETROS`.
- Guardar en `WAR ROOM QVP\Actas\ACTA SEM xx - Cuarto de Guerra QVP.*`.

## 6. Relación con otras skills
- `control-financiero-semanal-qvp` → la plantilla que el comité acordó centralizar; recibe los
  insumos reales y proyectados.
- `memoria-financiera-inteligenciada` → análisis crítico (margen, deuda, apalancamiento i>RE).
- `neuro-oratoria-presentacion-persuasiva` → deck consolidado y agenda para que la reunión sea
  efectiva.
- `wolfram-forensic-engine` → recálculo/validación de cifras dudosas (p. ej. promedios de precio).

## Caso de referencia
**SEM 24 (15-jun-2026):** ver `WAR ROOM QVP\Actas\ACTA SEM 24 - Cuarto de Guerra QVP.*`.
Riesgos top: crisis de caja (crédito importación ~$900k vence SEM 27), trazabilidad de exportación
(Cargill), brecha de ventas ~$200k SEM 25.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
