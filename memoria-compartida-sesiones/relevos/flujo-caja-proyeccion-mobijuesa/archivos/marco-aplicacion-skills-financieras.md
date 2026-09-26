# Marco de aplicación — skills financieras → flujo de caja y proyección Mobijuesa

_Preparado por el espejo (nube), 2026-09-26, mientras se espera el volcado de la PC._
_Objetivo: que, en cuanto llegue la publicación de LinkedIn 7508480383286452224 y el modelo actual,
la directriz se aplique en minutos y con un criterio ya acordado._

## 1. Qué aporta cada skill del repo

| Skill | Qué aporta al modelo de Mobijuesa | Prueba o regla clave |
|---|---|---|
| `modelo-tres-estados-integrado` | Arquitectura: supuestos → ingresos por inductor → costos fijos/variables → capital de trabajo por días → CapEx/depreciación → deuda con cronograma → flujo indirecto → cuadre | Balance cuadra **sin plug**; +1 % de precio mueve todo; DSCR dentro del modelo |
| `modelo-excel-sistema-vivo` | Disciplina del libro: una palanca por concepto, amarillo `FFF2CC` = independiente, azul `DDEBF7` = dependiente, controles que dan 0, mapa de vínculos en la fila 2 | Cambiar una palanca → `CalculateFull()` → verificar → revertir. Nunca `Move(After=…)` |
| `memoria-financiera-inteligenciada` | Doctrina de lectura: caja > utilidad, 12 KPIs predictivos, OCF/FCFE/FCFF, CapEx fuera del EBITDA, apalancamiento i vs RE, retiros del socio (R27), proyección por inductores con 3 escenarios (R17) | «Utilidad = rentabilidad; caja = supervivencia» |
| `cfo-mensual-con-claude` | Operación mensual: W1–W7 (facturas → conciliación → gastos sin factura → P&L por rubro → cobranza → dashboard e indicadores → gestoría). Mobijuesa aparece en W4 (margen por línea/cliente) y en la cuota de Mobijuesa (942) que **no pasa por Produbanco** | Reconciliación dura: suma de movimientos = saldo final − saldo inicial; correos siempre en BORRADOR |
| `control-financiero-semanal-qvp` | Plantilla semanal replicable: margen bruto de equilibrio, costo de ventas máximo, caja con punto de equilibrio, proyección a 3 semanas, semáforos 3 %/5 % | Margen de equilibrio = (gastos operativos + financieros netos) / ventas |
| `bancabilidad-matriz-cuatro-bloques` (relacionada) | Matriz del banco: liquidez · apalancamiento · cobertura · estructura de deuda | Deuda/EBITDA ≤ 3,5; EBITDA/intereses ≥ 2; DSCR ≥ 1,2 |
| `politica-retiros-socio-propietario` (relacionada) | Sueldo de mercado al dueño; separar sueldo, dividendo y devolución de capital | Recalcular la utilidad con el sueldo de mercado |

## 2. Esqueleto propuesto para el modelo (a validar contra el archivo real de la PC)

1. **SUPUESTOS** (solo amarillos): ventas por línea (unidades × precio), días de cobro, inventario y pago,
   costos fijos mensuales, costo variable por línea, CapEx, deuda (monto, tasa, plazo, gracia),
   caja inicial, sueldo de mercado del dueño, retiros planificados.
2. **VENTAS Y MARGEN POR LÍNEA/CLIENTE**: margen de contribución y quién hace perder dinero (W4).
3. **FLUJO DE CAJA 13 SEMANAS** (táctico) + **FLUJO MENSUAL 12–36 MESES** (proyección).
4. **PyG → BALANCE → FLUJO INDIRECTO** articulados (cuadre al centavo).
5. **INDICADORES**: DSCR, Deuda/EBITDA, ciclo de conversión de caja, OCF/ventas, margen FCF, runway,
   margen bruto de equilibrio.
6. **ESCENARIOS** base / optimista / pesimista con una sola celda selectora.
7. **CONTROLES** (todos deben dar 0) y hoja de cambios (qué supuesto nuevo entró y por qué).

## 3. Plantilla para aplicar la directriz de la publicación (se llena cuando llegue)

| Campo | Contenido |
|---|---|
| Autor / fecha / enlace | _pendiente (PC)_ |
| Tesis de la publicación en una línea | _pendiente_ |
| Método o fórmula que propone | _pendiente_ |
| Métricas nuevas | _pendiente_ |
| ¿Ya está en alguna skill? (R1–R31 de `memoria-financiera-inteligenciada`) | _pendiente_; si es nueva, se registra como R32 |
| Brecha contra el modelo actual | _pendiente_ |
| Cambio concreto al modelo (hoja, fila, fórmula) | _pendiente_ |
| Supuesto nuevo y su fuente | _pendiente_ |
| Prueba de vida tras el cambio | cambiar una palanca → recalcular → verificar → revertir |

## 4. Criterios de aceptación de cualquier cambio
- Ninguna cifra fija dentro de una fórmula; todo supuesto en SUPUESTOS y comentado.
- El balance cuadra sin celda de ajuste; la caja del flujo es igual a la caja del balance.
- Se documenta la fuente de cada supuesto nuevo (publicación, skill o dato del usuario).
- Sin credenciales, cuentas ni datos privados en `archivos/`; las cifras reales se quedan en la PC
  si el usuario lo prefiere.

## 5. Preguntas abiertas para la PC / el usuario
- ¿Cuál es el archivo principal (Excel) y en qué ruta está?
- ¿Qué es Mobijuesa en el modelo: empresa con líneas de venta, o proyecto/cuota (942) dentro de Finanza Integral?
- Horizonte y granularidad esperados (¿13 semanas + 36 meses?).
