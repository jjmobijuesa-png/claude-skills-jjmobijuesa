#!/usr/bin/env bash
# Hook UserPromptSubmit: antes de cada respuesta trae lo último de main
# (lo que dejó el otro agente) y muestra el TURNO de cada hilo.
DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
cd "$REPO" || exit 0
git fetch -q origin main >/dev/null 2>&1
git merge -q --no-edit origin/main >/dev/null 2>&1 || git merge --abort >/dev/null 2>&1
echo "[relevo] Sincronizado con origin/main $(git log -1 --format='%h %cd' --date=format:'%Y-%m-%d %H:%M' origin/main 2>/dev/null)"
for f in "$DIR"/relevos/*/ESTADO.md; do
  case "$f" in */_plantilla/*) continue;; esac
  h="$(basename "$(dirname "$f")")"
  t="$(grep -m1 '\*\*TURNO\*\*' "$f" | sed 's/.*| *\([A-Z]*\) *|.*/\1/')"
  c="$(grep -m1 'Último checkpoint' "$f" | sed 's/.*Último checkpoint *| *//; s/ *|$//')"
  echo "[relevo] $h — TURNO: $t — último checkpoint: $c"
done
exit 0
