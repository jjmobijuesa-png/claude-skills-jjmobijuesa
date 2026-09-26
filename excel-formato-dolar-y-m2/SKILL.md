---
name: excel-formato-dolar-y-m2
description: >
  Formato monetario y de área uniforme en libros Excel vía COM (pywin32): dinero
  con signo $ y dos decimales, y las áreas con la unidad " m²" visible, más ancho
  de columnas proporcional al contenido. Úsala siempre que haya que dar formato a
  cifras en dólares o metros cuadrados en un .xlsx, o mantener ese criterio al
  crear o editar hojas. Resuelve el error frecuente de que $#,##0.00 salga mal.
metadata:
  type: reference
---

# Formato $ y m² uniforme en Excel (COM)

**Criterio de la casa (Francisco Duque):** en TODO libro financiero, el dinero se
muestra con **signo `$`, separador de miles y dos decimales**; las **áreas** llevan
la unidad **`m²`** visible; y el **ancho de cada columna es proporcional a su
contenido** (autoajuste, sin que un texto largo la ensanche).

## La trampa que cuesta tiempo (léela antes de tocar `NumberFormat`)

En esta instalación (Office es-EC), la propiedad **`.NumberFormat` interpreta los
separadores en el sentido LOCAL español**: el punto es miles y la coma es decimal.
Por eso `"$#,##0.00"` se corrompe y sale `$100428,44016`. **Solución:** escribir el
patrón con separadores españoles y asignarlo por **`.NumberFormatLocal`**:

```python
MONEY = "$#.##0,00;[Rojo]-$#.##0,00"   # → $1.234,56 ; negativos en rojo
M2    = '#.##0,00" m²"'                 # → 1.234,56 m²
celda.NumberFormatLocal = MONEY         # NUNCA .NumberFormat aquí
```

Verificación barata (formulable en una línea antes de dar por bueno el pase):
`rng.NumberFormatLocal` debe devolver `$#.##0,00;[Rojo]-$#.##0,00` y `rng.Text`
algo como `$3.375.263,55`. Si ves `$#,##000` o cinco decimales, quedó en local mal.
El token de color va en español: `[Rojo]`, no `[Red]`.

## Qué celdas son dinero y cuáles son área

No fiarse del encabezado por texto: las fórmulas que citan la hoja «5-ÁREAS»
contienen la palabra «área» y contaminan cualquier detector por palabra clave.
Regla robusta en dos capas:

1. **Regla del `$` (todo el libro):** con **openpyxl** (lectura rápida) recoger las
   coordenadas de toda celda cuyo `number_format` ya contenga `$` y no contenga `%`.
   Esas son dinero seguro → estandarizarlas a `MONEY`. Repara de paso cualquier
   formato viejo inconsistente (`$#,##0`, contable, etc.).
2. **Mapas explícitos por columna/banda** para las celdas monetarias o de área que
   aún NO llevan `$` (p. ej. tasas $/m², áreas). Definir por hoja las columnas
   dólar y las columnas m² y aplicarlas a la banda de datos. En hojas de
   presupuesto el patrón típico es: `D,E` = m² (Cantidad/Área) y `F` en adelante =
   dinero; `C` = unidades (entero); columnas de ratio/`%` se dejan.

Los porcentajes (`%` en el formato) NO se tocan.

## Ancho proporcional sin que el texto largo mande

`WrapText=True` en las celdas de texto largo (títulos, MAPA DE VÍNCULOS, notas)
**antes** de autoajustar: el autoajuste de columna ignora las celdas ajustadas, así
mide solo el contenido corto. Luego `ws.Columns.AutoFit()`, se **acota** el ancho a
`[5, 44]` y `ws.Rows.AutoFit()` crece el alto de las filas con texto envuelto.

## Pila COM segura (idéntica al resto de skills de Excel)

- `xl = win32com.client.DispatchEx("Excel.Application")` — **instancia propia**;
  nunca `EnsureDispatch` (engancha el Excel del usuario y al `Quit()` se lo cierra).
- `xl.Visible=False; xl.DisplayAlerts=False`; `try/finally` que cierra los libros
  sin guardar y hace `xl.Quit()`; verificar que no quede `EXCEL.EXE` huérfano.
- **Respaldo antes de escribir** en `_Versiones anteriores (MUPI 2023)\… - respaldo
  pre-<paso> <timestamp>.xlsx`. Comprobar bloqueo `~$` (¡ojo! el `~$` de un `.docx`
  abierto NO bloquea el `.xlsx`).
- **Unión de rangos:** `ws.Range("A1,B2,…")` tiene un tope de ~255 caracteres de
  dirección. Trabajar en fragmentos de **≤12 coordenadas** con reintento celda por
  celda si el fragmento falla.
- Escribir con COM (no openpyxl) para **preservar imágenes y gráficos** (openpyxl
  los elimina al guardar).

## Snippet reutilizable

```python
import os, shutil, datetime, openpyxl, win32com.client as w32
MONEY = "$#.##0,00;[Rojo]-$#.##0,00"; M2 = '#.##0,00" m²"'
def chunks(s,n):
    for i in range(0,len(s),n): yield s[i:i+n]
def apply_coords(ws, coords, fmt):
    for ch in chunks(coords,12):
        try: ws.Range(",".join(ch)).NumberFormatLocal = fmt
        except Exception:
            for a in ch:
                try: ws.Range(a).NumberFormatLocal = fmt
                except Exception: pass
# 1) openpyxl: recoger celdas con $ (dinero) y textos largos (wrap)
# 2) DispatchEx: wrap → regla del $ → mapas explícitos $/m² → AutoFit+clamp[5,44]+Rows.AutoFit
```

Skills hermanas: [[xlsx-a4-portrait-merge-pdf]], [[excel-pagina-a4-optima]],
[[excel-macro-vba-embebido-gui]]. Constitución COM y respaldos: ver la memoria del
proyecto San Sebastián. Ante cualquier fallo, [[regla-del-primer-tropiezo]].
