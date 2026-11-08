---
name: armar-semana-informe-ventas-qvp
description: |
  Arma de punta a punta la carpeta semanal «Sem ven NN» del War Room de Extractora
  Quevepalma y produce sus dos entregables para el CEO: el informe ejecutivo en PDF
  A4 (una o dos carillas, nunca tres) y el hilo de WhatsApp que lo introduce.
  Documenta que TODAS las fuentes —imágenes y adjuntos— provienen del WhatsApp
  +593 99 387 9355, de los chats «Bs Inmobiliaria Mobijuesa» y «Alfredo Sevilla
  Ventas QVP». Reconoce el patrón entre el nombre de cada subcarpeta de área y la
  información que contiene, clasifica el material nuevo según ese patrón y levanta
  el acta de procedencia. Destilada de las semanas 42, 43 y 44 (oct-2026).
trigger_phrases:
  - "arma la semana 45"
  - "arma la semana"
  - "informe ejecutivo de la semana"
  - "hilo de WA para don omar de la semana"
  - "de dónde salieron las fuentes de la semana"
  - "clasifica las imágenes de WhatsApp de la semana"
metadata:
  type: skill
  version: 1.0
  fecha: 2026-10-28
  estado: production
  proyecto: War Room QVP — Extractora Quevepalma S.A.
  destinatario: Don Omar Juez Zambrano, Presidente del Directorio
---

# armar-semana-informe-ventas-qvp

> **La orden que la dispara es de tres palabras: «arma la semana NN».** A partir de
> ahí no hay que preguntar nada: la carpeta, las subcarpetas, la clasificación del
> material, el acta de procedencia, el PDF y el hilo salen de corrido.

## 0 · Acerca de mí (cargar al arrancar)

Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md`
y el `MEMORY.md` del mismo directorio. Voz: **Francisco Duque**, usted,
cortés-formal; **nunca `≈` ni `~`** ([[feedback_humanizar_sin_firma_ia]]). El
informe lo lee un presidente de directorio que no tiene tiempo: cada párrafo debe
decir el número y lo que hay que hacer con él.

## 1 · Qué produce y para quién

Cada semana, de la carpeta `Sem ven NN` salen **exactamente dos entregables**:

| Entregable | Formato | Nombre |
|---|---|---|
| Informe ejecutivo | PDF A4, **máximo 2 carillas** | `QVP_Informe_Ejecutivo_Semana_NN.pdf` |
| Hilo de WhatsApp | texto plano, para envío manual | `QVP_Hilo_WA_Semana_NN_Don_Omar.txt` |

Ambos van **en la misma carpeta que las fuentes**, no en otra ruta. Nada de Word,
nada de Excel para el CEO: PDF y texto.

Raíz de trabajo:
`C:\Users\datos\Dropbox\7 Quevepalma\1 WAR ROOM QVP\Entregables\I Inf Sem Ventas`

## 2 · Procedencia: la regla de origen único

**Todo el material de estas carpetas sale de un solo sitio:** el WhatsApp de la
cuenta **+593 99 387 9355**, de los chats **«Bs Inmobiliaria Mobijuesa»** y
**«Alfredo Sevilla Ventas QVP»**, en las fechas de la semana respectiva.

- Las **imágenes** (`WhatsApp Image <fecha> at <hora>.jpeg`) son fotografías de
  los reportes semanales que cada área publica en esos chats.
- Los **adjuntos** (`.xlsx`, `.xlsm`, `.pptx`, `.pdf`) son los archivos enviados
  por esos mismos chats, descargados **sin renombrar**.
- No entra material de correo, ni descargas de sistemas, ni archivos entregados
  en mano. Si aparece uno, se anota aparte en el acta y se avisa.

Esto se deja escrito, semana a semana, en `FUENTES_Semana_NN.md` dentro de la
carpeta. El modelo es
`…\I Inf Sem Ventas\Sem ven 44\FUENTES_Semana_44.md`
(38 fuentes: 32 fotografías y 6 adjuntos). **El acta no es burocracia: es lo que
permite que Don Omar o un auditor comprueben a mano cualquier cifra del PDF**
buscando en el chat por la fecha y la hora del nombre del archivo.

### El desfase del ciclo — no es un error

La carpeta `Sem ven NN` se arma con material capturado el **lunes o martes de la
semana NN**, y ese material reporta **los resultados reales de la semana NN−1 y
el programa de la semana NN**. Por eso en la carpeta de la 44 conviven el libro
de cartera «QVP **43**» y la hoja de precios «SEMANA **44**». No conciliarlos a la
fuerza: explicarlo.

Semanas ISO (`datetime.date.fromisocalendar(2026, NN, 1)`): la 42 fue del 12 al
18 de octubre, la 43 del 19 al 25, la **44 del 26 de octubre al 1 de noviembre**,
la **45 del 2 al 8 de noviembre de 2026**.

## 3 · El patrón: nombre de subcarpeta ↔ contenido

Siete subcarpetas, con los nombres **tal cual** se escribieron en la semana 44,
**erratas incluidas** —`area finaciera y cartera` va sin la segunda «n»—. No
corregirlas: romperían el emparejamiento con lo ya hecho.

| Subcarpeta | Qué contiene | Qué alimenta del informe |
|---|---|---|
| `area comercial` | hoja de seguimiento de precios DSJ vs Colombia vs costo de oleína G y H, comité ejecutivo (`.pptx`), propuestas, precios de la competencia nacional, góndola, resultados reales por producto, programa de ventas, cumplimiento contra la meta | §1 precios y márgenes, §2 competencia, §3 góndola, §6 ventas contra la meta, §7 resultados reales, §8 programa |
| `area finaciera y cartera` | libro `MACRO - Resumen del control semanal de cartera QVP NN.xlsm`, cartera por cliente, vencido y por vencer, cobranza contra meta, flujo de caja planificado | §4 evolución de cartera, alerta de caja |
| `area logistica` | «LOGISTICA - SEMANA #NN.pdf» y «ACOPIOS.pdf» fotografiados: concentración del movimiento de fruta por proveedor, fruta transportada interno/externo, vueltas por placa, merma | §9 transporte de fruta |
| `area de mantenimiento` | indicadores de extractora y refinería | §5 las demás áreas |
| `area control de calidad` | no conformidades de la semana | §5 las demás áreas |
| `area compra de fruta` | compra de fruta de la semana | §5 las demás áreas |
| `area compra de materiales` | compras e insumos | §5 las demás áreas |

Si llega material de un área nueva, **se crea su subcarpeta con el mismo
patrón de nombre** (`area <lo que sea>`, en minúsculas, sin tildes) y se le abre
una tarjeta en §5.

## 4 · La orden «arma la semana NN» — procedimiento

> **Compuerta de cupo:** antes de arrancar, decir en una línea cuántas carillas y
> qué secciones se van a producir. Si el cupo está corto, se produce primero el
> PDF y después el hilo, nunca al revés.

### Paso 1 — armar la carpeta y clasificar

```bash
python "C:/Users/datos/.claude/skills/armar-semana-informe-ventas-qvp/armar_semana.py" --semana 45
```

Muestra el plan sin tocar nada: qué archivo va a qué subcarpeta y por qué.
Revisarlo, y recién entonces:

```bash
python "C:/Users/datos/.claude/skills/armar-semana-informe-ventas-qvp/armar_semana.py" --semana 45 --aplicar
```

El script crea `Sem ven 45` con sus siete subcarpetas, clasifica cada archivo
—primero por nombre, después por el título y las palabras del contenido vía
OCR—, lo mueve y escribe `FUENTES_Semana_45.md`. Lo que no logra decidir queda en
`_sin_clasificar`: esas imágenes **se leen a ojo** y se mueven a mano. Usa el
intérprete del sistema
(`C:\Users\datos\AppData\Local\Programs\Python\Python312\python.exe`), que es el
que tiene `rapidocr-onnxruntime`; el venv de NotebookLM **no** lo tiene.

Opciones: `--origen "C:/Users/datos/Downloads"` si las descargas no están sueltas
en la raíz de `I Inf Sem Ventas`; `--raiz <ruta>` para ensayar en una carpeta de
prueba sin tocar Dropbox; `--anio` si se arma una semana de otro año.

**Calibración medida:** contra las 32 fotografías de la semana 44 el clasificador
acierta **32 de 32**, sin ninguna colocación errónea. El umbral está puesto del
lado prudente: prefiere mandar a `_sin_clasificar` antes que colocar mal. Varias
entradas de la tabla `TITULOS` del script son **la grafía que devuelve el OCR**,
no la correcta —`logsticasemana`, `flujodecaia`, `acopos`—, porque es contra esa
lectura real que se calibró. Al añadir un título nuevo, añadir también lo que el
OCR lee de él.

### Paso 2 — leer las fuentes

Orden de lectura, de lo más denso a lo más barato:

1. **El libro de precios** (`Seguimiento Precio … SEMANA NN.xlsx`) con
   `openpyxl(data_only=True)` — trae los valores calculados, no las fórmulas.
2. **El libro de cartera** (`MACRO - … QVP NN.xlsm`), igual.
3. **El comité ejecutivo** (`.pptx`) con `python-pptx`; las imágenes incrustadas
   se sacan con `sh.shape_type == 13` → `sh.image.blob`.
4. **Las fotografías**, con `rapidocr-onnxruntime` en lote.
   🚦 **El `Read` visual de imágenes se agota cerca de las 30 por sesión**
   («media removed: request limit»), de modo que el OCR va primero y el ojo se
   reserva para lo dudoso ([[feedback_pdf_escaneado_ocr_rapidocr]]).

### Paso 3 — componer el informe

Clonar `referencias/modelo_informe_semana_44.html` y reemplazar contenido. Es un
HTML **autocontenido** (cero peticiones externas) que ya produjo dos carillas de
263,3 mm y 273,8 mm. La estructura probada:

**Hoja 1** — cabecera → cinta de veredicto (3 columnas) → fila de 4 KPIs →
§1 precios y márgenes de las semanas N−3 a N → §2 competencia nacional y
§3 góndola, lado a lado → §4 evolución de cartera → §5 las demás áreas (tarjetas)
→ pie con fuentes.

**Hoja 2** (`.hoja2{page-break-before:always;}`) — cinta → 4 KPIs → §6 ventas
contra la meta → §7 resultados reales y §8 programa, lado a lado → §9 transporte
de fruta → alerta de caja → bloque de decisiones (3 columnas) → pie con fuentes.

**Ventana histórica: siempre las cuatro últimas semanas, N−3 a N.** La semana 44
mostró de la 41 a la 44; la 45 mostrará de la 42 a la 45.

Fichas de la casa:

```css
--azul:#1d4e78;  --ok:#1a7a4c;  --mal:#b3261e;  --avi:#a86a00;
```

Tablas con `table-layout:fixed` y `<colgroup>` explícito. **Los hijos de un grid
necesitan `min-width:0`** o la tabla se desborda del cuadro.

### Paso 4 — renderizar y verificar

```bash
python "C:/Users/datos/.claude/skills/armar-semana-informe-ventas-qvp/render_a4.py" "C:/Users/datos/war_room_tmp/sem45_inf.html" "C:/Users/datos/Dropbox/7 Quevepalma/1 WAR ROOM QVP/Entregables/I Inf Sem Ventas/Sem ven 45/QVP_Informe_Ejecutivo_Semana_45.pdf" --sondas "DISEBAJ;88.572,38;millones"
```

Mide cada carilla contra la **caja útil de 283,0 mm**, cuenta peticiones externas
(deben ser cero), saca un PNG de cada página en `verif/` y comprueba las sondas.

### Paso 5 — el hilo de WhatsApp

Cinco mensajes numerados más una versión ultracorta de dos, en el modelo de
`…\Sem ven 44\QVP_Hilo_WA_Semana_44_Don_Omar.txt`:

1. Apertura: qué trae el informe y cuántos mensajes son.
2. **Lo bueno**, con cifras.
3. **Lo que conviene mirar con calma** (precios, márgenes, competencia).
4. **La alerta** y por qué se escribe hoy y no el lunes.
5. **Lo que le piden decidir**, más el resto de las áreas.

Registro: entre iguales, concreto y a la vez explicativo
([[construccion-hilos-wa-don-omar]]). Cada mensaje se sostiene solo.

🚦 **La cuenta +593 99 387 9355 tiene restringido el envío automatizado.** El hilo
se entrega **como texto para envío manual desde el teléfono**; esa nota va al pie
del archivo. Y **nunca pulsar «Usar aquí»** en WhatsApp Web: mata la sesión del
usuario.

### Paso 6 — entregar

`SendUserFile` con el PDF y el `.txt`, y un mensaje de cierre que diga lo bueno,
la alerta y la decisión que se pide. Nada más.

## 5 · Hechos que no se vuelven a averiguar

Correcciones que ya costaron una ronda. Darlas por ciertas mientras la fuente no
diga otra cosa:

- **Quevepalma no tiene flota propia.** El capítulo de transporte no se lee como
  eficiencia interna sino como **quién concentra el movimiento de la fruta**. En
  la semana 44: familia Juez 44.415,75 t = **50,2 %** de 88.572,38 t; Don Omar
  solo 29,3 %, más que los doce últimos proveedores juntos; los siete primeros,
  85 %. La prioridad de la flota de Don Omar padre se argumenta con el dato de que
  la flota interna rodó al 40,74 % de su capacidad mientras se pagaba flete
  externo en la misma semana.
- **El cupo de DISEBAJ es de USD 2.000.000.** La celda del libro que dice
  1.000.000 está mal. No tomarla.
- **SEMVRA despacha en IBC de 950 kg, no a granel.** Su precio nominal de $1.290
  por «tonelada» equivale a **$1.357,89 por tonelada real**. Siempre incluir
  volumen y presentación en los cuadros de margen por cliente.
- **Mundosnack: el precio es $1.280**, no $1.350 (errata de tipeo del deck, que
  además infla su total en $2.100).
- **Odesa es solo un ejemplo.** La cifra de $1.800 la tonelada no es un precio y
  no debe aparecer en ningún entregable.
- **Defecto sistemático del libro de precios:** la fila «Margen de Venta a DSJ vs
  Oleína G» está calculada contra el precio de **Colombia**, no contra el de
  DISEBAJ, y por eso subdeclara el margen en exactamente la prima. La fila de
  oleína H sí usa el precio correcto. Recalcular siempre y decirlo.
- **El costo contable real manda sobre la hoja de seguimiento.** En la semana 43
  la oleína guineensis costó $1.310,12 por tonelada y no los $1.270,48 de la hoja:
  $15.155 de diferencia en una semana sobre la hoja con la que se fija precio.
- **Nunca mencionar a EPACEM**, salvo donde Francisco lo autorizó expresamente
  (Anexo III-B). El lenguaje sobre la auditoría del ERP es discreto: nunca «robo»,
  «hurto» ni «fraude».

## 6 · Verificación obligatoria antes de entregar

Ninguna de estas es opcional. Las cinco nacieron de un error real.

1. **Medir las carillas.** `render_a4.py` lo hace. Tres páginas es un fallo, no un
   detalle: se rebalancea moviendo bloques enteros entre hojas, no recortando
   frases sueltas.
2. **Leer a ojo el PNG de cada página.** Es lo único que detecta cabeceras que se
   enciman y signos de dólar comidos. En la semana 44 apareció
   «4,47 millones sobre una meta de 00 millones».
3. **Nunca generar texto con `python -c "…"` entre comillas dobles.** Bash expande
   `$1`, `$5`, `$8` como parámetros posicionales y **se come los signos de dólar
   en silencio**. Todo script que contenga `$` se escribe con la herramienta Write
   y se ejecuta como archivo.
4. **No fiarse del OCR para emparejar nombre y número.** `rapidocr` desalineó las
   columnas del cuadro de ACOPIOS y estuvo a punto de atribuir 15.180,38 t a la
   persona equivocada. Los cuadros de nombre + cifra se confirman a ojo.
5. **Sondas de texto en el PDF.** Las tres o cuatro cifras que sostienen el
   informe tienen que aparecer en el texto extraído, no solo en la pantalla.

## 7 · Cómo depurar si falla

- **`armar_semana.py` no encuentra archivos** → están en otra carpeta. Pasar
  `--origen`. Si WhatsApp los dejó en varias, correr el script una vez por cada
  una; es idempotente y no pisa nada.
- **Todo cae en `_sin_clasificar`** → el OCR no corrió. Comprobar con
  `python -c "import rapidocr_onnxruntime"` **en el intérprete del sistema**, no
  en un venv. Si falta, clasificar a mano guiándose por la tabla del §3.
- **Un archivo cae en el área equivocada** → la regla de nombre mandó sobre el
  contenido. Moverlo a mano y, si el caso se repetirá, añadir la palabra a
  `CLAVES` o afinar `REGLAS_NOMBRE` en el script. Una regla que no se automatiza
  es solo una recomendación ([[regla-del-primer-tropiezo]] §6.bis).
- **El PDF sale en tres páginas** → medir con
  `[...document.querySelectorAll('.page')].map(e=>e.getBoundingClientRect().height)`
  y mover un bloque completo de hoja, con renumeración de secciones. Bajar el
  cuerpo de letra solo cuando falten menos de 10 mm.
- **`PermissionError` al copiar el PDF** → está abierto en el visor. El script
  renderiza a temporal y avisa; cerrar el visor y repetir solo la copia.
- **El hilo cita un dato que el PDF ya no tiene** → se corrigió uno y no el otro.
  Tras cada corrección, pasar por los **dos** archivos y por la versión ultracorta
  del hilo. Es el fallo más frecuente de todos.
- **La hoja de precios y el libro de cartera no cuadran de semana** → es el
  desfase del §2, no un error. Explicarlo en el pie.

## 8 · El 20 % volátil (revisar al reusar)

El número de semana y sus fechas ISO; los nombres de las subcarpetas de área (si
Quevepalma abre o cierra áreas); el nombre exacto de los libros de Excel, que
cambia de semana; los dos chats de WhatsApp de origen; y la ruta de Dropbox. Lo
estable es el procedimiento: clasificar → leer → componer en dos carillas →
medir → verificar a ojo → entregar con hilo.

## 9 · Reuso (no empezar de cero)

- Lectura y envío por WhatsApp → [[whatsapp-web-cdp-lectura-envio]] y
  [[whatsapp-desktop-app-lectura]] (solo Edge, `channel="msedge"`, CDP 9222).
- Registro del hilo para el CEO → [[construccion-hilos-wa-don-omar]].
- Marco financiero y de márgenes → [[control-financiero-semanal-qvp]].
- Acta del comité y compromisos → [[comite-cuarto-guerra-qvp]].
- Compra de fruta → [[compra-fruta-semanal-qvp]].
- Página A4 que cabe → [[excel-pagina-a4-optima]] y [[documentos-encuadrados-margenes]].
- OCR en lote → [[feedback_pdf_escaneado_ocr_rapidocr]].
- Formato ejecutivo escaneable → [[feedback_formato_ejecutivo_escaneable]].

## 10 · Archivos de esta skill

| Archivo | Para qué |
|---|---|
| `armar_semana.py` | crea la carpeta y las siete subcarpetas, clasifica, mueve y levanta el acta |
| `render_a4.py` | HTML → PDF A4 con medición, conteo de peticiones externas, PNG de control y sondas |
| `referencias/modelo_informe_semana_44.html` | el informe de dos carillas que funcionó: clonar y reemplazar |
| `referencias/modelo_hoja_unica_semana_43.html` | la variante de una sola carilla |

## Ejemplos de invocación

- «Arma la semana 45.»
- «¿De dónde salieron las fuentes de la semana 44?»
- «Clasifica estas imágenes de WhatsApp en las carpetas de área.»
- «Hazme el informe ejecutivo de la semana 46 y su hilo para Don Omar.»
