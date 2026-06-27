---
name: notebooklm-reorganize
description: "Reorganize labels and sources in a NotebookLM notebook via the web UI (Playwright + Edge). Use when the user wants to rename auto-generated category labels, add custom labels, move sources between labels, or delete labels. Triggers: 'reorganize NotebookLM notebook', 'rename notebook categories', 'create new label in NotebookLM', 'move sources between labels', 'agrupar fuentes en NotebookLM', 'renombrar etiquetas del cuaderno', 'mover fuente entre categorías'. The NotebookLM Python CLI's rename only changes the source title — the category labels visible in the web UI are a separate layer that must be edited through the UI. This skill drives the actual UI to make changes the user sees."
user-invocable: true
---

# NotebookLM — Reorganize categories & sources

NotebookLM auto-groups sources into AI-generated category labels visible in the source panel as expansion accordions. These labels are separate from the source `title` field that the `notebooklm` CLI manipulates. To change what the user sees in the web UI, drive the UI itself.

## Setup

- Requires the `notebooklm-py[browser]` venv at `~/.notebooklm-venv` (Playwright + Chromium/Edge installed) — see `anthropic-skills:notebooklmskill` for installation.
- Requires the user's NotebookLM session captured in `~/.notebooklm/browser_profile_edge` (persistent Edge profile). Run `anthropic-skills:notebooklmskill` once to log in.
- On Windows, Playwright Chromium often fails with side-by-side errors. Use `channel="msedge"` with the system Edge instead.

## When NOT to use this skill

- For renaming the source's **title** (filename shown in the source list), use the `notebooklm` CLI: `notebooklm source rename <id> "<new title>"`. That's faster and doesn't require a browser.
- For uploading new sources, use `notebooklm source add <path>`.

## Workflow

### 1. Diagnose current state

Always start by reading the current category → sources mapping. Open the notebook in Playwright, expand all panels, dump structure.

```python
# scripts/diagnose.py — open notebook, expand all panels, dump categories → sources
```

### 2. Plan operations

For the target structure, list:
- **Renames**: `(old_category_name, new_category_name)` tuples
- **New labels**: list of names to create
- **Moves**: `(source_aria_substring, target_category_substring)` tuples
- **Deletions**: list of category names to remove (after sources moved out)

### 3. Execute via Playwright primitives

Use the primitives in `scripts/nlm_ui.py`:

- `rename_category(page, old, new)` — opens category `more_vert` menu → "Rename" → types new name + Enter
- `add_new_label(page, name)` — opens "Undo or re-label sources" → "Add new label" → creates a "New Label", then renames it via `more_vert → Rename`
- `move_source(page, source_aria_substring, target_substring)` — locates the source via substring match on its aria-label, finds the `More` button inside the same `div.single-source-container`, opens it → "Move to" → clicks target in submenu
- `delete_category(page, panel_idx)` — opens category `more_vert` → "Remove"

### 4. Verify

Re-dump the state and confirm counts per category.

## Critical UI patterns discovered

1. **`more_vert` and `More` buttons have class `show-on-hover`** — invisible until hovered. Use `force=True` on `.click()` after hovering the parent.
2. **`Move to` is additive, not exclusive** — clicking it ADDS a label without removing existing ones, so a source can end up in multiple categories. To get strict 1-source-per-label assignment, you must `delete + re-upload + move`, since re-uploaded sources in a notebook with existing manual labels are NOT auto-categorized.
3. **Category title input** — clicking "Rename" focuses an `<input type="text">` with the current title pre-selected. Just `keyboard.press("Control+a")` + `keyboard.type(new_name)` + `Enter`.
4. **`Add new label` creates "New Label" with default name** — does NOT prompt for a name. You must rename it afterward via the category `more_vert → Rename`.
5. **`Escape` closes the entire compose dialog or active panel** — do not use it to dismiss dropdowns; use a click elsewhere or rely on natural focus shift.
6. **Source More button is a sibling inside `div.single-source-container`** — find via `xpath=ancestor::div[contains(@class, "single-source-container")][1]//button[@aria-label="More"]`.
7. **Auto-generated categories return after deletion if sources still match the AI's clustering**. Either remove the sources or accept that the AI may re-create the category. Empty manual labels persist correctly.

## Strict 1-source-per-label workflow

When the user explicitly wants each source in exactly one label (no duplication):

1. CLI delete the source: `notebooklm source delete <id>`
2. CLI re-upload: `notebooklm source add <path>`
3. CLI rename to PBC prefix if needed: `notebooklm source rename <new_id> "<prefix_name>"`
4. Playwright move to the target label: `move_source(page, prefix, target)`

Step 2 in a notebook that already has manual labels does NOT trigger AI auto-categorization — the source lands "uncategorized" and the subsequent move places it in exactly the target label.

## Files in this skill

- `scripts/nlm_ui.py` — primitive functions (rename_category, add_new_label, move_source, delete_category, expand_all, find_panel, dump_state)
- `scripts/diagnose.py` — open notebook and print current category → sources map
- `scripts/example_reorganize.py` — full example showing rename + add label + move for the EPACEM notebook
- `scripts/reauth.py` — re-login the NotebookLM session if expired

## Common errors and fixes

| Symptom | Fix |
|---|---|
| `more_vert` click times out | Hover the panel header first; click with `force=True`; `scroll_into_view_if_needed()` |
| "Source not found" when moving | `expand_all()` first — collapsed panels lazy-render their children |
| `Locator.click: element is not visible` | The element has class `show-on-hover` — hover its parent container |
| Subject input not found | A dropdown is overlaying — use `force=True` to bypass the overlap check |
| `innerHTML` raises TrustedHTML error | Use `textContent` + `createElement('br')` instead — Gmail/NotebookLM use CSP Trusted Types |
