---
name: inventario-extensiones-edge-jjmobijuesa
description: |
  Mapa curado de las 76 extensiones físicas instaladas en Edge del
  usuario jjmobijuesa@gmail.com, clasificadas por familia funcional
  (IA + chat / Claude / Perplexity / NotebookLM / YouTube / OSINT /
  productividad / utilidades). Indica qué extensiones complementan
  cada skill local del agente y cuáles son redundantes con scripts
  propios ya construidos (candidatas a desinstalar).

  Política operativa: **solo Edge**. Chrome tiene apenas 4 extensiones
  residuales (Adobe Reader, McAfee, Google Docs offline, Hangouts) —
  no es navegador de trabajo del usuario y se ignora.

trigger_phrases:
  - "qué extensión Edge usar para"
  - "inventario extensiones Edge"
  - "extensiones IA del usuario"
  - "auditar extensiones Edge"

idioma_de_salida: español neutro
nivel_madurez: basica
fuente: inventario 2026-06-26 de C:\Users\datos\AppData\Local\Microsoft\Edge\User Data\Default\Secure Preferences
---

# Inventario de extensiones Edge — usuario jjmobijuesa@gmail.com

## Doctrina operativa

**Trabajamos solo con Edge.** Chrome del usuario tiene 4 extensiones
genéricas; Edge tiene 76 instaladas con foco claro en IA y curaduría
del conocimiento. Esto se documenta como feedback memory permanente
(ver `feedback_solo_edge.md`).

## Familias funcionales y mapeo a skills locales

### Familia 1 — Claude (8 extensiones)

| Extensión | Versión | Complementa | Recomendación |
|---|---|---|---|
| Claude | 1.0.77 | Acceso directo a claude.ai | **Mantener** |
| ClaudeBuff (UI mejorada) | 1.0.5 | UX claude.ai | Mantener |
| Claude Search | 2.1.0 | Búsqueda en chats antiguos | Mantener |
| Claude Studio | 1.0.4 | Estudio de prompts | Mantener |
| Claude Usage Meter | 1.1.4 | Indicador de cuota | Mantener |
| Claude Usage Monitor | 1.0.6 | Monitor de uso | **Redundante** con Meter; desinstalar uno |
| Claude Usage Tracker - Chat & Code Export | 1.2.4 | Export de chats | Mantener — sustituye parcialmente a `fetch-claude-share` |
| Claude Enter Key Control | 1.2.1 | Cambia comportamiento Enter | Mantener |
| Claude AI RTL Transformer | 2.1.0 | RTL (árabe/hebreo) | **Desinstalar** — no aplica |
| Claude i18n | 1.1.2 | Localización | Mantener |
| Exportador de Chat IA (Claude→PDF/MD) | 2.26.0 | Export | **Redundante** con `fetch-claude-share`; mantener como UI |
| Resumir y Traducir con Claude | 1.4.32 | Resumen on-page | Mantener |

### Familia 2 — Perplexity (3 extensiones)

| Extensión | Función | Complementa |
|---|---|---|
| Perplexity Omnibox | 2026.5.2 | Buscar desde la barra Edge | Complemento de [[perplexity-active-use]] |
| Monitor de Límites para Perplexity | 1.1.0 | Cuota | Mantener |
| NextaThema for Perplexity | 0.0.7 | Tema visual | Mantener si gusta |

### Familia 3 — NotebookLM (8 extensiones)

| Extensión | Función |
|---|---|
| NotesLM | Acceso |
| NotebookLM Importer | Importar fuentes |
| NotebookLM Audio Video Extractor | Bajar audio/video Studio |
| NotebookLM PDF Downloader | Bajar PDF Studio |
| NotebookLM Language Switcher | Cambiar idioma |
| NotebookLM Clip | Recortar fuentes |
| Notebook LM WideScreen Mode | UI |
| lmexporter (NotebookLM → PDF/Word/PNG) | Export |
| YouTube to NotebookLM for Edge | Importar YouTube |

**Mapeo**: complementan a [[auditor-integral-notebooklm]] y al CLI `notebooklm-py`. El stack del usuario es el más completo de NotebookLM que conozco.

### Familia 4 — YouTube (10+ extensiones)

| Extensión | Función | Complemento de [[youtube-corpus-jjmobijuesa]] |
|---|---|---|
| YouTube Summary with ChatGPT & Claude | Resumen | Útil en navegación humana |
| Resumen de YouTube con ChatGPT | Resumen alterno | Redundante |
| TranscribeYT (transcripts & summaries) | Transcripción | **Redundante** con `youtube-transcript-api` del agente |
| YouTube to NotebookLM | Importar a NotebookLM | Útil |
| YouTube Videos Summary with AI | Resumen | Redundante |
| YouTube Transcript & Subtitle Control (Ultra-Reader) | Subtítulos | Mantener |
| YouTube Adblocker | Quitar ads | Mantener |
| Traductor de YouTube | Traducir audio | Mantener |
| YouTube Dubbing | Doblaje IA | Mantener |
| Oculta la distracción de YouTube | Limpieza UI | Mantener |
| Limpia YouTube (cortos, comentarios) | UI | Mantener |
| Youtube video downloader free | Bajar MP4 | Útil para casos puntuales |
| X Descargador de videos | YouTube + X | Mantener |

**Decisión**: tener 4-5 extensiones de "resumen YouTube" es ruido. Una sola (la mejor: **YouTube Summary with ChatGPT & Claude**) basta para uso interactivo; la captura masiva la hace el agente con `extraer_transcripciones.py`.

### Familia 5 — Sidebar IA multi-modelo (4 extensiones)

| Extensión | Función |
|---|---|
| Sider: barra lateral de IA con todos los modelos | Sidebar Claude/GPT/Gemini |
| Sider: Chatea con todas las IA: GPT-5, Claude, DeepSeek | Variante actualizada |
| MaxAI (Pregunta a la IA mientras navegas) | Sidebar competidor |
| Free ChatGPT Chatbot (GPT-4 & Claude3) | Acceso multi |
| Free ChatGPT AI Chatbot (GPT-4) | Variante |
| GPT Workspace | Productividad |
| ChatGPT search | Buscador OpenAI |
| Edge Copilot Bridge | Bridge Copilot interno |

**Decisión**: 2 Sider + 2 ChatGPT free + MaxAI + Edge Copilot = sobrepoblación. Dejar **una** sidebar (Sider o MaxAI) + Edge Copilot nativo.

### Familia 6 — Mapas mentales y notas (5 extensiones)

| Extensión | Función |
|---|---|
| Mapify - Mapa Mental y Resumen IA por Claude & ChatGPT | Mapas mentales | Usado en [[triage-inbox-rapido-jjmobijuesa]] |
| Recall - Your Knowledge is Your Edge | Notas tipo Obsidian | Mantener |
| Noted - Minimalist Notebook | Notas simples | Redundante con Recall |
| iNotebook | Cuaderno | Redundante |
| Quick Bookmarks Menu | Bookmarks | Mantener |
| My Workspace | Workspace | Mantener |

### Familia 7 — Traductores (5+ extensiones)

DeepL, autoTranslate, Simple Translate, DeepTranslate, Translight, Traductor (genérico), Edge relevant text changes.

**Decisión**: DeepL es el mejor; los demás son ruido — desinstalar al menos 3.

### Familia 8 — Privacidad y anti-fingerprint (4 extensiones)

| Extensión | Función |
|---|---|
| Canvas Blocker - Fingerprint Protect | Anti-fingerprinting | Mantener |
| Canvas Fingerprint Defender | Alternativo | Redundante |
| Suppress Consent Prompt | Saltar GDPR popups | Mantener |
| Adblock - bloqueador gratuito | Ads | Mantener |

### Familia 9 — Captura y descargas

| Extensión | Función |
|---|---|
| Screenshot with URL - Full Page Screenshot | Captura | Mantener |
| Twitter Downloader HD (X2Twitter) | Bajar de X | Útil para [[consulta-bookmarks-fdc-ec]] |
| X Comments Exporter | Exportar comentarios X | Útil para análisis |
| Auto Data Filler | Llenado de formularios | Riesgoso — auditar |

### Familia 10 — Específicas del usuario

| Extensión | Caso de uso |
|---|---|
| Law Notebook | Cuaderno jurídico | Aplica a EcuaLedger Soberana |
| Wolfram Alpha (Official) | Cálculo | Complementa [[wolfram-forensic-engine]] |
| Grammarly | Corrección | Mantener |
| Fathom AI Note Taker for Google Meet | Reuniones | Usado en [[comite-cuarto-guerra-qvp]] |
| Canva Automation Tool / Canva AutoMaker / InstantDownload for Canvas | Canva | Mantener si se hace marketing |
| Checker Plus for Gmail | Gmail | Complementa MCP Gmail |
| Campus AI (Canvas LMS) | Tareas | Específico — solo si aplica |

### Familia 11 — Microsoft / Edge nativo (8 extensiones)

Web Store, Microsoft Clipboard, Microsoft Store, Microsoft Edge PDF Viewer, Microsoft Voices, Edge Feedback, Edge relevant text changes, Edge Copilot Bridge, Media Internals, WebRTC Internals, WebRTC Extension. **Mantener todo** — son del navegador.

## Lista de desinstalación recomendada (limpieza)

1. Claude Usage Monitor (redundante con Meter)
2. Claude AI RTL Transformer (no aplica idioma)
3. Resumen de YouTube con ChatGPT (duplicado)
4. YouTube Videos Summary with AI (duplicado)
5. TranscribeYT (el agente ya transcribe vía CLI)
6. Sider variante vieja (dejar la nueva)
7. Free ChatGPT Chatbot (uno de los dos)
8. Noted + iNotebook (redundante con Recall)
9. Simple Translate / autoTranslate / Translight (dejar DeepL)
10. Canvas Fingerprint Defender (redundante con Canvas Blocker)

**Total ahorro estimado**: 12-15 extensiones menos = menos memoria + arranque más rápido + menos vectores de fingerprint.

## Compuertas 🚦

1. **Antes de desinstalar**: confirmar con el usuario; algunas pueden tener configuración personal.
2. **No instalar nuevas IA sidebars** — ya hay tres (Sider, MaxAI, ChatGPT search); más es ruido.
3. **Auto Data Filler** y similares pueden capturar credenciales — auditar antes de mantener.
4. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Relacionado

- [[feedback_solo_edge]] — política operativa.
- [[perplexity-active-use]] — vinculada con Perplexity Omnibox.
- [[youtube-corpus-jjmobijuesa]] — vinculada con familia YouTube.
- [[fetch-claude-share]] — vinculada con Claude Usage Tracker.
- [[auditor-integral-notebooklm]] — vinculada con familia NotebookLM.
