---
name: memoria-financiera-inteligenciada
description: |
  Analista financiero estratégico, transversal y crítico. Convierte los estados financieros
  (un año o una serie de auditorías de varios años) en una MEMORIA FINANCIERA que sirve de
  brújula para la estrategia, no en un informe que se archiva. Agrupa y aplica el marco destilado
  de 16 referencias de expertos (LinkedIn) sobre lectura de estados financieros, flujo de caja,
  EBITDA, ratios, bancabilidad, apalancamiento financiero bien calculado y control de gestión, más
  un método propio para reconstruir series históricas desde informes de auditoría (xls, PDF digital
  y PDF escaneado por OCR de visión), graficarlas e identificar dónde se comprime el margen, se
  quiebra la deuda o el apalancamiento se vuelve negativo (costo de deuda > rentabilidad económica).
  Doctrina central: «utilidad = rentabilidad; caja = supervivencia». Combate tres sesgos: creer
  que se vendió todo, confundir caja con utilidad, y ganancia sin saber el costo de lo vendido.
  Triggers: "análisis financiero transversal", "memoria financiera", "analiza los estados
  financieros", "leer flujo de caja", "bancabilidad", "serie histórica de auditorías", "margen y
  deuda en el tiempo", "diagnóstico financiero estratégico", "análisis crítico de EEFF",
  "12 KPIs del CEO", "indicadores predictivos", "KPIs prospectivos", "tablero de alerta temprana".
user-invocable: true
metadata:
  version: 1.5
  fecha: 2026-06-19
  origen: 16 referencias LinkedIn (flujo de caja/EBITDA/ratios/bancabilidad) + R17 proyección (Gajardo) + R18 apalancamiento (López Martín) + R19 panel 12 KPIs predictivos del CEO (Saucedo Vaca) + R20 CapEx/OpEx (UpGrade Plus CFO) + R21 bancabilidad por EBITDA (Zevallos Bustamante) + R25 tipos de flujo de caja OCF/FCFE/FCFF (Altimira) + R27 retiros del socio (Gavilánez) + R28 ratios como preguntas de gestión (Da Costa) + R29 EBITDA radiografía (Zevallos) + método transversal QVP
  relacionada: control-financiero-semanal-qvp, politica-retiros-socio-propietario
---

# Skill `memoria-financiera-inteligenciada`

## Propósito
Leer estados financieros como un **sistema de creación de valor** y como **prueba de
supervivencia de caja**, en perspectiva **transversal** (varios años) y con **espíritu crítico**
(buscar el punto donde algo se rompe). El producto no es un informe: es una **memoria financiera**
que define el mínimo a sostener, el control que lo vigila y la dirección de la estrategia.

## I. Marco de lectura (destilado de 16 referencias de expertos)
1. **Leer los 3 estados como sistema conectado** (no línea por línea): Balance (qué tienes vs. qué
   debes) · Resultados (Revenue → Margen bruto → OPEX → EBITDA/EBIT → Neto) · Flujo de Caja
   (operativo/inversión/financiamiento). La utilidad neta pasa al flujo; el efectivo final, al activo.
2. **Caja > utilidad. EBITDA ≠ caja.** Una empresa puede "ganar" y quedarse sin caja. Vigilar
   cuentas por cobrar, rotación de inventario, capital de trabajo y el **ciclo de conversión de
   efectivo** (días inv. + días cartera − días proveedores).
3. **Red flags del estado de resultados:** ingresos creciendo con margen en caída; costos creciendo
   más rápido que ventas; ingresos no recurrentes; beneficios inflados por eventos únicos.
4. **Panel de 12 KPIs del CEO** (detalle predictivo y preguntas críticas en §V-quinquies): margen
   bruto/operativo, crecimiento, ROIC, ciclo de conversión de efectivo, capital de trabajo/ingresos,
   FCO/ventas, margen de FCF, liquidez corriente, **Deuda/EBITDA**, **DSCR**, EBITDA/FCO.
5. **Bancabilidad (la matriz del banco), 4 bloques:** Liquidez (corriente, ácida, capital trabajo) ·
   Apalancamiento (Deuda/Patrimonio, Deuda/EBITDA ≤3,5) · Cobertura (EBITDA/Intereses ≥2, FCO/deuda) ·
   Estructura de deuda (% corto plazo, concentración de vencimientos). *Corregir lo rojo antes de
   pedir crédito.*
6. **Control de gestión:** los ratios son **señales para decidir**; analizar tendencia, integrar en
   proyección de escenarios, automatizar alertas.

Detalle y fuentes: `WAR ROOM QVP\Analisis\referencias-linkedin-flujo-caja.md` (R1–R16 + R18 apalancamiento).

## II. Método transversal (serie histórica de auditorías)
1. **Inventariar** los informes por año; cada auditoría trae el año + el comparativo anterior
   (los informes pares cubren 2 años → mitad de OCR).
2. **Extraer el Estado de Resultados** por fuente:
   - `.xls` internos → **Excel COM** (openpyxl no lee .xls).
   - PDF **digital** → **PyMuPDF** (`fitz.get_text`); P&L suele estar en pág. ~7–8.
   - PDF **escaneado** (texto = 0) → **OCR de visión**: `fitz` renderiza la página a PNG (≥150 dpi)
     y se lee con visión. Localizar la pág. del "ESTADO DE RESULTADOS" (cuidado: a veces la pág. 7
     es el de Cambios en Patrimonio y el de Resultados es la 6).
3. **Validar por solapamiento**: el comparativo de un informe debe coincidir con el año del informe
   siguiente.
4. **Series + gráficos** (matplotlib): ventas, margen bruto %, utilidad/pérdida neta, gastos
   financieros. Marcar el equilibrio y anotar quiebres.
5. **Buscar críticamente**: ¿cuándo se comprimió el margen? ¿cuándo se disparó la deuda? ¿desde
   cuándo la utilidad es marginal?

## III. Doctrina de la memoria financiera
- El análisis **renueva la estrategia** (no se archiva): define el **mínimo financiero para no
  perder** y la **dirección del crecimiento** (hacia el margen, no el volumen).
- **Transversal**: la verdad aparece en la serie, no en el año aislado.
- **Crítico**: nombrar el punto exacto de ruptura y monetizar su costo.

## IV. Caso aplicado (Quevepalma) — qué reveló
- Margen estructuralmente fino 17 años (~5 %), colapso a 2,2 % y pérdida en 2025; segunda pérdida
  histórica (2017 −65k). **Quiebre de deuda en 2019** (gastos financieros 0,1–0,5 M → 1,2–2,0 M)
  que subió el umbral de supervivencia. Refinados 1,66 % vs. valor agregado ~11 % → tesis
  "valor agregado sobre commodity" (Estrategia 2.0).
- Artefactos: `Analisis\analisis-transversal-2009-2025.md`, `Tableros\SERIE HISTORICA 2009-2025 QVP.xlsx`,
  `Tableros\GRAFICOS TRANSVERSAL 2009-2025 QVP.png`, `Plan de Negocios 2-0\ESQUEMA ESTRATEGICO QUEVEPALMA 2.0.md`.

## V. Entregables típicos
Serie histórica (xlsx) + gráficos (PNG) + narrativa crítica (md) + panel de KPIs/bancabilidad +
síntesis estratégica que conecta el diagnóstico con las decisiones (mapa conceptual).

## V-bis. Proyección financiera a futuro (R17 — Gajardo)
Filosofía: «proyectar no es adivinar; es prepararse» → transformar incertidumbre en información.
Método driver-based de los 3 estados a 3–5 años:
1. **Ingresos** = volumen × precio por línea, con la **mezcla** migrando según el plan estratégico.
2. **Costos** = costo variable por línea + ahorros de integración; mantener costo ≤ techo de margen.
3. **Caja** = cobranza (peso del contado) − servicio de deuda − capex.
4. **Balance** = capex (activo), amortización (pasivo, bajar Deuda/EBITDA), resultados (patrimonio).
5. **Escenarios** base / optimista / pesimista; medir Deuda/EBITDA, DSCR y valor de la acción.

## V-ter. Valuación de equity (estimación de gestión)
Triangular varios métodos y dar **rango**, nunca un solo número:
- **Valor en libros** (patrimonio neto) y libros ajustado (sin superávit por revaluación).
- **EV/EBITDA** (múltiplo sectorial) **− deuda neta** = equity; si la deuda supera el EV, el equity
  tiende a cero (sobre-apalancamiento).
- **Múltiplo de utilidad normalizada** (P/E).
- **DCF** a 5 años (con la proyección V-bis) para una valoración formal.
Por acción = valor / nº de acciones (confirmar nº y valor nominal). Señalar de qué palancas
(desapalancar, mejorar margen) depende el extremo alto del rango. No es un *fairness opinion*.
Caso QVP: libros ~$2,05/acción vs. base EBITDA ≈ $0 por deuda de ~$19 M (Deuda/EBITDA ~10×).

## V-quáter. Apalancamiento financiero bien calculado (R18 — F. J. López Martín)
Doctrina: **un ROE alto NO prueba rentabilidad** — puede ser solo deuda barata financiando activos.
Hay que medir el apalancamiento bien, o el diagnóstico sale equivocado. Tres errores frecuentes:
1. **Contar todo el pasivo como deuda financiera.** Proveedores y fisco no cobran interés; incluirlos
   infla el costo de la deuda. Usar **solo deuda con costo** (interest-bearing).
2. **Usar saldos de cierre** en vez de **saldos promedio** (apertura+cierre)/2.
3. **Ignorar el ajuste fiscal**: trabajar la rentabilidad económica **después de impuestos** (×(1−t));
   omitirlo subestima el retorno del activo.
El ratio clásico (rent. financiera ÷ rent. económica) solo dice «positivo/negativo» y oculta tres cosas:
- la **magnitud de amplificación** (multiplica la ganancia… y también la pérdida);
- el **umbral de quiebre**: a partir de qué punto el apalancamiento **destruye** valor;
- los **retornos por impuestos** que **desaparecen en años de pérdida**.
Efecto palanca: `ROE ≈ [RE + (RE − i)·(D/E)]·(1−t)`. Si el **costo de la deuda i > rentabilidad
económica RE**, la palanca es **negativa** y cada dólar de deuda resta. **Caso QVP:** i real ≈ 10,49 %
muy por encima de la RE del activo en 2024–2025 → apalancamiento **negativo**, coherente con la pérdida
de 2025 y con que la deuda se come el 82 % del margen. Aplicación **transversal**: en bancabilidad y en
toda lectura de EEFF, separar deuda con costo de pasivo operativo, usar saldos promedio y base
después de impuestos, y **marcar la alarma cuando i > RE**. Soporte: modelo Excel reproducible (15
hojas, 215 fórmulas) descrito en la fuente. Detalle: [[reference-apalancamiento-financiero-lopezmartin]].

## V-quinquies. Panel de 12 KPIs predictivos del CEO (R19 — Orlando Saucedo Vaca)
Doctrina: **la mayoría de los CEOs siguen ingresos y utilidad** —métricas **retrospectivas**—; para
cuando el estado de resultados muestra el problema, **el margen de maniobra ya es mínimo**. El líder
estratégico vigila **indicadores prospectivos** que anticipan el deterioro (p. ej. *ventas récord con
la caja cayendo mes a mes*, o *márgenes sanos pero sin liquidez*). Cada KPI se lee con su **pregunta
crítica** y por **tendencia** (no por el dato aislado), con **umbrales de alerta** automatizados.

| # | KPI | Pregunta crítica que anticipa el problema |
|---|---|---|
| 1 | **Margen bruto** | ¿Suben los costos antes de que se note en la utilidad? |
| 2 | **Margen operativo** | ¿El negocio principal es rentable por sí mismo? |
| 3 | **Tasa de crecimiento de ingresos** | ¿El crecimiento es sostenible o forzado? |
| 4 | **ROIC** | ¿Creamos o destruimos valor sobre el capital invertido? |
| 5 | **Ciclo de conversión de caja** | ¿Cuántos días está atrapado el efectivo? |
| 6 | **Capital de trabajo / ingresos** | ¿El crecimiento está consumiendo la caja? |
| 7 | **Flujo de caja operativo / ventas** | ¿Las ventas se convierten de verdad en efectivo? |
| 8 | **Margen de flujo de caja libre** | ¿El negocio puede autofinanciarse? |
| 9 | **Ratio corriente** | ¿Podemos cumplir las obligaciones de corto plazo? |
| 10 | **Deuda / EBITDA** | ¿Cuántos años de EBITDA tomaría pagar la deuda? |
| 11 | **DSCR** | ¿El flujo cubre el servicio de deuda (capital + intereses)? |
| 12 | **EBITDA / flujo operativo** | ¿Las ganancias están respaldadas por efectivo real? |

Aplicación: montar un **tablero de alerta temprana** con estos 12 y revisarlos **antes** de que el P&L
confirme el daño. Mapeo al caso QVP (refuerza «caja = supervivencia»): #5/#6/#7 capturan el patrón
"ventas récord / caja en caída"; #10/#11 son la alarma del **quiebre de deuda** (concuerdan con
*i > RE* de §V-quáter, R18); #12 detecta EBITDA no respaldado por caja. Estos mismos KPIs alimentan el
panel del War Room ([[control-financiero-semanal-qvp]]) y la proyección de escenarios de §V-bis.
Fuente: Orlando Saucedo Vaca, LinkedIn ("La mayoría de los CEOs siguen los ingresos…", activity-7471139283639386112).

## V-sexies. CapEx vs OpEx — por qué el EBITDA engaña a la caja (R20 — UpGrade Plus CFO)
Distinción que evita el autoengaño de «ganamos pero no hay plata»:
- **OPEX** = gasto operativo del día a día (sueldos, alquiler, suministros, software) → **golpea el
  P&L del período**.
- **CAPEX** = inversión de futuro (maquinaria, tecnología, instalaciones, equipo productivo) → **sale
  de caja YA**, pero **no** impacta el resultado de inmediato (se activa y se deprecia).
- **Trampa:** se puede mostrar **EBITDA positivo y ventas creciendo mientras la caja se agota**, porque
  el CapEx grande es salida inmediata de efectivo sin reflejo proporcional en el estado de resultados.
  *«El EBITDA mide rentabilidad operativa; la caja mide supervivencia.»*
- **Regla:** planificar el **CapEx dentro del flujo de caja** (no solo en el balance) y no confundir
  rentabilidad con liquidez. **Caso QVP:** el CapEx en los 4 proyectos fallidos drenó caja sin retorno
  — exactamente esta trampa; por eso la proyección (§V-bis) descuenta capex de la caja, fila a fila.
  Fuente: UpGrade Plus CFO, LinkedIn (activity-7472173682430390272).

## V-septies. Bancabilidad por EBITDA — el banco financia capacidad de pago (R21 — W. Zevallos Bustamante)
- **Crecer en ventas ≠ capacidad de pago.** Caso real: **+40 % en ventas** y aun así alertas
  financieras. *«Los bancos no financian historias; financian capacidad de pago.»*
- **3 rasgos de una empresa bancable:** rentabilidad operativa **consistente**, EBITDA **estable y
  predecible**, **disciplina financiera**.
- **Señales de alerta en empresas que crecen:** costos creciendo **más rápido** que los ingresos,
  **márgenes en reducción**, **EBITDA bajo presión** y **generación de caja limitada**.
- **Principio:** la pregunta no es *cómo consigo más financiamiento*, sino *si mi empresa genera la
  suficiente confianza para que me presten*. **Caso QVP:** presenta las cuatro señales a la vez →
  refuerza la hoja **H_BANCABILIDAD** ([[control-financiero-semanal-qvp]]) y el régimen de margen
  mínimo; conecta con la alarma *i > RE* (§V-quáter) y los KPIs #10/#11/#12 (§V-quinquies).
  Fuente: Walter Zevallos Bustamante, LinkedIn (activity-7472136518502010880).

## V-octies. Tipos de flujo de caja — OCF, FCFE, FCFF, EBITDA (R25 — Jordi Altimira)
Doctrina: **EBITDA solo sirve para comparativas rápidas** porque ignora impuestos, CAPEX y
cambios en capital de trabajo. Para evaluar sostenibilidad operativa real se usa **OCF**
(Operating Cash Flow). Para valoración accionaria, **FCFE** (Free Cash Flow to Equity, ya
descontada deuda); para valor económico total de la firma, **FCFF** (Free Cash Flow to Firm,
antes de deuda).

**Regla práctica en negociaciones**: pregunta SIEMPRE *"¿qué entiendes por flujo de caja libre?"*
antes de cerrar inversión o financiamiento; cada parte usa la métrica que le conviene.

**Doctrina del usuario reforzada**: un negocio rentable en P&L puede colapsar por liquidez. La
disciplina mensual de OCF y FCF es el indicador de **viabilidad operativa tangible** —vista
distinta y complementaria a los 12 KPIs (§V-quinquies) y al margen de bancabilidad (§V-septies).
Tabla de uso:

| Métrica | Sirve para | NO sirve para |
|---|---|---|
| **EBITDA** | comparativa rápida entre años o pares sectoriales | medir caja real (ignora capex/working capital/impuestos) |
| **OCF** | sostenibilidad operativa real | valoración accionaria |
| **FCFE** | retornos al accionista, P/E formal | valuar la firma completa antes de deuda |
| **FCFF** | valuación de la firma (DCF, EV) | analizar retorno solo del equity |

**Aplicación a QVP y al Vista al Río**: en la PLANTILLA ÚNICA agregar columna **OCF mensual**
además del flujo de caja contable; en el modelo de factibilidad del Edificio Vista al Río la
utilidad caja USD −423 K vs utilidad TOTAL USD 447 K es exactamente el delta que Altimira
describe entre caja y resultado patrimonial.

Fuente: Jordi Altimira, LinkedIn (`activity-7472573800476340224`). Detalle: [[reference-tipos-flujo-caja-jordialtimira]].

## V-novies. Retiros del socio + ratios como preguntas + EBITDA radiografía (R27–R29)
- **R27 — Retiros del gerente-propietario (Gavilánez).** En PyME/empresa familiar los retiros del
  dueño se desconectan de la rentabilidad real → "la empresa se vuelve la caja personal de los socios"
  (iliquidez, dependencia de préstamos, conflictos, crecimiento estancado). Regla: asignar al
  propietario un **sueldo de mercado** (como un empleado más) y recalcular la utilidad para ver si el
  negocio es rentable de verdad; separar **sueldo / dividendo / devolución de capital**. → skill
  dedicada [[politica-retiros-socio-propietario]]. Detalle: [[reference-retiros-socio-gavilanez]].
- **R28 — Ratios como preguntas de gestión (Da Costa).** Los ratios no son cálculos: son preguntas.
  3 funciones (señal temprana · conectar operación-finanzas · datos→decisiones) y 3 áreas: liquidez
  (¿cubro el corto plazo sin tensionar la operación?), eficiencia (días cobranza/pago/inventario =
  capital de trabajo) y rentabilidad (ROA/ROE leídos con riesgo, apalancamiento y calidad de
  utilidades). Converge con el panel de 12 KPIs (§V-quinquies). Detalle: [[reference-ratios-preguntas-gestion-dacosta]].
- **R29 — EBITDA como radiografía de eficiencia (Zevallos).** Vender mucho ≠ ganar: facturación récord
  con destrucción de valor operativo. Vigilar señales (costos creciendo más que ventas, descuentos
  excesivos, logística/compras ineficientes, sobrecostos ocultos) y monitorear **EBITDA mensual**.
  Detalle: [[reference-ebitda-radiografia-zevallos]].

## VI. Relación con otras skills
- `control-financiero-semanal-qvp` — operacionaliza el mínimo financiero (War Room).
- `wolfram-forensic-engine` — recálculo/validación forense de las cifras.
- `xlsx-a4-portrait-merge-pdf` — entregables PDF.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
