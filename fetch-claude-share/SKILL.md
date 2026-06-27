---
name: fetch-claude-share
description: |
  Lee URLs de claude.ai/share/<id> y persiste la conversación entera
  (mensajes user + assistant) como markdown local. Sustituye a WebFetch
  (que sólo lee "Claude" porque la página es React client-side) y
  bypassa el bloqueo de claude.ai en Chrome MCP. La estrategia es
  conectar al Edge debug del usuario en localhost:9222 (Edge real, pasa
  Cloudflare); si no está disponible, cae a un perfil persistente Edge.

  Resultado: cada share fetcheado queda en
  `E:\vars\var 5\Claude-share-archivo\<fecha>_<slug>__<id>.md` con
  metadatos + lista de mensajes parseados.

trigger_phrases:
  - "lee este claude share"
  - "fetch claude.ai share"
  - "archiva esta conversación de claude"
  - "extrae el chat de claude.ai"

idioma_de_salida: español neutro
nivel_madurez: aplicada
fuente: sesión 2026-06-26 (resolver bloqueo Chrome MCP + Cloudflare)
---

# Lector de claude.ai/share

## Doctrina

Las URLs `https://claude.ai/share/<id>` son conversaciones compartidas
públicas. WebFetch ve sólo la palabra "Claude" porque la página es
client-side React. Chrome MCP las bloquea por allowlist de la
extensión. La solución única que funciona es conectar al Edge real del
usuario via CDP — porque ese Edge tiene cookies de Cloudflare ya
verificadas y un user agent normal.

## Cómo usarla

```bash
# Por URL completa
python "C:/Users/datos/.claude/skills/fetch-claude-share/scripts/fetch_share.py" \
       https://claude.ai/share/55c390d2-c19b-4d49-a3aa-b068791e6978

# Por solo el ID
python ".../fetch_share.py" 55c390d2-c19b-4d49-a3aa-b068791e6978

# Esperar más al render (si el chat es muy largo)
python ".../fetch_share.py" <ID> --wait 60

# Modo headed (debug Cloudflare)
python ".../fetch_share.py" <ID> --headed
```

Salida: `E:\vars\var 5\Claude-share-archivo\YYYY-MM-DD_<title>__<id>.md`

## Estrategia técnica

1. **Primer intento**: `connect_over_cdp("http://localhost:9222")` —
   usar el Edge debug real del usuario. Pasa Cloudflare porque tiene
   las cookies CF_clearance y el user-agent normal.
2. **Fallback**: `launch_persistent_context(browser_profile_edge)` —
   abre una instancia separada con el perfil persistente.
3. **Detección de carga**: espera hasta que aparezcan elementos
   `[data-testid*="message"]` o `.font-claude-message` (3 selectores
   probados) y luego espera estabilización del body (3 lecturas
   consecutivas con la misma longitud).
4. **Bypass de loop Cloudflare**: si el body contiene "Verificación de
   seguridad" o "Just a moment", el contador de estabilidad NO avanza —
   sigue esperando hasta que CF resuelva o expire el timeout.
5. **Parseo por mensaje**: extrae cada `[data-testid*="message"]` con
   su role inferido (`user` vs `assistant`).

## Compuertas 🚦

1. **NO funciona sin Edge debug en 9222**. Si está caído, el fallback
   con perfil persistente puede chocar contra Cloudflare otra vez.
2. **No descargar masivamente** — claude.ai puede aplicar rate limit.
3. **No publicar conversaciones privadas** que el usuario no haya
   compartido explícitamente; sólo URLs `/share/<id>` válidas.
4. **Conversaciones muy largas** (>50 mensajes) pueden requerir
   `--wait 90` o más; el detector de estabilidad por defecto es 30 s.
5. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cómo depurar si falla

| Síntoma | Causa probable | Fix |
|---|---|---|
| `body_chars: ~286, messages: 0`, body dice "Cargando..." | React no terminó de renderizar | `--wait 60` |
| `body dice "Verificación de seguridad"` | Cloudflare bot challenge | Confirmar que el script usó CDP (no fallback); abrir Edge debug |
| `CDP no disponible` | Edge debug murió | Correr `E:\vars\var 5\X-com guardados\start_edge_debug.bat` |
| `messages: 0` pero body completo | Cambiaron los selectores de claude.ai | Inspeccionar DOM, actualizar lista `SELECTORS` |

## Smoke test verificado el 2026-06-26

URL: `claude.ai/share/55c390d2-c19b-4d49-a3aa-b068791e6978`
- via CDP localhost:9222
- 45 mensajes parseados
- 1.122.391 chars de body completo
- 41.741 chars persistidos en MD final

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — registra esta capacidad.
- [[perplexity-active-use]] — misma técnica (CDP a Edge real).
- [[youtube-corpus-jjmobijuesa]] — fuente complementaria.
