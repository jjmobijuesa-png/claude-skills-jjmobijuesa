# Marco del informe financiero — Mobijuesa

_Preparado por el espejo (nube), 2026-09-26, sin volcado previo de la PC._
_**Este archivo no contiene cifras reales.** Solo tiene estructura, indicadores, umbrales genéricos de referencia
y preguntas. Las cifras se calculan y se quedan en la PC (nivel N3/N4 según `gobernanza-datos-financieros-ia`)._

## 0. Regla de datos del hilo (recordatorio operativo)

| Qué | Dónde vive | Qué sube a este repo |
|---|---|---|
| Estados financieros, cierres, balances y auxiliares | PC (local) | Ruta local + resumen cualitativo |
| Deuda, saldos, DSCR y ratios calculados con datos reales | PC (local) · **N3** | Semáforo (verde/ámbar/rojo) sin el valor, o valor **escalado** con un factor no revelado |
| Clientes, socios, personas naturales, cédulas y escrituras | PC (local) · **N4** | Nada; si hace falta, un seudónimo («Cliente 03», «Banco 2») |
| Estructura, método, preguntas y conclusiones sin cifras | Repo | Sí |

Si un resumen necesita la magnitud para razonar, usar el **escalado** (se conservan los ratios y la estructura)
o **rangos** («entre X y Y»). Antes de guardar en `archivos/`, releer el texto: todo lo que se escribe aquí se publica solo.

## 1. Estructura propuesta del informe

| # | Sección | Contenido | Skill que la gobierna |
|---|---|---|---|
| 1 | **Síntesis ejecutiva** (1 página) | Tres conclusiones, el ratio que rompe, las decisiones que se piden y el semáforo general | `memoria-financiera-inteligenciada` §III (el análisis renueva la estrategia) |
| 2 | **Alcance y fuentes** | Periodo, entidad, base contable, fuentes, qué quedó conciliado y qué no, y qué datos se sustituyeron (rastro de desidentificación) | `gobernanza-datos-financieros-ia` paso 5 · `cfo-mensual-con-claude` W2 |
| 3 | **Serie histórica** | Resultados, balance y flujo por periodo. La verdad sale de la serie, no del año aislado | `memoria-financiera-inteligenciada` §II |
| 4 | **Estado de resultados por línea/cliente** | Margen de contribución por línea, quién hace perder dinero, fijos frente a variables | `cfo-mensual-con-claude` W4 · `modelo-tres-estados-integrado` paso 3 |
| 5 | **Balance y capital de trabajo** | Días de cobro, de inventario y de pago; ciclo de conversión de caja | `modelo-tres-estados-integrado` paso 4 |
| 6 | **Flujo de efectivo** (indirecto) | Tipos de flujo: OCF, FCFF, FCFE. Comparar el EBITDA con la caja y separar CapEx de OpEx | `memoria-financiera-inteligenciada` V-sexies, V-octies |
| 7 | **Deuda** | Cronograma, costo, concentración de vencimientos a 12 meses y apilamientos | `bancabilidad-matriz-cuatro-bloques` bloque 4 |
| 8 | **Matriz de bancabilidad** | Los cuatro bloques contra **estándares bancarios**, no contra el histórico propio; qué ratio rompe | `bancabilidad-matriz-cuatro-bloques` |
| 9 | **Panel de alerta temprana** | Los 12 KPIs predictivos, leídos por tendencia y con su pregunta crítica | `memoria-financiera-inteligenciada` V-quinquies |
| 10 | **Retiros y partes relacionadas** | Sueldo de mercado del dueño; separar el sueldo, el dividendo y la devolución de capital | `memoria-financiera-inteligenciada` V-novies |
| 11 | **Proyección y escenarios** | Base, optimista y pesimista por inductores. **Coordinar con el hilo `flujo-caja-proyeccion-mobijuesa`, sin duplicarlo** | `modelo-tres-estados-integrado` · `memoria-financiera-inteligenciada` V-bis |
| 12 | **Diagnóstico crítico y decisiones** | Punto exacto de ruptura, costo monetizado, mínimo financiero para no perder y dirección del crecimiento (hacia el margen) | `memoria-financiera-inteligenciada` §III |
| A | **Anexos** | Controles de cuadre, supuestos y glosario | `modelo-tres-estados-integrado` (cinco pruebas de vida) |

**Entregables** (`memoria-financiera-inteligenciada` §V): serie en xlsx, gráficos, narrativa crítica en md, panel de KPIs
y bancabilidad, y síntesis estratégica. Para decidir se usa un dashboard HTML (`cfo-mensual-con-claude` W6).
**Todos se generan y se quedan en la PC.** Si algo se publica, solo puede ser N1/N2.

## 2. Indicadores clave

### 2.1 Matriz del banco (para pedir financiamiento)

| Bloque | Indicadores | Referencia genérica de las skills |
|---|---|---|
| 1 · Liquidez | Razón corriente · Prueba ácida · Capital de trabajo neto | Cubrir el corto plazo sin depender de ventas futuras |
| 2 · Apalancamiento | Deuda/Patrimonio · Deuda/EBITDA | Deuda/EBITDA ≤ 3,5 |
| 3 · Cobertura | EBITDA/Intereses · OCF/Deuda · DSCR | EBITDA/Intereses ≥ 2 · DSCR ≥ 1,2 |
| 4 · Estructura de deuda | % corto frente a largo plazo · Concentración de vencimientos | Sin apilamientos en los próximos 12 meses |

Dos reglas duras: basta **un** ratio fuera de rango para reclasificar el perfil, y la comparación se hace contra el rango del banco, no contra el histórico propio.

### 2.2 Tablero de ocho (para no perder la bancabilidad entre pedido y pedido)
Liquidez disponible · Capital de trabajo · EBITDA · Margen EBITDA · Flujo operativo · Prueba ácida ·
Cobertura de intereses · Ciclo de conversión de efectivo.

### 2.3 Los 12 KPIs predictivos (se leen por tendencia)
Margen bruto · Margen operativo · Crecimiento de ingresos · ROIC · Ciclo de conversión de caja ·
Capital de trabajo/ingresos · OCF/ventas · Margen FCF · Ratio corriente · Deuda/EBITDA · DSCR · EBITDA/OCF.

### 2.4 Controles de integridad (sin estos no se emite el informe)
- La caja del flujo coincide con la caja del balance, y Activo = Pasivo + Patrimonio **sin celda de ajuste**.
- Conciliación bancaria dura: suma de movimientos = saldo final − saldo inicial.
- Prueba de +1 % en precio: todo se mueve de forma coherente.
- El DSCR se calcula **dentro** del modelo, y ninguna cifra queda fija dentro de una fórmula.

## 3. Qué debe dejar la PC en `archivos/` (solo `.md`, sin cifras reales)

| # | Archivo sugerido | Contenido permitido |
|---|---|---|
| P1 | `alcance.md` | Qué es el informe, para quién (banco, socios o gerencia), periodo, base contable y fecha de entrega |
| P2 | `punteros-fuentes.md` | **Ruta local** de cada fuente (estados, balances, auxiliares, cronograma de deuda, modelo), con fecha de corte y estado (conciliado sí/no) |
| P3 | `hallazgos-cualitativos.md` | Conclusiones sin cifras: «el margen bruto cae tres periodos seguidos», «el bloque 3 está en rojo», «vencimientos apilados en el trimestre X» |
| P4 | `semaforo-indicadores.md` | Tabla indicador → verde/ámbar/rojo → tendencia (↑/↓/=). Sin valores; si hace falta, valores escalados con factor no revelado |
| P5 | `estructura-modelo.md` | Hojas del libro, qué calcula cada una, controles y si pasa las cinco pruebas de vida |
| P6 | `razonamiento-en-curso.md` | En qué sección va, qué se decidió y qué falta (volcado en caliente) |

## 4. Preguntas abiertas (para la PC o para Francisco)

1. **Destinatario y propósito:** ¿el informe es para un banco (renegociación o crédito nuevo), para los socios o para la gestión interna? Eso cambia el orden: para un banco, la matriz va primero.
2. **Entidad y perímetro:** ¿Mobijuesa como empresa sola o consolidada con otras unidades? ¿Qué línea de negocio es la principal?
3. **Periodo:** ¿cierre anual, año a la fecha o una serie de varios años? ¿Cuál es la fecha de corte?
4. **Base contable:** ¿estados auditados, declarados o de gestión? ¿Hay NIIF para PYMES?
5. **Relación con el flujo personal:** en `cfo-mensual-con-claude` aparece una cuota a Mobijuesa en el flujo personal. ¿Hay saldos con partes relacionadas (socio ↔ empresa) que deban tratarse en la sección 10?
6. **Frontera con el hilo `flujo-caja-proyeccion-mobijuesa`:** ¿la proyección del informe se toma de ese modelo (solo se cita) o se construye aquí? Propuesta: citarla y no duplicarla.
7. **Formato de entrega:** ¿Word/PDF, dashboard HTML o ambos? ¿Hay plantilla o idioma requerido? (El título del hilo está en inglés.)
8. **Escalado:** si hace falta discutir magnitudes con la nube, ¿se autoriza usar un factor de escalado no revelado?

## 5. Bloqueantes actuales
- Sin volcado de la PC: no se conocen el alcance, las fuentes ni el periodo. El espejo no puede avanzar más allá del marco
  hasta tener P1, P2 y las respuestas a las preguntas 1 a 3.
