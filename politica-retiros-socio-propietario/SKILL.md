---
name: politica-retiros-socio-propietario
description: |
  Diagnostica y diseña la POLÍTICA DE RETIROS del gerente-propietario / socios en
  empresas familiares y PyME: separa sueldo de mercado, dividendo (utilidad real) y
  devolución de capital, y detecta cuándo "la empresa se volvió la caja personal de
  los socios" (descapitalización). Producto: diagnóstico + política de retiros y
  dividendos atada a rentabilidad y caja, no a necesidades personales del momento.
trigger_phrases:
  - "política de retiros"
  - "cuánto debe ganar el dueño / gerente propietario"
  - "sueldo de mercado del socio"
  - "retiros de socios vs rentabilidad"
  - "la empresa es la caja personal de los socios"
  - "política de dividendos PyME / empresa familiar"
idioma_de_salida: español
nivel: especializada
dominio: financiero / empresa-familiar
metadata:
  version: 1.0
  fecha: 2026-06-19
  origen: LinkedIn — C. Javier Gavilánez (R27, retiros vs rentabilidad) reforzado con Da Costa (R28, ratios) y Zevallos (R29, EBITDA)
  fuente: post Gavilánez activity-7473347568140386304 (+ R28 Da Costa, R29 Zevallos)
  relacionada: memoria-financiera-inteligenciada, control-financiero-semanal-qvp
---

# Skill `politica-retiros-socio-propietario`

## Acerca de mí (cargar al arrancar)
Lee `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y `MEMORY.md`.
Casos vivos: **Quevepalma** (familia Juez) y **Edificio Vista al Río / INMOBILIARIA JUEZ & JUEZ**
— ambas empresas familiares donde aplica directamente.

## Doctrina central
En la PyME familiar, finanzas de la empresa y del dueño están **conectadas pero no son lo mismo**.
Cuando los **retiros personales superan la rentabilidad real**, la empresa se vuelve "la caja
personal de los socios": liquidez frágil, dependencia de préstamos, menor inversión, conflictos y
crecimiento estancado. La cura es una **política**: tratar al gerente-propietario como un empleado
con **sueldo de mercado**, y que todo lo demás salga solo como **dividendo de utilidad real** (no de
caja prestada). Doctrina hermana: «utilidad = rentabilidad; caja = supervivencia» de
[[memoria-financiera-inteligenciada]].

## Qué NO hacer / compuertas 🚦
- 🚦 No es asesoría tributaria/legal personalizada ni decide repartos: **propone política**; aprueba el dueño/Directorio.
- No confundir las **tres salidas de dinero**: (a) sueldo (gasto), (b) dividendo (utilidad), (c) devolución de capital. Mézclalas y el diagnóstico miente.
- No usar caja como prueba de ganancia (sesgo «confundir caja con utilidad»). No inventar cifras: pídelas o márcalas como supuesto.

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Reunir** EEFF (resultados + balance + flujo), historial de **retiros de cada socio** y nº de socios/%.
2. **Sueldo de mercado:** asignar al gerente-propietario un sueldo fijo de mercado (como "un empleado más") y recalcular la utilidad operativa/EBITDA **después** de ese sueldo → ¿el negocio sigue siendo rentable por sí mismo? (radiografía EBITDA, R29 Zevallos).
3. **Clasificar los retiros reales** del período en sueldo / dividendo / devolución de capital; comparar el total contra la **utilidad neta real** y la **caja libre** del período.
4. **Señales de alerta** (R27 Gavilánez): falta de liquidez, dificultad para cumplir obligaciones, dependencia de préstamos, menor capacidad de inversión, conflictos entre socios, crecimiento estancado. Marcar las presentes.
5. **Lentes de ratios** (R28 Da Costa): liquidez (corriente/ácida, capital de trabajo), eficiencia (días de cobranza/pago/inventario) y rentabilidad (ROA/ROE con riesgo y apalancamiento) para ver si el retiro está descapitalizando.
6. **Política propuesta:** (a) sueldo de mercado mensual del/los socio(s) operativos; (b) **regla de dividendos** = % de la utilidad neta real **solo si** la caja y los covenants lo permiten; (c) tope de retiros vs. utilidad; (d) fondo de reinversión/contingencia; (e) tablero de seguimiento mensual.
7. **Entregable:** diagnóstico (¿el negocio financia al dueño o el dueño construye un negocio sostenible?) + política redactada + tablero. Persistir en la carpeta del caso (QVP → `WAR ROOM QVP\`; Vista al Río → su carpeta).

## Cómo depurar si falla
Si no cuadran retiros con EEFF, casi siempre es por **mezclar las tres salidas** (paso 3) o por contar caja como utilidad. Pide el mayor de "cuentas por cobrar a socios"/"préstamos de socios" y reconcília. Si faltan EEFF, usa [[memoria-financiera-inteligenciada]] para reconstruir la serie.

## Portabilidad (revisar 20% al reusar)
Sueldo de mercado de referencia (país/sector), % de dividendo objetivo, covenants bancarios y nº/estructura de socios. El método es estable.

## Reuso
Backbone analítico en [[memoria-financiera-inteligenciada]] (ratios, EBITDA, caja>utilidad) y operación en [[control-financiero-semanal-qvp]] (mínimo financiero/caja). No reimplementar ratios: invocarlos de ahí.

## Ejemplos de invocación
- «¿Cuánto debería ganar el gerente-propietario de Quevepalma sin descapitalizar la empresa?»
- «Arma la política de retiros y dividendos para INMOBILIARIA JUEZ & JUEZ.»
- «¿Los retiros de los socios este año superaron la utilidad real? Diagnóstico.»


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
