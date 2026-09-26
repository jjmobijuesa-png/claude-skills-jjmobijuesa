---
name: modelo-tres-estados-integrado
description: |
  Construye y AUDITA un modelo financiero de tres estados articulados —resultados,
  balance y flujo de efectivo— donde el flujo se DERIVA de los otros dos y el balance
  cuadra por construcción, no por ajuste manual. Es el formato que exigen la banca y
  los fondos multilaterales, y el que convierte una proyección de Excel en un modelo
  defendible.

  Prueba de vida innegociable: si el balance cuadra porque alguien metió una celda
  de «ajuste», el modelo está roto. Debe cuadrar solo.

trigger_phrases:
  - "modelo de tres estados"
  - "3-statement model"
  - "proyección financiera para el banco"
  - "arma el modelo financiero del proyecto"
  - "audita este modelo de Excel"
  - "el balance no cuadra"
idioma_de_salida: español
nivel_madurez: aplicada
dominio: finanzas / modelación
metadata:
  version: 1.0
  fecha: 2026-09-05
  origen: destilada el 2026-09-05 de los ítems 6 y 10 del post de Nicolas Boucher (lnkd.in/p/eYTCmUEW). 🚦 Ninguno de los dos videos existe en su canal (92 videos verificados); la técnica se reconstruyó desde MIT 15.401 y OpenStax Financial Accounting, ambos verificados.
  relacionada: bancabilidad-matriz-cuatro-bloques, analisis-variaciones-cascada, cfo-mensual-con-claude, calificacion-fondos-multilaterales-impacto, excel-pagina-a4-optima
---

# Skill `modelo-tres-estados-integrado`

## Doctrina

La mayoría de las «proyecciones» que circulan son un estado de resultados con una fila de caja
pegada abajo. Eso no es un modelo: es un deseo con formato. Un modelo de tres estados tiene una
propiedad que ningún deseo tiene — **está sobredeterminado**: la caja se calcula dos veces, por el
flujo y por el balance, y ambas deben coincidir. Esa redundancia es justamente lo que lo hace
auditable, y es la razón por la que un banco lo pide.

**Las tres articulaciones que lo sostienen:**

1. **Utilidad neta** del estado de resultados entra al **patrimonio** del balance (menos dividendos).
2. **Utilidad neta** es también el punto de partida del **flujo de efectivo** por el método indirecto.
3. **Caja final** del flujo es la **caja del balance**. Si no coincide, hay un error, no una diferencia.

## Orden de construcción (no se puede alterar)

| # | Paso | Detalle |
|---|---|---|
| 1 | **Supuestos en una sola hoja** | Todo dato exógeno vive ahí, en celdas de un solo color. Ninguna cifra suelta dentro de una fórmula. |
| 2 | **Ingresos con inductor explícito** | Unidades × precio, o m² × $/m², nunca «crecimiento del 8 %» sin inductor detrás. |
| 3 | **Costos: fijos y variables separados** | El apalancamiento operativo solo se ve si están separados. |
| 4 | **Capital de trabajo por rotación** | Días de cobro, de inventario y de pago. Es donde muere la caja de las constructoras. |
| 5 | **Activo fijo y depreciación** | Cronograma propio: CapEx, vida útil, depreciación acumulada. |
| 6 | **Deuda con su cronograma** | Amortización, interés sobre saldo, y **el interés vuelve al estado de resultados**. |
| 7 | **Flujo indirecto** | Utilidad + depreciación − variación de capital de trabajo − CapEx + financiamiento. |
| 8 | **Cuadre** | Caja del flujo = caja del balance. Activo = pasivo + patrimonio. **Al centavo.** |

## Las cinco pruebas de vida 🚦

Antes de mostrar un modelo a un banco, a un fondo o a un socio:

1. **El balance cuadra sin celda de ajuste.** Si existe un «plug», el modelo miente.
2. **Sube el precio 1 % y todo se mueve de forma coherente** — resultados, capital de trabajo, caja.
   Si algo no se mueve, está desconectado.
3. **No hay referencias circulares no declaradas.** El interés sobre caja promedio crea circularidad
   legítima: se declara y se resuelve con iteración, no se esconde.
4. **Ninguna cifra dura dentro de una fórmula.** Todo constante vive en supuestos.
5. **El DSCR se calcula dentro del modelo**, no aparte. Ver [[bancabilidad-matriz-cuatro-bloques]].

## Cómo auditar un modelo ajeno (o uno propio heredado)

Aplicar las cinco pruebas anteriores en orden y, además, rastrear **de dónde sale la TIR**: si la
tasa se calcula sobre un flujo que no es el flujo del modelo sino una fila aparte, el resultado no
significa nada. **Precedente en casa:** la hoja `6-IND FIN` de San Sebastián tenía VAN y TIR
inutilizables por esa razón; el modelo corregido dio TIR 38,81 % y VAN al 10 % de $1.076.698.

## Aplicación en esta casa

- **Belén** y **San Sebastián**: el modelo que exige el banco y el que sostiene la decisión de precio.
- **Fondos BID Lab y CAF VELA**: la proyección financiera del anexo va en este formato o no pasa el
  primer filtro. Ver [[calificacion-fondos-multilaterales-impacto]].
- **QVP**: articula el presupuesto de compra de fruta con la caja semanal.
- **Bodegas**: modelo pequeño pero completo; sirve de plantilla de entrenamiento.

## Fuente y honestidad de origen

Disparado por un post de LinkedIn que prometía dos videos sobre modelos financieros y FP&A. **Ninguno
de los dos existe en el canal del autor.** La técnica se reconstruyó desde fuentes verificadas:
**MIT 15.401 Finance Theory I** (CC BY-NC-SA) y **OpenStax Financial Accounting** (CC BY). Detalle en
`E:\vars\var 5\Universidad-Abierta\notas\2026-09-05_destilacion-post-boucher.md`.

## Relacionado

- Microciclo 5 del [[programa-estudio-profundo-mit]] · [[analisis-variaciones-cascada]]
- [[bancabilidad-matriz-cuatro-bloques]] · [[cfo-virtual-44-agentes]]
