#!/usr/bin/env bash
# Checkpoint en caliente del relevo PC ⇄ nube (aprobado por el usuario, 2026-09-26).
# Se ejecuta desde hooks PostToolUse (cada Write/Edit) y Stop (fin de respuesta),
# y el agente puede llamarlo a mano en medio de una respuesta.
# Si cambió algo en memoria-compartida-sesiones/: commit, integra origin/main y
# publica en main (canal único del relevo) y en la rama actual.
DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
cd "$REPO" || exit 0
[ -n "$(git status --porcelain -- memoria-compartida-sesiones)" ] || exit 0
git add memoria-compartida-sesiones >/dev/null 2>&1
git commit -q -m "relevo: checkpoint en caliente $(date '+%Y-%m-%d %H:%M:%S')" >/dev/null 2>&1
git fetch -q origin main >/dev/null 2>&1
git merge -q --no-edit origin/main >/dev/null 2>&1 || git merge --abort >/dev/null 2>&1
git push -q origin HEAD:main >/dev/null 2>&1
BR="$(git rev-parse --abbrev-ref HEAD)"
[ "$BR" != "main" ] && git push -q origin "HEAD:$BR" >/dev/null 2>&1
exit 0
