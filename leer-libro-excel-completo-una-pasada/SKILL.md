---
name: leer-libro-excel-completo-una-pasada
description: >
  Antes de analizar un libro Excel grande (exportado de un ERP como XASS, varias
  hojas, 5-6 MB), léelo COMPLETO en UNA sola pasada —todas las hojas, celdas,
  filas, columnas, texto Y fórmulas— y vuélcalo a un .txt; luego analiza sobre ese
  .txt sin recargar el xlsx. Incluye el método para clasificar y AGRUPAR los pagos
  por OBRA FÍSICA cuando una misma obra la ejecutan varios contratistas (la columna
  de observaciones/concepto es la llave). Evita el desperdicio de crédito por
  lecturas parciales y repetidas del mismo archivo pesado.
metadata:
  type: feedback
---

# Leer el libro Excel completo en una pasada (y agrupar por obra)

## Por qué existe (el fallo que la originó)
En el control de pagos de bodegas de Mobijuesa se leyó el libro **parcialmente y
con `data_only`**, varias veces (cada carga del .xlsx de 5,8 MB tarda 2-3 min). Eso
(1) **desperdició crédito** y (2) produjo cifras mal clasificadas (p. ej. un saldo
de Torres por 8.439,40 contado como pagado porque la 2.ª factura iba sin anticipo,
y el material "no asignado" que en realidad era todo eléctrico de Molina). La regla:
**leer el libro entero, de la primera celda a la última, una sola vez, y entenderlo
como un todo antes de calcular.**

## Procedimiento
1. **Una sola pasada, dos cargas** (valores + fórmulas) con el helper:
   ```bash
   python -I "C:/Users/datos/.claude/skills/leer-libro-excel-completo-una-pasada/volcar_libro.py" "<ruta.xlsx>" "<salida.txt>"
   ```
   Vuelca TODAS las hojas / celdas / filas / columnas / texto / **fórmulas** a un
   `.txt` y imprime un RESUMEN (por hoja: celdas, nº de fórmulas, filas de
   total/saldo, columna de estado). Correrlo en segundo plano (tarda).
2. **Analizar sobre el `.txt`** (barato): leer el RESUMEN y hacer `Grep` de lo
   puntual (área, m2, total, saldo, pendiente, cancelado, hormigón…). **Nunca**
   recargar el xlsx grande para cada pregunta.
3. **Estado real del pago** vive en la columna de estado del libro por contratista
   («Cancelado» / «Pendiente de pago»), y el **saldo** en su columna de saldo —no
   en el maestro, cuyo «Procesado» solo significa "ingresado al sistema".
4. **Verificar al centavo** los totales y las sumas contra los pies de hoja con
   Wolfram (`WolframLanguageEvaluator`); cada entregable debe cuadrar.

## Clasificar y agrupar por OBRA (clave: columna H = observación/concepto)
Una **obra física** puede estar ejecutada por **varios contratistas a la vez**, y
cada contratista la factura por separado (mano de obra) con sus propios materiales.
La columna de observación/concepto (H en el maestro; el "detalle" en los libros por
contratista, que suele traer el **área**: 1300, 800, 864, 150, 56 m²) es la llave
para agrupar. Ejemplos reales (Mobijuesa):
- La obra de **800 m² (Flores)** y la de **864 m² (Torres)** son **la misma**:
  ampliación de la fábrica de tubos.
- La **bodega de 150 m²**: eléctrico (Guillermo) + parte metálica (Tapia) + obra
  civil (Flores).
- La **bodega de 1300 m²**: cimentación + estructura + acabados de varios frentes.

**Costo unitario de la obra** = se calcula el $/m² de cada contratista por separado
(su costo ÷ su área reportada) y **se suman** los unitarios individuales de los
rubros que componen esa obra → costo unitario consolidado (ponderado/sumado). Cada
contratista aporta mano de obra + sus materiales asignados.

Pasos de agrupación:
1. Mapear cada bloque de obra del libro (y sus materiales) a una **obra física**
   por el área/keyword del concepto.
2. Por obra: sumar MO + material de cada contratista; calcular su $/m²; sumar los
   $/m² de los contratistas de esa obra.
3. Consolidar: costo total por obra, costo por contratista dentro de la obra, y
   $/m² consolidado. Clasificar además pagado/pendiente por estado.
4. Si un bloque no mapea claro a una obra, **no adivinar en silencio**: listarlo
   aparte y pedir confirmación al usuario (solo él sabe qué estructura física es).

## Cómo depurar si falla
- **`FileNotFoundError` con un path que tiene acentos** (Construcción/Facturación):
  Git Bash corrompe el argumento (Construcci�n). Invocar el helper **por PowerShell**
  con `& $py -I $sk $xlsx $out` y variables, o hardcodear el path como literal
  dentro de un `.py` (el fuente va en utf-8 y sí resuelve). No pasar rutas con
  acentos como argumento desde el Bash tool.
- Si el libro está abierto en Excel/Drive, puede aparecer un `~$` lock; para
  **leer** no estorba, pero para **escribir** un .xlsx hay que cerrarlo antes.

## Relación con otras skills
- Formato de salida y A4/PDF: [[excel-formato-dolar-y-m2]], [[xlsx-a4-portrait-merge-pdf]], [[entrega-visual-html-vs-texto]].
- Doctrina de verificación: [[cierre-verificado-integridad]], [[control-versiones-entregables]].
- Captura del hallazgo como aprendizaje: [[llave-maestra-autoaprendizaje-ia]], [[regla-del-primer-tropiezo]].
