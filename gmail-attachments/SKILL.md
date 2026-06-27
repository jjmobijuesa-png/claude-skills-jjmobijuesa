---
name: gmail-attachments
description: "Download attachments from Gmail messages to a local folder. Use when the user wants to download files attached to specific Gmail emails by sender/subject/threadId. The Gmail MCP returns attachment metadata but not the binary content, so this skill drives Gmail web via Playwright with the user's logged-in Edge profile to fetch the actual files. Triggers: 'download Gmail attachments', 'save attachments from email', 'descargar adjuntos de Gmail', 'guardar archivos del correo de X'. Filters out inline signature images (image001.png etc.) by default."
user-invocable: true
---

# Gmail — Download attachments via Playwright

The Gmail MCP exposes `search_threads` and `get_thread` which return `attachments` metadata (filename, id, mimeType) but NOT the binary content. To get the actual files, drive the Gmail web UI in Playwright with the user's logged-in Edge profile.

## Setup

- Requires `~/.notebooklm-venv` with Playwright installed.
- Requires a persistent Edge profile authenticated to the target Gmail account at `~/.notebooklm/browser_profile_<account_tag>`. If not present, run the script with `--login` once and have the user sign in.

## Método recomendado: "Descargar todos" → ZIP (robusto)

⭐ **Usa `scripts/download_all_zip.py` primero.** Descargar adjunto por adjunto se cuelga cuando
Gmail abre vistas previas (`page.expect_download` se queda esperando). El camino fiable es el botón
**"Descargar todos los archivos adjuntos"** de Gmail, que entrega **UN solo ZIP**, y luego se extrae.

```
<venv>\Scripts\python.exe scripts/download_all_zip.py <profile_tag> "<target_dir>" <thread_id> [authuser_idx] [--keep-zip]
```
- `profile_tag`: perfil dedicado en `~/.notebooklm/browser_profile_<tag>`. **`jjm` = jjmobijuesa@gmail.com**
  (en ese perfil dedicado la cuenta es índice **0**, aunque en el navegador normal del usuario sea `u/1`).
- El script clica "Descargar todos" (selectores ES/EN), y si no lo halla, construye la URL `disp=zip`
  desde un enlace `view=att`. Luego **extrae** los archivos a la carpeta y borra el zip (salvo `--keep-zip`).
- Caso real (SEM 24): `download_all_zip.py jjm "...\WAR ROOM QVP\Adjuntos SEM 24" 19ecdd85755653c2`.

## Flujo del comité "cuarto de guerra" (automatización end-to-end)
1. Gmail MCP `search_threads` con `from:reunionesqp@quevepalma.com subject:"SEM xx"` → tomar el `id`.
2. `download_all_zip.py jjm "...\WAR ROOM QVP\Adjuntos SEM xx" <id>`.
3. Verificar/leer con openpyxl (xlsx), python-pptx (pptx), python-docx (docx) — ver `comite-cuarto-guerra-qvp`.

## Fallback: adjunto por adjunto

1. **Identify the threads.** Use the Gmail MCP `search_threads` to find target emails by sender, date, subject. Capture each `id` (the thread ID).
2. **Build the download list.** For each thread, decide what to keep (real attachments, not inline signature images). Pattern to skip: `image\d+\.(png|jpe?g|gif)` filenames.
3. **Run the downloader** (`scripts/download.py`). It:
   - Opens Gmail web in headed Edge using the persistent profile
   - For each thread ID, navigates via `window.location.hash = 'inbox/<tid>'`
   - Waits for the conversation to render
   - Extracts attachment download URLs from the page via JS (`a[href*="view=att"]`)
   - For PDFs, rewrites `disp=inline` → `disp=attd` to force download instead of in-browser preview
   - Triggers download via `page.expect_download()` + injected anchor click
   - Saves each file to the target folder, filtering signature images

## Discovered URL patterns

- Attachment preview links: `https://mail.google.com/mail/u/0?ui=2&ik=<IK>&attid=<N>&permmsgid=<MSG>&th=<TH>&view=att&zw&disp=inline`
- Download (forced): same URL with `disp=attd` instead of `disp=inline`
- Multi-account: use `/mail/u/N/` where N is the account index. Best to use a profile dedicated to one account to avoid the chooser.

## Files in this skill

- `scripts/download.py` — main downloader. Takes list of thread IDs + target folder + optional login mode.
- `scripts/login.py` — initial login for the persistent profile (if not yet authenticated).

## Common errors and fixes

| Symptom | Fix |
|---|---|
| Account chooser appears | The profile holds a different account. Use a separate `browser_profile_<account_tag>` per Gmail account, or pass `authuser=...` in URL. |
| `Timeout waiting for "download"` event on a PDF | Gmail opens PDFs in its inline viewer. Rewrite `disp=inline` → `disp=attd` in the URL before triggering. |
| Empty attachments list in DOM | Thread didn't fully render. Wait longer or scroll the message into view. |
| Cloudflare verification page | Switch to non-headless mode and have user click the verification once; the profile's cookies will persist. |
