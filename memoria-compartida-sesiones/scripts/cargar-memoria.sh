#!/usr/bin/env bash
# Carga la memoria compartida al iniciar sesión (hook SessionStart).
# Sincroniza el repo y muestra el índice + las últimas entradas de la bitácora.
DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
git -C "$REPO" pull -q --ff-only >/dev/null 2>&1 || true
echo "=== MEMORIA COMPARTIDA (memoria-compartida-sesiones) ==="
[ -f "$DIR/MEMORIA.md" ] && cat "$DIR/MEMORIA.md"
echo
echo "=== Últimas entradas de bitácora ==="
ls -1 "$DIR/bitacora"/*.md 2>/dev/null | sort | tail -n 3 | while read -r f; do
  echo "--- $(basename "$f") ---"
  cat "$f"
  echo
done
exit 0
