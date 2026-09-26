---
name: excel-pagina-a4-optima
description: |
  Configura la CONFIGURACIÓN DE PÁGINA de cualquier archivo Excel (.xlsx)
  para que su contenido aproveche al máximo la superficie de una hoja
  A4, eligiendo automáticamente la ORIENTACIÓN apropiada según la forma
  del contenido (horizontal si es ancho, vertical si es alto) y
  calculando el PORCENTAJE DE ESCALA para que el contenido LLENE la
  hoja, no solo que quepa.

  Regla de oro: "que ocupe toda la superficie, en la proporción y
  porcentaje correctos, preferentemente A4". No dejar tablas
  diminutas en una esquina ni cortadas por mala orientación.

  Es la capa de PREPARACIÓN de página. Se combina con
  [[xlsx-a4-portrait-merge-pdf]] y [[xlsx-to-pdf-a4]] (que exportan a
  PDF) y con [[documentos-encuadrados-margenes]] (documentos Word).

trigger_phrases:
  - "configura las páginas del Excel"
  - "orientación correcta de las hojas"
  - "que el Excel ocupe toda la hoja A4"
  - "ajusta la escala para llenar la página"
  - "horizontal o vertical según el contenido"
  - "prepara el xlsx para imprimir en A4"

idioma_de_salida: español
nivel: aplicada
dominio: ofimática / preparación de documentos
metadata:
  version: 1.0
  fecha: 2026-07-22
  script: scripts/configurar_paginas_a4.py
  relacionada:
    - xlsx-a4-portrait-merge-pdf
    - xlsx-to-pdf-a4
    - documentos-encuadrados-margenes
    - numeracion-paginas-informes
---

# Skill `excel-pagina-a4-optima`

## Doctrina

Un Excel bien hecho pero mal paginado se imprime pésimo: tablas
diminutas en una esquina, columnas cortadas, media hoja en blanco. La
regla del usuario es clara: **cada hoja debe ocupar toda la superficie
de una A4, en la proporción correcta**, eligiendo orientación por la
forma del contenido y escalando el porcentaje para LLENAR (no solo
caber).

Esto NO es lo mismo que "Ajustar a una página" de Excel, que solo
REDUCE. Aquí se calcula el % de escala que hace que el contenido crezca
o se reduzca hasta llenar la A4.

## Qué hace el script (`configurar_paginas_a4.py`)

Para CADA hoja del libro:

1. Mide el tamaño real del contenido (suma de anchos de columna y
   altos de fila del rango usado).
2. Prueba las dos orientaciones y elige la que da **mayor factor de
   llenado** de la A4 (contenido ancho → horizontal; alto → vertical).
3. Calcula la **escala %** = el mínimo entre (ancho útil / ancho
   contenido) y (alto útil / alto contenido), acotada a **[40, 250]%**.
4. Fija: papel **A4** (paperSize 9), la orientación elegida, la escala
   calculada, **márgenes estrechos** (0,5 cm) y **centrado horizontal +
   vertical**.
5. Si el contenido es tan grande que no cabe ni al 40%, cae a
   "ajustar a 1 página de ancho" (`fitToWidth=1`) como respaldo.

Verificado: hoja ancha → horizontal 121%; hoja alta → vertical 139%.

## Qué NO hacer / compuertas 🚦

- 🚦 **Backup automático**: el script crea `<archivo>.xlsx.bak` la
  primera vez antes de sobreescribir. No borrar el backup hasta
  confirmar el resultado.
- 🚦 **No altera los DATOS ni el formato de celdas** — solo la
  configuración de página. Es reversible.
- 🚦 **Escala máxima 250%**: evita inflar una tabla de 3 celdas a
  tamaño póster. Si se necesita más, ajustar `SCALE_MAX` en el script.
- 🚦 **Estimación de anchos**: openpyxl mide el ancho en "caracteres";
  la conversión a puntos es aproximada (±10%). Para precisión absoluta,
  abrir en Excel y usar Vista Previa. El 20% volátil de esta skill.

## Protocolo paso a paso

> **Tómate tu tiempo. Calidad antes que velocidad.**

1. Identificar el/los .xlsx a preparar.
2. Ejecutar:
   ```bash
   "C:\Users\datos\.notebooklm-venv\Scripts\python.exe" ^
     "C:\Users\datos\.claude\skills\excel-pagina-a4-optima\scripts\configurar_paginas_a4.py" ^
     "<ruta\archivo.xlsx>"
   ```
   (o pasar una segunda ruta para no sobreescribir el original).
3. Revisar la salida: cada hoja imprime su orientación + modo (escala %
   o fit-ancho) + tamaño de contenido.
4. Si luego se exporta a PDF, encadenar con
   [[xlsx-a4-portrait-merge-pdf]] (que ya respeta la config de página).

## Cómo depurar si falla
- **Sale muy pequeño/grande**: el contenido tiene columnas ocultas o
  filas vacías al final que agrandan el rango usado; limpiarlas y
  reejecutar.
- **`openpyxl` no instalado**: usar el venv
  `C:\Users\datos\.notebooklm-venv`.
- **Hoja con imágenes/gráficos grandes**: la medida se basa en celdas;
  revisar manualmente en Vista Previa de Excel.

## Portabilidad (revisar el 20%)
Ruta del venv, factor de conversión ancho-carácter→punto, y los límites
`SCALE_MIN/MAX` y `MARGIN_CM`. El resto (elegir orientación por
llenado) es estable.

## Relacionado
- [[xlsx-a4-portrait-merge-pdf]] — exporta el xlsx (ya con esta config) a PDF A4.
- [[xlsx-to-pdf-a4]] — variante de exportación.
- [[documentos-encuadrados-margenes]] — equivalente para Word.
- [[numeracion-paginas-informes]] — foliado de informes.
