---
name: xlsx-a4-portrait-merge-pdf
description: |
  Limpia uno o varios libros de Excel (.xlsx) y los convierte en UN SOLO PDF en
  formato A4 VERTICAL (retrato), uniendo todas las hojas en el orden indicado y
  ajustando cada columna para que el texto se lea a lo ancho de la hoja y los
  cuadros queden encuadrados dentro del A4. Antes de exportar, retira emoticones
  y diseños tipo imagen (pictogramas, formas, fotos) que restan profesionalismo,
  elimina residuos de IA (preámbulos "Aquí tienes un ejemplo...", preguntas
  finales "¿Quieres que genere...?", etiquetas de fuente tipo [grepalma]) y deja
  el documento con redacción humana y sobria. Usa el motor nativo de Excel (COM)
  para máxima fidelidad de página y exporta a PDF, luego fusiona con pypdf.
  Triggers: "convertir Excel a PDF A4 vertical", "unir hojas de Excel en un solo
  PDF", "quitar emojis del Excel y pasar a PDF", "subir Excel a NotebookLM"
  (NotebookLM no acepta xlsx), "excel a PDF retrato encuadrado", "merge xlsx to
  single A4 portrait PDF".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-03
  engine: Excel COM (win32com) + pypdf
  plataforma: Windows con Microsoft Excel instalado
---

# Skill `xlsx-a4-portrait-merge-pdf`

## Propósito

Convertir libros de Excel en un **único PDF A4 vertical, profesional y legible**,
listo para imprimir, firmar o subir a sistemas que rechazan `.xlsx` (NotebookLM).
A diferencia de `xlsx-to-pdf-a4` (que produce un PDF horizontal por hoja), esta
skill:

1. Trabaja en **A4 retrato (vertical)**.
2. **Une todas las hojas / todos los libros en un solo PDF** en el orden pedido.
3. **Limpia** el contenido antes de exportar (emojis, formas/imágenes, residuos
   de IA, etiquetas de fuente).
4. **Encuadra** cada hoja: autoajusta columnas, limita el ancho de columnas de
   texto y activa ajuste de línea para que nada se corte, y aplica
   `FitToPagesWide = 1` para que el cuadro entre perfecto en el ancho del A4.

## Requisitos

- Windows con **Microsoft Excel** instalado (se usa vía COM).
- Python con `pywin32` y `pypdf`:
  ```bash
  pip install pywin32 pypdf
  ```

## Qué produce

- Un PDF fusionado en la ruta `--out`.
- (Opcional) Copias `.xlsx` ya limpias en `--cleaned-dir`, una por libro de
  entrada, con el sufijo ` (limpio)`.

## Uso

```bash
python scripts/xlsx_to_a4_pdf.py ^
  --inputs "C:\ruta\A.xlsx;C:\ruta\B.xlsx;C:\ruta\C.xlsx" ^
  --out "C:\ruta\salida\DOCUMENTO_UNIFICADO.pdf" ^
  --cleaned-dir "C:\ruta\salida" ^
  --replacements "C:\ruta\replacements.json" ^
  --maxw 48 ^
  --orientation portrait
```

- `--inputs`: libros en el **orden exacto** en que deben aparecer en el PDF,
  separados por `;`.
- `--maxw`: ancho máximo (en caracteres) de cualquier columna; si una columna es
  más ancha, se recorta a ese valor y se activa ajuste de línea (wrap). Default 48.
- `--replacements` (opcional): JSON con reemplazos puntuales por celda para
  limpiar residuos de IA. Formato:
  ```json
  {
    "B.xlsx": { "B2": "Texto profesional de entrada.", "B275": "__CLEAR__" }
  }
  ```
  El valor `"__CLEAR__"` vacía la celda. Las claves son nombres de archivo
  (basename) y direcciones de celda absolutas (p.ej. `B2`).

## Limpieza automática (sin configuración)

En cada celda de texto se aplica:

- **Emojis / pictogramas fuera**: rangos Unicode `1F000–1FAFF`, `2600–27BF`,
  `2B00–2BFF`, selectores de variación `FE00–FE0F` y relojes `231A–231B` /
  `23E0–23FF`. Se **conservan** el guion largo `—` y la flecha `→` por ser
  tipografía legítima.
- **Etiquetas de fuente** tipo `[grepalma]`, `[es.trackingtime]`,
  `[ecuador.pochteca]` (corchete con minúsculas/puntos) → se eliminan. **No** se
  tocan corchetes con mayúsculas o espacios (`[ÁREA: ...]`, `[ ]`, `[LEER ...]`).
- **Espacios dobles** colapsados y recorte de extremos.
- **Formas e imágenes**: se borran todas las `Shapes` de cada hoja.

## Encuadre A4 (page setup aplicado por hoja)

- `Orientation = xlPortrait (1)`, `PaperSize = xlPaperA4 (9)`.
- `Zoom = False`, `FitToPagesWide = 1`, `FitToPagesTall = False` (fluye en alto).
- Autoajuste de columnas → recorte a `maxw` + wrap → autoajuste de filas.
- Márgenes 0.4" laterales / 0.5" sup-inf, `CenterHorizontally = True`,
  `PrintGridlines = False`.

## Fusión

Se exporta cada libro a un PDF temporal con `Workbook.ExportAsFixedFormat` y se
fusionan en orden con `pypdf.PdfWriter`. El resultado es un único documento
continuo.

## Límites

- Requiere Excel (no LibreOffice). Si Excel no está, falla.
- Las celdas con "tablas markdown" (pipes `|`) se respetan tal cual; esta skill
  no reconstruye tablas markdown a celdas reales.
- Fórmulas: se exporta el último valor calculado por Excel.

## Archivos

- `scripts/xlsx_to_a4_pdf.py` — el conversor (limpieza + page setup + export + merge).
