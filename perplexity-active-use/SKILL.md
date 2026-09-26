---
name: perplexity-active-use
description: |
  Usa Perplexity en modo ACTIVO (no sólo lectura): redacta una pregunta,
  la inyecta en el textarea, dispara el submit, espera la respuesta
  streamed y devuelve el texto + las URLs citadas. Funciona sobre la
  sesión logueada del usuario en Edge debug (puerto 9222) vía la
  herramienta Chrome MCP `javascript_tool` (DOM-aware, no requiere
  permisos de "click pixel").

  Esta skill NO sustituye a WebSearch ni a Nimble; los complementa
  cuando se necesita la fuerza de razonamiento de Perplexity Pro y la
  curación de fuentes que el usuario ya tiene como contexto en su
  cuenta (mobijuesa JJ).

  Resultado: cada consulta se persiste en
  `E:\vars\var 5\Perplexity-consultas\YYYY-MM-DD_<slug>.md` con la
  pregunta, la respuesta, las URLs citadas y la URL canónica del hilo
  para poder volver a abrirlo.

trigger_phrases:
  - "pregúntale a perplexity"
  - "consulta perplexity"
  - "usa perplexity activamente"
  - "lánzale a perplexity"
  - "perplexity pro investiga"

idioma_de_salida: español neutro
nivel_madurez: aplicada
fuente: sesión 2026-06-26 (capacidad nueva pedida por el usuario)
---

# Perplexity activo — desde Edge debug

## Doctrina

Perplexity es la fuente de razonamiento + búsqueda más sólida que el
usuario tiene como suscripción. Usarla sólo como lectura es desperdiciar
la mitad del valor. Esta skill agrega la capacidad activa:

1. **Inyecta pregunta vía DOM** (no requiere computer-use ni teclado).
2. **Espera streaming** con detección de estabilidad (4,5 s sin cambios
   = respuesta terminada).
3. **Captura URLs** citadas en la respuesta para archivo + verificación.
4. **Persiste** en `Perplexity-consultas/` con fecha + slug + URL del
   hilo creado.

## ⭐ Método PRIMARIO (verificado 2026-07-12): Playwright directo

La extensión Claude-in-Chrome **bloquea** la navegación a `perplexity.ai`
(`Navigation to this domain is not allowed`). El método que SÍ funciona
—y el que se debe usar por defecto— es Playwright directo sobre el perfil
persistente ya logueado, exactamente como las skills de Gmail/bookmarks:

```
python "C:\Users\datos\.claude\skills\perplexity-active-use\scripts\ask_perplexity_playwright.py" "<pregunta>" <slug>
```

- Perfil: `C:\Users\datos\.notebooklm\browser_profile_jjm` (jjmobijuesa@gmail.com).
- Requiere solo `pip install playwright` (usa `channel="msedge"`, sin binarios).
- Abre Edge headed fuera de pantalla, inyecta la query en el
  `div[contenteditable]`, espera estabilidad del `innerText`, extrae la
  respuesta (`div.prose`) + URLs citadas, y persiste el `.md`.
- Luego Claude lee el `.md` y destila el 20% accionable.

El flujo por Chrome MCP de abajo queda como **fallback histórico** (solo
si algún día se habilita `perplexity.ai` en la allowlist de la extensión).

## ⭐ Leer un hilo YA EXISTENTE de la biblioteca (verificado 2026-09-05)

Distinto de preguntar: aquí se recupera una conversación que el usuario ya tuvo.

- **Perfil según la cuenta:** `browser_profile_edge` = **mobijuesa360** (el mismo de NotebookLM);
  `browser_profile_jjm` = jjmobijuesa. Elegir el que corresponda a la cuenta que pide el usuario.
- La biblioteca vive en `https://www.perplexity.ai/library`.
- 🚦 **Los `<a>` de la biblioteca tienen `innerText` VACÍO.** Filtrar anchors por texto devuelve
  cero resultados y `get_by_text(...).click()` da timeout. El título está en un `div` hermano, no
  dentro del enlace.
- **Lo que sí funciona:** recolectar `href` de `a[href*="/search/"]` — vienen **en el mismo orden
  que el panel lateral** — y navegar directo a `https://www.perplexity.ai/search/<uuid>`.
  Verificar con `pg.title()`, que sí trae el título del hilo.
- Tomar un `screenshot` de la biblioteca es la forma más rápida de mapear título ↔ posición y de
  confirmar qué cuenta está logueada (aparece abajo a la izquierda).
- Rechazar cookies opcionales antes de interactuar (`get_by_role("button", name="Rechazar
  opcionales")`); el banner intercepta clics.
- Para volcar el hilo completo: subir con `mouse.wheel(0,-5000)` varias veces, luego bajar hasta
  que `document.body.innerText.length` se estabilice.

Script de referencia: `scratchpad/pplx_leer_hilo.py` del proyecto donde se usó.

## Pre-requisitos (método fallback por extensión)

- Edge debug corriendo en `localhost:9222` con sesión Perplexity
  logueada (perfil `mobijuesa JJ`). Si no está, correr
  `E:\vars\var 5\X-com guardados\start_edge_debug.bat`.
- Chrome MCP `mcp__Claude_in_Chrome__*` conectado.

## Flujo de uso por Claude

```
1. tabs_context_mcp → encontrar/crear tab Perplexity
2. navigate → https://www.perplexity.ai/ (si no estás)
3. javascript_tool con scripts/submit_query.js
   (reemplazar __QUERY_PLACEHOLDER__ por la pregunta real,
    escapando comillas)
4. Parsear el JSON devuelto:
     { query, length, text, truncated }
5. get_page_text para capturar las URLs ya enriquecidas
6. Guardar en Perplexity-consultas/<fecha>_<slug>.md
```

Plantilla del archivo persistido:

```markdown
# Consulta Perplexity — <slug>
- Fecha: <ISO>
- Pregunta: <Q>
- URL del hilo: <https://www.perplexity.ai/search/...>
- Fuentes citadas (top 10):
  - <url 1>
  - <url 2>

## Respuesta

<texto streamed completo>
```

## Compuertas 🚦

1. **No relanzar la misma query** si ya existe archivo del día (revisar
   primero `Perplexity-consultas/` por slug).
2. **No insertar credenciales** en la query; el navegador está logueado.
3. **No pretender que Perplexity es "buscador neutral"**: tiene sesgo
   editorial; siempre verificar URL citada.
4. **Timeout 60 s** — si Perplexity sigue streaming pasados los 60 s,
   capturar lo que haya y marcar `truncated: true`.
5. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cómo depurar si falla

- `no textarea encontrado` → Perplexity cambió el DOM. Inspeccionar con
  `read_page` y ajustar selector en `submit_query.js`.
- Respuesta vacía → puede ser captcha/throttle; abrir Perplexity en
  Edge a la vista del usuario y reintentar.
- `Navigation to this domain is not allowed` → añadir `perplexity.ai`
  a la allowlist de la extensión Claude in Chrome (la extensión, no
  settings.json — está documentado en `update-config`).
- **La APP de escritorio se cuelga** (ventana en blanco que solo muestra
  el menú «View → Toggle Developer Tools») → el render webview de Electron
  no cargó. NO basta con reabrir: el proceso colgado intercepta el nuevo
  lanzamiento y vuelve a la ventana vacía. Hay que cerrar TODO el árbol y
  relanzar:
  ```powershell
  $pp = Get-Process Perplexity -ErrorAction SilentlyContinue; $ids=@($pp.Id)
  Get-CimInstance Win32_Process -Filter "Name='msedgewebview2.exe'" |
    Where-Object { $ids -contains $_.ParentProcessId } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -EA SilentlyContinue }
  $pp | Stop-Process -Force -EA SilentlyContinue; Start-Sleep 2
  Start-Process (Join-Path $env:LOCALAPPDATA "Programs\Perplexity\Perplexity.exe")
  ```
  Mata solo los `msedgewebview2.exe` hijos de Perplexity (no toca
  WhatsApp/Teams/Edge). Señal de éxito: relanza con 8–9 procesos y la
  ventana carga el contenido. *Las skills locales (.md) NUNCA causan esto;
  son inertes.* Verificado 2026-06-28.

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — registra esta capacidad como
  fuente activa.
- [[youtube-corpus-jjmobijuesa]] — fuente complementaria en video.
- [[anthropic-skills:notebooklmskill]] — destino natural de las
  conclusiones (subir como nota al cuaderno temático).
