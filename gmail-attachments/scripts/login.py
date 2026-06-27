"""Login inicial al perfil Edge para un Gmail especifico.

Uso:
    python login.py <profile_tag>

Abre Edge con perfil dedicado y espera a que el usuario inicie sesion.
Cuando el usuario confirma (envia senal), guarda la sesion.

Senal de guardado (desde otra shell):
    python -c "import tempfile, os; open(os.path.join(tempfile.gettempdir(), 'gmail_login_signal'), 'w').close()"
"""
import sys, time, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    tag = sys.argv[1]
    profile = Path.home() / ".notebooklm" / f"browser_profile_{tag}"
    signal = Path(tempfile.gettempdir()) / "gmail_login_signal"
    signal.unlink(missing_ok=True)

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(profile),
            channel="msedge",
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto("https://mail.google.com/mail/u/0/#inbox")
        print(f"Edge abierto con perfil '{tag}'. Inicia sesion y envia la senal de guardado...")
        while not signal.exists():
            time.sleep(1)
        signal.unlink(missing_ok=True)
        # Verify
        page.wait_for_timeout(2000)
        if "accounts.google.com" in page.url:
            print(f"AVISO: aun en pagina de login: {page.url}")
        else:
            print(f"OK. Sesion guardada para '{tag}'.")
        ctx.close()


if __name__ == "__main__":
    main()
