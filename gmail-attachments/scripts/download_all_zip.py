"""Descarga TODOS los adjuntos de un hilo Gmail como UN ZIP y los extrae.

Más robusto que descargar adjunto por adjunto (que se cuelga en page.expect_download
cuando Gmail abre vistas previas). Usa el botón "Descargar todos los archivos adjuntos".

Uso:
    python download_all_zip.py <profile_tag> <target_dir> <thread_id> [authuser_index] [--keep-zip]

    profile_tag : perfil Edge persistente (~/.notebooklm/browser_profile_<tag>); ej. 'jjm'.
    target_dir  : carpeta destino (se crea si no existe).
    thread_id   : id del hilo (de search_threads del Gmail MCP).
    authuser_index : índice de cuenta en /mail/u/N/ (por defecto 0; el perfil dedicado suele ser 0).

Ejemplo:
    python download_all_zip.py jjm "C:/.../Adjuntos SEM 24" 19ecdd85755653c2
"""
import sys, re, zipfile
from pathlib import Path
from playwright.sync_api import sync_playwright

def main():
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    tag = sys.argv[1]
    target = Path(sys.argv[2]); target.mkdir(parents=True, exist_ok=True)
    tid = sys.argv[3]
    rest = sys.argv[4:]
    keep_zip = "--keep-zip" in rest
    idx = next((a for a in rest if a.isdigit()), "0")

    prof = Path.home() / ".notebooklm" / f"browser_profile_{tag}"
    if not prof.exists():
        print(f"Perfil no existe: {prof}. Corre login.py con tag '{tag}'."); sys.exit(1)

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(prof), channel="msedge", headless=False,
            accept_downloads=True, args=["--disable-blink-features=AutomationControlled"])
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.set_default_timeout(60000)
        page.goto(f"https://mail.google.com/mail/u/{idx}/#inbox", wait_until="load")
        page.wait_for_timeout(4000)
        if "accounts.google.com" in page.url:
            print(f"Sesion no activa. Corre login.py con tag '{tag}'."); ctx.close(); sys.exit(1)

        page.evaluate(f"() => {{ window.location.hash = 'inbox/{tid}'; }}")
        page.wait_for_timeout(7000)

        # 1) intentar el enlace/boton "Descargar todos" (zip) — ES e EN
        sels = ('[aria-label*="Descargar todos"],[data-tooltip*="Descargar todos"],'
                '[aria-label*="Download all"],[data-tooltip*="Download all"],'
                'a[href*="disp=zip"]')
        zip_saved = None
        el = page.query_selector(sels)
        if el:
            try:
                with page.expect_download(timeout=45000) as dli:
                    el.click()
                d = dli.value
                zip_saved = target / (d.suggested_filename or f"adjuntos_{tid}.zip")
                d.save_as(str(zip_saved))
                print(f"  zip -> {zip_saved}")
            except Exception as e:
                print(f"  fallo boton 'Descargar todos': {str(e)[:120]}")

        # 2) fallback: construir URL disp=zip desde cualquier enlace view=att
        if not zip_saved:
            href = page.evaluate(r"""() => {
                const a = document.querySelector('a[href*="view=att"]');
                return a ? a.href : null;
            }""")
            if href:
                zurl = re.sub(r"&disp=[^&]*", "", href)
                zurl = re.sub(r"&attid=[^&]*", "", zurl) + "&disp=zip&zw"
                try:
                    with page.expect_download(timeout=45000) as dli:
                        page.evaluate("""(u)=>{const a=document.createElement('a');a.href=u;a.target='_self';
                            document.body.appendChild(a);a.click();a.remove();}""", zurl)
                    d = dli.value
                    zip_saved = target / (d.suggested_filename or f"adjuntos_{tid}.zip")
                    d.save_as(str(zip_saved)); print(f"  zip(fallback) -> {zip_saved}")
                except Exception as e:
                    print(f"  fallo fallback zip: {str(e)[:120]}")
        ctx.close()

    if not zip_saved:
        print("NO se pudo descargar el zip. Usa download.py (adjunto por adjunto) como respaldo.")
        sys.exit(2)

    # extraer
    n = 0
    with zipfile.ZipFile(zip_saved) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            name = Path(info.filename).name
            with z.open(info) as src, open(target / name, "wb") as out:
                out.write(src.read()); n += 1
                print(f"    extraido: {name}")
    if not keep_zip:
        zip_saved.unlink(missing_ok=True)
    print(f"OK: {n} adjuntos en {target}")

if __name__ == "__main__":
    main()
