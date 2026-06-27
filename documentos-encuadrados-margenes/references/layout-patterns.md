# Patrones de layout para los 6 tipos de documento mas usados

Cada patron especifica: orientacion recomendada, distribucion de columnas, y ratios
para usar con `distribute_widths(usable_w, ratios)`.

## 1. Memo ejecutivo (1-3 paginas)

Orientacion: **PORTRAIT**. Texto narrativo + bloques de informacion estructurada.

- Cabecera (Para/De/Asunto): tabla 2 cols, ratios `[1, 4]` (etiqueta breve | valor largo)
- Hallazgos/decisiones: tabla 2 cols, ratios `[1, 2]`
- Cierre con firma simple

## 2. Oficio de requerimiento / agenda de reunion (3-8 paginas)

Orientacion: **PORTRAIT**. Listas estructuradas + espacios para anotar respuestas.

- Identificacion de las partes: tabla 2 cols, ratios `[1, 3]`
- Hechos verificados: tabla 3 cols, ratios `[1, 8, 5]` (Ref, Hecho, Fuente)
- Discrepancias: tabla 2 cols al mismo ancho, ratios `[1, 1]` (Version A | Version B)
- Bloques de respuesta: mono-columna al ancho util
- Firmas: N=3 columnas iguales

## 3. Informe forense estructurado (10-30 paginas)

Orientacion: **PORTRAIT** salvo seccion de tablas financieras.

- Indice (TOC): mono-columna
- Capitulos: encabezado en banda + texto narrativo
- Cedulas de cuadre numerico: PUEDE necesitar LANDSCAPE en seccion dedicada
- Anexos: mono-columna

## 4. Dashboard financiero / Cedula de cuadre (1-2 paginas)

Orientacion: **LANDSCAPE**. Tablas anchas, KPI cards.

- KPI cards: tabla N x 1 (4-5 cards lado a lado), ratios `[1] * N`
- Tabla de cuadre principal: 7-10 columnas, font 7-8pt
- Notas a pie: mono-columna, font 8pt

## 5. Tabla de amortizacion / plan de pagos largo

Orientacion: **PORTRAIT** si <= 6 columnas; **LANDSCAPE** si > 6 columnas.

Estructura tipica (6 cols PORTRAIT):
- Periodo, Saldo, Capital, Interes, Cuota, Fecha
- Ratios: `[1, 2, 2, 2, 2, 2]`
- Font 8pt
- Paginacion: 50-60 filas por pagina con repeticion de cabecera

## 6. Cronologia / linea de tiempo

Orientacion: **PORTRAIT** (vertical es natural para cronologias).

- Tabla 2 cols, ratios `[1, 3]` (Fecha | Hecho)
- Cada hito en una fila
- Color de banda alternada cada 5 filas para legibilidad

## Reglas finas adicionales

| Caso | Decision |
|---|---|
| Tabla tiene una celda con texto > 60 caracteres | Aumentar el ratio de esa columna |
| Tabla con 8+ columnas en portrait | Rotar a landscape o dividir en dos tablas |
| Imagen o screenshot | Insertar con `width = usable_w_cm * 0.9` para dejar margen |
| Firmas al pie | Siempre N columnas iguales al ancho util |
| Pie de pagina con numeracion | Texto centrado, font 8pt, color GREY |
| Encabezado con logo | Imagen alineada izquierda + texto institucional derecha, ambos dentro del ancho util |

## Ejemplo minimo de uso

```python
import sys
sys.path.insert(0, r"C:\Users\datos\.claude\skills\documentos-encuadrados-margenes\scripts")
from doc_helpers import (
    PortraitDoc, add_heading_box, add_body, add_table_safe, add_callout,
    add_signature_row, distribute_widths,
    NAVY_BG, AMBAR_BG, LIGHT_BG, NAVY, GREY,
)

doc, uw = PortraitDoc()
add_heading_box(doc, "TITULO", uw, NAVY_BG, size=14)
add_body(doc, "Texto introductorio.")
add_table_safe(doc, rows=[
    ["Concepto", "Cifra", "Cita"],
    ["Saldo", "USD 1.701.058,82", "Hoja CONSOLIDADA"],
], col_widths_cm=distribute_widths(uw, [3, 2, 4]))
add_callout(doc, "Aviso importante.", uw, AMBAR_BG, NAVY)
add_signature_row(doc, ["Solicita", "Recibe", "Dispone"], uw)
doc.save("salida.docx")
```

Luego validar:

```bash
python ~/.claude/skills/documentos-encuadrados-margenes/scripts/page_layout_validator.py salida.docx
```
