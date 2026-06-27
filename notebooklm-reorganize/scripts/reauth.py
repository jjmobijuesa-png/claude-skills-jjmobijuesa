"""Reautenticacion del perfil Edge persistente para NotebookLM.

Abre Edge en modo no-headless, el usuario inicia sesion en su cuenta NotebookLM,
y se guardan las cookies en ~/.notebooklm/profiles/default/storage_state.json para
que el CLI `notebooklm` tambien funcione.

Uso:
    1. python reauth.py    (abre Edge)
    2. Inicia sesion en la cuenta deseada en notebooklm.google.com
    3. Cuando estes dentro, ejecuta en otra shell:
       python -c "import tempfile, os; open(os.path.join(tempfile.gettempdir(), 'nlm_save_signal'), 'w').close()"
    4. El script captura, guarda y sale.
"""
import json, time, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

STORAGE_PATH = Path.home() / ".notebooklm" / "profiles" / "default" / "storage_state.json"
PROFILE_PATH = Path.home() / ".notebooklm" / "browser_profile_edge"
SIGNAL_FILE = Path(tempfile.gettempdir()) / "nlm_save_signal"

SIGNAL_FILE.unlink(missing_ok=True)
STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Abriendo Edge. Inicia sesion en NotebookLM y luego envia la senal de guardado...", flush=True)
with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=str(PROFILE_PATH),
        channel="msedge",
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
    )
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto("https://notebooklm.google.com/")
    while not SIGNAL_FILE.exists():
        time.sleep(1)
    storage = browser.storage_state()
    with open(STORAGE_PATH, "w") as f:
        json.dump(storage, f)
    print(f"Guardadas {len(storage.get('cookies', []))} cookies en {STORAGE_PATH}", flush=True)
    browser.close()
SIGNAL_FILE.unlink(missing_ok=True)
print("OK. Ahora `notebooklm auth check --test` deberia pasar Token fetch.")
