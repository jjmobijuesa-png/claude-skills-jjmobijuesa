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
- **PPTX — cierre al proyectar RESUELTO (26-sep):** el disparador NO era el archivo sino el ENTORNO de la máquina.
  WER: `POWERPNT.EXE` caía en `mso20win32client.dll` (offset `0x00304902`), intermitente. Arreglo (reversible):
  (1) vaciada la cola OTele de PowerPoint; (2) `DisableHardwareAcceleration=1` en `HKCU\...\Office\16.0\Common\Graphics`.
  Verificado: 5 aperturas + 2 proyecciones de 28 láminas = 0 caídas. Detalle en la memoria local
  `project_diagnostico_explorador_windows.md` (§2026-09-26). Respaldo garantizado: PDF de 28 láminas en `02 Financiero`.
  (Los 2 gráficos de estadística ya eran imágenes; charts nativos = 0 — eso no era el problema.)
- **PPTX rebuild 26-sep (tarde):** (a) las 3 **fachadas** reemplazadas por las nuevas con **adoquinado de colores en el portal**
  (fuente `05 Comercial y Marketing\Modelos de Viv y Dep\FACHADA *`, actualizadas 21:5x); (b) **lámina 27** corregida:
  «Instalaciones sanitarias con tubería de PVC empotrada; agua fría y caliente en duchas y lavamanos (salvo baño de visitas),
  llaves monocomando» — **sin marca comercial** (el usuario pidió no citar FV/EDESA); (c) en `build_pptx_v3.py` el `rect()` ahora
  **elimina el nodo `<p:style>`** en vez de `shadow.inherit=False` → **0 `<a:effectLst/>` vacíos** en todo el deck (se retiró el
  sospechoso de caída que quedaba). Tres entregables en `02 Financiero`: editable (1,95 MB), **«CEO (robusta, imagenes).pptx»**
  (solo-imágenes, a prueba de caídas por contenido) y PDF (1,42 MB). 🚦 La caída al proyectar en la lámina 2 NO se reprodujo por
  COM en 4 vías; queda por confirmar con el usuario si la versión solo-imágenes también cae (→ sería controlador de video, no el archivo).

## Ajustes por las observaciones al informe (28-sep-2026)
Revisión externa «Observaciones a las presentaciones» — solo San Sebastián. El revisor no halló errores de
cálculo de fondo; sí de terminología, denominador y prudencia tributaria. Aplicado al libro y a los entregables:
- **«Utilidad bruta» → «Resultado antes de particip. e IR»** (los $1.055.336 llevan ya todos los costos + financiero).
  La utilidad bruta contable REAL es `PyG!C24` = **$3.412.866 (24%)**, ahora surfaciada en el deck.
- **Márgenes sobre VENTAS ($13,54 M)**, no sobre ventas+IVA: neto **10,1%** (con IVA) y **4,97%** (sin IVA). El 9,6%
  anterior salía de dividir entre $14,23 M.
- **EBITDA retirado del deck** (se armaba sobre ingresos+IVA; no se reconstruía de lo visible). Queda en el libro.
- **Escenarios de IVA A/B/C** en `ESTADÍSTICA A54:D58` y en la lámina 7: A pleno neta $1,37 M (10,1%) · B sin IVA
  $0,67 M (5,0%) · C 50% $1,02 M (7,5%). El proyecto es rentable aun sin la devolución.
- **MEMORIA §25** documenta cada cambio y su motivo. Controles = 0 tras editar. Respaldo del libro en `_Versiones anteriores`.

## 🚦 Pendiente único de afinar
- `C5` (fracción de obra gravada con IVA, hoy 0,65) con la **APU detallada de la vivienda** del constructor
  (materiales / mano de obra / equipo por m²). Cuando llegue, recalcular y recascadear a deck/PDFs.

## Reparto de trabajo PC ⇄ nube (IMPORTANTE)
- **La edición del `.xlsx`/`.pptx` se hace en la PC** (requiere Windows + Excel/PowerPoint por COM, que preserva
  imágenes y formato). **La nube NO puede editar el libro por COM.**
- **La nube (espejo) mantiene viva la posta:** razona, planifica, redacta texto/informes, actualiza este relevo,
  y deja el «siguiente paso» claro. Cuando la PC regresa, ejecuta los cambios COM.
