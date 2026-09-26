# Prompt para pegar en la sesión "Agente IA Local autoreflexivo"

Copia lo que está entre las líneas y pégalo en esa sesión (en la PC o desde la app vía Remote Control).

---
Vamos a activar el protocolo de relevo automático con un agente espejo en la nube para este hilo. Lo apruebo expresamente.

1. Sincroniza mis skills: `cd ~/.claude/skills && git pull origin main`.
   Lee `memoria-compartida-sesiones/SKILL.md` y `memoria-compartida-sesiones/RELEVO.md` y aplícalos desde ahora.
2. Agrega en `~/.claude/settings.json` (sin borrar hooks existentes) dos hooks:
   - `SessionStart` → `bash ~/.claude/skills/memoria-compartida-sesiones/scripts/cargar-memoria.sh`
   - `Stop` → `bash ~/.claude/skills/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh`
   Muéstrame el JSON final antes de guardarlo.
3. Haz el PRIMER CHECKPOINT de este hilo en `~/.claude/skills/memoria-compartida-sesiones/relevos/agente-ia-local-autoreflexivo/`:
   - Copia a `archivos/` los documentos y archivos centrales en los que estamos trabajando (marca el principal). Nada de credenciales.
   - Completa `ESTADO.md`: tema, razonamiento en curso (suficiente para que otro agente continúe sin esta conversación), archivos centrales, siguiente paso concreto y pendientes. Deja TURNO = PC.
   - Commit y push a `main`.
4. Desde ahora, actualiza `ESTADO.md` y `archivos/` después de cada avance significativo. Si ves un aviso de límite de uso, de cupo o crédito por agotarse, o te digo "pasa la posta", entrega la posta (TURNO = NUBE) según RELEVO.md y avísame.
5. Cuando te diga "retoma la posta", haz `git pull`, lee ESTADO.md y lo que el espejo cambió en `archivos/`, y continúa desde ahí.

Confírmame qué archivos subiste y cuál es el siguiente paso registrado.
---
