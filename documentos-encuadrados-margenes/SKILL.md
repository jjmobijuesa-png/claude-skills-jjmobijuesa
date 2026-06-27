---
name: documentos-encuadrados-margenes
description: "Reglas y utilidades para que TODO documento Word o PDF generado por el sistema (memos, oficios, informes, agendas de reunión, tablas, dashboards) tenga su contenido perfectamente encuadrado dentro de los márgenes de la hoja, con tablas que NUNCA se desborden de la página. Orientación por defecto VERTICAL (portrait), salvo cuando el contenido — por número de columnas o por necesidad de visualización tipo dashboard — justifique la HORIZONTAL (landscape). Triggers: 'documento encuadrado', 'tablas dentro del margen', 'cuadros desbordados', 'ajustar al margen', 'hoja vertical', 'hoja horizontal', 'memo bien formateado', 'no se sale de la página'. Aplica a python-docx, reportlab y a cualquier generador de docs. Incluye validador que reporta tablas que se desbordan."
user-invocable: true
---

# Documentos encuadrados dentro de márgenes — Regla maestra de layout

Todo documento Word o PDF que el sistema entregue al usuario debe tener su contenido (texto, tablas, imágenes, callouts, firmas, encabezados) **completamente contenido dentro del área útil de la página**, sin desbordes horizontales ni cortes feos en impresión. La orientación por defecto es **VERTICAL (portrait)**, y la **HORIZONTAL (landscape)** se reserva para casos justificados de diseño.

## Cuándo usar VERTICAL (default)

- Memorandos, oficios, cartas, agendas de reunión
- Informes con texto narrativo dominante
- Tablas hasta **5 columnas** de texto o **3 columnas de cifras**
- Documentos pensados para **lectura humana secuencial**

## Cuándo usar HORIZONTAL (excepción justificada)

- Tablas de **6+ columnas** con cifras (ej. estados financieros comparativos multi-periodo)
- Dashboards (KPI cards lado a lado)
- Tablas de amortización, planes de pagos largos
- Cronologías visuales tipo Gantt
- Diagramas o flujos que requieren ancho
- **Mapas, planos y diagramas de proceso**

En todos los casos, **el contenido siempre dentro de los márgenes**.

## Parámetros base (A4)

```
A4 portrait:  21.0 cm x 29.7 cm
A4 landscape: 29.7 cm x 21.0 cm

Margenes default: top=2.0 / bottom=2.0 / left=2.0 / right=2.0 cm

Area util portrait:  17.0 cm ancho  x  25.7 cm alto
Area util landscape: 25.7 cm ancho  x  17.0 cm alto
```

**Regla de oro**: ningún elemento (tabla, imagen, callout) puede exceder el **ancho útil** de la orientación elegida.

## 5 reglas no negociables al construir documentos

1. **Toda tabla con anchos de columna explícitos**. Nada de `autofit = True` sin verificar — termina desbordando. Suma de columnas ≤ ancho útil.

2. **Toda tabla centrada horizontalmente**. `table.alignment = WD_TABLE_ALIGNMENT.CENTER` en python-docx; `hAlign = "CENTER"` en reportlab.

3. **Tablas de una sola columna también con ancho explícito**. Si no, ocupan todo el ancho de la sección y pueden romper la maquetación. Usar el ancho útil completo.

4. **Texto en celdas con tamaño escalado al número de columnas**:
   - ≤ 4 columnas → 10pt
   - 5-6 columnas → 9pt
   - 7-10 columnas → 8pt
   - 11+ columnas → 7pt (considerar landscape)

5. **Verificación final del documento generado** con el validador `scripts/page_layout_validator.py`, que reporta tablas y filas que se desbordan.

## Helpers Python listos para usar

Importar desde `scripts/doc_helpers.py`:

```python
from doc_helpers import (
    PortraitDoc, LandscapeDoc,
    add_table_safe, add_heading_box, add_body, add_callout, add_cita,
    USABLE_W_PORTRAIT, USABLE_W_LANDSCAPE,
    distribute_widths,
)

# Crear documento vertical con margenes encuadrados
doc, usable_w = PortraitDoc()

# Tabla con 3 columnas — los anchos se distribuyen automaticamente para sumar al ancho util
add_table_safe(doc, rows=[
    ["Concepto", "Cuantia", "Cita"],
    ["Saldo consolidado", "USD 1.701.058,82", "Hoja CONSOLIDADA, 10-may-2023"],
    ...
], col_widths_cm=distribute_widths(usable_w, ratios=[3, 2, 4]), header_bg="1F2A44")
```

El helper `distribute_widths` calcula anchos exactos en cm que **suman al ancho útil**, dadas razones relativas.

## Validador post-generación

```bash
python ~/.claude/skills/documentos-encuadrados-margenes/scripts/page_layout_validator.py archivo.docx
```

Reporta:
- Anchura física de cada tabla vs. ancho útil de la sección
- Tablas con `autofit=True` (red flag)
- Tablas sin centrar
- Tablas que exceden el ancho útil
- Recomendación: rotar a landscape si > 80% de tablas exceden portrait

## Archivos del skill

- `scripts/doc_helpers.py` — utilidades Python: `PortraitDoc`, `LandscapeDoc`, `add_table_safe`, `add_heading_box`, `add_body`, `add_callout`, `add_cita`, `distribute_widths`, paleta de color institucional
- `scripts/page_layout_validator.py` — validador que escanea un `.docx` y reporta desbordes
- `references/layout-patterns.md` — patrones de layout para los 6 tipos de documento más usados (memo, oficio, agenda, informe, dashboard, cédula numérica)

## Por qué este skill existe

Surge de una iteración del expediente forense EPACEM en la que un documento generado con tablas de columnas explícitas (que matemáticamente sumaban al ancho útil) terminó con cuadros visualmente desbordados al abrirse en Word. La regla pasó de "los anchos suman" a "los anchos suman, las tablas se centran, y un validador independiente lo confirma antes de entregar".
