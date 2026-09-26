# Prompt para la sesión local "<nombre>"

---
Este hilo tiene un agente espejo en la nube; nos comunicamos por GitHub (repo privado `jjmobijuesa-png/claude-skills-jjmobijuesa`, clonado en `~/.claude/skills`). Lo apruebo expresamente.

1. `cd ~/.claude/skills && git pull origin main`. Lee `memoria-compartida-sesiones/SKILL.md` y `RELEVO.md` y aplícalos.
2. Tu canal es `memoria-compartida-sesiones/relevos/<hilo>/`. Haz el primer checkpoint: copia a `archivos/` los archivos centrales (marca el principal; sin credenciales), completa `ESTADO.md` (tema, razonamiento en curso, siguiente paso, pendientes) y agrega una fila a `HISTORIAL.md`. Commit y push a `main`.
3. Checkpoint después de cada avance. Ante aviso de límite o "pasa la posta": TURNO = NUBE, push, y avísame.
4. "Retoma la posta": `git pull origin main`, lee ESTADO y los cambios del espejo en `archivos/`, y continúa.
---
