---
name: ui-tars-desktop-control-local
description: |
  Delega al agente UI-TARS Desktop (ByteDance, ya instalado en
  C:\Users\datos\AppData\Local\UiTars\) las tareas que requieren
  CONTROL REAL de la GUI del escritorio Windows — mover el mouse,
  hacer clics y escribir sobre aplicaciones nativas SIN API (Excel con
  macros, ERP legacy, apps de escritorio, ventanas modales). Es el
  ÚNICO valor que UI-TARS aporta y que Claude Code no cubre por su
  restricción de tier en computer-use.

  Corre 100% LOCAL: un modelo de visión (qwen2.5vl:7b) en Ollama ve la
  pantalla y decide los clics; ningún dato sale del computador.

  Esta skill NO controla el mouse desde Claude Code: prepara el
  entorno (Ollama + modelo de visión), arranca UI-TARS Desktop, y le
  entrega al usuario la tarea redactada en español para pegar en la
  app. Claude Code sigue siendo el cerebro que planifica; UI-TARS es
  la mano que ejecuta sobre el escritorio.

trigger_phrases:
  - "controla el escritorio"
  - "abre esa app de Windows y haz"
  - "automatiza el Excel con macros"
  - "usa UI-TARS para"
  - "mueve el mouse y haz clic en"
  - "control GUI de una app sin API"
  - "arranca UI-TARS Desktop"

idioma_de_salida: español
nivel: aplicada
dominio: control de escritorio / GUI agent
metadata:
  version: 1.0
  fecha: 2026-07-11
  app: C:\Users\datos\AppData\Local\UiTars\UI-TARS.exe (v0.2.4)
  config: C:\Users\datos\AppData\Roaming\ui-tars-desktop\ui_tars.setting.json
  modelo_vision: qwen2.5vl:7b (Ollama, local)
  relacionada:
    - agent-tars-instalacion-y-uso
    - era-pc-agentico-doctrina
    - llave-maestra-autoaprendizaje-ia
---

# Skill `ui-tars-desktop-control-local`

## Doctrina — división de trabajo cerebro/mano

Claude Code (esta sesión) es el **cerebro**: planifica, redacta, razona
sobre el corpus, orquesta skills. Pero tiene una restricción de tier en
`computer-use` (navegadores solo-lectura, IDEs solo-clic) que le impide
controlar libremente apps nativas de Windows.

UI-TARS Desktop es la **mano**: un agente GUI que VE la pantalla con un
modelo de visión y mueve el mouse/teclado sin restricción, porque corre
local sin sandbox. Su valor único (ver [[agent-tars-instalacion-y-uso]]
§5.1) es exactamente esto.

**Regla de oro**: si la tarea se puede resolver por API, CLI, web
scraping o archivo → Claude Code. Si SOLO se puede resolver clicando en
una app de escritorio sin API → delegar a UI-TARS Desktop con esta
skill.

## Configuración local aplicada (2026-07-11)

`ui_tars.setting.json` quedó así:

| Campo | Valor | Por qué |
|---|---|---|
| `language` | `es` | UI en español |
| `vlmProvider` | `Hugging Face for UI-TARS-1.5` | Provider OpenAI-compatible |
| `vlmBaseUrl` | `http://localhost:11434/v1` | **Ollama LOCAL** (sin nube) |
| `vlmApiKey` | `ollama-local` | Dummy (Ollama ignora la clave) |
| `vlmModelName` | `qwen2.5vl:7b` | Modelo de VISIÓN local (~6 GB) |
| `operator` | `Local Computer Operator` | Controla TODO el escritorio |
| `maxLoopCount` | `60` | Tope de pasos por tarea |

Backup del config original en `ui_tars.setting.json.bak-20260711`.

🚦 **Nota de seguridad**: el config original tenía una API key `hf_...`
(HuggingFace) puesta en el slot de VolcEngine — mismatch que impedía el
grounding y exponía un token en claro. Se reemplazó por el endpoint
local. Si ese token `hf_...` se usó en otro lado, conviene rotarlo en
https://huggingface.co/settings/tokens.

## ⚠️ GOTCHA DE MONITOR (verificado 2026-07-11)

Esta máquina tiene DOS monitores: **"Built-in Display"** (pantalla del
portátil, marcada como PRIMARIA pero normalmente **APAGADA**) y
**"LG HD"** (monitor externo donde el usuario TRABAJA).

Windows abre las ventanas nuevas en el monitor PRIMARIO → aparecen en
la pantalla del portátil apagada, **invisibles**. Una captura del
primario sale toda **negra** (no es un bug de render de UI-TARS ni de
la app; es que ese monitor está apagado).

**Solución** al lanzar UI-TARS Desktop (o cualquier app que aparezca
"en negro"):
1. Con la ventana enfocada, pulsar **`Win + Shift + ←`** (o `→`) para
   moverla al monitor visible LG HD.
2. O fijar LG HD como monitor principal en Configuración → Pantalla,
   de una vez y para siempre.

Sin esto, parece que la app "no abre" cuando en realidad está corriendo
en la pantalla apagada.

## Qué NO hacer / compuertas 🚦

- 🚦 **UI-TARS mueve el mouse y teclado REALES.** Antes de darle una
  tarea con efecto (guardar, enviar, borrar), revisa el plan. Empieza
  siempre con tareas de lectura/navegación.
- 🚦 **No delegarle operaciones financieras** (transferencias, órdenes
  de compra, firma) — igual que Claude Code, esas quedan para el
  usuario.
- 🚦 **Cerrar la ventana no siempre cancela** una acción en curso. Ten
  a mano `taskkill /IM UI-TARS.exe /F` para abortar.
- 🚦 **El grounding con qwen2.5vl es "bueno, no perfecto".** Para apps
  con botones pequeños o densos, puede fallar el clic. Si la precisión
  no alcanza, ver "Mejora de grounding" abajo.
- 🚦 **Un solo agente controla el escritorio a la vez.** No uses el
  computador mientras UI-TARS trabaja: le robas el foco y falla.

## Protocolo paso a paso

> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

### Paso 1 — Confirmar que la tarea SÍ es para UI-TARS
Preguntarse: ¿esto se puede hacer por API/CLI/web/archivo? Si la
respuesta es sí, hacerlo con Claude Code y NO invocar UI-TARS. Solo
seguir si la tarea exige clicar una app nativa sin API.

### Paso 2 — Arrancar el entorno
```
"C:\Users\datos\.claude\skills\ui-tars-desktop-control-local\scripts\lanzar_ui_tars.bat"
```
El .bat verifica Ollama, verifica/descarga el modelo de visión, y abre
UI-TARS Desktop. La primera vez descarga qwen2.5vl:7b (~6 GB, una vez).

### Paso 3 — Redactar la tarea GUI en español
Claude Code redacta una instrucción CLARA y ATÓMICA para pegar en la
caja de UI-TARS Desktop. Buenas instrucciones:
- "Abre el Excel que está en <ruta>, ve a la hoja 'Resumen', y en la
  celda B2 escribe la fecha de hoy. Guarda con Ctrl+S."
- "En la ventana de <app>, haz clic en el menú Archivo → Exportar →
  PDF, y guarda en <carpeta>."

Malas instrucciones (demasiado abiertas): "organiza mi Excel".

### Paso 4 — Supervisar
El usuario mira cómo UI-TARS ejecuta. Si se desvía, detener con el botón
de la app o `taskkill /IM UI-TARS.exe /F`.

### Paso 5 — Verificar el resultado
Claude Code verifica el archivo/estado resultante (ej.: leer el Excel
modificado con openpyxl) y reporta al usuario.

## Casos de uso reales (del ecosistema del usuario)

| Caso | Por qué UI-TARS y no Claude Code |
|---|---|
| Correr una macro del War Room QVP que solo existe en el Excel | Excel local sin API; requiere clic en el botón de macro |
| Exportar un reporte desde un ERP legacy de escritorio | El ERP no tiene API ni exportación por línea de comandos |
| Rellenar un formulario en una app contable de escritorio | Ventana modal sin acceso web |
| Registrar una demo en video de un flujo de escritorio | Necesita clics visibles reales |

## Mejora de grounding (si qwen2.5vl no alcanza)

Para precisión de clic nivel producción, dos rutas:
1. **Modelo UI-TARS nativo local** — descargar un GGUF de
   `UI-TARS-1.5-7B` a Ollama (más pesado, mejor grounding GUI):
   ```
   ollama pull hf.co/<repo>/UI-TARS-1.5-7B-GGUF:Q4_K_M
   ```
   y cambiar `vlmModelName` en el config.
2. **Doubao 1.5 UI-TARS en la nube** (VolcEngine ARK) — mejor grounding
   pero de pago y sale de "local"; requiere una API key ARK válida
   (NO un token `hf_`). Solo si el usuario lo autoriza.

## Cómo depurar si falla

- **La app no abre** → verificar `C:\Users\datos\AppData\Local\UiTars\UI-TARS.exe`
  existe; reinstalar desde el pending Setup si hace falta.
- **"Connection refused" al VLM** → Ollama no está corriendo; arrancar
  `ollama app.exe` o correr `ollama serve`.
- **Grounding erra los clics** → subir a modelo UI-TARS nativo (ver
  arriba) o reducir densidad de la UI objetivo (zoom in en la app).
- **Se queda en loop** → `maxLoopCount` alcanzado; reformular la tarea
  en pasos más pequeños.

## Portabilidad (revisar el 20% al reusar)
Ruta del `.exe` (versión de la app), ruta de Ollama, nombre del modelo
de visión, y el `operator` (Computer vs Browser). El resto es estable.

## Relacionado
- [[agent-tars-instalacion-y-uso]] — la versión Web (multimodal) y el
  análisis crítico vs Claude Code / Cowork.
- [[era-pc-agentico-doctrina]] — marco: el agente como nueva aplicación.
- [[llave-maestra-autoaprendizaje-ia]] — doctrina padre.
