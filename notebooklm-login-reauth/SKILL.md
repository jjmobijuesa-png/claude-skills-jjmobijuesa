---
name: notebooklm-login-reauth
description: Re-autentica un perfil de la CLI notebooklm-py cuando su sesión de Google caduca (el `auth check` pasa pero `list`/`ask` devuelven "Authentication expired or invalid. Redirected to accounts.google.com"). El login abre un navegador headed y NO puede correr desde el sandbox del agente (spawn UNKNOWN), así que esta skill PREPARA y ENTREGA al usuario el comando exacto de PowerShell a ejecutar, detecta cuándo la sesión quedó guardada (por el timestamp de storage_state.json) y reanuda el trabajo automáticamente. Triggers — "la sesión de NotebookLM caducó", "re-loguea el perfil X", "notebooklm authentication expired", "no puedo listar los cuadernos de la cuenta Y".
metadata:
  type: reference
  version: 1.0
  created: 2026-07-11
  scope: cualquier perfil de notebooklm-py (default, mobijuesa360@gmail.com, fedphd@gmail.com, ...)
---

# notebooklm-login-reauth

> Skill de re-autenticación de perfiles NotebookLM. Resuelve el caso recurrente "la sesión caducó" sin que el agente pierda tiempo en scripts custom que no funcionan.

## 1. El problema

La CLI `notebooklm-py` guarda cookies de Google en `~/.notebooklm/profiles/<perfil>/storage_state.json`. Google **invalida el token de sesión cada 1-2 semanas** aunque las cookies sigan en disco. Síntoma:

- `notebooklm --profile X auth check` → **pasa** (las cookies existen, SID presente).
- `notebooklm --profile X list` (o `ask`, `use`) → **falla** con:
  `Unexpected error: Authentication expired or invalid. Redirected to: https://accounts.google.com/...`

## 2. Por qué el agente NO puede resolverlo solo

El comando de login (`notebooklm --profile X login --browser msedge`) abre un **navegador headed** (visible). Desde el sandbox del agente, lanzar Chromium/Edge headed falla con `spawn UNKNOWN` (restricción del entorno para GUI). Ver `feedback-aprendido §6`.

**Conclusión:** el login lo dispara el usuario en su propia terminal. El agente prepara el comando, lo entrega, y detecta cuándo terminó.

## 3. Protocolo de la skill

### Paso 1 — Diagnóstico (el agente ejecuta)

```powershell
$NLM = "$env:USERPROFILE\.notebooklm-venv\Scripts\notebooklm.exe"
& $NLM --profile "<perfil>" list 2>&1 | Select-Object -First 3
```

Si devuelve "Authentication expired" → sesión caducada, continuar.

### Paso 2 — Entregar el comando al usuario (mensaje del agente)

> Abre PowerShell (Win → `powershell` → Enter) y pega:
> ```powershell
> & "$env:USERPROFILE\.notebooklm-venv\Scripts\notebooklm.exe" --profile "<perfil>" login --browser msedge
> ```
> Se abre Edge → inicia sesión en la cuenta `<perfil>` → espera a ver tus cuadernos. La CLI captura la sesión y cierra el navegador sola. Dime "listo" cuando termine.

> **Nota:** el `.bat` de escritorio `NotebookLM-Login-Perfil.bat` hace lo mismo — pero si falla (no detecta el login), el comando directo de PowerShell es más confiable.

### Paso 3 — Verificar (el agente ejecuta cuando el usuario dice "listo")

```powershell
# Verificar que storage_state se actualizó hace < 5 min
$storage = "$env:USERPROFILE\.notebooklm\profiles\<perfil>\storage_state.json"
$mins = ((Get-Date) - (Get-Item $storage).LastWriteTime).TotalMinutes
Write-Output "storage actualizado hace $mins min"
# Y probar list de verdad
$NLM = "$env:USERPROFILE\.notebooklm-venv\Scripts\notebooklm.exe"
& $NLM --profile "<perfil>" list 2>&1 | Select-Object -First 5
```

- Si `storage` se actualizó hace **> 30 min** y `list` sigue fallando → el login del usuario NO se guardó (cerró Edge antes de tiempo, o inició sesión en la cuenta equivocada). Volver al Paso 2.
- Si `list` devuelve cuadernos → **éxito**, continuar con el trabajo original.

## 4. Regla de oro (aprendida 2026-07-07 y confirmada 2026-07-11)

**NO reinventar el login con scripts custom** (`nlm-login-perfil.py`, `nlm-capture-storage.py`, extracción `--browser-cookies`). Todos fallan por la encriptación app-bound de cookies de Chromium 127+. La única ruta confiable es el comando nativo `notebooklm --profile X login --browser msedge`, que abre su propio Edge de Playwright y captura la sesión correctamente.

## 5. Automatización posible (futuro)

El agente NO puede lanzar el navegador headed, pero SÍ puede:
- Diagnosticar la caducidad (Paso 1).
- Escribir el comando exacto y entregarlo (Paso 2).
- Verificar por timestamp + list real (Paso 3).
- Monitorear el `storage_state.json` con un loop de espera si el usuario lo pide.

Lo que el agente NO debe hacer: intentar 5 variantes de scripts Playwright headless para "capturar" la sesión — es tiempo perdido. Ir directo al comando nativo.

## 6. Referencias cruzadas

- Workspace SAS Agua: `E:\vars\var 13 RedSerAk\SAS-Agua-Cerebro-Operativo\` — `feedback-aprendido §6, §6b`.
- `docs/notebooklm-multi-perfil.md` en el workspace SAS Agua.
- CLI upstream: `notebooklm-py` (teng-lin/notebooklm-py).
