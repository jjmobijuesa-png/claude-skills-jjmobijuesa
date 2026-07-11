---
name: agent-tars-instalacion-y-uso
description: |
  Instala, configura, arranca y opera Agent-TARS y UI-TARS Desktop
  (ByteDance, open-source) en este computador. Agent-TARS es un agente
  MULTIMODAL que razona, navega la web y usa herramientas via un LLM
  configurable (Anthropic, OpenAI, DeepSeek, Gemini, Ollama, LM Studio).
  UI-TARS Desktop es su versión Electron con control de la GUI del
  computador (mouse/teclado guiados por Vision-Language Model).

  La skill cubre:
  - Prerrequisitos (Node.js LTS, pnpm) — YA INSTALADOS 2026-07-11.
  - Instalación de dependencias del monorepo + submonorepo multimodal.
  - Configuración (agent-tars.config.ts + .env con claves API).
  - Arranque: web (puerto 8888) o desktop (Electron).
  - Integración con los proyectos vigentes del usuario (Quevepalma,
    EcuaLedger Soberana, Vista al Río, bookmarks X.com, LinkedIn
    fedphd, YouTube jjmobijuesa).

trigger_phrases:
  - "arranca Agent-TARS"
  - "instala Agent-TARS"
  - "corre el agente TARS"
  - "actualiza la config de TARS"
  - "prueba TARS con Ollama local"
  - "TARS control de escritorio"
  - "UI-TARS desktop"

idioma_de_salida: español
nivel: aplicada
dominio: instalación / operación
metadata:
  version: 1.0
  fecha: 2026-07-11
  origen: pedido del usuario 2026-07-11; repo bytedance-UI-TARS-desktop-0ee8730
  relacionada:
    - llave-maestra-autoaprendizaje-ia
    - era-pc-agentico-doctrina
    - agentic-ai-hitchhiker-guide
    - perplexity-active-use
    - deepseek-active-use
  ruta_repo: C:\Users\datos\Downloads\bytedance-UI-TARS-desktop-0ee8730
  puerto_web: 8888
---

# Skill `agent-tars-instalacion-y-uso`

## Doctrina

**Agent-TARS materializa la doctrina del PC agéntico** (Jensen + Satya,
video `nT17ASj4gdQ`, ver [[era-pc-agentico-doctrina]]): un OS + LLM que
razona sobre el entorno del usuario, navega la web, opera herramientas
y controla la GUI. Es open-source, corre local, y permite conectar
cualquier LLM (paga o local).

Se complementa con nuestras skills existentes:
- **`perplexity-active-use`** y **`deepseek-active-use`**: consultan
  modelos remotos via Edge CDP (barato en tokens, sin API key).
- **`agent-tars-instalacion-y-uso`** (esta): agente completo con
  herramientas propias (browser, filesystem, MCPs), configurable.

## Hallazgo empírico 2026-07-11: modelo qwen3:1.7b es demasiado lento

Prueba en vivo con Ollama local (CPU, sin GPU dedicada):
- Prompt trivial "Cuenta hasta 5" → 18 s.
- Prompt agéntico con system prompt (15 K chars) + tool call + thinking
  → ejecuta el tool en 17 ms pero la síntesis final tarda >10 min por
  iteración. Agent-TARS hace hasta 6 iteraciones → **>1 h por tarea**.

**Recomendaciones**:
1. **Con API key** (más rápido) — cualquier proveedor cloud responde en
   1-5 s. Rellenar `.env` con `ANTHROPIC_API_KEY` o `DEEPSEEK_API_KEY`
   y quitar `--model.provider ollama` del `.bat`.
2. **Modelo Ollama más grande y capaz** — `qwen3:8b` (5.2 GB) o
   `qwen2.5-coder:7b` (4.7 GB, mejor con JSON tool calls). Instala con:
   ```powershell
   ollama pull qwen3:8b
   ```
   Luego cambia `--model.id qwen3:1.7b` a `--model.id qwen3:8b` en
   `launch-agent-tars.bat`.
3. **Desactivar thinking mode** — reduce tokens/iteración drásticamente
   pero mantén qwen3:1.7b. Añadir `--thinking.type disabled` al comando.
4. **GPU dedicada** — si tienes NVIDIA con CUDA, Ollama lo detecta
   automáticamente y qwen3:1.7b corre a ~50 tok/s en vez de ~10 tok/s.

## Estado actual (2026-07-11)

- ✅ Node.js v24.18.0 (winget OpenJS.NodeJS.LTS).
- ✅ pnpm **9.15.9** (via `npm i -g pnpm@9` — el submonorepo `multimodal`
  fuerza `engines.pnpm: 9`).
- ✅ `pnpm install` raíz del monorepo (2 763 packages).
- ✅ `pnpm install` en `multimodal/` submonorepo (2 360 packages).
- ⏳ `pnpm run build` en `multimodal/` (necesario — `tarko/pnpm-toolkit`
  requiere `dist/cli` compilado; `pnpm dev` falla sin esto).
- ✅ `.claude/launch.json` con 2 configuraciones (web + desktop) usando
  `.bat` wrappers para propagar PATH al proceso de preview.
- ✅ `agent-tars.config.ts` con providers Anthropic/OpenAI/DeepSeek/Ollama.
- ✅ `.env.example` combinado (VLM del Desktop + LLMs del Web).
- ❌ `.env` con claves reales — PENDIENTE (usuario debe rellenar).

## Qué NO hacer / compuertas 🚦

- 🚦 **NUNCA commitear `.env`** al git — ya está en `.gitignore`.
- 🚦 **NUNCA pegar la clave API en un `.ts`, `.json` ni en el chat.**
  Solo en `.env` local o variables de entorno de la sesión.
- 🚦 **Antes de arrancar UI-TARS Desktop** (Electron con control de
  GUI), el usuario debe entender que el agente puede mover el mouse y
  escribir. Empezar con tareas de bajo blast radius (buscar un archivo,
  abrir una web) antes de darle tareas transaccionales.
- 🚦 **Si usas Anthropic/OpenAI** vigila la cuota — Agent-TARS puede
  consumir muchos tokens en tareas largas. Usar Ollama local para
  pruebas.
- 🚦 **No conectar Agent-TARS a cuentas sensibles del usuario** (Gmail
  con credenciales, banca, GitHub con push) sin autorización explícita
  y contexto de sesión aislada.

## Setup rápido (primera vez)

Ya realizado. Los tres pasos que quedan:

1. **Terminar `pnpm install`** en `multimodal/` (en curso, ver
   background task).
2. **Rellenar `.env`** con al menos UNA clave del proveedor a usar:
   ```bash
   cd "C:\Users\datos\Downloads\bytedance-UI-TARS-desktop-0ee8730"
   cp .env.example .env
   notepad .env
   # completar ANTHROPIC_API_KEY o similar
   ```
3. **Arrancar el servidor web**:
   ```bash
   pnpm.cmd -C multimodal dev
   # abrir http://localhost:8888
   ```

## Modo sin claves (Ollama local)

Si no quieres pagar API:
```bash
# Instalar Ollama Desktop desde https://ollama.com/download
ollama pull qwen3:1.7b
# En agent-tars.config.ts el provider "ollama" ya está listo
pnpm.cmd -C multimodal dev
```

## Arranque diario (después del setup)

```powershell
cd "C:\Users\datos\Downloads\bytedance-UI-TARS-desktop-0ee8730"

# WEB (razona + navega + tools)
pnpm.cmd -C multimodal dev
# → http://localhost:8888

# DESKTOP (Electron con control GUI)
pnpm.cmd dev:ui-tars
# → ventana propia
```

## Cambio de modelo en runtime

En la interfaz web (`localhost:8888`), en el panel de config: elegir
provider + modelo. Se persiste en `agent-tars.config.ts` o en el
session state según versión.

## Depuración

- **`Error: Cannot find module 'ptk'`** → falta `pnpm install` dentro
  de `multimodal/`.
- **`ANTHROPIC_API_KEY not defined`** → `.env` no cargado; verificar
  que existe en el directorio de trabajo desde donde arrancas.
- **`Port 8888 already in use`** → matar proceso previo:
  `netstat -ano | findstr :8888` + `taskkill /PID <PID> /F`.
- **Electron no abre** → verificar que Windows Defender no bloquea
  `apps/ui-tars/*.exe`; excluir la carpeta.
- **VLM del Desktop no responde** → verificar `VLM_*` en `.env`;
  UI-TARS-1.5 requiere endpoint de HuggingFace o Volcengine.

## Integración con proyectos actuales

### 1. Quevepalma (control financiero)
Agent-TARS puede leer un Excel del War Room QVP y proponer análisis:
> "Abre `C:\...\WAR ROOM QVP\Adjuntos SEM 24\plantilla.xlsx`, calcula el
> margen semanal realizado, y compáralo con el objetivo 3,6%. Reporta
> alertas en Markdown."

Skills involucradas: [[control-financiero-semanal-qvp]],
[[memoria-financiera-inteligenciada]].

### 2. EcuaLedger Soberana (jurídico-legislativo)
Agent-TARS con browser tool puede buscar novedades regulatorias:
> "Busca en el sitio de la Asamblea Nacional del Ecuador cualquier
> proyecto que mencione 'tokenización', 'RWA' o 'fideicomiso digital'
> ingresado el último mes. Reporta con URL canónica."

Skills involucradas: [[inteligencia-politica-estrategica-multivectorial]],
[[defensa-apologetica-juridica]].

### 3. Bookmarks X.com (autoreflexivo)
Complementa [[agente-local-autoreflexivo-bookmarks]] con razonamiento
más potente que la clasificación por keyword:
> "Lee el `analisis\2026-07-05_*.md` del corpus bookmarks y prioriza los
> 5 temas más accionables para esta semana."

### 4. LinkedIn fedphd (nueva integración)
Sobre las skills `intereses-lkd-*` recién creadas:
> "Toma la skill `intereses-lkd-finanzas-control`, filtra los 10 posts
> más recientes de autores diferentes y proponme 3 hilos para redactar
> como comentarios propios."

### 5. YouTube jjmobijuesa (transcripciones)
> "Lee la transcripción de `E:\vars\var 5\YouTube-jjmobijuesa\
> transcripciones\_manuales\nT17ASj4gdQ__nT17ASj4gdQ.md` y genera un
> quiz de 8 preguntas para fijar el aprendizaje."

Skill involucrada: [[youtube-corpus-jjmobijuesa]].

### 6. Vista al Río (comercial inmobiliario)
> "Compón un brochure HTML autocontenido para la OLA 3 del edificio
> Vista al Río en modalidad obra gris; segmento hijos de empresarios
> retornados; sin precio explícito."

Skill involucrada: [[vista-al-rio-obra-gris-hijos-exitosos]].

## Ventaja frente a las skills `*-active-use`

| Aspecto | perplexity/deepseek-active-use | Agent-TARS |
|---|---|---|
| Fuente | Chat remoto (Perplexity, DeepSeek) | LLM directo + tools locales |
| Persistencia | Historial del chat externo | Session state propio |
| Tools | Web search remoto | Browser + FS + MCP + tools custom |
| Coste | Suscripción del chat | Tokens API (o local sin coste) |
| Uso | Consultas puntuales | Tareas agénticas multi-paso |
| Modelo | Fijo por proveedor | Configurable en runtime |

Los tres coexisten. **Regla**: si la tarea cabe en 1 pregunta →
Perplexity/DeepSeek. Si necesita 3+ pasos con tools → Agent-TARS.

## Portabilidad (revisar al reusar en otra máquina)

- Node.js 24 LTS + pnpm 11.x.
- Ruta del repo — si moviste el repo, actualizar todos los paths.
- `.env` — nunca portátil; el usuario lo rellena en cada máquina.
- LM Studio / Ollama — instalación local aparte.

## Relacionado

- [[era-pc-agentico-doctrina]] — marco histórico-arquitectónico.
- [[agentic-ai-hitchhiker-guide]] — capa técnica (paper Roitman).
- [[perplexity-active-use]], [[deepseek-active-use]] — hermanas
  remotas (chats), no sustitutas.
- [[llave-maestra-autoaprendizaje-ia]] — doctrina padre.
