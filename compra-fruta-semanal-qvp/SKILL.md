---
name: compra-fruta-semanal-qvp
description: >
  Analiza el «Reporte de Compra de Palma Sem #NN» que asiscon03@quevepalma.com envía
  cada semana a jjmobijuesa@gmail.com, con sus cuatro adjuntos, y lo contrasta con la
  semana anterior y con el grupo de WhatsApp «Calidad d fruta agroaereo». Extrae lo que
  el reporte NO dice: el precio de referencia escondido al pie del correo, la
  reliquidación sistemática a la parte relacionada, la dispersión de precios entre
  proveedores, el castigo con signo negativo, la cobertura real del muestreo de calidad
  y el porcentaje de guineensis frente a las variedades de peor rendimiento.
  Disparadores: "reporte de compra de palma", "compra de fruta semana", "asiscon03",
  "analiza la compra de fruta", "precio de la fruta esta semana", "escasez de guineensis",
  "calidad de la fruta", "cuánto pagamos por la fruta".
---

# Compra de fruta semanal — Quevepalma

## 0. Qué llega y de dónde

| | |
|---|---|
| **Remitente** | `asiscon03@quevepalma.com` |
| **Asunto** | `Reporte de Compra de Palma Sem #NN del 2026` |
| **Buzón** | `jjmobijuesa@gmail.com` (va en copia; los destinatarios son Don Omar y la Gerencia) |
| **Cadencia** | Semanal, normalmente lunes por la tarde. A veces llega una versión **ACTUALIZADO** horas después: **usar siempre la última** |
| **Adjuntos** | `tipo de fruta por proveedor sem#NN.xls` · `COMPRAS NN.xlsx` · dos PDF (planta y sucursal) · imágenes de firma |

**El cuerpo del correo es tan importante como los adjuntos**: trae tres tablas en texto plano
(acopios con precio, ingreso diario por acopio, ingreso por extractora) **y un cuarto bloque sin
título** que es el que casi nadie lee. Ver §2.

## 1. Cómo se descargan los adjuntos

Gmail MCP devuelve metadatos, no binarios. Usar [[gmail-attachments]]:

```
python "$env:USERPROFILE\.claude\skills\gmail-attachments\scripts\download_all_zip.py" jjm "<...>\Actas\sem NN\Adjuntos compra fruta" <threadId>
```

Localizar el hilo con `search_threads` y `from:asiscon03@quevepalma.com`. El `.xls` es formato
Excel antiguo: se lee con **xlrd**, no con openpyxl.

## 2. 🔑 El bloque de precio de referencia (lo que nadie mira)

Al final del cuerpo del correo, después de la tabla de ingresos diarios, hay un bloque suelto con
tres columnas repetidas: **toneladas · un precio · un importe**. Ese precio es una **referencia**
(205 para casi todos los acopios, 202,33 para Río Coca, 225 para Grupo Agroaéreo en ago-2026).

**La cuenta que hay que hacer siempre:**

```
exceso = Σ (precio_real_acopio − precio_referencia_acopio) × toneladas_acopio
```

Valores observados: **semana 33 = 68.262 · semana 34 = 39.740**. Anualizado al ritmo de la 34 son
**2,07 millones de dólares**, equivalentes a **2,19 puntos de margen bruto** sobre ventas de 94,3 M.

🚦 **Sigue pendiente confirmar qué es esa referencia** (meta presupuestaria, precio de tabla o
comparación de mercado). Presentar la cifra siempre con esa salvedad.

## 3. La reliquidación: revisar SIEMPRE

**Grupo Agroaéreo es el único acopio que recibe reliquidación**, y al dividirla por el tonelaje da
**exactamente 10,00 dólares por tonelada, semana tras semana**. No es un ajuste: es un premio
sistemático. Al ritmo actual, **703.451 al año**.

Agro Aéreo concentra la mayoría accionaria de Quevepalma y Agro Aéreo S.A. es además el mayor
proveedor individual (903,26 t en la semana 34). **Es operación con parte relacionada**: exige
acuerdo escrito con fundamento técnico, aprobación con abstención y revelación contable.
Ver [[negociacion-parte-relacionada-familiar]].

## 4. El archivo de proveedores (`tipo de fruta por proveedor`)

Pese al nombre, **no trae la variedad**: es la lista de proveedores. Columnas útiles (base 0):

| col | campo |
|---|---|
| 1 | Código · 2 Proveedor |
| 14 | Ticket (número de viajes) |
| 15 | **Neto** (toneladas) |
| 17 | **Castigo** |
| 21 | Precio |
| 26 | **Liquidado** |

Filas de datos desde la 15; la fila con `TOTAL REPORTE` cierra (col 14/15/17 y el total en col 24).

**Qué calcular:**
- **Dispersión de precio.** En la semana 34: mínimo 125,00 · máximo 256,58 · rango **105 %** ·
  mediana 200,39 · ponderado 215,03. Tramos: el **18,8 % del volumen se compró a 230 o más**,
  entre solo 14 proveedores.
- **Signo del castigo.** 🔑 **Hay castigos NEGATIVOS**, que son créditos a favor del proveedor.
  Semana 34: 42 proveedores y **30,7 % del volumen** con castigo negativo, frente a 46,7 % con
  castigo positivo y 22,5 % en cero.
- **Concentración.** Top 1 = 14,9 % · top 10 = 43,9 % · top 50 = 71 %.

## 5. El archivo de calidad (`COMPRAS NN.xlsx`)

Una hoja por día (`AGOSTO-17`…). Cabecera en fila 2, datos desde la 3. Campos: fecha, semana,
proveedor, hacienda, ticket, entrada, salida, **peso neto**, **VARIEDAD**, tamaño de muestra (80),
conteos de defecto y sus porcentajes.

🚦 **Filtrar por variedad alfabética** (`GUINENSIS`, `COARI`, `TAISHA`…): las filas de totales
diarios traen números en esa columna y contaminan cualquier agregación.

**La medición que hay que hacer primero — la cobertura:**

> semana 34: **2.237,70 t en 274 tickets** con registro de calidad, sobre **6.061,18 t en 967
> tickets** comprados = **36,9 % del tonelaje y 28,3 % de los tickets**.

Y el contraste que duele: **el castigo se aplicó sobre el 46,7 % del volumen y solo el 36,9 %
tiene muestra**. Hay volumen castigado sin muestra que lo respalde. No es acusación: es que **no
es verificable con el registro disponible**.

**Calidad por variedad (semana 34, ponderada por tonelaje):**

| Variedad | % del muestreo | % maduro | % malformación |
|---|---|---|---|
| **GUINENSIS** | 92,5 % | 93,5 % | **0,63 %** |
| COARI | 4,1 % | 75,6 % | **14,64 %** |
| TAISHA | 3,4 % | 84,4 % | **9,97 %** |

## 6. La escasez de guineensis: dónde se ve

**Regla observada: la escasez no aparece en el volumen, aparece en el precio.** En la semana 34 el
volumen se sostuvo (6.061 t contra 6.056 de la 33) y la guineensis siguió siendo el 92,5 % de lo
muestreado. Lo que cambió fue **cuánto hubo que pagar por conseguirlo**.

**El riesgo a vigilar es la sustitución.** Si la guineensis escasea y se compensa con Coari y
Taisha, la malformación salta de 0,63 % a 10-15 % y eso pega en la tasa de extracción, justo donde
el margen de la extractora ya cayó de 12,3 % a 1,8 %.

**Indicador a llevar al comité:** porcentaje de guineensis sobre el total recibido, por semana,
junto al precio promedio pagado. Dos líneas.

## 7. El grupo de WhatsApp «Calidad d fruta agroaereo»

38 participantes. Los inspectores reportan camión por camión con formato constante:
*Hda. X — N racimos verdes — N mal formados — Chofer: Sr. …* más foto.

Se lee con [[whatsapp-web-cdp-lectura-envio]]. 🚦 Dos trampas resueltas:
- Al arrancar el perfil dedicado, WhatsApp tarda **varios minutos** en «Cargando tus chats»;
  esperar a que exista `#pane-side` antes de operar.
- El panel está **virtualizado**: capturar el texto una sola vez al final devuelve solo lo
  renderizado. Hay que **bajar al fondo, luego subir por tramos con la rueda del ratón acumulando
  líneas únicas** (ver `wa_calidad_v3.py` en la carpeta de la semana 34).

**Lo que aporta y el archivo no:** el conteo absoluto de defectos por viaje y por chofer, la
variedad declarada en campo, y **observaciones operativas que no entran a ningún sistema**.

Correlaciones halladas en la semana 34: la malformación se concentra en San Martín 4 y 5, mismo
transportista, variedad Coari o Taisha —**coincide con el Excel**, lo que valida ambas fuentes—; y
**Pepita concentra el 45 % de los racimos verdes reportados**.

## 8. Errores de forma recurrentes del reporte

Se repiten semana a semana y conviene pedir que se corrijan de una vez:
encabezado con el **número de semana equivocado** · dos bloques titulados «SEMANA #4 DEL 2026» ·
fila «% Semanal» de Ercilia con un número suelto en vez de porcentaje · columna «% TOTAL» que
suma porcentajes de bases distintas y da 861 % · el archivo de calidad con la semana anterior en
su columna · diferencia de decenas de dólares entre el total del `.xls` y el del correo.

## 9. Guion del análisis (el orden importa)

1. **Empezar por lo bueno si lo hay.** En la 34 el precio bajó 2,2 % con el mismo volumen: 27.754
   menos que la semana anterior. El reporte no lo destaca y conviene que alguien lo haga.
2. Exceso sobre el precio de referencia, y su variación contra la semana previa.
3. Reliquidación de la parte relacionada.
4. Dispersión de precio y signo del castigo.
5. Cobertura del muestreo, antes de opinar sobre la calidad.
6. Variedad y escasez.
7. WhatsApp: correlaciones y lo que se pierde.
8. Errores de forma.
9. Acciones con responsable y plazo.

## 10. Compuertas 🚦

- **Nunca afirmar irregularidad.** Todo lo hallado admite explicación legítima. Lo que se señala
  es que **falta el documento que la explique**, no que exista una falta.
- **Decir siempre la cobertura antes que el resultado de calidad.** Afirmar «buena calidad» sobre
  un muestreo del 36,9 % sin decir que es el 36,9 % es el error más fácil de cometer.
- **Contrastar siempre con la semana anterior.** Una sola semana es una fotografía de algo que se
  mueve.
- **Usar la última versión** del correo cuando llegue un «ACTUALIZADO».
- Al presentar a la Presidencia, respetar [[voz-y-tono-usuario]] y no usar `≈` ni `~`.

## Skills hermanas

[[gmail-attachments]] · [[whatsapp-web-cdp-lectura-envio]] ·
[[control-financiero-semanal-qvp]] (la vara: margen de equilibrio 3,63 %) ·
[[comite-cuarto-guerra-qvp]] · [[negociacion-parte-relacionada-familiar]] ·
[[forrester-efecto-latigo-sistemas]] · [[poder-cinco-leyes-estructura]] (por qué el dato
disperso en un chat es un problema de estructura, no de disciplina).

Caso trabajado: `Actas\sem 34\SEM34_Analisis_Compra_de_Fruta` + `Datos procesados` + `Scripts`.
