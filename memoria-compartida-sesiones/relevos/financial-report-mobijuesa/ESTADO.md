# RELEVO — Financial report for Mobijuesa

| Campo | Valor |
|---|---|
| **TURNO** | PC |
| Principal | Sesión local "Financial report for Mobijuesa" (PC) |
| Espejo | Sesión nube "Espejo — Financial report for Mobijuesa" [8a8198] |
| Último checkpoint | 2026-10-27 (v6) — FLUJO GENERAL con motor de financiamiento: desembolso banco 90d, construcción ajustada a venta 2 años, CAPITAL PROPIO FRESCO $0 (reinversión de utilidad) + APALANCAMIENTO mínimo (pico $1.545.226 feb-27, cancelado ago-27, interés $73k), caja nunca en rojo. Neta proyecto $2.746.700. Palancas: tope aporte $0, tasa apal = BDE 6,55% (verificada en Fondos BDE: financia hasta 80% costos directos, gracia en construcción). Apal máx $1.535.068 feb-27, cancelado ago-27, interés $47.204. Hilo WA ejecutivo entregado. Verif. Python |
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

## ⭐⭐ v7 (27-10-2026) — RUTA CANÓNICA NUEVA + actualización mayor
**Todos los entregables viven ahora en** `G:\Mi unidad\3 Urbanización San Sebastian\02 Financiero\Presupuesto Definitivo v1`
(libro Excel + 2 PDF A4 de una hoja). Fuentes de esa carpeta. Generador: `scratchpad\build_sistema_cerrado.py` (v7).
Cambios v7:
- **Fechas:** primer desembolso (anticipo NES $200k) **1-nov-2026**; inicio de obra **1-dic-2026**; entrega 1.ª etapa 29-may-2027 (pág. 2 de la Presentación Ejecutiva).
- **Áreas REALES por unidad** (RESUMEN GENERAL ULTIMO 27-10, Hoja2): T1 (18 dep)=6/planta 64,68/64,68/61,33/43,14/43,14/61,33; T2 (12 dep)=4×60/planta; 3 plantas. PVP sobre área privada; costo sobre área bruta (ancla). DEPARTAMENTOS ahora tiene piso+condominio+dormitorios por unidad.
- **Fiscalización de obra** $1.200/mes × 24 = $28.800 (rubro separado; se quitó "fiscaliz" de indirectos).
- **Marketing:** meses 1-2 $1.355; desde mes 3 ADS $500 + activaciones $600.
- **Flujo estacional equilibrado:** base estable bancable 60% + estacionalidad Quevedo 40%; **80% compradores bancables precalificados cobran a ~45 días, resto a 90 días** → **pico de crédito $1.590.916 (cancelado dic-27), interés $74.613**, caja nunca en rojo. (Palancas editables en PARAMETROS.)
- **Hojas nuevas:** CONTRATO (resumen de blindaje NES, llave en mano, garantías a primer requerimiento — SIN fideicomiso por decisión) y PROCESO MIT (compra-venta; paso ★ de score crediticio apenas hay interés real y CON autorización expresa del cliente, antes de la reserva).
- **Resultado v7 (verif. Python):** Ventas **$13.763.090**; Costos $10.513.238; Utilidad neta **$2.437.389 (17,71%)**; Retorno total (neta + $2,3M recuperado) **$4.737.389** (+IVA $683.360 → $5.420.750). 1.ª etapa: ventas $619.240, costos $1.217.218, capital de arranque **$597.978** (respaldado por 9 retenidos $485.910 + devIVA $56.584 + bono $60.732).
🚦 Pendiente: anclar los % de segmentos (base estable / bancable) con el doc `Presentacion Marketing y Ventas San Sebastian (16-10-2026)` (lectura quedó interrumpida). Hilos WA aún sin rehacer con cifras v7.

## RETORNO REAL — "utilidad escondida" (registrado 27-10-2026, idea de Ing. Gallegos-Anda)
Los $2.300.000 ya invertidos (terreno $600.000 + urbanización inicial $1.700.000) figuran como costo
hundido, pero el modelo los **recupera dentro del PVP**: son capital que vuelve, no desembolso futuro.
Por eso el retorno real no es solo la utilidad neta:
- Utilidad neta (tras IR 25%): **$2.746.700** (19,42% s/ventas $14.144.499; verif. Python).
- (+) Terreno + urbanización recuperados: **$2.300.000**.
- = **RETORNO TOTAL DEL PROPIETARIO: $5.046.700** ("2,3 + 2,75 = 5,05 M").
- (+) Devolución IVA construcción recuperable $681.345 → retorno $5.728.045.
Entregado: **PDF A4 de una hoja** `02 Financiero\Resumen Ejecutivo A4 - Presupuesto General San Sebastián.pdf`
(HTML→Edge headless, generador `scratchpad\resumen_a4_ss.html`). Hilo WA ejecutivo rehecho con esta lectura.

**Arranque de obra tentativo: diciembre de 2026** (Condominio 1; anticipo NES nov-26, obra física dic-26 → entrega may-27).
Añadido al PDF general. **2.º PDF A4 — PRIMERA ETAPA** `02 Financiero\Resumen Ejecutivo A4 - Primera Etapa San Sebastián.pdf`
(generador `scratchpad\resumen_a4_etapa1.html`). Cifras 1.ª etapa (verif. Python): ventas $639.360, costos $1.199.164,
**capital de arranque $559.804**, que vuelve como activo de renta (9 deptos retenidos $549.110) + devolución IVA $56.584 +
bono Yapa $60.732. Contrato de obra NES = $796.594 (edificación $628.710 + área social $167.884); caja de obra mínima $941 (mar-27).

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
