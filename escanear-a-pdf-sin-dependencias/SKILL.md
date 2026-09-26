---
name: escanear-a-pdf-sin-dependencias
description: |
  Escanea un documento en la impresora multifunción y entrega un PDF
  verificado en la ruta que se pida, SIN Word, sin Acrobat y sin el
  software del fabricante. Solo WIA (el motor de imagen de Windows),
  System.Drawing y un escritor de PDF propio de unas cien líneas.

  Sirve para el cristal y para el alimentador automático (lotes
  multipágina), en color, gris o blanco y negro, a la resolución que se
  elija. El PDF sale a tamaño real 1:1 con el original, sin bordes
  blancos ni reescalados, y se valida byte a byte antes de darlo por bueno.

  Nace de comprobar que la vía «obvia» —montar el PDF con Word por COM—
  se cuelga: Word arranca en modo `-Embedding`, se queda dando vueltas
  contra un bloqueo huérfano de `Normal.dotm` y no termina nunca.

trigger_phrases:
  - "escanea el documento"
  - "escanear a pdf"
  - "pasa esto a pdf desde la impresora"
  - "digitaliza estos papeles"
  - "escanea y guarda en la ruta"
  - "escaneo multipágina con alimentador"

idioma_de_salida: español
nivel: aplicada
dominio: digitalización / PDF / hardware
metadata:
  version: 1.0
  fecha: 2026-08-31
  scripts:
    - scripts/escanear_a_pdf.ps1
    - scripts/escanear.ps1
    - scripts/imagen_a_pdf.ps1
    - scripts/validar_pdf.ps1
  relacionada:
    - impresion-local-hp-diagnostico
    - saneamiento-complementos-office
    - xlsx-to-pdf-a4
---

# Skill `escanear-a-pdf-sin-dependencias`

## Doctrina

**Un JPEG se mete dentro de un PDF tal cual, sin recomprimir.** Basta
declararlo como XObject con `/Filter /DCTDecode`. El PDF pesa lo mismo que
el JPEG, no pierde un ápice de calidad, y armarlo son cien líneas de
PowerShell.

Todo lo demás —Word, Acrobat, la utilidad del fabricante— es peso muerto
que además introduce sus propios modos de fallo.

## Uso

```powershell
$S = "$env:USERPROFILE\.claude\skills\escanear-a-pdf-sin-dependencias\scripts"

# Caso normal: una hoja del cristal, color, 300 dpi
& powershell -ExecutionPolicy Bypass -Command "& '$S\escanear_a_pdf.ps1' -Destino 'E:\ruta'"

# Documento de texto: gris y 200 dpi pesa la tercera parte y se lee igual
& powershell -ExecutionPolicy Bypass -Command "& '$S\escanear_a_pdf.ps1' -Destino 'E:\ruta' -Nombre 'Contrato' -Dpi 200 -Modo Gris"

# Lote por el alimentador automático
& powershell -ExecutionPolicy Bypass -Command "& '$S\escanear_a_pdf.ps1' -Destino 'E:\ruta' -Alimentador"
```

Sin `-Nombre` el archivo sale como `Escaneo_<fecha>_<hora>.pdf`, y **nunca
pisa uno existente**: añade `_1`, `_2`…

⚠️ Hay que invocar con **`-Command`, no con `-File`**. Con `-File`,
PowerShell no separa los arreglos por comas y los parámetros llegan como
una sola cadena.

## Las cuatro piezas

| Script | Qué hace |
|---|---|
| **`escanear_a_pdf.ps1`** | El flujo completo: captura, arma, valida, limpia |
| `escanear.ps1` | WIA → JPEG. Detecta alimentador, tapa abierta y atasco |
| `imagen_a_pdf.ps1` | JPEG → PDF, escribiendo el PDF a mano |
| `validar_pdf.ps1` | Comprueba el PDF byte a byte |

## Lo que hay que saber de WIA

- **Capturar siempre en BMP** (`{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}`) y
  comprimir después. Pedir JPEG directamente al `Transfer` falla en muchos
  escáneres. El BMP intermedio es enorme —25 MB para una A4 a 300 dpi en
  color— pero se borra al instante y el JPEG queda en 1 MB.
- **Las propiedades se fijan por nombre**, no por número mágico:
  `'Horizontal Resolution'`, `'Vertical Resolution'`, `'Data Type'`
  (3 = color, 2 = gris, 0 = blanco y negro). Y hay que envolver cada
  asignación en `try`: los escáneres rechazan valores que no admiten.
- **`Document Handling Capabilities`** dice qué hay: bit `0x001` =
  alimentador. Sin ese bit, `-Alimentador` no sirve de nada.
- **`Document Handling Status`**: `0x01` hay papel en el alimentador ·
  `0x02` cristal listo · `0x08` tapa levantada · `0x20` atasco.
- Con alimentador, **quedarse sin papel se manifiesta como una excepción**
  en `Transfer`, no como un final ordenado. Hay que capturarla y tratarla
  como fin de lote.
- El mismo aparato suele aparecer **varias veces** en `DeviceInfos`: el
  `Type=1` es el escáner WIA propiamente dicho; los `Type=65535` son
  variantes del fabricante o eSCL, con resoluciones distintas por omisión.

## Anatomía del PDF que se genera

Seis objetos por una página. La matriz `cm` estira la imagen —que en su
propio espacio mide 1×1— hasta el tamaño completo de la página:

```
1  Catalog
2  Pages
3  Page      /MediaBox [0 0 ancho_pt alto_pt]
4  XObject   /Subtype /Image /Filter /DCTDecode  <- el JPEG, intacto
5  Contents  q  ancho 0 0 alto 0 0 cm  /Im0 Do  Q
xref + trailer + startxref
```

`ancho_pt = píxeles ÷ dpi × 72`. Así el PDF queda **1:1 con el papel**.

**Lo delicado son los desplazamientos de la tabla `xref`.** Hay que anotar
`fs.Position` justo antes de escribir cada objeto y volcarlos con formato
`{0:D10}` — exactamente diez dígitos, y cada entrada de exactamente 20
bytes contando el espacio final. Un byte de más y el PDF no abre. Por eso
existe `validar_pdf.ps1`: comprueba que cada desplazamiento apunte de
verdad a su `N 0 obj`.

Limitación: **el JPEG debe ser de línea base**, no progresivo. `DCTDecode`
no admite progresivos. `System.Drawing` genera línea base por omisión.

## Por qué NO usar Word para armar el PDF

Fue el primer intento y hay que dejarlo escrito para no repetirlo:

> Word arrancó como `WINWORD.EXE /Automation -Embedding`, quemó **235
> segundos de CPU** sin producir nada y no terminó nunca. Al inspeccionar
> apareció un **bloqueo huérfano `~$Normal.dotm`** —dejado por otra
> instancia `-Embedding` que el Explorador había arrancado para generar
> miniaturas— con la plantilla global tomada.

Es la misma cadena diagnosticada en
[[forense-cuelgues-y-caidas-windows]]. Si alguna vez hace falta Word por
COM: comprobar antes que no haya `WINWORD.EXE` sin ventana vivo y que no
exista `%APPDATA%\Microsoft\Templates\~$Normal.dotm`.

## Elegir resolución y modo

| Uso | Ajuste | Peso de una A4 |
|---|---|---|
| Texto para archivar o enviar | `-Dpi 200 -Modo Gris` | 0,4 MB |
| Documento firmado, uso oficial | `-Dpi 300 -Modo Color` | 1,0 MB |
| Fotografía o plano con detalle | `-Dpi 600 -Modo Color` | 4 MB o más |

## Caso de referencia — 2026-08-31

Carta de responsabilidad del **Acuatlón Quevedo 2026** firmada a mano,
escaneada en la HP Smart Tank 580-590 (predeterminada, escáner plano sin
alimentador) a 300 dpi en color. Resultado: `1,03 MB`, una página,
`21,6 × 29,7 cm`, PDF validado, entregado en
`E:\vars\var 91\Deporte varios`.

## Vecindad en la red

Racimo de mantenimiento y de documentos. Nació de comprobar que la vía por COM de Word se cuelga; entrega PDF a la misma cadena documental que los demás.

- [[forense-cuelgues-y-caidas-windows]]
- [[impresion-local-hp-diagnostico]]
- [[pdf-escaneado-listo-para-imprimir]]
- [[xlsx-to-pdf-a4]]
- [[documentos-encuadrados-margenes]]

> Puente tendido el 9-sep-2026: este racimo estaba conectado entre sí pero desprendido del cuerpo principal ([[regla-del-primer-tropiezo]] §10).
