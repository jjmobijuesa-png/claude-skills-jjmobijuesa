---
name: gastos-whatsapp-gracias-totales
description: |
  Rastrea, extrae e inventaria los GASTOS PERSONALES que Francisco Duque reporta por
  WhatsApp. El marcador es la frase **«gracias totales»** al inicio del mensaje: solo
  esos mensajes son reportes de egreso. Lee el chat por CDP (perfil dedicado), obtiene
  la **FECHA EXACTA** de cada mensaje desde `data-pre-plain-text`, parsea las lineas
  `<monto> <concepto>` (soporta sumas «3.75 + 3.75»), clasifica cada renglon en los
  rubros del sistema (FIJO / VARIABLE / RUBRO ABIERTO) y lo acumula en un libro de
  registro listo para el asiento en el flujo de caja y el cierre mensual.
trigger_phrases:
  - "gastos de whatsapp"
  - "gracias totales"
  - "rastrea los gastos del chat"
  - "inventaria los gastos reportados"
  - "carga los gastos de WA al flujo"
  - "lee los reportes de gasto"
idioma_de_salida: espanol
nivel: aplicada
dominio: finanzas / captura de datos
metadata:
  version: 1.0
  fecha: 2026-08-05
  origen: >
    Pedido del usuario (2026-08-05) como prueba piloto con datos reales. La convencion
    inicial era «Gracias» a secas, pero se corrigio a «gracias totales» el mismo dia
    porque «Gracias» aparece como cortesia en decenas de mensajes del chat y generaba
    falsos positivos.
  relacionada:
    - whatsapp-web-cdp-lectura-envio
    - cfo-mensual-con-claude
    - project-finanza-integral-perfil-millonario
---

# Skill `gastos-whatsapp-gracias-totales`

## Acerca de mi (cargar al arrancar)
Espacio de trabajo: `E:\vars\var 171 9 Finanza Integral`. Libro de registro:
`02 Egresos\Registro WhatsApp\registro_gastos_wa.xlsx`. Los rubros y su clasificacion
salen de `02 Egresos\Fijos\Tipos de rubros fijos.txt` y `02 Egresos\Variables\Egresos variables.txt`.

## Doctrina central
- **El marcador es `gracias totales`** (sin distinguir mayusculas/acentos) al INICIO del mensaje.
  Todo lo que no empiece asi NO se registra, aunque contenga cifras.
  🚦 «Gracias» a secas NO sirve: es cortesia habitual y produce falsos positivos.
- **La fecha manda.** El asiento se hace con la fecha REAL del mensaje, no con la fecha de lectura.
  La fuente de la fecha es el atributo `data-pre-plain-text` de WhatsApp Web.
- **Todo numero es USD.** Convencion declarada por el usuario en el propio chat:
  «siempre los numeros indican valor monetario en dolares».
- **Formato de cada renglon:** `<monto> <concepto>`. El monto admite sumas: `3.75 + 3.75 comida restaurante`
  se registra como DOS consumos del mismo concepto (o uno de 7,50 — ver §Parseo).
- **Las fotos de recibos se archivan.** Instruccion del usuario en el chat: toda foto de recibo
  se descarga y se guarda en `02 Egresos\Comprobantes`.

## Selectores vigentes (verificados 2026-08-05)
🚦 El DOM de WhatsApp Web cambio otra vez: `.message-in` / `.message-out` devuelven **0**.
Lo que SI funciona:

```python
CHATS  = '#pane-side [role="row"]'          # lista de chats
MSGS   = '#main [data-pre-plain-text]'      # mensajes CON metadatos de fecha
PANEL  = '#main div[role="row"]'            # filas de conversacion (fallback)
```

**`data-pre-plain-text` es la mina de oro.** Formato:
`[11:08 p. m., 5/8/2026] Autor: ` → hora, meridiano, **dia/mes/anio** y autor.
Regex probada:
```python
r'\[(\d{1,2}:\d{2})\s*([ap])\.?\s*m\.?,\s*(\d{1,2})/(\d{1,2})/(\d{4})\]\s*(.*?):'
```

## Protocolo paso a paso
0. **Conexion (heredada de [[whatsapp-web-cdp-lectura-envio]]):** adjuntarse por CDP a
   `127.0.0.1:9222` sobre el perfil dedicado `~/.sas-agua-wa/browser_profile`.
   🚦 **NUNCA clicar «Usar aqui»** (roba la sesion y desloguea al usuario).
   🚦 **Regla de una sola pestana:** cerrar duplicadas de `web.whatsapp.com` antes de operar.
   ⏳ **Paciencia en el primer arranque:** WhatsApp muestra «cargando tus chats [N %]» y puede
   tardar **2-4 minutos** en sincronizar. No es un error: esperar a que aparezca `#pane-side`.
1. **Abrir el chat de reportes.** Localizar la fila por nombre en `#pane-side [role="row"]`
   y clicar con `page.mouse.click(x,y)` sobre el centro del `bounding_box()`
   (el `element.click()` reporta exito pero no abre).
2. **Cargar historial:** rueda del raton hacia arriba en bucle, acumulando en un dict por
   `meta+texto` para deduplicar (WhatsApp recicla nodos).
3. **Extraer, filtrar y parsear:** `scripts\leer_gastos_wa.py`.
4. **Clasificar** cada renglon en FIJO / VARIABLE / RUBRO ABIERTO.
5. **Registrar** en `registro_gastos_wa.xlsx` sin duplicar (clave = fecha+hora+concepto+monto).
6. **Asentar** en el flujo del mes correspondiente segun la FECHA del mensaje.

## Parseo de los renglones
| Entrada | Interpretacion |
|---|---|
| `13 comida restaurante` | 1 consumo de 13,00 → «Comida fuera de casa» |
| `3.75 + 3.75 comida restaurante` | suma 7,50 en el mismo concepto (se guarda el desglose en la nota) |
| `340 ... pago a la mutualista Pichincha` | 340,00 → FIJO «Cuota Mutualista» |
| `117 pago al IESS ( habra recibo del pago)` | 117,00 → FIJO «IESS» |
| `3.5 + 2.5 gastos de mascota` | 6,00 → VARIABLE «Mascotas» |
| `9 medicina` | 9,00 → VARIABLE «Medicina» |

Regla: el **primer numero (o cadena de numeros sumados)** del renglon es el monto;
el resto del renglon es el concepto. Los parentesis son notas, no montos.

## Clasificacion (segun las definiciones del usuario)
- **FIJO:** servicios basicos (agua, CNT, CNEL), botellones de agua, cuotas de credito
  (Mutualista 340, IESS 117, Peruzzi 89,90, pago por devolucion 100), CPA, cuotas de prestamos.
- **VARIABLE:** cine, comer fuera, arreglo de vehiculo, ropa, viajes, peajes, pago de IA,
  combustible — y **todo lo que no sea gasto fijo**.
- **RUBRO ABIERTO:** todo lo que no tenga denominacion reconocible, para poder conciliar.

## Que NO hacer / compuertas 🚦
- 🚦 **Solo lectura.** Esta skill NUNCA escribe ni envia mensajes por WhatsApp.
- 🚦 No registrar mensajes que empiecen con «Gracias» a secas: solo **«gracias totales»**.
- 🚦 No inventar la fecha. Si un mensaje no trae `data-pre-plain-text`, marcarlo como
  `fecha=?` y pedirla al usuario antes de asentar.
- 🚦 No duplicar: antes de agregar, comprobar la clave fecha+hora+concepto+monto.
- No asumir el mes: un mensaje del 31 puede reportar un gasto del 30. Si el texto menciona
  una fecha distinta, esa manda y se anota la discrepancia.

## Uso
```bash
"C:\Users\datos\.notebooklm-venv\Scripts\python.exe" ^
  "C:\Users\datos\.claude\skills\gastos-whatsapp-gracias-totales\scripts\leer_gastos_wa.py" "<nombre del chat>"
```
Salida: tabla en consola + `registro_gastos_wa.xlsx` actualizado.

## Aprendizajes que costaron tiempo (no repetir)
1. `.message-in/.message-out` → **0 resultados** en el DOM de agosto 2026. Usar `[data-pre-plain-text]`.
2. El buscador (`input[data-tab="3"]`) a veces no filtra: es mas fiable **recorrer la lista de chats**
   y buscar por nombre.
3. WhatsApp Web tarda **minutos** en la primera sincronizacion; interpretarlo como fallo lleva a
   relanzar Edge y arriesgar la sesion.
4. El historial del navegador es **parcial**: para meses anteriores hay que exportar el chat
   desde el telefono (ver [[whatsapp-web-cdp-lectura-envio]] §6).
