---
name: claude-routines-apis-skills-github
description: |
  Doctrina y procedimiento para extender Claude con (a) Routines
  remotas que disparan automaticamente, (b) llamadas a APIs externas
  con autenticación (caso ejemplo: webhook de Notion con
  `Authorization`/`Notion-Version`/`Content-Type`), y (c) sincronización
  de Skills locales con un repositorio GitHub para versionado y
  portabilidad. Destilada del tutorial de Laura Cilleruelo (canal
  «Claridad Artificial», video YouTube `oIxLOiITVwk`, ~29 min).

  Cubre la brecha entre tener skills locales valiosas y poderlas
  ejecutar desde fuera del computador (móvil, otro escritorio, agente
  remoto), versionarlas como cualquier proyecto de software y
  compartirlas controladamente.

trigger_phrases:
  - "claude routines remoto"
  - "API desde Claude"
  - "webhook desde Claude"
  - "subir skills a GitHub"
  - "versionar mis skills"
  - "sincronizar skills entre máquinas"

idioma_de_salida: español neutro técnico
nivel_madurez: aplicada
fuente: video YouTube oIxLOiITVwk (Laura Cilleruelo · Claridad Artificial) — descripción + timestamps oficiales en `E:\vars\var 5\YouTube-jjmobijuesa\transcripciones\_manuales\oIxLOiITVwk__oIxLOiITVwk.md`. Parte 1 previa: youtu.be/kyKADQOetU4 (no analizada todavía).
---

# Extender Claude — Routines + APIs + Skills en GitHub

## Doctrina

Una skill local es valiosa pero **prisionera del disco** donde nació.
Para que el agente local del usuario sea verdaderamente útil debe
poder:

1. **Disparar automáticamente** (Routines) — sin estar uno en el chat.
2. **Llamar el mundo exterior** (APIs) — Notion, Sheets, Stripe,
   Slack, Webhooks, etc.
3. **Sincronizarse entre máquinas** (Git/GitHub) — móvil, portátil,
   sobremesa, agente remoto.

Las tres capas convierten un agente personal en un agente con
**alcance operacional real** sobre el ecosistema del usuario.

## Capa 1 — Claude Routines remotas

### Qué es

Una Routine es una rutina de Claude que vive **fuera del chat** y se
ejecuta:
- Por horario (cron-style).
- Por evento externo (webhook entrante).
- Bajo demanda desde un dispositivo del usuario.

### Implementación equivalente en este computador (hoy)

| Routine de Cilleruelo | Equivalente local existente |
|---|---|
| Routine programada | `mcp__scheduled-tasks__create_scheduled_task` |
| Routine que se autoejecuta sin estar en el chat | El watcher de X.com (autostart al login) |
| Routine que llama a APIs externas | Cualquier script Python con `requests` lanzado desde una skill |

### Procedimiento para crear una Routine remota (según video)

1. **Crear** la Routine desde cero en el panel de Anthropic.
2. **Configurar conectores** — fuentes de datos / servicios externos.
3. **Generar Token API** del servicio que se va a llamar (Notion en el
   ejemplo).
4. **Configurar la llamada** — endpoint, método, payload.
5. **Configurar encabezados HTTP** con las claves requeridas por el
   servicio (ver Capa 2 para el caso Notion).
6. **Activar y probar** — primero en seco, después con datos reales.

## Capa 2 — APIs externas (caso Notion)

### Encabezados requeridos por Notion

```
Authorization: Bearer <secret_xxxxxxxxxxxxx>
Notion-Version: 2022-06-28
Content-Type: application/json
```

- `Authorization` con el token secreto generado en
  https://www.notion.so/my-integrations.
- `Notion-Version` fija la versión del API contra la que se programa
  (Notion es estricto con esto).
- `Content-Type: application/json` siempre que el body sea JSON.

### Patrón general para CUALQUIER API

| Paso | Qué hacer | Compuerta 🚦 |
|---|---|---|
| 1 | Leer la doc oficial del proveedor | No improvisar |
| 2 | Crear el Token con el scope MÍNIMO | No darle "admin" si solo necesitas "lectura" |
| 3 | Guardar el Token en variable de entorno o gestor de secretos | **Nunca** dentro del SKILL.md |
| 4 | Programar la primera llamada con `curl` o Postman | Validar antes de meter en Routine |
| 5 | Manejar errores 401 (auth) y 429 (rate limit) | Backoff exponencial |

### Resolución de errores del video (timestamp 21:35)

El video dedica varios minutos a *solución de errores* — síntoma de
que la frustración más común son:
- Token mal pegado (espacios, comillas).
- Encabezado faltante (`Notion-Version` es el más olvidado).
- Body con JSON malformado (comas sobrantes).
- Permisos del Token: olvidaron compartir la página de Notion con la
  integración.

## Capa 3 — Skills en GitHub

### Qué propone Cilleruelo (timestamp 24:05)

Vincular un repositorio GitHub a la cuenta de Claude para que las
skills locales se publiquen + versionen + sirvan a Routines remotas.

### Estado actual de este computador

- `C:\Users\datos\.claude\skills\` tiene **60+ skills** locales (ver
  MEMORY.md).
- NO está bajo control de versiones git.
- NO está en GitHub.
- Riesgo concreto: una corrupción del disco o un error de edición
  pierde meses de destilación.

### Camino propuesto (NO ejecutado todavía — esperando confirmación)

Ver skill hermana [[skills-versionado-git-github]] para el plan
operativo: convertir el directorio en repo git, separar
secretos/cookies vía `.gitignore`, conectar a GitHub privado del
usuario, automatizar commits diarios.

## Compuertas 🚦

1. **Nunca subir cookies, tokens, archivos cookie.txt, ni SID** —
   `.gitignore` obligatorio antes del primer commit.
2. **Nunca subir credenciales** de Edge debug, NotebookLM, Wolfram,
   ni de cuentas Gmail.
3. **Repo privado** por defecto, no público.
4. **Antes de cada commit revisar el diff** — la auto-augmentación
   por pipeline puede meter datos del usuario (URLs de tweets, autores
   curados) que pueden ser personales.
5. **Routines remotas pueden facturar tokens** — vigilar el monitor
   de uso (skill `inventario-extensiones-edge-jjmobijuesa` lista la
   extensión "Claude Usage Meter" que ayuda).
6. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cómo depurar si falla

- **401 Unauthorized** — Token expirado o mal pegado. Re-generar.
- **403 Forbidden** — La integración no tiene acceso al recurso
  (Notion: compartir página con la integración).
- **Routine no dispara** — Verificar que el conector esté autorizado
  y el cron sea válido.
- **Skill no aparece desde GitHub** — El YAML frontmatter debe estar
  intacto y el archivo debe llamarse exactamente `SKILL.md`.

## Relacionado

- [[era-pc-agentico-doctrina]] — marco histórico-arquitectónico.
- [[skills-versionado-git-github]] — plan operativo para Capa 3.
- [[llave-maestra-autoaprendizaje-ia]] — doctrina padre.
- [[agente-local-autoreflexivo-bookmarks]] — instancia ya funcional.
- `mcp__scheduled-tasks__*` — Routines locales (hoy).
