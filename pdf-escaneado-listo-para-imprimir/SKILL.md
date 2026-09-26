---
name: pdf-escaneado-listo-para-imprimir
description: |
  Prepara un PDF ESCANEADO para que salga completo en una impresora doméstica,
  normalizando el lienzo de todas las páginas a una medida estándar antes de
  mandarlo. Resuelve el fallo en que la impresora expulsa la hoja **con solo
  una esquina impresa** y el resto en blanco.

  La causa no es el peso del archivo ni un JPEG dañado: es que los PDF
  escaneados traen **cada página de un tamaño ligeramente distinto**, y una
  medida no estándar hace que la impresora componga sobre un área equivocada.

  Regla dura: **ante un PDF escaneado, normalizar SIEMPRE antes de imprimir.**
  No intentar adivinar qué página fallará — no se puede predecir con fiabilidad.

  Trae además el diagnóstico forense (cuatro pruebas), el aligerado que
  sustituye al inexistente «modo borrador» de los drivers genéricos, y el
  partido en dos pasadas para doble cara manual.

trigger_phrases:
  - "la impresora saca la hoja a medias"
  - "solo se imprimió una esquina / parte de la página"
  - "imprimir un PDF escaneado"
  - "imprimir escrituras / documentos digitalizados"
  - "el PDF pesa mucho para imprimir"
  - "modo borrador / imprimir más rápido"

idioma_de_salida: español
nivel: aplicada
dominio: impresión / PDF / documentos escaneados
metadata:
  version: 1.0
  fecha: 2026-09-06
  scripts:
    - scripts/diagnosticar_pdf.py
    - scripts/normalizar_a4.py
    - scripts/partir_duplex.py
    - scripts/contacto_tops.py
    - scripts/aligerar_pdf.py
  relacionada:
    - impresion-local-hp-diagnostico
    - escanear-a-pdf-sin-dependencias
    - forense-cuelgues-y-caidas-windows
---

# Skill `pdf-escaneado-listo-para-imprimir`

## Doctrina

**Un PDF escaneado no es un documento: es una colección de fotos de tamaños
distintos metidas en un contenedor.** El escáner recorta cada hoja donde
puede, y cada página acaba midiendo algo ligeramente diferente —595×842,
595×824, 583×842, 577×843…—. En pantalla no se nota. En la impresora sí.

Cuando llega una página de medida **no estándar**, una impresora doméstica con
driver genérico compone sobre un área equivocada y **expulsa la hoja con una
esquina impresa y el resto en blanco**. Siempre la misma página, siempre el
mismo corte.

> **La regla: normalizar el lienzo SIEMPRE, antes de imprimir.**
> Es barato, no deforma nada y elimina la variable de raíz.

## El error que hay que evitar: intentar predecir

En el caso de referencia se probaron cuatro hipótesis antes de dar con la
buena, y **las tres primeras fallaron**:

| Hipótesis | Cómo se refutó |
|---|---|
| Es el peso del ráster | La página que fallaba era de las medianas (5,99 MP). La más pesada (7,04 MP / 612 KB) salía perfecta |
| Es un JPEG progresivo | Las 12 eran **SOF0 línea base** |
| El JPEG está corrupto | Todas con marcador **EOI** y decodificación **completa**; rotación 0° |
| **Es el tamaño de página** | **Las dos únicas páginas de 595 × 824 pt eran justo las dos que fallaban** — y siguieron fallando tras re-rasterizarlas desde cero |

Y aun así el criterio **no es predictivo**: en el mismo documento había páginas
de 585×842 y 587×843 (también no estándar) que salían bien. Lo único fiable es
**normalizar todo**.

## Uso

```powershell
$S = "$env:USERPROFILE\.claude\skills\pdf-escaneado-listo-para-imprimir\scripts"

# 1. Ver qué trae el documento
python "$S\diagnosticar_pdf.py" "documento.pdf"

# 2. Normalizar (esto es lo que hay que imprimir)
python "$S\normalizar_a4.py" "documento.pdf" "LISTO.pdf" --dpi 150 --calidad 70 --gris

# 3. Si va a doble cara manual, partir en dos pasadas
python "$S\partir_duplex.py" "LISTO.pdf" "salida" --prefijo DOC
```

## Las siete herramientas

| Script | Para qué |
|---|---|
| **`diagnosticar_pdf.py`** | Las cuatro pruebas de una pasada: tamaño de página, peso, codificación JPEG e integridad. Marca las páginas de riesgo |
| **`normalizar_a4.py`** | **La corrección.** Todas las páginas a A4 exacto, contenido centrado y a escala conservando proporción |
| `partir_duplex.py` | Parte en impares/pares con el orden horneado dentro del PDF |
| `unir_pdfs.py` | Une varios PDF **en el orden dado**. Para armar las tandas cuando cada documento es una hoja |
| `contacto_tops.py` | Tira con la cabecera de varias páginas, etiquetada. Sirve para identificar contra el papel qué página salió mal |
| `ver_propietario.py` | Recorre una carpeta y extrae las líneas con nombre de propietario/contribuyente. Detecta si el PDF es texto o escaneado |
| `aligerar_pdf.py` | Baja el ráster conservando el tamaño original de página |

## Varios documentos de UNA hoja: las dos tandas

Cuando hay N documentos y **cada uno cabe en una hoja** (2 páginas), no se
imprimen uno a uno — son 2N interacciones. Se hace en **dos tandas**:

1. **Tanda 1**: la página 1 de todos, unidas con `unir_pdfs.py` en un orden fijo.
2. El usuario gira el taco **sin alterar el orden**.
3. **Tanda 2**: la página 2 de todos, **en el MISMO orden** (la bandeja de esta
   casa alimenta en ascendente: la primera que salió es la primera que entra).

Cada hoja se autoidentifica por su propio contenido (número de clave catastral,
lote, etc.), así que no se pierde trazabilidad.

⚠️ **Si un documento debe llevar un lado en blanco**, retirar esa hoja del taco
antes de la tanda 2 y omitir su página en el PDF. Dejarla al final «porque el
trabajo tiene menos páginas» funciona, pero si la impresora arrastra dos hojas
juntas el desfase arruina el resto. Sacarla cuesta un segundo.

## Color

Todo lo anterior vale igual a color: basta **no pasar `--gris`**. Para
documentos oficiales en color, `--dpi 200 --calidad 85` da buena lectura sin
inflar el archivo. Y hay que acordarse de la impresora:

```powershell
Set-PrintConfiguration -PrinterName $p -PaperSize A4 -DuplexingMode OneSided -Color $true
```

## El «modo borrador» que no existe

Con el **Microsoft IPP Class Driver** —el genérico que Windows pone a las
impresoras WSD— no se puede pedir calidad borrador:

```
Set-PrintConfiguration ... -PrintTicketXml (con psk:PageOutputQuality)
  -> HRESULT 0x80040003   (el driver no expone esa opción)
```

El equivalente real es **mandar menos datos**: rasterizar a 150 dpi en escala
de grises. En el caso de referencia bajó el peso un **42%** y tres hojas
salieron en 2 minutos, frente a los 9 que habían tardado doce.

```powershell
--dpi 150 --calidad 70 --gris     # borrador: rápido, legible
--dpi 200 --calidad 80 --gris     # documento oficial
--dpi 300 --calidad 85            # cuando importa el detalle o el color
```

⚠️ Son documentos legales: bajar la resolución es una decisión del usuario,
no del agente. Preguntar antes de un lote grande y **calibrar con una hoja**.

## Doble cara manual: lo que hay que calibrar cada vez

**El orden de apilado depende de la impresora, no es una constante.** En la
campaña del libro sirvió el **descendente**; en la HP Smart Tank 585 el orden
correcto resultó ser **ascendente**, y aplicar el de la skill anterior costó
una hoja.

Protocolo, sin excepciones:

1. Imprimir la **primera página par** sobre el taco ya girado. Una sola.
2. El usuario mira el reverso y dice **qué página hay al otro lado**.
   - Si es la impar que le corresponde → orden correcto, lanzar el resto.
   - Si es la primera impar del documento → el taco va al revés, invertir.
3. Comprobar también que **el borde superior coincida** en ambas caras. Si el
   reverso sale cabeza abajo, faltó el giro de 180° en el plano.

## Cómo identificar una hoja defectuosa

Cuando el recorte se come la columna derecha, dos páginas del mismo formulario
son indistinguibles. Dos vías:

- **`contacto_tops.py`** — genera una tira con las cabeceras etiquetadas por
  número de página, para comparar contra el papel.
- **La posición en el taco** — las hojas salen en orden conocido; contar la
  posición identifica la página sin ambigüedad.

## Caso de referencia — 2026-09-06

**Escritura 7** (`7 - Escr Lote C 1-3-6-8 FDC.pdf`), 26 páginas escaneadas,
13 tamaños distintos. Las páginas **7, 19 y 8** —las tres de 595 × 824 pt—
salían recortadas siempre. Normalizadas a A4 exacto, salieron completas a la
primera. Coste del diagnóstico a ciegas: unas 20 hojas.

**Escritura 17** (`17 - Escr Lote L 2-8 FDC.pdf`), 30 páginas: **18 tamaños
distintos, 22 páginas marcadas de riesgo**. Normalizada antes de imprimir:
**salió limpia a la primera, cero reimpresiones.**

Ese contraste es la medida de la skill:

| | Escritura 7 (a ciegas) | Escritura 17 (con la skill) |
|---|---|---|
| Tamaños mezclados | 13 | **18** |
| Páginas en riesgo | 3 | **22** |
| Hojas desperdiciadas | ~20 | **0** |
| Rondas de reimpresión | 3 | **0** |

**Resto del expediente COAC (38 hojas, 75 páginas)**: certificados de gravamen
(5 hojas), linderos + avalúos (5), y tres documentos habilitantes a color. En
todos ellos el diagnóstico encontró tamaños no estándar —`595 × 855`,
`595 × 841`, `587 × 842`, `581 × 842`— que habrían salido recortados.
Ninguna hoja perdida.

## Regla de oficio: qué NO imprimir

Antes de mandar, mirar si hay páginas que no aportan:

- **Páginas de cierre sin contenido útil** — bloque de firma del registrador y
  «Página 3 de 3». Se detectan con pocas decenas de caracteres y **cero
  imágenes**.
- **Documentos con titular distinto** al del trámite. `ver_propietario.py`
  ayuda cuando son texto; si son escaneados, hace falta mirarlos con
  `contacto_tops.py`. En el caso de referencia, uno de diez estaba a nombre de
  otra persona y ese lado quedó en blanco por decisión del usuario.

Preguntar siempre antes de omitir: **qué se imprime y qué no es decisión suya,
no del agente.**
