"""Diagnostico: abre un cuaderno y dumpea categoria -> fuentes.

Uso:
    python diagnose.py <notebook_id>
"""
import sys, json, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
from nlm_ui import dump_state

PROFILE = Path.home() / ".notebooklm" / "browser_profile_edge"


def main():
    if len(sys.argv) < 2:
        print("Uso: python diagnose.py <notebook_id>")
        sys.exit(1)
    nb = sys.argv[1]
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE),
            channel="msedge",
            headless=False,
            viewport={"width": 1500, "height": 950},
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.set_default_timeout(60000)
        page.goto(f"https://notebooklm.google.com/notebook/{nb}", wait_until="load")
        page.wait_for_timeout(8000)
        state = dump_state(page)
        print(json.dumps(state, indent=2, ensure_ascii=False))
        time.sleep(2)
        ctx.close()


if __name__ == "__main__":
    main()
