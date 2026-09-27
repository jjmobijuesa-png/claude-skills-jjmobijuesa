# Bitácora — 2026-09-26 (nube) — Relevo automático y agente espejo

Continuación de la sesión nube "Ver otras sesiones de Claude Code".

## Qué se pidió
- Que el razonamiento de un hilo no se rompa por fin de cupo, intervalo de 5 h o crédito.
- Que un agente espejo en la nube continúe el mismo archivo y devuelva la posta al agente principal (PC).
- Que sea automático y en caliente. El usuario eligió expresamente la **opción 2: relevo automático**.

## Qué se hizo
- `RELEVO.md`: protocolo de posta con el campo TURNO (PC | NUBE); trabaja un solo agente a la vez.
- `relevos/agente-ia-local-autoreflexivo/`: ESTADO.md (TURNO = PC), HISTORIAL.md, archivos/.
- `scripts/checkpoint-relevo.sh` + hook `Stop` en `.claude/settings.json` del repo.
- `PROMPT-agente-local.md`: prompt completo con toda la historia para el agente de la PC.
- PR #2 hacia `main`: https://github.com/jjmobijuesa-png/claude-skills-jjmobijuesa/pull/2

## Decisiones
- El espejo es esta sesión de la nube; el principal es "Agente IA Local autoreflexivo".
- El agente no ve su saldo exacto → checkpoint después de cada avance, no solo al final.
- Los checkpoints de la nube caen en la rama de la sesión; al devolver la posta, el espejo lleva los cambios a `main` con confirmación del usuario.

## Pendientes
- [ ] Merge del PR #2.
- [ ] Pegar PROMPT-agente-local.md en la sesión local (hooks + primer checkpoint).
- [ ] Identificar el archivo principal.
