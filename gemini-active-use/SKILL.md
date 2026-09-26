---
name: gemini-active-use
description: |
  Usa Google Gemini en modo ACTIVO (no sólo lectura): redacta una
  pregunta, la inyecta en el editor, dispara el submit, espera la
  respuesta y devuelve el texto. Funciona sobre la sesión de Google
  ya logueada en el perfil Edge de automatización (jjmobijuesa@gmail.com)
  vía Playwright directo — NO usa la extensión Claude-in-Chrome, que
  bloquea la navegación a gemini.google.com.

  Complementa a [[perplexity-active-use]] y [[deepseek-active-use]]:
  delega a Gemini el razonamiento con su ventana de búsqueda de Google
  y trae solo el resultado destilado → eficiencia multi-modelo.

  Resultado: cada consulta se persiste en
  `E:\vars\var 5\Gemini-consultas\YYYY-MM-DD_<slug>.md`.

trigger_phrases:
  - "pregúntale a gemini"
  - "consulta gemini"
  - "usa gemini activamente"
  - "lánzale a gemini"
idioma_de_salida: español neutro
nivel_madurez: aplicada
fuente: sesión 2026-07-12 (acceso resuelto vía Playwright directo, verificado)
---

# Gemini activo — vía Playwright + perfil Edge logueado

## Doctrina

Gemini es la tercera fuente de razonamiento+búsqueda del usuario (con
Perplexity y DeepSeek). El acceso por la extensión Claude-in-Chrome
**está bloqueado** (`Navigation to this domain is not allowed` para
`gemini.google.com`). La solución robusta —verificada 2026-07-12— es
**Playwright directo con el perfil persistente `browser_profile_jjm`**,
que ya tiene la sesión de Google (jjmobijuesa@gmail.com) iniciada. Es
el mismo patrón que usan las skills de Gmail y bookmarks.

## Pre-requisitos

- Paquete Python `playwright` instalado (`pip install playwright`). NO
  hace falta `playwright install` porque se usa `channel="msedge"`
  (el Edge del sistema).
- Perfil `C:\Users\datos\.notebooklm\browser_profile_jjm` logueado en
  Google. Si `NO_INPUT`, la sesión caducó → abrir Gemini a la vista del
  usuario en ese perfil y volver a loguear (cuentas: jjmobijuesa@gmail.com
  o mobijuesa360@gmail.com).
- El perfil NO debe estar bloqueado por otro proceso (revisar que no
  exista `SingletonLock` en la carpeta del perfil).

## Cuenta Pro (Deep Research / Gemini 3 Pro) — mobijuesa360  ⭐ (2026-08-22)
El plan **Google AI Pro** está en **mobijuesa360@gmail.com** (la misma cuenta del NotebookLM), NO en
jjmobijuesa. Por tanto:
- Para consultas **normales/rápidas**: perfil `browser_profile_jjm` (jjmobijuesa) — está bien.
- Para **grado Pro** (razonamiento Pro, **Deep Research**, 4× límites): apuntar el script al perfil
  **`browser_profile_edge`** (mobijuesa360), donde el plan Pro está activo. Pasar la ruta del perfil
  como variable/argumento (o duplicar el script con ese `user_data_dir`).
- **Deep Research** es un **modo largo** (varios minutos, navega decenas de fuentes): no esperes el
  timeout de 110 s; lánzalo, deja que termine, y luego lee el informe. Plantillas de Deep Research listas
  en `E:\vars\var 5\Gemini-Pro\` (p. ej. fondos BID Lab + CAF VELA). Ver [[reference_gemini_pro_mobijuesa360]].
- Doctrina de reparto multimodelo intacta: delegar a Gemini Pro el razonamiento/búsqueda pesado y traer
  solo el destilado (eficiencia de tokens).

## Método robusto v3 — mobijuesa360 (VERIFICADO 2026-08-25)  ⭐
Fin de las vueltas. El acceso fiable a Gemini de **mobijuesa360** es el **perfil persistente
`browser_profile_edge`** (el mismo de NotebookLM). El script `ask_gemini.py` (v3) ya:
- **Confirma la cuenta** en pantalla (imprime `ACCOUNT(s): mobijuesa360@gmail.com`) → cero ambigüedad de `u/N`.
- **Abre un hilo por título** (`GEM_OPEN_TITLE`), **envía** con botón Enviar (o Enter) y **confirma el submit**.
- **Lee la respuesta REAL** del panel de conversación (no el sidebar).
- **Reutiliza un hilo fijo**: guarda/lee la URL en el `.txt` de `GEM_THREAD`.

**Hilo coprocesador canónico** (NO abrir chats nuevos): `«Gemini Pro vs. Claude Pro»` →
`https://gemini.google.com/app/030a3f951422d528` (persistido en
`E:\vars\var 5\Gemini-Pro\coproc_thread_url.txt`).

**Canal de archivos directo** (sin latencia de lenguaje): `G:\Mi unidad` está montado y es el
**Drive nativo de mobijuesa360** → lo que Claude escribe ahí, Gemini lo ve nativo. Carpeta
`G:\Mi unidad\IA Sinergia - Claude x Gemini\` (01 Entradas · 02 Salidas · 03 Deep Research ·
04 Prompts · 05 Activos). Sync 1–2 min. Ver [[multi-agente-gemini-coprocesador]].

## Flujo de uso por Claude

```powershell
# Continuar el hilo coprocesador y leer la respuesta:
$env:GEM_PROFILE='edge'; $env:GEM_THREAD='E:\vars\var 5\Gemini-Pro\coproc_thread_url.txt'
python "C:\Users\datos\.claude\skills\gemini-active-use\scripts\ask_gemini.py" "<mensaje>" <slug>
# Abrir un hilo concreto por título antes de escribir:  $env:GEM_OPEN_TITLE='Claude Pro'
# Perfiles: GEM_PROFILE = edge (mobijuesa360, DEFAULT) | jjm (jjmobijuesa) | fedphd
```
El script abre Edge headed fuera de pantalla (`--window-position=2200,2200`), navega al hilo,
detecta el editor `div.ql-editor[contenteditable]`, escribe con `insert_text`, envía, espera
estabilidad de la respuesta y persiste el `.md`. Luego Claude lee el `.md` y destila el 20% accionable.

> Consultas rápidas normales pueden usar `GEM_PROFILE=jjm`; para **grado Pro / Deep Research / coprocesador**, usar `edge` (mobijuesa360).

## Compuertas 🚦

1. **No usar la extensión** para navegar a Gemini (bloqueada) — siempre
   Playwright directo.
2. **No insertar credenciales** en la query; el perfil ya está logueado.
3. **Verificar antes de citar**: Gemini puede alucinar nombres/cifras
   (p.ej. clasificó empresas como maquiladores sin fuente dura). Tratar
   los nombres como pistas a confirmar, no como hecho.
4. **Timeout 110 s**; si sigue generando, capturar lo que haya.
5. **Tómate tu tiempo. Calidad antes que velocidad.**

## Cómo depurar si falla

- `NO_INPUT` → login/consent; re-loguear el perfil a la vista del usuario.
- Selector del editor cambió → inspeccionar el DOM y ajustar la lista de
  selectores en `scripts/ask_gemini.py` (Gemini usa Quill: `div.ql-editor`).
- Respuesta vacía → subir el `time.sleep` inicial (7→10 s) por si el
  render de la app tardó.

## Relacionado

- [[perplexity-active-use]] — hermana; misma arquitectura Playwright directo.
- [[deepseek-active-use]] — tercer modelo delegable.
- [[llave-maestra-autoaprendizaje-ia]] — registra esta capacidad activa.
- [[feedback_solo_edge]] — solo Edge, canal msedge, perfil de automatización.
