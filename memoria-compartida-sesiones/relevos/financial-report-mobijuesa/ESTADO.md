# RELEVO — Financial report for Mobijuesa

| Campo | Valor |
|---|---|
| **TURNO** | PC |
| Principal | Sesión local "Financial report for Mobijuesa" (PC) |
| Espejo | Sesión nube "Espejo — Financial report for Mobijuesa" [8a8198] |
| Último checkpoint | 2026-10-26 — NUEVO libro «PRESUPUESTO GENERAL REVISADO» como sistema cerrado (10 hojas, 195 unidades, SIN BDE); verificado Python+Wolfram |
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
para el CEO Ing. Omar Juez Zambrano, PDFs y documentos comerciales.

## Razonamiento en curso / estado
- **NUEVO libro «PRESUPUESTO GENERAL REVISADO - Proyecto San Sebastián.xlsx»** (en `02 Financiero`),
  construido como **sistema cerrado de fórmulas** (script `build_sistema_cerrado.py`). 10 hojas:
  PARAMETROS (22 palancas), DEPARTAMENTOS (108 líneas/unidad), VIVIENDAS (87), PRE-OPERATIVOS, RUBROS
  (composición+trazabilidad), PyG, BALANCE GENERAL (control=0), PRIMERA ETAPA, RESUMEN EJECUTIVO, CURVA S.
- **Mezcla NUEVA 195 u** (108 dep en 7 condominios + 76 casas 95 + 11 casas 112); ubicaciones de condominios
  validadas por Francisco (ver skill `lectura-planos-lotes-superpuestos`).
- **Decisiones de Francisco 26-10:** SIN BDE (100% capital propio, costo financiero $0); terreno $600.000;
  indirectos 9,75%; eléctrica extrapolada por unidades (34.681,35÷19×195, 🚦 estimada); área social e
  infraestructura **al 100% sobre la 1.ª etapa, SIN prorratear** (confirmado).
- **Resultado (Python=Wolfram):** proyecto ventas $14.693.608, costos $10.474.744, utilidad neta $2.689.526
  (18,30%), ROE 20,43%. Primera etapa: ventas $1.188.470, costos $1.097.568, neta $57.950 (4,88%),
  caja mínima $940,67 (mar-27). Construcción $7.642.635 = RESUMEN GENERAL.
- Herramienta Wolfram (MCP) disponible para verificación/sensibilidad. (El libro BDE anterior queda como histórico.)

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
