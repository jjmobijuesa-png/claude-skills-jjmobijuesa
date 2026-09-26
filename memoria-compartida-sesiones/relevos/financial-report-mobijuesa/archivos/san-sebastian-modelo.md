# San Sebastián — modelo financiero vivo y entregables (puntero + estado)

> **Regla de datos:** este `.md` es un PUNTERO + RESUMEN. El libro y los entregables con
> cifras reales viven en Google Drive (acceso por la cuenta mobijuesa360). NO se suben al
> repo (`.gitignore` bloquea todo lo que no sea `.md`). Rige `gobernanza-datos-financieros-ia`.

## Dónde vive todo (Google Drive — misma cuenta)
- **Libro vivo (fuente única):** `G:\Mi unidad\Urbanización San Sebastian\02 Financiero\San_Sebastian_Presupuesto_31Ago2026_Analisis_por_Rubro 12092026.xlsx` (28→ actualmente ~24 hojas de trabajo; sistema de fórmulas vivo).
- **Deck CEO:** `…\02 Financiero\Presentacion Ejecutiva San Sebastian - CEO Omar Juez (25-09-2026).pptx` (28 láminas).
- **PDFs A4:** `Presupuesto San Sebastian 13-09-2026 (A4).pdf`, `Resumen por Rubros San Sebastian (A4).pdf` (02 Financiero).
- **Docs:** Manual de vivienda + Estrategia de mezcla social (05 Comercial y Marketing).
- **Respaldos** de cada paso: `02 Financiero\_Versiones anteriores (MUPI 2023)`.
- Memoria detallada (local, NO en repo): `~/.claude/projects/C--Users-datos-Downloads/memory/project_financiero_san_sebastian.md`.

## Estado del modelo (metodología, no volcado de cifras)
- **Palancas independientes** (una celda por concepto, todo lo demás cuelga por fórmula):
  monto del crédito BDE = `PRESUPUESTO 13-09-2026!P60`; tasa = `P65`. Comprobado independientes.
- **Flujo de caja estresado (26-sep):** cobranza = escritura + bono **90 días después de terminada cada unidad**
  (viviendas construidas meses 1-24 → cobran 4-27; departamentos 25-36 → cobran 28-36). Desembolso BDE
  recalendarizado al ritmo de obra (~24 meses). **Saldo mensual nunca negativo** (control B53 ≥ 0).
  Fracciones: FLUJO filas 63/64 (viviendas), 65/66 (deptos/parqueos), 71 (desembolso).
- **Devolución de IVA** no gravable: PyG C14 = IVA(15%) × %obra gravada (C5) × %recuperable (C7) × (1−fee E7) ×
  base_obra / (1+IVA). Excluida de participación e IR (ajuste B34). Criterio legal/matemático: MEMORIA §23.
- **Guía para no financieros:** MEMORIA §24 (cada cálculo con su fórmula, lenguaje sencillo).
- **Controles del sistema = 0**: PRESUPUESTO G13, FLUJO B57/B58, BALANCE C18, tabla de amortización.
- **Comentarios de celda ocultos** (solo al seleccionar).
- **PPTX robusto:** los 2 gráficos de la lámina de estadística son IMÁGENES (no gráficos nativos con Excel
  embebido) — eso resolvió el cierre de PowerPoint al abrir/proyectar. Charts nativos = 0.

## 🚦 Pendiente único de afinar
- `C5` (fracción de obra gravada con IVA, hoy 0,65) con la **APU detallada de la vivienda** del constructor
  (materiales / mano de obra / equipo por m²). Cuando llegue, recalcular y recascadear a deck/PDFs.

## Reparto de trabajo PC ⇄ nube (IMPORTANTE)
- **La edición del `.xlsx`/`.pptx` se hace en la PC** (requiere Windows + Excel/PowerPoint por COM, que preserva
  imágenes y formato). **La nube NO puede editar el libro por COM.**
- **La nube (espejo) mantiene viva la posta:** razona, planifica, redacta texto/informes, actualiza este relevo,
  y deja el «siguiente paso» claro. Cuando la PC regresa, ejecuta los cambios COM.
