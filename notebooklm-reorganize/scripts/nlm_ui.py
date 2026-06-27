"""Primitivas Playwright para manipular categorias y fuentes en NotebookLM.

Estas funciones operan sobre un objeto `page` de Playwright ya navegado al cuaderno.
Se asume que el perfil Edge persistente esta autenticado.

Imports tipicos en un script consumidor:
    from playwright.sync_api import sync_playwright
    from pathlib import Path
    PROFILE = Path.home() / ".notebooklm" / "browser_profile_edge"
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
        # ... operaciones ...
"""
import json
from pathlib import Path


def expand_all(page, wait_ms_per_panel=400):
    """Expande todos los paneles colapsados para que sus fuentes sean visibles."""
    headers = page.locator('mat-expansion-panel-header')
    for i in range(headers.count()):
        try:
            if headers.nth(i).get_attribute("aria-expanded") == "false":
                headers.nth(i).click()
                page.wait_for_timeout(wait_ms_per_panel)
        except Exception:
            pass


def find_panel(page, title_text):
    """Devuelve el indice del primer panel cuyo titulo contenga title_text, o -1."""
    return page.evaluate(rf"""() => {{
        const panels = document.querySelectorAll('mat-expansion-panel');
        for (let i = 0; i < panels.length; i++) {{
            const t = panels[i].querySelector('mat-panel-title');
            if (t && t.innerText.includes({json.dumps(title_text)})) return i;
        }}
        return -1;
    }}""")


def find_all_panels(page, title_text):
    """Devuelve lista de indices de paneles cuyo titulo contenga title_text."""
    return page.evaluate(rf"""() => {{
        const result = [];
        const panels = document.querySelectorAll('mat-expansion-panel');
        for (let i = 0; i < panels.length; i++) {{
            const t = panels[i].querySelector('mat-panel-title');
            if (t && t.innerText.includes({json.dumps(title_text)})) result.push(i);
        }}
        return result;
    }}""")


def expand_panel(page, idx):
    """Expande un panel especifico por indice."""
    panel = page.locator('mat-expansion-panel').nth(idx)
    header = panel.locator('mat-expansion-panel-header')
    if header.get_attribute("aria-expanded") == "false":
        header.click()
        page.wait_for_timeout(1000)


def _category_action(page, panel_idx, action_text, hover_first=True):
    """Abre el more_vert de la categoria y hace click en la opcion (Rename/Remove/Add emoji)."""
    panel = page.locator('mat-expansion-panel').nth(panel_idx)
    header = panel.locator('mat-expansion-panel-header')
    header.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    if hover_first:
        header.hover()
        page.wait_for_timeout(500)
    more_vert = panel.locator('button:has-text("more_vert")').first
    more_vert.click(force=True, timeout=8000)
    page.wait_for_timeout(1200)
    page.locator(f'[role="menuitem"]:has-text("{action_text}")').first.click(timeout=5000)
    page.wait_for_timeout(1500)


def rename_category(page, old_name, new_name):
    """Renombra una categoria. Idempotente: si new_name ya existe, retorna True."""
    if find_panel(page, new_name) >= 0:
        return True
    idx = find_panel(page, old_name)
    if idx < 0:
        return False
    expand_panel(page, idx)
    _category_action(page, idx, "Rename")
    page.keyboard.press("Control+a")
    page.wait_for_timeout(150)
    page.keyboard.type(new_name)
    page.wait_for_timeout(300)
    page.keyboard.press("Enter")
    page.wait_for_timeout(2000)
    return find_panel(page, new_name) >= 0


def rename_panel_by_idx(page, panel_idx, new_name):
    """Variante que renombra por indice (util cuando varios paneles tienen el mismo nombre)."""
    _category_action(page, panel_idx, "Rename")
    page.keyboard.press("Control+a")
    page.wait_for_timeout(150)
    page.keyboard.type(new_name)
    page.wait_for_timeout(300)
    page.keyboard.press("Enter")
    page.wait_for_timeout(2000)


def add_new_label(page, name):
    """Crea una etiqueta nueva.

    El boton 'Add new label' crea una categoria con nombre default 'New Label' y NO
    pregunta por el nombre. Despues hay que renombrarla via more_vert -> Rename.
    """
    if find_panel(page, name) >= 0:
        return True

    # Open the relabel panel
    btn = page.locator('button[aria-label="Undo or re-label sources"]').first
    btn.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    btn.click(force=True)
    page.wait_for_timeout(2000)

    try:
        page.locator(
            '[role="menuitem"]:has-text("Add new label"), button:has-text("Add new label")'
        ).first.click(timeout=5000)
    except Exception:
        page.keyboard.press("Escape")
        return False
    page.wait_for_timeout(2500)

    # Find the freshly-created "New Label" panel and rename it
    new_idx = find_panel(page, "New Label")
    if new_idx < 0:
        return False
    try:
        rename_panel_by_idx(page, new_idx, name)
    except Exception:
        return False

    # Cleanup any extra "New Label" that may have been created accidentally
    while True:
        extras = find_all_panels(page, "New Label")
        if not extras:
            break
        try:
            delete_category(page, extras[0])
            page.wait_for_timeout(1500)
        except Exception:
            break

    return find_panel(page, name) >= 0


def delete_category(page, panel_idx):
    """Borra una categoria. Si NotebookLM pide confirmacion, intenta confirmarla."""
    _category_action(page, panel_idx, "Remove")
    page.wait_for_timeout(1500)
    try:
        page.locator(
            'button:has-text("Remove"), button:has-text("Confirm"), '
            'button:has-text("Eliminar"), button:has-text("Borrar")'
        ).last.click(timeout=3000)
        page.wait_for_timeout(1500)
    except Exception:
        pass


def move_source(page, src_substring, target_substring):
    """Mueve una fuente a otra categoria.

    IMPORTANTE: en NotebookLM, 'Move to' es ADITIVO — agrega la etiqueta sin remover
    las existentes. Para asignacion exclusiva, usa el flujo delete + re-upload + move
    documentado en SKILL.md.

    src_substring: substring del aria-label de la fuente (parte del nombre del archivo)
    target_substring: substring del nombre de la categoria destino
    """
    expand_all(page)
    page.wait_for_timeout(1500)

    src_loc = page.locator(f'button.source-stretched-button[aria-label*="{src_substring}"]').first
    if src_loc.count() == 0:
        return False

    src_loc.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    bbox = src_loc.bounding_box()
    page.mouse.move(bbox["x"] + 50, bbox["y"] + bbox["height"] / 2)
    page.wait_for_timeout(1200)

    # More button is inside div.single-source-container ancestor
    more_btn = src_loc.locator(
        'xpath=ancestor::div[contains(@class, "single-source-container")][1]//button[@aria-label="More"]'
    ).first
    try:
        more_btn.click(force=True, timeout=10000)
    except Exception:
        return False
    page.wait_for_timeout(1500)

    try:
        page.locator('[role="menuitem"]:has-text("Move to")').first.click(timeout=5000)
    except Exception:
        page.keyboard.press("Escape")
        return False
    page.wait_for_timeout(2500)

    try:
        page.locator(f'[role="menuitem"]:has-text("{target_substring}")').first.click(timeout=5000)
        page.wait_for_timeout(3000)
        return True
    except Exception:
        page.keyboard.press("Escape")
        return False


def dump_state(page):
    """Devuelve lista de {category, sources[]} para todos los paneles. Expande primero."""
    expand_all(page)
    page.wait_for_timeout(2000)
    return page.evaluate(r"""() => {
        const out = [];
        document.querySelectorAll('mat-expansion-panel').forEach(panel => {
            const t = panel.querySelector('mat-panel-title');
            const title = t ? t.innerText
                .replace('keyboard_arrow_down','')
                .replace('keyboard_arrow_right','')
                .replace('more_vert','').trim() : '';
            const sources = [];
            panel.querySelectorAll('button.source-stretched-button').forEach(b => {
                sources.push(b.getAttribute('aria-label') || '');
            });
            out.push({category: title, count: sources.length, sources});
        });
        return out;
    }""")
