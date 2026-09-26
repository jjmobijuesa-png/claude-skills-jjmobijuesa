---
name: excel-macro-vba-embebido-gui
description: >
  Incrusta una macro VBA REAL dentro de un libro de Excel en ESTE computador,
  donde el acceso programático al proyecto VBA está bloqueado por Office.
  Incluye la escalera de diagnóstico (AccessVBOM, políticas, VBE7.DLL, versión
  C2R), el hallazgo clave (Alt+F11 SÍ funciona pero el editor abre en el otro
  monitor y parece "no hacer nada"), el procedimiento GUI que sí funciona
  (Insertar→Módulo + pegar + compilar + guardar), la trampa de escalado DPI que
  desvía los clics, y cómo verificar el resultado sin abrir el editor.
  Disparadores: "hazme una macro en Excel", "el botón no ejecuta nada",
  "Alt+F11 no funciona", "no me deja importar el .bas", "automatiza esta hoja".
---

# Macro VBA incrustada en Excel por GUI (cuando el acceso programático está bloqueado)

## 0. Regla de oro

En este computador **NO se puede inyectar VBA por código**. Cualquier intento con
`wb.VBProject.VBComponents.Import/Add` falla con:

> «El acceso mediante programación al proyecto de Visual Basic no es de confianza.»

Esto **no se arregla con el registro**. Ya está comprobado (2026-07-24):

| Comprobación | Resultado |
|---|---|
| `HKCU\...\Office\16.0\Excel\Security\AccessVBOM` | **= 1** (vista 32 y 64 bits) |
| Claves de directiva (`Policies`, HKCU y HKLM) | **inexistentes** |
| Motor VBA `VBE7.DLL` / `VBEUI.DLL` | **instalado** |
| Prueba en libro NUEVO, Excel recién lanzado | **bloqueado igual** |
| Prueba **fuera del sandbox** (`dangerouslyDisableSandbox`) | **bloqueado igual** |

Office aquí es **2019 ProPlus Retail, Click-to-Run, x86, build 16.0.20131.20154**
y deniega el acceso en tiempo de ejecución. **No pierdas tiempo con el registro.**

## 1. El hallazgo que desbloquea todo

**Alt+F11 SÍ abre el editor VBA. Lo que pasa es que la ventana aparece en el OTRO
monitor**, fuera de la vista del usuario — por eso parece que "no hace nada" y por
eso «no aparece el diálogo de importar».

Comprobarlo sin screenshots (barato y definitivo): enumerar ventanas del proceso
EXCEL y buscar la clase **`wndclass_desked_gsk`** (ésa es la ventana del VBE):

```powershell
# ver scripts/vbe_window.ps1  -> Find / Move / Force
[W]::Go((Get-Process EXCEL).Id)   # lista clase | visible | título
```

Si aparece `wndclass_desked_gsk | vis=True | Microsoft Visual Basic para Aplicaciones - <libro>`
→ el editor está abierto y solo hay que traerlo a la vista.

## 2. Procedimiento que funciona (probado de punta a punta)

1. **Abrir el libro** lanzando `EXCEL.EXE` con la ruta como argumento
   (`Start-Process`), fuera del sandbox. Verificar con `Get-Process EXCEL`.
2. **Pedir control**: `request_access` con `["Excel"]` + `clipboardWrite`.
   El VBE pertenece al mismo proceso EXCEL.EXE, así que **queda cubierto por la
   misma concesión**.
3. **Abrir el VBE**: `Alt+F11` con Excel al frente.
4. **Traer el VBE a la vista**: `MoveWindow` + `SetForegroundWindow`
   (usar `AttachThreadInput`, ver §4).
5. **Cargar el código al portapapeles** — NO tecleado, pegado:
   ```powershell
   $c = (Get-Content $bas -Raw) -replace '(?m)^Attribute VB_Name.*\r?\n',''
   Set-Clipboard -Value $c
   ```
   Quitar la línea `Attribute VB_Name` (sirve para importar, **rompe al pegar**).
6. **Insertar módulo por TECLADO** (evita el desfase de clics):
   `Alt+I` → menú Insertar → tecla `M` (Módulo).
   El cursor queda dentro de la ventana de código nueva.
7. **Pegar**: `Ctrl+V`.
8. **Compilar**: `Alt+D` → `Enter` (queda resaltado «Compilar VBAProject»).
   **Si no aparece ningún diálogo, compiló limpio.**
9. **Guardar**: `Ctrl+S`. No pide nada si el libro ya es `.xlsm`.

## 3. Verificación (sin volver a abrir el editor)

**a) ¿Quedó la macro dentro del archivo?** Inspeccionar el ZIP del `.xlsm`:

```powershell
Add-Type -AssemblyName System.IO.Compression.FileSystem
$z=[IO.Compression.ZipFile]::OpenRead($f)
$z.Entries | Where-Object { $_.FullName -like "*vbaProject.bin*" }
```
Si aparece `xl/vbaProject.bin` con decenas de KB → **la macro está incrustada de
forma permanente**. Éste es el criterio de éxito definitivo.

**b) ¿Produce los números correctos?** Leer las celdas por COM —
`GetActiveObject("Excel.Application")`. **Ejecutar macros por COM NO está
bloqueado** (`$xl.Run("MiMacro")`), solo lo está tocar el VBProject.
⚠️ Si la macro termina en `MsgBox`, `$xl.Run` **se queda colgado** hasta que
alguien cierre el aviso: lanzarla en proceso aparte o pulsar el botón por GUI.

**c) Validar la lógica** contra un equivalente en Python sobre los mismos datos.
La macro es correcta cuando ambos dan la misma cifra.

## 4. Trampas conocidas (todas verificadas en vivo)

| Trampa | Síntoma | Solución |
|---|---|---|
| **VBE en otro monitor** | Alt+F11 «no hace nada» | Buscar `wndclass_desked_gsk` y moverla |
| **Escalado DPI** | Los clics caen ~50 px a la derecha / ~60 px arriba | El monitor **primario 1536×864 tiene escalado**; el **LG 1366×768 (X=1920) responde exacto**. Mover ahí la ventana objetivo, o **manejar todo por teclado** |
| **Robo de foco** | `FAILED — desktop shell is frontmost` / `Msedge ... tier read` | Reenfocar con `AttachThreadInput` + `BringWindowToTop` + `SetForegroundWindow` antes de CADA lote |
| **Pegado que no entra** | El código no cambia y no hay error | El clic no dio foco a la ventana de código. **Verificar el cambio antes de dar por hecho el pegado** |
| **Ctrl+F4** | Cierra el LIBRO si el foco está en Excel | No usarlo para cerrar ventanas del VBE |
| **`.bas` con acentos** | Caracteres corruptos al importar | Escribir el módulo en **ASCII puro** (sin tildes ni `°`) |
| **Excel colgado** | `RPC_E_CALL_REJECTED`, 0 libros | Matar el proceso y relanzar; el archivo en disco está a salvo |

## 5. Diseño del módulo VBA (lecciones)

- **Preservar** título, encabezados y explicaciones que hizo el usuario: limpiar
  SOLO el rango de datos (`B4:L20000`), nunca `Cells.Clear`. Así los encabezados
  con acentos sobreviven aunque el `.bas` sea ASCII.
- **Ancho de columna**: un rótulo largo en una columna angosta se ve cortado si la
  celda vecina tiene contenido. Colocar los rótulos de paneles en la columna
  ancha (la de nombres), no en la del consecutivo.
- Dejar **fórmulas vivas** (no valores) para que el usuario ajuste la tasa y
  recalcule sin re-ejecutar.
- Terminar con `MsgBox` de resumen: es la confirmación visible de que corrió.
- `Application.ScreenUpdating/Calculation = manual` al entrar y restaurar en
  `CleanExit:` **y** en el manejador `ErrH:`.

## 6. Caso de referencia

`MACRO - Resumen del control semanal de cartera QVP.xlsm`
(`...\1 WAR ROOM QVP\Plan de Negocios 2-0\Cartera Vencida QVP`).
Módulo `mCartera` → `Sub ActualizarResumen`. Mina la hoja **Base** (export XASS)
y llena **Resumen de Cartera** con 156 clientes + aging + concentración.
Resultado validado: cartera **8.290.839,59** (coincide con el `TOTAL GENERAL` que
trae la propia base), costo crédito 249.963,90, vencido 1.810.250,60, costo mora
124.168,41, DISEBAJ 59,4%.

Relacionado: [[agente-gui-autoaprobado-windows]], [[ui-tars-desktop-control-local]],
[[control-financiero-semanal-qvp]], [[excel-pagina-a4-optima]].
