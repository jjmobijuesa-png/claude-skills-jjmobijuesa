"""Ejemplo completo de reorganizacion: 5 renames + 2 new labels + 2 moves + cleanup.

Adapta NOTEBOOK_ID, RENAMES, NEW_LABELS y MOVES a tu caso.
"""
import sys, json, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
from nlm_ui import (
    rename_category, add_new_label, move_source, delete_category,
    dump_state, find_all_panels,
)

PROFILE = Path.home() / ".notebooklm" / "browser_profile_edge"

# === CONFIG (ejemplo: cuaderno EPACEM de la auditoria forense QVP) ===
NOTEBOOK_ID = "1a04175a-37e6-49e8-8cb9-abc961b19fdc"

RENAMES = [
    ("Auditoría Forense", "0. METODO — Marco Forense"),
    ("Gestión de Información", "0. METODO — Oficio y Gestión"),
    ("Deuda Oro Rojo", "PBC-A · Registros (Préstamo Oro Rojo)"),
    ("Maquila Orojuez", "PBC-A · Registros (Maquila OROJUEZ)"),
    ("Deuda David Juez", "PBC-B · Tesorería (Ancla USD 600 K)"),
]

NEW_LABELS = [
    "1. CONTEXTO — Perfil del Caso",
    "PBC-C — Contratos",
]

# (source_aria_substring, target_category_substring)
MOVES = [
    ("01-CONTEXTO_Datos Epacem", "1. CONTEXTO"),
    ("PBC-C1_Tabla de amortizacion", "PBC-C —"),
]


def main():
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE),
            channel="msedge",
            headless=False,
            viewport={"width": 1500, "height": 950},
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.set_default_timeout(60000)
        page.goto(f"https://notebooklm.google.com/notebook/{NOTEBOOK_ID}", wait_until="load")
        page.wait_for_timeout(8000)

        print("=== RENAMES ===")
        for old, new in RENAMES:
            ok = rename_category(page, old, new)
            print(f"  '{old}' -> '{new}': {'OK' if ok else 'FAIL'}")

        print("\n=== ADD LABELS ===")
        for name in NEW_LABELS:
            ok = add_new_label(page, name)
            print(f"  '{name}': {'OK' if ok else 'FAIL'}")

        # Cleanup any stray "New Label" panels left over
        while find_all_panels(page, "New Label"):
            extras = find_all_panels(page, "New Label")
            print(f"  cleanup 'New Label' at panel {extras[0]}")
            try:
                delete_category(page, extras[0])
                page.wait_for_timeout(1500)
            except Exception:
                break

        print("\n=== MOVES ===")
        for src, tgt in MOVES:
            ok = move_source(page, src, tgt)
            print(f"  '{src}' -> '{tgt}': {'OK' if ok else 'FAIL'}")

        print("\n=== ESTADO FINAL ===")
        print(json.dumps(dump_state(page), indent=2, ensure_ascii=False))

        time.sleep(3)
        ctx.close()


if __name__ == "__main__":
    main()
