---
name: numeracion-paginas-informes
description: |
  Convención obligatoria de NUMERACIÓN DE PÁGINAS para TODO informe formal que genere el sistema
  (Word/DOCX, PDF de informe). Regla: el número va en la parte INFERIOR DERECHA; la numeración empieza
  a MOSTRARSE desde la página 2; la página 1 (portada / títulos) SÍ cuenta en la secuencia pero NO
  muestra su número. Así, la página 2 muestra «2», la 3 «3», etc. Aplica a python-docx, reportlab y a
  cualquier generador de documentos de informe.
  Triggers: "numerar las páginas del informe", "pie de página con número", "numeración secuencial",
  "página sin número en la portada", "foliar el informe".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-28
  origen: instrucción del usuario sobre el Informe Extendido del CEO (Quevepalma)
  relacionada: documentos-encuadrados-margenes
---

# Skill `numeracion-paginas-informes`

Regla de oro para todo informe formal: **numeración inferior derecha, visible desde la página 2; la
portada cuenta pero no muestra el número.**

## Especificación
- Posición: **pie de página, alineado a la derecha**.
- La **página 1** (portada / títulos) **no muestra** número (footer de primera página vacío).
- Desde la **página 2** se muestra el número correlativo real (2, 3, 4, …) — *no* se reinicia el conteo.
- Fuente discreta (gris, ~9 pt). Nada de "Página X de Y" salvo que se pida.

## Receta python-docx (probada)
```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

sec = doc.sections[0]
sec.different_first_page_header_footer = True          # portada con footer propio (vacío)
fp = sec.footer.paragraphs[0]; fp.alignment = AL.RIGHT  # footer normal, a la derecha
run = fp.add_run()                                      # campo PAGE
f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin')
it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = "PAGE"
f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'end')
run._r.append(f1); run._r.append(it); run._r.append(f2)
sec.first_page_footer.paragraphs[0].text = ""           # portada sin número
```
Word recalcula el campo PAGE al abrir; al exportar a PDF (Word COM FileFormat=17) queda fijado.

## Receta reportlab
En `onPage`/`canvas`: si `doc.page == 1` no dibujar; si `doc.page >= 2`,
`canvas.drawRightString(ancho - margen_der, margen_inf/2, str(doc.page))`.

## Verificación
Renderizar el PDF (fitz) y confirmar visualmente que la página 1 NO trae número y la 2 trae «2» abajo
a la derecha. Caso de referencia: `Informe Extendido del CEO - Quevepalma 2.0 (INTEGRAL).docx/pdf`.

> Es una convención de presentación; combínala con [[documentos-encuadrados-margenes]] (tablas dentro
> del margen) en todo informe.
