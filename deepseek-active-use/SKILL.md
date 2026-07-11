---
name: deepseek-active-use
description: |
  Usa DeepSeek (chat.deepseek.com) en modo ACTIVO sobre la sesión logueada del usuario en Edge debug
  (puerto 9222): redacta un prompt, lo inyecta en el textarea, dispara el envío, espera la respuesta
  streamed y devuelve el texto. Hermana de `perplexity-active-use`. Su propósito estratégico es la
  EFICIENCIA DE TOKENS multi-modelo: delegar el razonamiento/síntesis pesado a DeepSeek (que el usuario
  ya paga y tiene en contexto) y traer de vuelta solo el resultado destilado, en vez de gastar tokens
  locales en cadenas largas. Persiste cada consulta para reutilizarla.
  Triggers: "pregúntale a DeepSeek", "usa DeepSeek", "manda esto a DeepSeek", "razonamiento profundo en
  DeepSeek", "lee este share de DeepSeek".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-28
  origen: pedido del usuario (análisis DISEBAJ vía DeepSeek) — hermana de perplexity-active-use
  relacionada: perplexity-active-use, eficiencia-generacion-respuestas, fetch-claude-share
---

# Skill `deepseek-active-use`

Aprovechar DeepSeek como "co-procesador de razonamiento" del agente local, igual que Perplexity, X y
LinkedIn ya se usan vía Edge real. **Solo Edge** (perfil del usuario jjmobijuesa@gmail.com).

## Doctrina de eficiencia (por qué)
Cada modelo tiene una fortaleza: Perplexity (búsqueda con citación), X/LinkedIn (curación del usuario),
**DeepSeek (razonamiento largo y barato)**. En tareas de análisis profundo, **delegar la cadena pesada
a DeepSeek y traer solo la conclusión** ahorra tokens locales y mejora la calidad. Encaja con
[[eficiencia-generacion-respuestas]]: el camino más barato que resuelve el prompt. Si el usuario ya
pegó el texto de un hilo DeepSeek, **no lo re-abras** — úsalo directo.

## Acceso (Edge debug 9222 + Chrome MCP)
1. Confirmar que Edge corre con `--remote-debugging-port=9222` y la sesión de DeepSeek está abierta
   (logueada como jjmobijuesa). Conectar con `list_connected_browsers` / `select_browser`.
2. Navegar/enfocar la pestaña `chat.deepseek.com`. (DeepSeek no suele estar en la lista de dominios
   bloqueados de la extensión; si lo estuviera, operar por `javascript_tool` sobre la pestaña ya abierta,
   como en Perplexity.)
3. **Inyectar el prompt** con `javascript_tool` (DOM-aware, no requiere click-pixel):
   - Input: `textarea` principal del chat (selector tipo `textarea#chat-input` o
     `textarea[placeholder*="Message"]`; verificar en runtime con `find`/`read_page`).
   - Fijar el valor, disparar `input`/`change`, y enviar con el botón de envío o `Enter`.
4. **Esperar el streaming**: sondear el contenedor de la última respuesta hasta que deje de crecer
   (timeout prudente). Extraer el texto del último mensaje del asistente.
5. Opcional: activar **DeepThink (R1)** si la tarea exige razonamiento profundo (botón del modo).

## Leer un SHARE de DeepSeek (https://chat.deepseek.com/share/<id>)
Como con claude.ai (ver [[fetch-claude-share]]), la página es client-side: WebFetch falla. Abrir el
share en el Edge debug y extraer el texto con `get_page_text`/`javascript_tool`. **Pero**: si el
usuario ya pegó el contenido del hilo en el prompt, sáltate este paso (eficiencia).

## Persistencia
Guardar cada consulta en `E:\vars\var 5\DeepSeek-consultas\YYYY-MM-DD_<slug>.md` con: prompt, respuesta,
modo (V3/R1) y la URL del hilo si existe, para reutilizarla en sesiones futuras sin volver a preguntar.

## Reglas
- Solo lectura/consulta; no publicar ni cambiar configuración de la cuenta.
- Verificar los selectores en runtime (la UI cambia); si fallan, leer el DOM con `read_page` y ajustar.
- Citar a DeepSeek como fuente del razonamiento cuando su salida entre a un entregable; los datos duros
  siguen viniendo de los archivos del proyecto, no del modelo.
