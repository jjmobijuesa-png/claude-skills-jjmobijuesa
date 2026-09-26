---
name: whatsapp-web-cdp-lectura-envio
description: Lee y envía mensajes de WhatsApp Web conectándose por CDP a un Edge lanzado con perfil DEDICADO. Resuelve el bloqueo de Chromium 136+ sobre el perfil por defecto y los selectores obsoletos tras el rediseño del DOM de WhatsApp (2026). Incluye guardas de destinatario obligatorias antes de escribir. Triggers — "lee el chat de X en WhatsApp", "envía un WhatsApp a X", "extrae la conversación de WA", "responde por WhatsApp".
metadata:
  type: skill
  version: 1.1
  fecha: 2026-07-20
  estado: production (v1.1 estabilizada — regla cero anti «Usar aquí»; adjuntar-no-relanzar; guarda por cabecera)
  reemplaza: sas-agua-whatsapp-envio v0.3 (archivada; selectores obsoletos)
---

# whatsapp-web-cdp-lectura-envio

> Destilada el 2026-07-19 tras resolver, por prueba y error, tres bloqueos encadenados. Sustituye a la skill archivada `sas-agua-whatsapp-envio`, cuyos selectores ya no funcionan.
> **Estabilizada el 2026-07-20** tras un incidente: clicar «Usar aquí» cerró la sesión de WhatsApp del usuario. Ver §0.

## 0. 🚨 REGLA CERO — NUNCA robar la sesión (estabilidad)

**PROHIBIDO clicar «Usar aquí» / «Use here».** Ese botón NO es «entrar»: es una TOMA DE CONTROL que arrastra la sesión activa de otra ventana hacia esta, y en la práctica **desloguea la sesión del usuario** (el 2026-07-20 dejó WhatsApp Web pidiendo QR y cerró la cuenta que el usuario tenía abierta). El destino queda peor que antes y hay que re-vincular con QR.

**Qué significa cada pantalla y qué hacer:**

| Pantalla | Qué significa | Acción correcta |
|---|---|---|
| Lista de chats (`#pane-side`) visible | Sesión activa y sana en ESTE perfil | Operar normal |
| «WhatsApp está abierto en otra ventana · Usar aquí» | Hay **otra pestaña/ventana del MISMO perfil** con WA abierto | **NO clicar «Usar aquí».** Cerrar la pestaña WA DUPLICADA de este perfil y quedarse con una sola. Si sigue, abortar y avisar al usuario. |
| «Escanea el código QR» | El perfil dedicado no está vinculado | Pedir al usuario que escanee el QR **una sola vez**. Es un dispositivo vinculado independiente (WhatsApp permite hasta 4); coexiste con el teléfono y con el WA del usuario. |
| «Cerrando sesión» | Se está desvinculando | No hicimos bien algo; detenerse y reportar. |

**Principio:** el perfil `.sas-agua-wa` es un **dispositivo vinculado propio y permanente**. Una vez escaneado, NO se vuelve a tocar el vínculo. Nuestro trabajo es **adjuntarse (CDP) a su sesión ya viva**, nunca relanzar-y-tomar-control. Un perfil dedicado y vinculado **jamás** debería mostrar «abierto en otra ventana» respecto del teléfono; si lo muestra, es por una **pestaña WA duplicada dentro del propio perfil** → cerrar la duplicada, no tomar control.

## 1. Los tres bloqueos y sus soluciones

| Bloqueo | Síntoma | Solución |
|---|---|---|
| **Perfil por defecto** | `--remote-debugging-port` no levanta; puerto 9222 muerto | **Chromium 136+ bloquea la depuración remota sobre el perfil por defecto** (antirrobo de cookies). Usar **`--user-data-dir` dedicado**. |
| **DOM reescrito (2026)** | `#main`, `.copyable-text`, `data-pre-plain-text`, `[role="listitem"]` → todos devuelven 0 | Los chats son **`#pane-side [role="row"]`**. El panel de conversación se localiza **por geometría**, no por selector. |
| **Clic que no abre** | `element.click()` reporta éxito pero la conversación no carga | Usar **`page.mouse.click(x, y)`** con coordenadas del `getBoundingClientRect()`: evento de ratón real. |

## 2. Arranque estable — ADJUNTAR primero, relanzar solo si hace falta

**Orden obligatorio (script listo: `scripts/wa_connect.py`):**

1. **¿Ya hay sesión viva?** `curl http://127.0.0.1:9222/json/version`. Si responde → **adjuntarse por CDP** (`connect_over_cdp`) y REUTILIZAR la pestaña WhatsApp existente. No lanzar Edge, no abrir otra pestaña WA. Esto es lo normal y lo que NO rompe nada.
2. **¿9222 muerto?** Antes de lanzar, matar SOLO los Edge de este perfil (nunca el Edge principal del usuario):
   ```powershell
   Get-CimInstance Win32_Process -Filter "Name='msedge.exe'" |
     Where-Object { $_.CommandLine -like '*sas-agua-wa*' } |
     ForEach-Object { Stop-Process -Id $_.ProcessId -Force -EA SilentlyContinue }
   ```
3. **Lanzar UNA instancia con UNA sola pestaña WA:**
   ```powershell
   $edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
   $prof = "$env:USERPROFILE\.sas-agua-wa\browser_profile"
   Start-Process $edge -ArgumentList "--user-data-dir=`"$prof`"","--remote-debugging-port=9222",
     "--no-first-run","--no-default-browser-check","--window-position=2200,2200",
     "--window-size=1300,950","https://web.whatsapp.com/"
   ```
4. **Verificar el estado (§0), NUNCA clicar «Usar aquí».** Si aparece «abierto en otra ventana», cerrar la pestaña WA duplicada de ESTE perfil (dejar una) y recargar; si persiste, abortar y avisar.
5. **Regla de una sola pestaña:** si al adjuntarse hay ≥2 pestañas `web.whatsapp.com`, cerrar todas menos una ANTES de operar. Dos pestañas WA en el mismo perfil = el diálogo «Usar aquí» reaparece.

Verificar puerto: `Invoke-RestMethod http://127.0.0.1:9222/json/version`
Primera vez (o si aparece QR): **el usuario escanea el QR UNA vez**; luego el vínculo persiste y solo nos adjuntamos.

## 3. Selectores vigentes (2026-07)

```python
SEARCH = 'input[data-tab="3"]'          # buscador: es un INPUT, no un div contenteditable
FILAS  = '#pane-side [role="row"]'      # cada chat de la lista

# Panel de conversación: por GEOMETRÍA (mitad derecha, alto > 200px)
PANEL_JS = """()=>{const W=innerWidth; let t='';
  document.querySelectorAll('div').forEach(e=>{const r=e.getBoundingClientRect();
    if(r.x>W*0.33 && r.width>W*0.25 && r.height>200){
      const x=e.innerText||''; if(x.length>t.length) t=x;}});
  return t;}"""

# Caja de texto: contenteditable en la franja inferior derecha
CAJA_JS = """()=>{const W=innerWidth;
  for(const e of document.querySelectorAll('div[contenteditable="true"]')){
    const r=e.getBoundingClientRect();
    if(r.x>W*0.33 && r.y>innerHeight*0.65 && r.width>150)
      return {x:Math.round(r.x+r.width/2), y:Math.round(r.y+r.height/2)};}
  return null;}"""
```

## 4. 🚦 GUARDAS DE DESTINATARIO — obligatorias antes de escribir

**Regla dura: nunca teclear una sola letra sin confirmar el chat abierto por partida doble.**

1. **Guarda 1** — la fila clicada debe casar con el patrón del destinatario (nombre **y** apellido cuando haya homónimos).
2. **Guarda 2** — leer **solo la CABECERA del chat** (`#main header`) y exigir que contenga el nombre objetivo. **No leer el panel completo:** el cuerpo del chat contiene mensajes antiguos que pueden mencionar a OTRA persona (el 2026-07-20 el historial del chat destino mencionaba «Don Omar» y la guarda que leía todo el panel abortó por falso positivo). La cabecera es el nombre del contacto, no el contenido.

```python
HEADER_JS = """()=>{const h=document.querySelector('#main header')||document.querySelector('header');
  return h ? (h.innerText||'').trim() : '';}"""
head = pg.evaluate(HEADER_JS)
if TARGET.lower() not in head.lower():      sys.exit("ABORTADO: destinatario no confirmado en la CABECERA")
if FORBID and FORBID.lower() in head.lower(): sys.exit("ABORTADO: la cabecera contiene el contacto prohibido")
```

**Añadir un FORBID** (un nombre que NUNCA debe recibir esta prueba, p.ej. el contacto real cuando se envía a una línea de prueba) y verificarlo **solo contra la cabecera**.

**Verificación POST-envío (obligatoria, §8):** tras `Enter`, confirmar que el texto salió leyendo los mensajes salientes, no la cabecera:
```python
OUT_JS = """()=>{const a=[...document.querySelectorAll('div.message-out')];
  return a.length? a[a.length-1].innerText : '';}"""
```
Buscar un marcador único del mensaje (una cifra, un título) en ese texto. Si no aparece, **NO declarar enviado**.

**Por qué la cabecera y no el panel:** el 2026-07-19 verificar por «el elemento más alto» falló 3 veces (leyó avisos y mensajes sueltos). El 2026-07-20, leer el panel COMPLETO dio falso positivo del FORBID por el historial. `#main header` es estable, es el nombre del contacto, y no arrastra el cuerpo del chat. Había 16 «Villavicencio» en la agenda: un envío al chat equivocado es irreversible.

## 5. Escribir con tildes

`page.keyboard.type()` con `delay` **distorsiona acentos y eñes**. Usar **`page.keyboard.insert_text()`**, que inserta el texto directamente.
Saltos de línea sin enviar: `Shift+Enter`. Enviar: `Enter`.

## 6. ⚠️ Límite infranqueable: el historial es PARCIAL

WhatsApp Web muestra el aviso **«Usa WhatsApp en tu teléfono para ver mensajes anteriores al <fecha>»**. El navegador **solo descarga historial reciente**; el completo vive en el móvil.

**Consecuencia:** para análisis histórico (negociaciones, cotizaciones), **exportar el chat desde el teléfono NO es un plan B, es el método correcto** (menú del chat → Exportar chat → sin archivos). Ningún scraping recupera lo que el navegador nunca descargó.

## 7. Riesgo conocido: dispositivo vinculado

Vincular WhatsApp Web **puede desvincular la app nativa de Windows** (límite de dispositivos de Meta). Ver `sas-agua-whatsapp-envio` archivada §motivo. Preguntar antes si el usuario depende de la app de escritorio. Alternativa limpia a futuro: **API de WhatsApp Business**, que convive con la app personal.

## 8. Reglas de conducta

- **Comunicación externa = borrador → revisión → envío**, salvo instrucción explícita del usuario para ese envío concreto.
- **El buzón es un recurso compartido**: el usuario puede estar usando WhatsApp en paralelo. **Abrir siempre el chat objetivo de forma explícita**; nunca asumir cuál está abierto.
- Reportar el envío solo tras **verificarlo en el panel**, nunca por el retorno del clic.

## 9. Referencias

- `E:\vars\var 13 RedSerAk\SAS-Agua-Cerebro-Operativo\_archived_skills\sas-agua-whatsapp-envio\` — antecesora.
- [[feedback-aprendido]] §8 (envío verificado) y §9 (revisar lo archivado antes de declarar imposible).
- Scripts de referencia en el scratchpad de la sesión 2026-07-19 (`wa_v3.py`, `wa_kleper.py`, `wa_alvimar_send.py`).
