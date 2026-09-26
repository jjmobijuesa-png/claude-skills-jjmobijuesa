#!/usr/bin/env bash
# Checkpoint en caliente: si cambió algo en memoria-compartida-sesiones/, commit + push.
# Pensado para un hook Stop (se ejecuta al terminar cada respuesta de Claude).
# Activación aprobada por el usuario el 2026-09-26 (relevo automático, opción 2).
DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
cd "$REPO" || exit 0
if [ -n "$(git status --porcelain -- memoria-compartida-sesiones)" ]; then
  git add memoria-compartida-sesiones >/dev/null 2>&1
  git commit -q -m "relevo: checkpoint automático $(date '+%Y-%m-%d %H:%M')" >/dev/null 2>&1
  git pull -q --rebase >/dev/null 2>&1
  git push -q >/dev/null 2>&1
fi
exit 0
