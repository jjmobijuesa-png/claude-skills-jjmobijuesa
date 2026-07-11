# -*- coding: utf-8 -*-
"""
Orquestador end-to-end de reenvío de adjuntos por Gmail.

Encadena las skills existentes gmail-attachments (descarga + extrae
ZIP) + gmail-send-playwright (envía con adjuntos) en un solo comando.

Uso mínimo:
    python relay.py \
        --profile jjm \
        --source-thread 19ecdd85755653c2 \
        --to "destino@dominio.com" \
        --subject "Reenvío adjuntos SEM 24" \
        --body-file body.txt

Opciones:
    --profile           tag del perfil Edge (~/.notebooklm/browser_profile_<tag>).
    --source-thread     thread_id origen (de Gmail MCP search_threads).
    --to                destinatarios coma-separados.
    --subject           asunto del nuevo mensaje.
    --body-file         archivo texto plano con el cuerpo.
    --attach-filter     regex opcional; solo reenvía adjuntos que
                        matcheen (por nombre). Ejemplos:
                        --attach-filter "\.pdf$"
                        --attach-filter "SEM.*\.xlsx?$"
    --exclude-filter    regex opcional; excluye adjuntos que matcheen.
    --extra-attach      ruta adicional a adjuntar (repetible).
    --work-dir          carpeta temp para extracción.
                        Default: %TEMP%\gmail-relay-<uuid>.
    --keep-work-dir     no borrar work-dir al final (para inspección).
    --dry-run           descarga+lista pero NO envía. Útil para validar.

Compuertas:
    - Nunca envía sin --to, --subject, --body-file y adjuntos ≥1.
    - Si --dry-run, imprime lista de adjuntos filtrados y sale.
    - Nunca envía credenciales, tokens ni cookies.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VENV_PY = Path(r"C:\Users\datos\.notebooklm-venv\Scripts\python.exe")
SKILL_DOWNLOAD = Path(
    r"C:\Users\datos\.claude\skills\gmail-attachments\scripts\download_all_zip.py"
)
SKILL_SEND = Path(
    r"C:\Users\datos\.claude\skills\gmail-send-playwright\scripts\send.py"
)


def parse_args():
    ap = argparse.ArgumentParser(
        description="Reenvía adjuntos de un hilo Gmail a otro destino."
    )
    ap.add_argument("--profile", required=True)
    ap.add_argument("--source-thread", required=True)
    ap.add_argument("--to", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("--body-file", required=True)
    ap.add_argument("--attach-filter", default=None,
                    help="regex; solo incluye archivos que matcheen")
    ap.add_argument("--exclude-filter", default=None,
                    help="regex; excluye archivos que matcheen")
    ap.add_argument("--extra-attach", action="append", default=[],
                    help="adjunto adicional del disco (repetible)")
    ap.add_argument("--work-dir", default=None)
    ap.add_argument("--keep-work-dir", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--authuser", default="0",
                    help="índice authuser Gmail (default 0 en perfil dedicado)")
    return ap.parse_args()


def pretty_size(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def paso(n, titulo):
    print(f"\n═══ Paso {n} · {titulo} ═══")


def main():
    args = parse_args()
    body_path = Path(args.body_file)
    if not body_path.exists():
        print(f"ERROR: body-file no existe: {body_path}")
        sys.exit(1)

    # Validaciones defensivas
    if not VENV_PY.exists():
        print(f"ERROR: venv Python no existe: {VENV_PY}")
        sys.exit(1)
    for s in (SKILL_DOWNLOAD, SKILL_SEND):
        if not s.exists():
            print(f"ERROR: script hermano no existe: {s}")
            sys.exit(1)

    # Carpeta de trabajo
    if args.work_dir:
        work = Path(args.work_dir)
    else:
        work = Path(tempfile.gettempdir()) / f"gmail-relay-{uuid.uuid4().hex[:8]}"
    work.mkdir(parents=True, exist_ok=True)
    print(f"Work-dir: {work}")

    try:
        # ============================================
        # Paso 1: descargar adjuntos como ZIP + extraer
        # ============================================
        paso(1, "Descargar ZIP del thread origen + extraer")
        cmd = [
            str(VENV_PY), str(SKILL_DOWNLOAD),
            args.profile, str(work), args.source_thread, args.authuser,
        ]
        print("  →", " ".join(cmd))
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        print(r.stdout[-2000:] if r.stdout else "")
        if r.returncode != 0:
            print(f"ERROR descarga (exit {r.returncode}):")
            print(r.stderr[-1500:])
            sys.exit(2)

        # =====================================
        # Paso 2: enumerar y filtrar adjuntos
        # =====================================
        paso(2, "Enumerar adjuntos extraídos + aplicar filtros")
        candidates = sorted(p for p in work.iterdir() if p.is_file())
        print(f"  Archivos extraídos: {len(candidates)}")
        for p in candidates:
            print(f"    - {p.name}  ({pretty_size(p.stat().st_size)})")

        selected = list(candidates)
        if args.attach_filter:
            rx = re.compile(args.attach_filter, re.I)
            selected = [p for p in selected if rx.search(p.name)]
            print(f"  Tras --attach-filter '{args.attach_filter}': {len(selected)}")
        if args.exclude_filter:
            rx = re.compile(args.exclude_filter, re.I)
            selected = [p for p in selected if not rx.search(p.name)]
            print(f"  Tras --exclude-filter '{args.exclude_filter}': {len(selected)}")

        # Extras del disco
        for extra in args.extra_attach:
            ep = Path(extra)
            if not ep.exists():
                print(f"  AVISO: extra-attach no existe: {ep}")
                continue
            selected.append(ep)
            print(f"    + extra: {ep.name}  ({pretty_size(ep.stat().st_size)})")

        if not selected:
            print("ERROR: no hay adjuntos que reenviar tras filtros.")
            sys.exit(3)

        total = sum(p.stat().st_size for p in selected)
        print(f"  Total a adjuntar: {len(selected)} archivos, {pretty_size(total)}")
        if total > 25 * 1024 * 1024:
            print("  AVISO: >25 MB; Gmail podría rechazar. Considera Drive.")

        # ============================
        # Paso 3: dry-run o enviar
        # ============================
        if args.dry_run:
            paso(3, "DRY-RUN — no se envía")
            print(f"  Would send to: {args.to}")
            print(f"  Subject: {args.subject}")
            print(f"  Body first 200: {body_path.read_text(encoding='utf-8')[:200]}")
            return

        paso(3, "Redactar y enviar el nuevo correo")
        cmd = [
            str(VENV_PY), str(SKILL_SEND),
            "--profile", args.profile,
            "--to", args.to,
            "--subject", args.subject,
            "--body-file", str(body_path),
        ]
        for p in selected:
            cmd += ["--attach", str(p)]

        print(f"  → send.py con {len(selected)} adjuntos …")
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        print(r.stdout[-2500:] if r.stdout else "")
        if r.returncode != 0:
            print(f"ERROR envío (exit {r.returncode}):")
            print(r.stderr[-1500:])
            sys.exit(4)

        print("\n✓ RELAY completado.")
        if "ENVIADO CONFIRMADO" in (r.stdout or ""):
            print("✓ Verificado en Sent.")
        else:
            print("AVISO: no se confirmó Sent en el primer barrido; revisar manualmente.")

    finally:
        if not args.keep_work_dir:
            try:
                shutil.rmtree(work)
                print(f"Work-dir borrado: {work}")
            except Exception as e:
                print(f"AVISO: no se pudo borrar work-dir: {e}")


if __name__ == "__main__":
    main()
