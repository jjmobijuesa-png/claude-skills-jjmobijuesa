---
name: auditor-integral-notebooklm
description: |
  Lee, asimila, controla y ANALIZA de forma integral cualquier cuaderno de
  NotebookLM al que la cuenta autenticada tenga acceso (propio, compartido o
  público): sus FUENTES, el CHAT interno y TODOS los artefactos de Studio
  (resúmenes, mapas conceptuales, presentaciones, audio, vídeo, quiz...).
  Produce un diagnóstico estructurado (tesis, fuentes clave citadas, vacíos y
  riesgos) y, si se pide, un nuevo artefacto. Incluye el truco de
  reautenticación del CLI en esta máquina (canal msedge).
trigger_phrases:
  - "analiza el cuaderno"
  - "audita el cuaderno de notebooklm"
  - "lee y asimila el cuaderno"
  - "qué hay en el cuaderno"
  - "control y análisis del cuaderno"
  - "diagnóstico del cuaderno notebooklm"
  - "revisa fuentes, chat y studio del cuaderno"
idioma_de_salida: español
nivel: aplicada
dominio: comunicación-institucional / investigación
metadata:
  version: 1.0
  fecha: 2026-06-19
  origen: sesión 2026-06-19 (prueba real con el cuaderno DARPA de mobijuesa360); construida sobre anthropic-skills:notebooklmskill
  fuente: anthropic-skills:notebooklmskill (CLI notebooklm-py v0.3.4) + truco de reauth de [[reference-cuaderno-toma-decisiones-qvp]]
  relacionada: notebooklmskill, analisis-cognitivo-intervenciones-qvp, llave-maestra-autoaprendizaje-ia
---

# Skill `auditor-integral-notebooklm`

## Acerca de mí (cargar al arrancar)
Lee primero `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md`
y `MEMORY.md` para heredar perfil y proyectos (QVP, EcuaLedger/FBSE, Vista al Río).
Cuenta NotebookLM por defecto: **mobijuesa360@gmail.com** (perfil `browser_profile_edge`).
Ver [[feedback-notebooklm-cuenta]].

## Doctrina central
NotebookLM no es solo un generador de artefactos: es un **corpus curado + un chat
con grounding + un Studio**. Auditarlo integralmente = leer las tres capas
(fuentes, chat, Studio), triangularlas y devolver un **diagnóstico** (qué dice,
con qué se sustenta, qué falta y qué arriesga), no un resumen plano. Es la versión
"de lectura/análisis" del genérico `notebooklmskill` (que es "de creación").

## Qué NO hacer / compuertas 🚦 (antes de los pasos)
- 🚦 **Límite de acceso real:** solo cuadernos que la cuenta autenticada pueda abrir
  (propios, compartidos o públicos). **No** se accede a cuadernos privados de terceros
  ajenos a la cuenta — eso es una barrera de control de acceso, no una capacidad.
- 🚦 **`download` / `generate` / `ask --save-as-note` / `delete`** → pedir OK (escriben o
  son procesos largos/destructivos). `list`, `use`, `status`, `source list`,
  `artifact list`, `history`, `source fulltext`, `ask` (sin guardar) → libres.
- No inventar contenido: si una fuente no se lee o un artefacto no se reconoce, decirlo.
- No cambiar de cuenta/perfil sin pedido explícito.

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

**0. Entorno (Windows):**
```bash
NLM="$HOME/.notebooklm-venv/Scripts/notebooklm.exe"   # Mac/Linux: ~/.notebooklm-venv/bin/notebooklm
"$NLM" auth check
"$NLM" list            # si falla con "Authentication expired", ver "Cómo depurar"
```

**1. Localizar y fijar el cuaderno:**
```bash
ID=$("$NLM" list --json | python -c "import sys,json;d=json.load(sys.stdin);print(next(n['id'] for n in d['notebooks'] if n['title'].strip().upper()=='<TITULO>'))")
"$NLM" use "$ID"; "$NLM" status
```

**2. Leer las tres capas (todo lectura, sin confirmación):**
- **Fuentes:** `"$NLM" source list` → para las clave, `"$NLM" source fulltext <src_id>`.
- **Chat interno:** `"$NLM" history` (turnos previos = hipótesis ya exploradas por el usuario).
- **Studio:** `"$NLM" artifact list` (audio, vídeo, slide-deck, mapa, quiz, informe).

**3. Asimilar + analizar con el chat groundeado:**
```bash
"$NLM" ask "Responde conciso con viñetas: (1) tesis central; (2) 4-6 fuentes clave que la sustentan; (3) vacíos y riesgos." 
```
Pedir `--json` si se quieren las referencias [n] mapeadas a fuentes.

**4. (Opcional, 🚦) Leer un artefacto de Studio a fondo:**
- Presentación: `"$NLM" download slide-deck ./x.pdf` (o `--format pptx`). *Las diapositivas
  suelen ser imágenes sin capa de texto → leer con visión si se necesita el contenido.*
- Informe/mapa/tabla: `download report ./x.md` · `download mind-map ./x.json` · `download data-table ./x.csv`.
- Audio/vídeo: `download audio ./x.mp3` · `download video ./x.mp4` (medios; referenciar, no "leer").

**5. Entregable:** diagnóstico estructurado (tesis · fuentes clave citadas · vacíos/riesgos ·
mapa de artefactos Studio) + recomendaciones. Persistir en la carpeta del proyecto que corresponda.

## Cómo depurar si falla
- **`auth check` pasa pero `list` redirige a accounts.google.com** (cookies presentes pero token
  expirado): refrescar el `storage_state.json` del CLI desde el perfil Edge vivo. El Chromium de
  Playwright falla con «spawn UNKNOWN» en esta máquina → usar **canal msedge**:
```bash
VENV_PY="$HOME/.notebooklm-venv/Scripts/python.exe"
"$VENV_PY" - <<'PY'
import json; from pathlib import Path; from playwright.sync_api import sync_playwright
EDGE=Path.home()/".notebooklm"/"browser_profile_edge"           # sesión de mobijuesa360
OUT =Path.home()/".notebooklm"/"profiles"/"default"/"storage_state.json"   # lo que lee el CLI
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir=str(EDGE),channel="msedge",headless=True,
        args=["--disable-blink-features=AutomationControlled"])
    pg=ctx.pages[0] if ctx.pages else ctx.new_page()
    pg.goto("https://notebooklm.google.com/",wait_until="domcontentloaded",timeout=60000); pg.wait_for_timeout(5000)
    OUT.write_text(json.dumps(ctx.storage_state())); ctx.close()
PY
```
  Cerrar Edge si el perfil está bloqueado. Otra cuenta: perfil `browser_profile_jjm` (jjmobijuesa@gmail.com).
- **`UnknownTypeWarning` / "No completed <tipo> artifacts found":** el CLI (v0.3.4 y aún v0.5.0)
  no reconoce tipos nuevos de artefacto: **tablas de datos xlsx/csv = tipo 10, cierto mapa mental =
  tipo 4**. Workaround: descargar otro tipo equivalente, pedir el contenido como texto por `ask`,
  regenerarlo (`generate …`, 🚦), o leer la fuente origen.
- **Artefactos `(UNKNOWN)` que el CLI no descarga: SÍ se rescatan (verificado 4-oct-2026, cuaderno IBPP).**
  Volcar el listado crudo con la librería del venv: `async with NotebookLMClient.from_storage() as c:
  raw = await c.artifacts._list_raw(NB)` y ubicar el artefacto por su id (`a[0]`), con el tipo en `a[2]`.
  - **Tipo 11 = documento enriquecido (mime docx):** el texto completo viene embebido en el propio listado,
    en `a[34][0][0][0]` (lista de párrafos). Título: `p[0] is None`, con texto en `p[2][0][0][2][0]`.
    Párrafo: runs `p[2][0]` = `[ini, fin, [texto, [negrita, cursiva]]]`; viñeta si `p[2][1] == [None, 1]`.
    **Artefacto incrustado:** párrafo de nulos con `p[12] = [<id_artefacto>, 1]`; no es texto perdido,
    hay que insertar la pieza referida. Reconstruir con python-docx y pasar a PDF con Word COM.
  - **Tipo 4 nuevo = mapa mental interactivo** (no figura en `list_mind_maps`, que solo trae los
    respaldados por notas): `rpc_call(RPCMethod.GET_INTERACTIVE_HTML, [id], source_path=f"/notebook/{NB}",
    allow_null=True)`; en `r[0][9][0]` viene un HTML cuyo atributo `data-app-data` (escapado en HTML)
    trae el árbol JSON `{name, children}` completo. Dibujarlo en SVG y exportar con Edge headless
    (`page.pdf(..., prefer_css_page_size=True, page_ranges="1")`).
  - Scripts de referencia: `E:/vars/var 9 FBSE/Tokenizacion Activos Reales - RWA/1 Matriz de Acuerdos/JRPFM/_generador_paquetes/` (`raw_art.py`, `mm2.py`, `build_nlm_pdfs.py`).
  - Ojo: `download quiz` guarda **JSON** aunque el archivo termine en `.md`.
- **`RPC response exceeded 52428800 bytes` en `ask` (verificado 13-sep-2026):** el transporte del CLI
  aborta cualquier respuesta mayor de 50 MiB (`MAX_RPC_RESPONSE_BYTES` en `_authed_transport.py`,
  ligado como *default* de `stream_post_with_size_cap`). Ocurre en cuadernos con muchas fuentes y chat
  largo (KleperBook: 63 fuentes, 9 turnos). Solución probada: envoltorio
  `C:\Users\datos\war_room_tmp\nlm_ask_big.py`, que sube el tope a 600 MiB parcheando
  `__kwdefaults__` y lanza el entry point real `notebooklm.notebooklm_cli:main`:
  ```bash
  "$HOME/.notebooklm-venv/Scripts/python.exe" "C:/Users/datos/war_room_tmp/nlm_ask_big.py" \
    --profile "mobijuesa360@gmail.com" ask "<pregunta>" --json > respuesta.json
  ```
  (No existe `notebooklm.cli.main`; el módulo es `notebooklm_cli`.) Con el envoltorio, la misma
  pregunta devolvió 7.506 caracteres con citas [n].
- **`history --json` sí devuelve los turnos completos** (`qa_pairs[].question/answer`); la tabla de
  `history` solo muestra previsualizaciones. Exportar a markdown para leerlo entero.
- **Carga masiva de archivos (verificado 19-sep-2026, 31 fuentes en un cuaderno nuevo):**
  (1) `source add <archivo> --title X` **ignora el título**: la fuente nace con el nombre del archivo
  → renombrar después con `source rename <id> "<título>"` y deduplicar por nombre de archivo, no por
  título. (2) Si la subida corta con `AssertionError: Data should not be empty` (asyncio
  `_write_send`), **queda igual una fuente muerta** en estado 5 «preparing» con tipo desconocido, que
  nunca se procesa: `source delete <id> -y` y volver a subir; el reintento entra a la primera.
  (3) `--json` viene precedido de líneas «Matched:» y WARNING: extraer el primer objeto con
  `json.JSONDecoder().raw_decode`. Cargador listo y idempotente:
  `E:\vars\var 5\Universidad-Abierta\subir_aula_notebooklm.py` (add + wait + rename + registro).

## Portabilidad (revisar el 20% al reusar)
Rutas/cuenta/canal de navegador (`browser_profile_edge` vs `_jjm`), versión del CLI (`notebooklm-py`)
y la ruta `profiles/default/storage_state.json` (puede cambiar entre versiones). El resto es estable.

## Reuso (no empezar de cero)
Se apoya en `anthropic-skills:notebooklmskill` (CLI y comandos). Para el FACTOR HUMANO de reuniones
usar [[analisis-cognitivo-intervenciones-qvp]]; para entrenar/defender un expediente, la suite
[[entrenador-experto-notebooklm-ecualedger]].

## Ejemplos de invocación
- «Analiza el cuaderno DARPA de mobijuesa360 y dame tesis, fuentes y riesgos.»
- «¿Qué artefactos de Studio tiene el cuaderno X y de qué tratan?»
- «Lee el chat interno del cuaderno Y y dime qué hipótesis ya se exploraron.»

## Prueba de aceptación realizada (2026-06-19)
Cuaderno **DARPA** (`4ffb0407-cb75-490c-b15c-2173925e8de8`, mobijuesa360): 38 fuentes (ready),
6 artefactos Studio (2 audio, 1 vídeo, 2 slide-decks, 1 mapa), 8 turnos de chat; `ask` analítico
devolvió la tesis "Alfa Lab = modelo DARPA transpuesto a la UTEQ para la soberanía EcuaLedger"
con citas [1]–[23] y 5 riesgos. Reauth aplicada con éxito (80 cookies, SID válido).

## Vecindad en la red

Skills que dependen de esta y que antes no la citaban de vuelta:

- [[notebooklm-reorganize]]

> Retroenlaces añadidos el 9-sep-2026 ([[regla-del-primer-tropiezo]] §10, movimiento «enlazar»).
