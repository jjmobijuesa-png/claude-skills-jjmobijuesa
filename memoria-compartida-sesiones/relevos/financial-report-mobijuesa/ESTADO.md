# RELEVO — Financial report for Mobijuesa

| Campo | Valor |
|---|---|
| **TURNO** | PC |
| Principal | Sesión local "Financial report for Mobijuesa" (PC) |
| Espejo | Sesión nube "Espejo — Financial report for Mobijuesa" [8a8198] |
| Último checkpoint | 2026-09-26 — modelo San Sebastián actualizado (flujo estresado, MEMORIA §23/§24, PPTX robusto, PDFs A4) |
| Motivo del último relevo | La PC retomó la posta y volcó el estado del modelo San Sebastián para que la nube pueda continuar si la PC se queda sin saldo |

## 🚦 Regla de datos de este canal — leer antes de escribir aquí
`archivos/` transporta **resúmenes y punteros en Markdown, nunca el documento fuente**
(`.gitignore` bloquea todo lo que no sea `.md`). El hook publica esta carpeta en `main`.
**No salen de la PC:** cédulas, nombres de personas naturales, escrituras, cifras de deuda,
DSCR, cierres mensuales ni modelos financieros con datos reales. Rige `gobernanza-datos-financieros-ia`.
Para pasar un documento: **ruta local/Drive + resumen de lo concluido** (ver `archivos/san-sebastian-modelo.md`).

## Tema / objetivo del hilo
Modelo financiero y entregables de la **Urbanización San Sebastián** (Mobijuesa S.A., Quevedo): libro Excel vivo
(presupuesto, PyG, flujo, balance, tabla de amortización BDE, normativa MIT, memoria de cálculo), deck ejecutivo
para el CEO, PDFs y documentos comerciales.

## Razonamiento en curso / estado
- **Libro vivo actualizado** con: crédito BDE [cifra en local] (palanca P60) a tasa [cifra en local] (P65) — independientes;
  devolución de IVA no gravable; bono de capital 14 SBU (solo VIS 2.º, 90 deptos); **flujo estresado**
  (cobranza 90 días después de terminar cada unidad; saldo mensual nunca negativo, mín +[cifra en local]);
  MEMORIA §23 (criterio matemático-legal del IVA) y §24 (guía para no financieros).
- **Deck CEO (28 láminas)** con gráficos como imágenes (abre y proyecta sin cerrarse); PDFs A4 regenerados.
- Detalle y cifras: en el libro de Drive y en la memoria local (ver `archivos/san-sebastian-modelo.md`).

## Archivos centrales
- `archivos/san-sebastian-modelo.md` — **principal** (puntero al libro/deck/PDF en Drive + estado + metodología).
- `archivos/marco-informe-financiero.md` — marco del informe (del espejo, sin cifras).

## Siguiente paso concreto
- **Único pendiente de fondo:** afinar `C5` (fracción de obra gravada con IVA) con la **APU detallada de la
  vivienda** del constructor. Cuando llegue: la PC la ingresa en PyG!C5, recalcula y recascadea deck + PDFs.
- Si la PC se detiene (fin de cupo/5 h/crédito) y el usuario escribe en el chat espejo: la nube
  **sincroniza, asume el TURNO, y continúa** con lo que SÍ puede hacer sin la PC (ver reparto abajo),
  dejando el resultado y el nuevo «siguiente paso» en este relevo. Cuando la PC vuelva, ejecuta lo COM.

## Reparto PC ⇄ nube
- **PC (Windows + Office):** todo lo que edite el `.xlsx`/`.pptx` por COM (preserva imágenes/formato/fórmulas vivas).
- **Nube (espejo):** razona, planifica, redacta informes/textos, verifica normativa con fuentes, actualiza este
  relevo. NO edita el libro por COM. Deja el trabajo listo para que la PC lo aplique.

## Políticas de seguridad y confiabilidad (obligatorias para ambos)
1. **Datos sensibles solo en Google Drive** (cuenta mobijuesa360). Nunca subir el `.xlsx`/`.pptx` ni volcar
   cifras reales, cédulas o datos de personas al repo. Solo `.md` de coordinación.
2. **Nada se envía, publica ni firma** hacia afuera (WhatsApp/email/portales): solo borradores. Automatización
   solo por Edge cuando aplique. Decisiones legales (aval, fideicomiso) se **modelan**, no se comprometen.
3. **Un solo agente trabaja a la vez** (TURNO). No editar el mismo archivo desde dos lados.
4. **Integridad del modelo vivo:** respaldo antes de editar; tras cada cambio, controles = 0 y prueba de palanca;
   nunca guardar un estado con saldo negativo o controles ≠ 0.
5. **Cero alucinación:** cifra normativa se verifica con ≥2 fuentes y se marca 🚦 lo no confirmado.
6. **Voz:** Francisco Duque, usted, cortés-formal; nunca `≈` ni `~`.
7. **Trazabilidad:** cada avance deja checkpoint en este relevo (commit + push a `main`).

## Pendientes / preguntas abiertas
- Confirmar la APU detallada de la vivienda (gobierna C5 y la magnitud de la devolución de IVA).
- Relacionado: hilo `flujo-caja-proyeccion-mobijuesa` (misma empresa; no mezclar razonamiento).
