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

## Pre-requisitos

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

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — registra esta capacidad como
  fuente activa.
- [[youtube-corpus-jjmobijuesa]] — fuente complementaria en video.
- [[anthropic-skills:notebooklmskill]] — destino natural de las
  conclusiones (subir como nota al cuaderno temático).
