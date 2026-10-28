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

## ⭐ NOMENCLATURA DE VERSIÓN (regla permanente, 28-10-2026)
Todo entregable lleva en el nombre `… vN (AAAA-MM-DD).<ext>`. **Cada actualización sube N y refresca la fecha** (v1→v2…),
para no confundir con versiones ya enviadas. Entregables vivos = **v1 (2026-10-28)** en `00 ENTREGABLES`:
`PRESUPUESTO GENERAL REVISADO - Proyecto San Sebastián v1 (2026-10-28).xlsx`, `Resumen Ejecutivo A4 - Presupuesto General San Sebastián v1 (2026-10-28).pdf`,
`Resumen Ejecutivo A4 - Primera Etapa San Sebastián v1 (2026-10-28).pdf`, `Lista de Precios por Unidad - San Sebastián v1 (2026-10-28).pdf`,
`Presentacion Marketing y Ventas San Sebastian (16-10-2026) v1 (2026-10-28).pptx`. El generador (OUT) y los renders deben escribir con el `vN (fecha)` vigente.
El PDF viejo del deck en `05 Comercial y Marketing` fue eliminado (carpeta sin entregables de este tema).

## ⭐⭐⭐ DESTINO ÚNICO DE ENTREGABLES (confirmado 28-10-2026)
**TODO entregable de este tema va a** `G:\Mi unidad\3 Urbanización San Sebastian\02 Financiero\Presupuesto Definitivo v1`.
Contenido actual: libro Excel (18 hojas), Resumen Ejecutivo A4 General (con Tablero de decisión), Resumen Ejecutivo A4 Primera Etapa,
Lista de Precios por Unidad (PDF), y el deck `Presentacion Marketing y Ventas (16-10-2026).pptx` (19 láminas: precios en 7, decisión al cierre).
Se eliminaron las copias v6 sueltas de la carpeta padre `02 Financiero`. El deck también vive (espejo de trabajo) en `05 Comercial y Marketing`
con su respaldo `- respaldo pre-cuadro.pptx`.
**Estructura de v1 (organizada 28-10-2026):** `00 ENTREGABLES` (Excel, 2 PDF A4, Lista de Precios, deck .pptx) · `01 Fuentes - Presentaciones y cronograma`
· `02 Fuentes - Áreas y planos` · `03 Fuentes - Costos y comercial` · `04 Fuentes - Legal y MIT` · `05 Versiones anteriores`.
**El generador escribe el Excel en `00 ENTREGABLES`** (OUT actualizado); los renders de PDF deben apuntar a esa subcarpeta.
**Deck (28-10): 20 diapositivas** — lista de precios (7), **especificaciones técnicas / acabados de entrega (8, fuente NES Arq. Ávila)**, tablero de decisión (cierre, 20). Vive SOLO en `00 ENTREGABLES`; se eliminaron la copia espejo y el respaldo de `05 Comercial y Marketing` (allí queda únicamente el PDF viejo 16-10, desactualizado). ⚠ Ojo con candados `~$...pptx` huérfanos de PowerPoint: bloquean el guardado aunque el archivo esté cerrado; borrarlos y reintentar.

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
- **v7.1 — PVP sobre ÁREA VENDIBLE estandarizada (decisión de Francisco):** se cotiza sobre área vendible por tipo (18 dep → 61,01; 12 dep → 63,09; $1.000/m²) para que cada unidad quede bajo el tope del bono (135 SBU = $65.070) y el retorno vuelva al nivel anterior (~$5 M). El área privada real por unidad (43-65 m²) se muestra como distribución interior. **Resultado (verif. Wolfram = Python):** Ventas **$14.144.500**; Costos $10.526.397; Utilidad neta **$2.713.577 (19,18%)**; Retorno total (neta + $2,3M) **$5.013.577** (+IVA $684.216 → $5.697.793). Apalancamiento pico **$1.553.292 (nov-27)**, interés $70.185, caja nunca en rojo. 1.ª etapa: ventas $639.360, costos $1.217.912, capital de arranque **$578.552** (respaldado por 9 retenidos $549.110 + devIVA $56.584 + bono $60.732).
- **Guía MIT:** área basis (61/63, casa 95/112, tope $65.070) YA consistente con el modelo → no requiere cambio (su cuadro cuenta 108 deptos y $14.693.610; el modelo retiene 9 → $14.144.500). **Deck 16-oct:** sus números son correctos (61/63 preserva el bono); no se edita el .pptx. Se creó el **documento aparte** que la Guía MIT menciona: `Cuadro de Áreas por Unidad - San Sebastián.pdf` (áreas reales por unidad). Hilos WA v7.1 rehechos.
**Segmentos anclados (deck «Presentacion Marketing y Ventas» 16-10):** deptos → parejas jóvenes IESS (BIESS CrediCasa 2,99%) + inversionistas de renta; casas 95/112 → nómina agroindustrial + profesionales (Miti-Miti 4,99%); comerciantes/independientes = cola a 90 días. Confirma el perfil mayoritariamente bancable → se mantienen 80% bancable / 60% base. **Verificado con Wolfram = Python (exacto); CONSTR $7.642.635,55 = ancla RESUMEN GENERAL.** Hilos WA v7 rehechos (general + 1.ª etapa).
✔ **v7.3 — HOJA «INDICADORES Y DECISIÓN» + Tablero de decisión del CEO (28-10-2026).** Umbrales fijados y confirmados por Francisco: **margen ≥15%, TIR anual ≥25%, VAN@15% >0, payback ≤24 m** (caja ≥0 y apalancamiento ≤80% costos directos como guardas). Resultados (verif. Wolfram=Python): **margen 19,18% · TIR anual 50,2% · VAN@15% $1.309.962 (@12% $1.471.691) · payback 19 m · ROI 25,8% · inversión máx en riesgo $3,22M**. Veredicto: **SÍ — PROCEDER** (4/4). Sensibilidad: ventas −10% → margen 13,27%; costos +10% → 13,60% (ambos bajo el piso; control de costos = variable crítica). La hoja trae el flujo del proyecto (25 meses, t0=−urbanización $1,7M, terminal=9 deptos retenidos) y TIR/VAN por fórmula viva (=IRR/=NPV); veredicto por fórmula. Añadido «Tablero de decisión del CEO» al PDF A4 general Y como **lámina de cierre del deck** (`05 Comercial y Marketing`, deck ahora 19 láminas: lista de precios en pos. 7, tablero de decisión como cierre). Nota: libro 18 hojas; abrir en Excel recalcula IRR/NPV.

✔ DECISIÓN CERRADA: PVP sobre área vendible. **v7.2 — LISTA DE PRECIOS POR UNIDAD (Opción A, confirmada por Francisco):** la hoja DEPARTAMENTOS es ahora la lista de precios del vendedor; cada unidad lleva su precio con alícuota + tope del bono DENTRO del precio: **1 dorm. $52.897 (entrada), 2 y 3 dorm. $65.070 (tope bono), tipo 2 $63.093**. Todas ≤ 65,07 m² vendibles → conservan el bono. Reparto balanceado venta/renta en C1 (6 grandes + 3 de 1 dorm. cada lado) → **totales idénticos** (Wolfram = Python): Ventas $14.144.525, Neta $2.713.595 (19,18%), Retorno $5.013.595, apalancamiento pico $1.553.290 (nov-27). Entregables en `Presupuesto Definitivo v1`: libro Excel (17 hojas), 2 PDF A4 (sin cambio) y **Lista de Precios por Unidad - San Sebastián.pdf**. Deck (`05 Comercial y Marketing`): lámina de lista de precios insertada en posición 7 (respaldo del original guardado). Los PDF A4 generales y los hilos WA no cambian (cifras globales iguales).

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
