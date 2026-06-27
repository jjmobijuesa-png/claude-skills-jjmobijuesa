---
name: gmail-send-playwright
description: "Send a Gmail email with attachments directly (not as draft) via Playwright + Edge. Use when the user wants to send an email with files attached AND have it actually go out — the Gmail MCP only exposes create_draft, not send. Triggers: 'envíalo por email', 'send this email', 'mandar correo con adjuntos', 'send with attachment'. Composes a fresh email, fills To/Subject/Body, attaches up to ~25MB of files via the hidden input[type=file], clicks Send, and verifies in the Sent folder."
user-invocable: true
---

# Gmail — Send with attachments via Playwright

The Gmail MCP `create_draft` requires base64-encoded attachments passed in the tool call, which blows up the context budget for any non-trivial file. And there's no `send_draft` exposed. This skill drives Gmail web to compose, attach files from disk, and click Send.

## Setup

- `~/.notebooklm-venv` with Playwright installed.
- Persistent Edge profile at `~/.notebooklm/browser_profile_<account_tag>` authenticated to the sending account.

## Workflow

`scripts/send.py` orchestrates:

1. **Open compose** by clicking `div[gh="cm"]`.
2. **Fill To** by typing each recipient, pressing `Enter` to commit each as a chip. Do NOT press `Escape` — Gmail interprets Escape as "minimize compose" and closes the window.
3. **Fill Subject** by `force=True` click on `input[name="subjectbox"]` (force bypasses the autocomplete dropdown overlay that blocks normal clicks).
4. **Fill Body** by `Tab` from Subject to the contenteditable body, then JS-insert the text. Avoid `innerHTML` — Gmail uses CSP Trusted Types which rejects it. Use `target.appendChild(document.createElement('div'))` per line, with `<br>` elements for blank lines.
5. **Attach files** by finding `input[type="file"]` inside the compose dialog and calling `set_input_files([path1, path2, ...])`. This bypasses the system file picker which Playwright can't drive.
6. **Wait for upload** ~20s for medium files (each ~50KB DOCX takes a few seconds).
7. **Click Send** — try both English (`Send`) and Spanish (`Enviar`) labels; fallback to `Ctrl+Enter`.
8. **Verify** by navigating to `#sent` and checking the subject appears in the recent threads. Or use the Gmail MCP `search_threads` with `in:sent newer_than:1h` post-send.

## Critical UI patterns

| Pattern | Detail |
|---|---|
| Autocomplete dropdown blocks Subject click | Use `click(force=True)` |
| Pressing `Escape` after To closes the compose | Don't — let focus shift naturally; click target field directly |
| `innerHTML` raises TrustedHTML error | Use `textContent` + `createElement('br')` |
| Send button labels vary by locale | Try `aria-label^="Send"` AND `aria-label^="Enviar"` |
| The hidden file input may not be in DOM until first hover/click of the attach button | Hover the attach paperclip or just look for `input[type="file"]` which usually IS present |

## Files in this skill

- `scripts/send.py` — main send orchestrator. Reads body from a file, accepts recipients/subject/attachments as args.

## Encoding caveat

If you write a log file with `✓`, `→`, or other non-cp1252 characters and run with `subprocess.run(...)` on Windows, the redirected stdout will fail with `UnicodeEncodeError`. Either set `PYTHONIOENCODING=utf-8` or strip such characters from log lines. The Send itself works fine — only the log-write fails.
