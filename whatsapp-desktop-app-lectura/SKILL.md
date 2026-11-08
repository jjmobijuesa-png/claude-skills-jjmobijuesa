---
name: whatsapp-desktop-app-lectura
description: |
  Lee (y opera) WhatsApp desde la APP DE ESCRITORIO del PC con control de GUI
  (computer-use), no desde WhatsApp Web. Es la vía oficial de esta casa desde el
  17-oct-2026, cuando el perfil Edge dedicado de `whatsapp-web-cdp-lectura-envio`
  quedó DESVINCULADO y volvió a pedir QR. La app del PC ya está sincronizada con
  el teléfono: no hay QR, no hay «Usar aquí», no se le roba la sesión a nadie.
  Resuelve los cuatro bloqueos reales que hacen que los clics «funcionen» sin
  tener efecto.
trigger_phrases:
  - "lee el WhatsApp del PC"
  - "abre la app de WhatsApp"
  - "revisa el chat en WhatsApp escritorio"
  - "busca gracias totales en WhatsApp"
  - "sincroniza con el WA del PC"
idioma_de_salida: espanol
nivel: aplicada
dominio: automatizacion / GUI
metadata:
  version: 1.0
  fecha: 2026-10-17
  estado: production (destilada de la sesion de conciliacion oct-2026)
  reemplaza_en_la_practica: whatsapp-web-cdp-lectura-envio (la via web quedo desvinculada)
  relacionada:
    - gastos-whatsapp-gracias-totales
    - agente-gui-autoaprobado-windows
    - regla-del-primer-tropiezo
    - conciliacion-multicuenta-fdc
---

# `whatsapp-desktop-app-lectura`

> Por qué existe: el 17-oct-2026 la vía web (perfil `.sas-agua-wa` + CDP 9222) devolvió
> «Escanea el código QR»: el dispositivo vinculado había caducado. La app del PC, en
> cambio, estaba viva y sincronizada. Insistir en la web habría costado una re-vinculación
> por QR y el riesgo de «Usar aquí». La app es la vía estable.

## 0. Identidad de la app (verificada)

| Dato | Valor |
|---|---|
| Paquete AppX | `5319275A.WhatsAppDesktop` (v2.2640.100.0) |
| Lanzamiento | `Start-Process "shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"` |
| Proceso lanzador | `WhatsApp.Root.exe` |
| **Proceso que posee la ventana** | **`msedgewebview2.exe`** — es una app WebView2 |

## 1. Los cuatro bloqueos y su solución

| # | Síntoma | Causa real | Solución |
|---|---|---|---|
| 1 | La captura muestra la ventana en **negro** o no la muestra | computer-use enmascara procesos no concedidos, y la ventana **no la posee WhatsApp sino `msedgewebview2.exe`** | `request_access` con **ambos**: `"WhatsApp"` y `"msedgewebview2.exe"` |
| 2 | `open_application` dice «Opened» pero **no hay proceso** | La activación AppX a veces no prende | Verificar con `Get-Process WhatsApp.Root`; si no está, lanzar por `shell:AppsFolder\...` |
| 3 | La app abre y no se ve | Abrió en el **otro monitor** | `switch_display` (en esta máquina: `Built-in Display` y `LG HD`) |
| 4 | El clic reporta **«Clicked»** y no pasa nada; luego falla con *«The desktop shell is frontmost»* | El shell de Windows roba el foco entre llamadas (se agrava si el usuario trabaja en otra pantalla) | `request_access` con **`"File Explorer"`** (queda en tier *click*: clics sí, teclado no). Y **frontear con `open_application` antes de cada tanda** |

## 1.a Ventana GRIS lisa con los botones de la barra visibles (2-nov-2026)

**Síntoma:** con `"WhatsApp"` y `msedgewebview2.exe` ya concedidos, la captura muestra la ventana
**gris uniforme**: los botones de minimizar, maximizar y cerrar están, pero no se ve ni un chat. Ni
maximizar, ni restaurar y volver a maximizar, ni pasar el ratón, ni clicar la barra de título lo
arreglan. El título dice «(6) WhatsApp»: la app está viva.

**Causa real:** el renderizador WebView2 quedó colgado en una app abierta desde la mañana (en esta
corrida llevaba unas 6 h). No es un enmascaramiento: un proceso no concedido se ve como rectángulo
macizo y aquí todos estaban concedidos.

**Solución, a la primera:** reiniciar en frío y volver a maximizar y forzar el foco (§1.bis).
```powershell
Stop-Process -Name WhatsApp.Root -Force; Start-Sleep 4
Start-Process "shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"; Start-Sleep 45
```
🚦 Si hay **dos versiones de WebView2** instaladas (aquí 156.0.4314.50 y .58), conceder `msedgewebview2.exe`
otra vez tras el reinicio si la captura avisa de procesos ocultos: cada versión es una ruta distinta.

**Notas de voz (resuelto el 2-nov-2026):** la app no las transcribe, y el audio en caché está cifrado
(`AC\INetCache\*.enc`). Solo las reenviadas o guardadas quedan en claro, en
`LocalState\sessions\<id>\transfers\<año-semana>\WhatsApp Ptt ….ogg`.
- **Vía que funciona:** grabar el altavoz con `soundcard` (WASAPI loopback) mientras se reproducen y
  transcribir con faster-whisper `medium` en español. Script: `grabar_loopback.py <seg> <salida.wav>`.
- **Reproducción:** WhatsApp encadena los audios consecutivos del mismo remitente. Basta pulsar el primero
  de cada grupo y esperar la duración del grupo; no pulsar uno que ya suena, porque se pausa.
- 🚦 **Si el usuario usa el PC, otra ventana tapa WhatsApp.** Fijar WhatsApp «siempre visible» con
  `SetWindowPos(h, -1, …, 0x43)` durante la grabación y retirarlo al final con `-2`. Antes de clicar,
  `open_application("WhatsApp")`.

## 1.bis Lo que de verdad desbloquea los clics (19-oct-2026)

La fila 4 de arriba se queda corta. `request_access` con «File Explorer» + `open_application`
**no bastó**: dos clics seguidos reportaron «Clicked» sin efecto alguno. Lo que sí funcionó,
y a la primera:

1. **Maximizar la ventana por API, no por clic**, y **forzar el foco** con `AttachThreadInput`
   (la receta de [[agente-gui-autoaprobado-windows]] §4a), todo desde PowerShell:
   ```powershell
   $w = Get-Process WhatsApp.Root | Select-Object -First 1
   [void][F]::ShowWindow($w.MainWindowHandle, 3)   # 3 = SW_MAXIMIZE
   [F]::Force($w.MainWindowHandle)                 # AttachThreadInput + BringWindowToTop + SetForegroundWindow
   ```
   Tras esto **todos los clics entraron**. La ventana pasó de 800x694 a ocupar los 1536x864.
2. 🚦 **Medir antes de suponer el mapeo de coordenadas.** La pantalla real es **1536x864** y el
   marco de captura **1456x819** (factor 0,9479). Confirmar la geometría con `GetWindowRect`
   antes de culpar al DPI: en esta corrida el problema era el foco, no el escalado.

**Corrige el §2.4:** el icono de lupa de la cabecera del chat **SÍ abre** el panel «Buscar
mensajes» — lo que lo impedía era el ancho de la ventana, no el icono. **Con la ventana
maximizada funciona**, y buscar `pdf` devuelve la lista de documentos del chat, que es la
forma rápida de inventariarlos sin desplazarse a ciegas.

## 1.ter Descargar adjuntos: ciclo de dos clics (19-oct-2026)

Cada burbuja de documento trae **«Guardar como…»**. El diálogo de Windows pertenece a
WhatsApp (tier *full*), así que no lo frena el candado de «File Explorer».

- **El diálogo recuerda la última carpeta**: tras fijar el destino una vez, cada libro
  siguiente es **«Guardar como…» → «Guardar»**, dos clics, sin teclear ruta.
- El nombre viene prerrelleno con el del archivo original: no hay que escribirlo.
- Confirmación: aparece el aviso «Se guardó el archivo». **Verificar siempre en disco**, que es
  canal independiente.
- 🚦 **Límite real de la app:** el escritorio solo tiene el historial sincronizado desde que se
  vinculó. En esta corrida eran **7 días** (desde el 12-oct-2026), con el aviso explícito
  «Usa WhatsApp en tu teléfono para ver mensajes anteriores al 15/9/2023». **Los adjuntos más
  viejos no están y no se pueden bajar desde el PC**: hay que abrirlos desde el teléfono.

## 2. Procedimiento

1. **Conceder de una sola vez:** `request_access(["WhatsApp", "msedgewebview2.exe", "File Explorer"])`.
   🚦 `"WhatsApp.Root.exe"` y `"Msedgewebview2"` **no** son nombres válidos: el resolutor los rechaza
   y **corta la llamada entera**. Usar exactamente `"WhatsApp"` y `"msedgewebview2.exe"`.
2. **Arrancar y esperar.** Desde frío la app tarda **35-45 s**: primero pantalla con el logo,
   luego barra de progreso, luego la lista de chats. **No clicar durante la carga.**
3. **Abrir el chat** clicando su fila en la columna izquierda. Esperar a que desaparezca el
   spinner del panel de mensajes (otros 15-20 s la primera vez).
4. **Buscar.** 🚦 Con la ventana angosta (~800 px) **el icono de lupa de la cabecera del chat
   NO abre el panel de búsqueda** — el clic entra y no pasa nada. Usar el **buscador global**
   de la columna izquierda («Buscar un chat o iniciar…»): devuelve una sección **«Mensajes»**
   con `chat · fecha · fragmento`. Clicando el resultado salta al mensaje dentro del chat.
5. **Leer por captura.** El texto se lee de la imagen; los comprobantes fotografiados se leen
   como imagen. Para OCR de recibos largos: [[feedback_pdf_escaneado_ocr_rapidocr]].

## 3. Callejón sin salida — NO reintentar

**`WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS=--remote-debugging-port=NNNN` NO funciona** para
adjuntarse por CDP a WhatsApp Desktop. La variable se fija bien en el entorno del usuario,
pero la app lanzada por activación **AppX no hereda ese entorno** y el puerto nunca abre.
Probado el 17-oct-2026 con el puerto 9224. Si vuelve a tentarle la idea de «es Chromium,
me adjunto por CDP»: ya se intentó y no va. La vía es GUI.

## 4. Qué NO hacer 🚦

- 🚦 **Nunca** pulsar «Usar aquí» en WhatsApp Web (regla cero de `whatsapp-web-cdp-lectura-envio`).
  En la app de escritorio ese diálogo no aparece: otra razón para preferirla.
- 🚦 No teclear en el shell: el grant de «File Explorer» es **solo clic**. Para comandos, Bash.
- 🚦 No dar por buena una captura sin leer el aviso de procesos enmascarados que la acompaña:
  ahí es donde el sistema dice qué proceso falta conceder.
- 🚦 Tres clics sin efecto = parar y barrer ([[regla-del-primer-tropiezo]]), no un cuarto clic.

## 5. Hallazgo de la primera corrida (17-oct-2026)

Buscando `gracias totales` en el chat **Bs Inmobiliaria Mobijuesa**: **un solo resultado**,
del **14/09/2026 15:21** (editado 15:24), con comprobante fotografiado de **Mutualista
Pichincha — recaudación IESS**:

```
Gracias totales
$ 11.50 Agua
$ 120 pago iess
$ sello 25
$ 8.58 + $ 12.33 + $ 4.86 alimentos
$ 10 donación
$ 3.75 + $ 6.25 alimentos      (20:11)
```
Total **202,27**. 🚦 **Desde el 14-sep no hay más reportes**, mientras el banco registra
15.992,95 de egresos solo en octubre: la captura por WhatsApp dejó de alimentarse y el
flujo quedó ciego. Ver [[gastos-whatsapp-gracias-totales]].

## 🚦 Notas de voz con el usuario en el PC (5-nov-2026)

- **«Siempre visible» le tapa la pantalla al usuario** y él reduce la ventana: la maximización se pierde y los clics caen en otra parte. Las grabaciones salen en silencio sin avisar.
  Con el usuario presente, no fijar la ventana: trabajar en su tamaño pequeño, midiendo las coordenadas en cada captura.
- **Medir antes de transcribir:** calcular la energía por segundo del WAV. Una transcripción vacía casi siempre es que no sonó, no que Whisper falló.
- **El encadenado se corta** en un documento o en un mensaje propio: los audios posteriores hay que pulsarlos aparte.
- **Una miniatura de foto abre el visor**, y una vez abierto el visor el botón X puede no responder si la ventana perdió el foco. Salir con Escape tras recuperar el foco.
