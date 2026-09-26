---
name: impresion-local-hp-diagnostico
description: |
  Diagnostica, repara e IMPRIME en la impresora local de este
  computador. La impresora física es la **HP Smart Tank 585**,
  registrada en Windows como `HPC4225C (HP Smart Tank 580-590 series)`
  — es la PREDETERMINADA, conectada por **puerto WSD** con el **driver
  genérico Microsoft IPP Class Driver** (esa combinación es la causa
  habitual de fallos: deja "trabajos zombi" en la cola).

  Cubre: (1) diagnóstico de impresoras/cola/spooler, (2) impresión de
  Excel por COM, (3) **impresión de documentos largos a DOBLE CARA con
  dúplex manual en dos pasadas controladas** (docx y PDF), (4) limpieza
  de trabajos zombi, (5) pausar/reanudar la impresora.

  El usuario concedió **acceso total autorizado** para revisar,
  diagnosticar y reparar la impresión (2026-07-24). Ampliada con la
  campaña de impresión del libro «Ingeniería de la consciencia»
  (2026-08-04/05), que costó ~10 hojas de aprendizaje.

trigger_phrases:
  - "no imprime / problemas para imprimir"
  - "imprime este Excel / estas hojas / este PDF"
  - "imprime el libro a doble cara"
  - "revisa la impresora / la cola de impresión"
  - "trabajo atascado en la cola / purga la cola"
  - "HP Smart Tank / impresora local"

idioma_de_salida: español
nivel: aplicada
dominio: operaciones / impresión Windows
metadata:
  version: 2.2
  fecha: 2026-09-22
  impresora_fisica: HP Smart Tank 585
  impresora_windows: "HPC4225C (HP Smart Tank 580-590 series)"
  puerto: WSD · driver Microsoft IPP Class Driver
  scripts:
    - scripts/diagnostico_impresora.ps1
    - scripts/imprimir_hojas_excel.ps1
  relacionada:
    - excel-pagina-a4-optima
    - xlsx-a4-portrait-merge-pdf
    - agente-gui-autoaprobado-windows
---

# Skill `impresion-local-hp-diagnostico`

## 🔌 PRE-CHEQUEO DE CONEXIÓN (obligatorio antes de imprimir)

Francisco a veces trabaja **fuera de la red compartida** de la impresora (la HP está
en otra red Wi-Fi / conexión compartida). **Antes de cualquier envío a impresión**,
verificar que la impresora esté en línea; **si no lo está, OMITIR la impresión y
CONTINUAR** con el resto de la tarea, avisándolo en una línea. Nunca bloquear el
trabajo por falta de impresora, ni encolar trabajos que quedarán zombis.

Comprobación barata (PowerShell), formulable en una línea antes de imprimir:

```powershell
$p = Get-Printer -Name "HPC4225C (HP Smart Tank 580-590 series)" -ErrorAction SilentlyContinue
if ($null -eq $p) { "SIN IMPRESORA (omitir impresión)" }
elseif ($p.PrinterStatus -ne 'Normal' -and $p.PrinterStatus -ne 'Idle') { "IMPRESORA NO DISPONIBLE: $($p.PrinterStatus) (omitir)" }
else {
  # confirmar alcance del puerto WSD/host (si es de red)
  $port = (Get-PrinterPort -Name $p.PortName -ErrorAction SilentlyContinue)
  "IMPRESORA LISTA"
}
```

Regla: si el resultado no es «IMPRESORA LISTA», **no se imprime**: se guarda el PDF/
archivo listo para imprimir, se le dice al usuario «no hay conexión con la HP, dejo el
archivo listo y sigo», y se continúa. Señal típica de estar fuera de red: el usuario
dice «estoy fuera de conexión / fuera de la red compartida / con la impresora». Ver
también [[cierre-verificado-integridad]] (omitir un paso no debe frenar el resto).

## 🐌 EXCEL SE CUELGA con la HP (WSD) offline como predeterminada (2026-09-22)

**Síntoma:** al abrir/editar/exportar un libro, Excel **no responde, sube la latencia y se
inhibe**. Causa raíz: la **HP está como impresora PREDETERMINADA en un puerto WSD**
(`WSD-8688316b-…`) y, con Francisco fuera de la red de la impresora, cada operación que
consulta el driver (abrir, `PageSetup`, `ExportAsFixedFormat`, vista de saltos de página,
incluso ciertos recálculos) **espera el timeout del WSD** → cuelgue.

⚠️ **Trampa de diagnóstico:** `Win32_Printer` (WMI) reporta la HP como `PrinterStatus =
Normal` y `Default = TRUE` **aunque no exista físicamente** (estado WSD cacheado). No
fiarse de WMI. Lo que de verdad usan las apps es `GetDefaultPrinter` (registro
`HKCU\…\Windows\Device`), que se lee con .NET:
```powershell
Add-Type -AssemblyName System.Drawing
(New-Object System.Drawing.Printing.PrinterSettings).PrinterName   # lo que ve Excel
```

**Arreglo de raíz (reversible) — dejar de apuntar a la HP mientras esté fuera de alcance:**
```powershell
# 1) Que Windows NO administre la predeterminada (si no, revierte el cambio)
Set-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Windows" `
  -Name LegacyDefaultPrinterMode -Value 1 -Type DWord
# 2) Predeterminada -> impresora VIRTUAL siempre disponible (instantánea, sin red)
(New-Object -ComObject WScript.Network).SetDefaultPrinter("Microsoft Print to PDF")
# 3) Verificar con la API real (NO con WMI):
Add-Type -AssemblyName System.Drawing; (New-Object System.Drawing.Printing.PrinterSettings).PrinterName
```
Revertir cuando la HP vuelva a la red: `SetDefaultPrinter("HPC4225C (HP Smart Tank 580-590 series)")`.

**En automatización COM:** fijar `xl.ActivePrinter` a la virtual ANTES de abrir el libro
o tocar `PageSetup`, para que la instancia nunca consulte el WSD. Y **no correr COM de
Excel en paralelo con faster-whisper**: whisper con `cpu_threads=os.cpu_count()` satura los
núcleos y mata de hambre a Excel (parece cuelgue y es contención de CPU). Serializar.

**Disparador concreto en una hoja — «Esperando conexión de impresora» (2026-09-22):** una
hoja guardada en **Vista previa de salto de página** (`ActiveWindow.View = 2`,
xlPageBreakPreview) hace que Excel **consulte la impresora cada vez que se activa** para
dibujar los saltos → aparece el cuadro «Esperando conexión de impresora / Espera la
conexión de la impresora o cancela la conexión» y la hoja no se puede ver. Pasó en la hoja
NORMATIVA MIT. **Reparación:** activar la hoja y `xl.ActiveWindow.View = 1` (xlNormalView),
guardar. Conviene pasar TODAS las hojas a Normal. Diagnóstico por COM: activar cada hoja y
leer `xl.ActiveWindow.View` (2 = culpable).

⚠️ **Fijar la predeterminada que Excel respeta:** `WScript.Network.SetDefaultPrinter` y
`rundll32 printui` NO bastan (Excel siguió viendo la HP; el default de WMI no cambiaba). Lo
que SÍ funciona es el método canónico de WMI:
`Invoke-CimMethod -InputObject (Get-CimInstance Win32_Printer -Filter "Name='Microsoft Print to PDF'") -MethodName SetDefaultPrinter`.
Verificar lanzando un Excel fresco y leyendo `xl.ActivePrinter` (debe decir «Microsoft Print
to PDF en Ne00:»). No editar a mano el puerto del registro `…\Windows\Device` (romper el
alias `Ne00:` deja a Excel sin resolver el default y revierte a la HP).

⚠️ **Impresora guardada DENTRO del .xlsx:** cada hoja guarda su `printerSettings` en
`xl/printerSettings/*.bin`; al abrir, Excel los resuelve y **se cuelga en el WSD de la HP**
aunque el default ya sea la virtual. Quitarlos SIN abrir Excel (rápido, sin riesgo para
imágenes/pivots) con cirugía de zip: eliminar `xl/printerSettings/`, quitar las
`<Relationship … printerSettings…/>` de `xl/worksheets/_rels/sheetN.xml.rels` y el
` r:id="…"` de `<pageSetup>` en `xl/worksheets/sheetN.xml`; validar con openpyxl. Resultado
medido: apertura de **>110 s (colgado) → 1,7-2,4 s**.

Regla operativa: **solo referirse a la HP cuando (a) Francisco dé la orden explícita de
imprimir Y (b) el PRE-CHEQUEO diga «IMPRESORA LISTA».** En cualquier otro caso la HP no se
menciona ni se consulta; la predeterminada vive en la virtual.

## 📄 EXPORTAR A PDF ≠ IMPRIMIR (regla de Francisco, 2026-09-22)

**Exportar una hoja/documento a PDF NO usa la impresora ni necesita conexión.** La
impresora física **solo entra cuando el usuario da la orden explícita de imprimir** — y
solo entonces corre el PRE-CHEQUEO de arriba. Para entregar «la hoja lista en A4», el
camino correcto es: **configurar el PageSetup de la hoja en A4 dentro de Excel y exportar
a PDF** (`Worksheet.ExportAsFixedFormat(0, ruta)`), sin tocar la cola ni el spooler.

🚦 **Trampa: `ExportAsFixedFormat` toma el tamaño de papel del DRIVER, no del PageSetup.**
Aunque se fije `PageSetup.PaperSize = 9` (xlPaperA4) y el *readback* devuelva `9`, con la
HP predeterminada (default **Letter**) el PDF sale **Carta (792×612 pt)**, no A4. No es
que falle el ajuste: el motor PDF de Excel usa la forma por defecto del driver. **No
cambiar el default de la impresora del usuario** para arreglarlo (es config persistente
suya).

✅ **Solución no invasiva — reencuadrar a A4 real con PyMuPDF** (vectorial, sin
rasterizar; conserva texto nítido). A4 apaisado = 842×595 pt; A4 vertical = 595×842:

```python
import fitz, shutil
shutil.copy2(pdf_carta, tmp_local)          # G:→C: no permite os.replace entre unidades
src=fitz.open(tmp_local); out=fitz.open()
A4W,A4H=842.0,595.0                          # apaisado (vertical: 595,842)
for i in range(src.page_count):
    r=src[i].rect; s=min(A4W/r.width, A4H/r.height)
    w,h=r.width*s, r.height*s; x0=(A4W-w)/2; y0=(A4H-h)/2
    out.new_page(width=A4W,height=A4H).show_pdf_page(fitz.Rect(x0,y0,x0+w,y0+h), src, i)
out.save(pdf_a4, deflate=True)
```

Igual dejar el PageSetup de la hoja en A4 y **guardar** el libro: así, cuando llegue la
orden real de imprimir, la hoja ya está configurada. Verificar el PDF con
`fitz.open(p)[0].rect` (debe dar 842×595). Config de página robusta: envolver cada
asignación de `PageSetup` en try/except (con la impresora offline algunas propiedades
lanzan); `FitToPagesWide=1`, `Zoom=False`, `PrintArea` explícita, `PaperSize=9`,
`Orientation=2`.

## La impresora

| | |
|---|---|
| Nombre físico | **HP Smart Tank 585** |
| Nombre en Windows | `HPC4225C (HP Smart Tank 580-590 series)` |
| Predeterminada | **Sí** |
| Puerto | **WSD** · Driver **Microsoft IPP Class Driver** (genérico) |
| Visor PDF disponible | **Adobe Acrobat DC** en `C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe` |

---

# 🔴 LAS SEIS LEYES (aprendidas a golpes, 2026-08-05)

### 1. CONGELAR EL ARCHIVO cuando empieza a salir papel
**El error más caro de toda la campaña.** Se corrigió el documento (mover el back
matter al final) *después* de haber impreso una cara del bloque. Eso desplazó la
paginación **una página** y dejó el bloque inservible para la segunda pasada.
👉 **Una vez que sale la primera hoja, el archivo NO se toca.** Toda mejora espera al
siguiente tiraje. Si hay que corregir, se reimprime desde cero.

### 2. NO suponer que el driver invierte el orden — CONSULTARLO
Se dio por hecho que el driver invertía porque una vez salió la 176 primero. **Falso.**
La configuración real decía `psk:JobPageOrder = Standard` (orden normal); lo que
confundía era **el apilado del bloque**, no la impresora.
```powershell
$xml = [xml](Get-PrintConfiguration -PrinterName $p).PrintTicketXML
$ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
$ns.AddNamespace("psf","http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework")
$xml.SelectSingleNode("//psf:Feature[@name='psk:JobPageOrder']", $ns).OuterXml
```
👉 **Solución definitiva: hornear el orden DENTRO del PDF** (ver §Receta). Así no
depende de ningún ajuste del driver ni de la app.

### 3. VERIFICAR EL TAMAÑO DE PAPEL
La impresora estaba en **Letter** con un documento **A4** (1,8 cm menos de alto): se
come el pie de página y el número.
```powershell
(Get-PrintConfiguration -PrinterName $p).PaperSize     # ¡mirar SIEMPRE!
Set-PrintConfiguration -PrinterName $p -PaperSize A4 -DuplexingMode OneSided
```

### 4. El DÚPLEX AUTOMÁTICO DEL DRIVER ABANDONA a media obra
Con `-DuplexingMode TwoSidedLongEdge`, el driver imprime la **primera cara de todas
las hojas** y luego **deja el trabajo muerto**: la cola se vacía, Word se cierra y la
segunda cara nunca se encola.
👉 **Tomar el control: dos pasadas propias a una sola cara.**

### 5. CALIBRAR CON 1–2 HOJAS antes del lote
Nunca mandar 88 hojas sin probar. Una hoja cuesta una hoja; equivocarse cuesta el
bloque entero. Protocolo en §Calibración.

### 6. VERIFICAR CONTRA EL PAPEL, no contra la teoría
Todas las cagadas vinieron de razonar sobre cómo *debería* apilarse el papel. El único
dato válido es **lo que el usuario ve en la hoja**. Pedirlo con marcadores concretos
(primera línea del texto, número al pie), no con jerga.

### 7. NORMALIZAR EL LIENZO de todo PDF ESCANEADO (2026-09-06)
Un PDF escaneado trae **cada página de un tamaño distinto** (595×842, 595×824,
583×842…). Una medida **no estándar** hace que esta impresora expulse la hoja
**con solo una esquina impresa**. Siempre la misma página, siempre el mismo corte.
No es el peso, ni un JPEG progresivo, ni un archivo dañado: se comprobaron las tres
y las tres fallaron.
👉 **Normalizar a A4 exacto ANTES de imprimir, sin intentar adivinar qué página
fallará** — el criterio no es predictivo. Ver [[pdf-escaneado-listo-para-imprimir]]:
```powershell
python "$env:USERPROFILE\.claude\skills\pdf-escaneado-listo-para-imprimir\scripts\normalizar_a4.py" `
       origen.pdf LISTO.pdf --dpi 150 --calidad 70 --gris
```
Caso: escritura 7 con 13 tamaños (3 páginas perdidas); escritura 17 con **18 tamaños
y 22 páginas de riesgo**.

### 8. NO HAY «modo borrador» por driver (2026-09-06)
El **Microsoft IPP Class Driver** rechaza `psk:PageOutputQuality` con
`HRESULT 0x80040003`. `Set-PrintConfiguration` no lo puede fijar.
👉 El equivalente real es **mandar menos datos**: rasterizar a 150 dpi en gris.
Bajó el peso un 42% y el tiempo de 9 min a 2 min por cada tres hojas.

---

# Receta: imprimir un documento largo a DOBLE CARA

## Paso 0 — Preparar
```powershell
$p = "HPC4225C (HP Smart Tank 580-590 series)"
Set-PrintConfiguration -PrinterName $p -PaperSize A4 -DuplexingMode OneSided
Get-PrintJob -PrinterName $p | Remove-PrintJob        # cola limpia
```

## Paso 1 — Generar los DOS PDF con el orden ya horneado
Exportar el documento a PDF (Word COM, `SaveAs` formato **17**) y partirlo con PyMuPDF:
```python
import fitz
src = fitz.open("LIBRO.pdf")
imp = fitz.open()                                   # PASADA 1: impares ASCENDENTE
for i in range(src.page_count):
    if (i+1) % 2 == 1: imp.insert_pdf(src, from_page=i, to_page=i)
imp.save("1-IMPARES-ascendente.pdf")
par = fitz.open()                                   # PASADA 2: pares DESCENDENTE
for i in range(src.page_count-1, -1, -1):
    if (i+1) % 2 == 0: par.insert_pdf(src, from_page=i, to_page=i)
par.save("2-PARES-descendente.pdf")
```
🚦 **EL ORDEN DEPENDE DE LA IMPRESORA — CALIBRARLO SIEMPRE.**
En la campaña del libro sirvió el **descendente**. En la **HP Smart Tank 585** el orden
correcto resultó ser el **ASCENDENTE** (2026-09-06): la bandeja alimenta primero la hoja
de la página más baja. Aplicar aquí el descendente de esta receta arruinó una hoja.

**Protocolo de calibración del orden, sin excepciones:**
1. Imprimir **una sola** página par sobre el taco ya girado.
2. Preguntar al usuario **qué página hay al otro lado de esa hoja**.
   - La impar que le corresponde → orden correcto, lanzar el resto.
   - La **primera** impar del documento → el taco va al revés, invertir el PDF.
3. Comprobar que el **borde superior coincida** en ambas caras (si no, faltó el giro
   de 180° en el plano).

## Paso 2 — Imprimir cada PDF con Acrobat (silencioso, sin diálogos)
```powershell
$acro = "C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
Start-Process -FilePath $acro -ArgumentList @("/n","/t","`"$pdf`"","`"$p`"")
```
`/t` = imprimir a la impresora indicada y cerrar. Imprime **todo** el archivo: por eso
el rango y el orden van horneados en el PDF.

## Paso 3 — La maniobra física (la valida el USUARIO)
Recargar el taco con **el giro que indica el instructivo HP** (deja la cara blanca
lista) **+ un giro adicional de 180° en el plano** (como girar un plato, sin voltear).
Sin ese segundo giro los reversos salen «patas arriba»: el libro se leería como libreta
(de abajo hacia arriba) en vez de como libro (de derecha a izquierda).

## Paso 4 — Verificar
El texto del frente debe **continuar** en el reverso. Si va hacia atrás → el taco está
invertido: usar el PDF de pares en el orden contrario.

---

# Calibración (obligatoria antes de un lote grande)

1. Cargar **1 hoja en blanco**. Imprimir la **página 1**.
2. El usuario hace su maniobra (giro HP + 180°).
3. Imprimir la **página 2**.
4. El usuario voltea la hoja como la página de un libro y comprueba: **¿el texto
   continúa y el borde superior es el mismo?**
   - Sí → maniobra validada, lanzar el lote.
   - Reverso girado 180° → falta el giro extra en el plano.
   - Reverso con otra página → el orden del taco está invertido; invertir el PDF.

**Enviar imágenes de referencia**: renderizar con PyMuPDF las páginas esperadas
(`page.get_pixmap(dpi=100).save(...)`) y mandárselas con `SendUserFile`. Que compare
contra el papel elimina toda ambigüedad verbal.

---

# Imprimir desde Word por COM (cuando no hay PDF)

⚠️ **`PrintOut` en PowerShell: NO usar `[ref]` con literales** (`[ref]0` lanza
«no se puede convertir el valor "0" de tipo "int"»). Pasar los argumentos planos:
```powershell
$miss = [System.Type]::Missing
# PrintOut(Background, Append, Range, OutputFileName, From, To, Item, Copies, Pages, PageType)
$doc.PrintOut($false,$false,4,$miss,$miss,$miss,0,1,"2-176",2)
```
- `Range = 4` → wdPrintRangeOfPages (el rango va en el **9.º** parámetro, `Pages`).
- `PageType`: **0** todas · **1** solo impares · **2** solo pares.
- `$word.Options.PrintBackground = $false` para que el spooling termine.
- `$word.Options.PrintReverse` invierte en Word — **ojo con duplicar** la inversión.

---

# Numerar páginas sin romper la paginación

```powershell
foreach($sec in $doc.Sections){
  $sec.PageSetup.FooterDistance = 1.0*28.3465          # dentro del margen
  $sec.Footers.Item(1).PageNumbers.Add(2, $false)      # 2 = derecha; sin nº en la 1ª
}
```
🚦 **Verificar el conteo antes y después.** Si cambia, el pie está comiendo caja y hay
que deshacerlo — con un bloque ya impreso, un desplazamiento de página lo arruina.

---

# Leer el estado de la cola (interpretación correcta)

| JobStatus | Significa |
|---|---|
| `Printing, Retained` con `PagesPrinted 0` | recién encolado, aún no sale nada |
| `Complete, Retained` con `PagesPrinted = TotalPages` | **imprimió bien** |
| `Error, Complete` con `PagesPrinted = TotalPages` | **imprimió**; el «Error» es ruido del WSD |
| `Error, Retained` con `PagesPrinted 0` | **falló** (papel, tinta, dormida) |
| `Error, Deleting, Printing` | zombi en borrado; **no bloquea trabajos nuevos** |

Acrobat encola **por tandas**: el `TotalPages` sube progresivamente (11 → 16 → 88). No
es un fallo.

---

# Pausar, reanudar y purgar

```powershell
$hp = Get-CimInstance Win32_Printer -Filter "Name LIKE 'HPC4225C%'"
Invoke-CimMethod -InputObject $hp -MethodName Pause     # suspender
Invoke-CimMethod -InputObject $hp -MethodName Resume    # reanudar
Get-PrintJob -PrinterName $p | Remove-PrintJob          # purgar
Get-Process Acrobat | ForEach-Object { $_.Kill() }      # dejar de alimentar la cola
```
- `Remove-PrintJob` puede colgarse >120 s con un trabajo en curso → lanzarlo en
  segundo plano y consultar después.
- Zombis irreductibles: solo se van reiniciando el Spooler **con admin**:
  `net stop spooler` · `del /Q "%SystemRoot%\System32\spool\PRINTERS\*.*"` · `net start spooler`

---

## Compuertas 🚦
- 🚦 Confirmar el **número de hojas** antes de un lote grande y ofrecer **dúplex** (mitad
  de papel). 368 págs a 6"×9" pasaron a **177 en A4**: siempre revisar que el tamaño del
  documento coincida con el papel real.
- 🚦 No purgar el Spooler ni tocar `spool\PRINTERS` sin admin.
- 🚦 No modificar el archivo fuente al imprimir (abrir en SOLO LECTURA).
- 🚦 Ante cualquier duda sobre el apilado: **preguntar al usuario qué ve en el papel**.

## Relacionado
- [[excel-pagina-a4-optima]] · [[xlsx-a4-portrait-merge-pdf]] · [[agente-gui-autoaprobado-windows]]
