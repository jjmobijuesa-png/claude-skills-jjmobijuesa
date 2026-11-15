---
name: linkedin-guardados-fedphd
description: |
  Entra a las PUBLICACIONES GUARDADAS de LinkedIn (cuenta fedphd@gmail.com) en
  Edge, hace scroll hasta capturarlas TODAS, las extrae (autor, texto, URL), las
  agrupa por concepto/tema y destila los conceptos recurrentes en skills nuevas o
  en referencias de memoria (vía la llave maestra). Es el equivalente LinkedIn del
  pipeline autorreflexivo de bookmarks de X. Solo lectura: nunca publica ni conecta.
trigger_phrases:
  - "guardados de LinkedIn"
  - "publicaciones guardadas LinkedIn"
  - "cosecha mis saved posts"
  - "agrupa mis guardados de LinkedIn"
  - "destila skills de mis guardados"
  - "saved-posts fedphd"
idioma_de_salida: español
nivel: aplicada
dominio: operación / aprendizaje
metadata:
  version: 1.0
  fecha: 2026-06-19
  origen: pedido del usuario (2026-06-19); modelado sobre el pipeline de bookmarks X (@fdc_ec) + perplexity-active-use (Edge debug 9222)
  fuente: https://www.linkedin.com/my-items/saved-posts/ (cuenta fedphd@gmail.com, sesión Edge)
  relacionada: agente-local-autoreflexivo-bookmarks, consulta-bookmarks-fdc-ec, llave-maestra-autoaprendizaje-ia, memoria-financiera-inteligenciada
---

# Skill `linkedin-guardados-fedphd`

## Acerca de mí (cargar al arrancar)
Lee `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y `MEMORY.md`.
**Política solo-Edge** ([[feedback_solo_edge]]). Esta cuenta es **fedphd@gmail.com**, distinta de la de
X (@fdc_ec) y de NotebookLM (mobijuesa360) → es un **corpus aparte**. Hasta ahora el usuario me pasaba
sus posts guardados de a uno (Gavilánez, Da Costa, Zevallos, Cervantes, Saucedo, López Martín…); esta
skill **automatiza ese flujo en lote**.

## Doctrina central
Los guardados de LinkedIn son **curación**: lo que al usuario le importa, no lo que firma. La skill los
**cosecha completos** (con scroll real, como en el navegador), los **agrupa por concepto**, y convierte
los **conceptos recurrentes** en capacidad permanente: aumenta una skill existente (p. ej. lo financiero
→ [[memoria-financiera-inteligenciada]]) o crea una nueva/`intereses-*`/referencia. Es el mismo bucle
que el agente autorreflexivo de bookmarks de X, sobre otra fuente y otra cuenta.

## Qué NO hacer / compuertas 🚦
- 🚦🚦 **ANTES de usar el corpus, leer `E:\vars\var 5\LinkedIn-guardados\ESTADO_COSECHA.txt`** (cuatro líneas; cuesta nada). Trae `veredicto`, `fecha`, `capturados` y `fallos_seguidos`. **Si el veredicto no es `COSECHA_OK`, el corpus está quieto y no se puede presentar como fresco**: se dice en voz alta, con la fecha del último acierto, antes de destilar o concluir nada. Con `fallos_seguidos >= 3` el archivo abre con una línea de alarma.
  *Por qué existe:* entre el 29-jun y el 8-nov-2026 el corpus estuvo **132 días** sin cambiar y el guión **sí avisaba** —en un `harvest.log` de 364 KB que nadie abría—. **Un aviso sin lector es idéntico al silencio.** Este archivo es el aviso con lector, y esta compuerta es el lector.
- 🚦 **LinkedIn = solo lectura.** NUNCA publicar, comentar, reaccionar, conectar ni enviar mensajes. Leer y resumir, sí.
- **Curar ≠ firmar:** no atribuir al usuario las opiniones de los autores; siempre **citar la URL** del post.
- **No guardar credenciales** en la skill ni en el corpus. La sesión vive en Edge; aquí solo se leen cookies vía CDP.
- **No `Read` el `guardados.json` completo** si es grande → usar `scripts\clasificar_guardados.py` (igual que [[feedback_uso_bookmarks_archivo]]).
- No inventar posts ni autores: si un campo no se extrae, dejarlo vacío y marcarlo.

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
0. **Pre-requisito:** Edge corriendo con **debug 9222** y con LinkedIn **logueado como fedphd@gmail.com**.
   - Verifica: `curl -s http://localhost:9222/json/version`. El autostart del watcher de X ya suele
     levantar Edge con `--remote-debugging-port=9222`; si no, lánzalo así y entra a LinkedIn como fedphd.
1. **Cosechar (scroll + extracción):**
   ```bash
   "C:\Users\datos\.notebooklm-venv\Scripts\python.exe" "C:\Users\datos\.claude\skills\linkedin-guardados-fedphd\scripts\extraer_guardados.py"
   ```
   Conecta por CDP a 9222, navega a `/my-items/saved-posts/`, **hace scroll hasta que deja de crecer**
   (y pulsa "Ver más resultados" si aparece), extrae cada tarjeta y guarda
   `E:\vars\var 5\LinkedIn-guardados\guardados.json` + un snapshot fechado.
2. **Agrupar (clasificar por concepto):**
   ```bash
   "C:\Users\datos\.notebooklm-venv\Scripts\python.exe" "C:\Users\datos\.claude\skills\linkedin-guardados-fedphd\scripts\clasificar_guardados.py"
   ```
   Produce `E:\vars\var 5\LinkedIn-guardados\analisis\<ts>_clasificacion.md` con buckets por tema
   (finanzas-control, ia-agentes, blockchain-fintech, cognición-metacognición, liderazgo, empresa-familiar,
   jurídico) y una lista de **candidatos a skill/referencia** (temas con ≥5 posts).
3. **Destilar (desarrollar las skills de los conceptos):** por cada concepto recurrente, aplica
   [[llave-maestra-autoaprendizaje-ia]] (Paso 3–5): destila el 20%, **aumenta la skill pertinente** o
   crea una nueva/referencia, citando la URL del post. Ej.: posts financieros → §§ de
   [[memoria-financiera-inteligenciada]]; posts de cognición → [[auditoria-cognitiva-reflexiva]];
   blockchain/jurídico → suite EcuaLedger.
4. **Registrar:** pointer en `MEMORY.md`; si nace una skill, añadirla a la matriz `_RnD`.

## Automatización DIARIA (agregada 2026-07-05)

El flujo completo corre solo **cada día a las 9:15 AM** vía Scheduled
Task de Windows `LinkedIn guardados fedphd (diario)`.

### Componentes
1. `harvest_diario.bat` (en `E:\vars\var 5\LinkedIn-guardados\`) — **reescrito el 8-nov-2026** con dos compuertas:
   `preflight_cdp → extraer → (si y solo si todo fue bien) clasificar → autoreflex_pipeline_linkedin`.
   - **Paso 0, `scripts\preflight_cdp.py`:** exige que el puerto 9222 **escuche Y hable CDP** (`/json/version`). Si no, levanta Edge **minimizado y sin robar el foco** con el perfil dedicado `C:\Users\datos\browser_profile_edge`. Si Edge ya está abierto con ese perfil pero sin el puerto, **no lo mata** —se llevaría las sesiones del usuario—: aborta con código 5 y dice qué hacer. Es reutilizable por **toda** la familia de skills por CDP: `--puerto` y `--perfil`.
   - 🚦🚦 **La cadena se corta si el paso 0 o el 1 fallan.** Antes no: con el puerto caído, el candado antipisada salvaba el corpus (bien) y los pasos 2 y 3 seguían corriendo sobre los mismos 443 posts de junio, informando «augmentada (217 posts)» como si fuera fresco. **Clasificar y augmentar sobre datos viejos es peor que no correr**: fabrica conclusiones nuevas sobre material rancio.
   - **Códigos de salida** (`extraer_guardados.py` y el `.bat`), para que `LastTaskResult` vuelva a significar algo:
     `0` cosecha buena · `2` no creíble (cero capturados o merma >20 %) · `3` muro de autenticación · `4` sin puerto CDP · `5` Edge abierto con el perfil pero sin puerto.
   - **Lanzador manual:** `lanzar_edge_9222.bat` en la misma carpeta, doble clic. Abre Edge con perfil dedicado y puerto, espera y **comprueba el puerto**, que es lo único que prueba que funciona.
2. `scripts\autoreflex_pipeline_linkedin.py` — **hermano del pipeline
   X.com**. Lee `guardados.json`, clasifica por los 7 temas, y para
   cada tema:
   - Si el tema tiene ≥20 posts y **no existe** `intereses-lkd-<tema>`
     → crea skill esqueleto nivel *básica* con autores top + semillas.
   - Si el tema tiene ≥10 posts y **sí existe** → augmenta
     `references/fuentes-linkedin-<fecha>.md`.
   - Registra en `MEMORY.md` cada skill nueva.
   - Nunca sobreescribe SKILL.md ya existente.

### Cadencia
- **Diaria 9:15 AM** (activa) → produce log en
  `E:\vars\var 5\LinkedIn-guardados\linkedin-autoreflex.log`.
- **Semanal** (deshabilitada, en respaldo) — no se ejecuta, se puede
  reactivar con `Enable-ScheduledTask -TaskName 'LinkedIn guardados fedphd (semanal)'`.

### Cómo verificar que corrió
```powershell
Get-ScheduledTaskInfo -TaskName 'LinkedIn guardados fedphd (diario)' |
  Select LastRunTime, LastTaskResult, NextRunTime
```
`LastTaskResult=0` significa éxito; cualquier otro código indica fallo
(revisar `harvest.log`).

### Compuertas 🚦 del pipeline autoreflexivo
- Umbral 20 crear / 10 augmentar — evita ruido con pocos posts.
- Slug `intereses-lkd-*` (no colisiona con `intereses-*` de X.com).
- Solo lee guardados **públicos** del usuario (curación propia).
- No incluye PII de terceros en las skills — solo autor público + URL
  canónica del post.
- Skill nueva nunca se sube al repo hasta que el usuario la valide
  con `git status` en cierre de jornada.

## Cómo depurar si falla
- ⭐⭐ **«Los dos guiones dan números distintos del mismo corpus» (8-nov-2026, resuelto).** La taxonomía de los 7 temas existía **por duplicado** —en `clasificar_guardados.py` y en `autoreflex_pipeline_linkedin.py`— y las copias habían divergido **por tildes**: aquí `gestión`, `hábito` y `sucesión` llevaban acento, allá no. Resultado medido: liderazgo **594 contra 550** (44 posts, solo por `gestión`) y cognición **422 contra 407** (15, por `hábito`). **Los dos números se escribían en artefactos distintos y nadie los comparó nunca.**
  - **Arreglado** haciendo la clasificación **insensible a acentos** en ambos (se pelan los diacríticos del texto y de las palabras clave), no parcheando las tres palabras. Comprobado: los 8 recuentos coinciden exactamente.
  - 🚦 **Siguen siendo dos copias.** Si se toca una taxonomía, tocar la otra. La comprobación barata: extraer `THEMES` de los dos fuentes con `ast.literal_eval`, pelar acentos y comparar los conjuntos. Lo correcto sería un solo módulo compartido; `clasificar_guardados.py` **no es importable** porque lee el corpus en el cuerpo del módulo, así que la consolidación exige refactor y está pendiente de decisión.
  - **Lección portable:** una regla copiada en dos sitios **divergirá**, y con acentos divergió sin que ningún error salte. Una cifra, un valor ([[control-versiones-entregables]]).
- **`extraer_guardados.py` captura 0:** LinkedIn cambió clases/markup → ajustar el bloque `EXTRACT_JS`
  del script (los selectores de tarjeta/autor) probando en la consola del navegador; es el **20% volátil**.
- **Redirige a login / muro de auth:** Edge en 9222 no está logueado como fedphd → iniciar sesión ahí.
- ⭐⭐ **`connect_over_cdp` falla:** correr `python scripts\preflight_cdp.py`, que lo diagnostica y lo arregla.
  🚦 **El remedio que esta sección daba antes —«relanzar Edge con `--remote-debugging-port=9222`»— ERA EL EQUIVOCADO, y por eso la avería duró 132 días.** Desde Chromium 136 ese indicador **se ignora en silencio** sobre el perfil por defecto; hace falta **además** un `--user-data-dir` propio. Y la comprobación válida no es ver el indicador en la línea de órdenes, sino **el puerto a la escucha respondiendo CDP**. Detalle en [[feedback_cdp_9222_ignorado_perfil_defecto]].
  El perfil dedicado **no hereda la sesión** del Edge normal: la primera vez hay que iniciar sesión en LinkedIn dentro de esa ventana.
  (El Chromium propio de Playwright falla con «spawn UNKNOWN» en esta máquina; **usar el Edge real vía CDP**.)
- **Pocos resultados:** subir el máximo de scrolls (`extraer_guardados.py <MAX_SCROLLS>`); LinkedIn carga
  perezosamente, conviene scroll lento.

## Portabilidad (revisar el 20% al reusar)
Cuenta/sesión (fedphd), selectores DOM de LinkedIn (cambian), puerto CDP (9222) y la ruta de corpus
`E:\vars\var 5\LinkedIn-guardados\`. El resto (scroll-hasta-estable, clasificación, destilación) es estable.

## Reuso (no empezar de cero)
- Patrón de cosecha+clasificación+destilación → [[agente-local-autoreflexivo-bookmarks]] (X).
- Edge debug 9222 + DOM-aware → [[perplexity-active-use]].
- Conversión de concepto en capacidad → [[llave-maestra-autoaprendizaje-ia]].

## Recurrencia (tarea programada local — NO /schedule)
`/schedule` es para agentes en la nube y **no alcanza el Edge local (9222)**. Por eso la recurrencia
es una **Tarea Programada de Windows**: `LinkedIn guardados fedphd (semanal)` (lunes 09:00) ejecuta
`E:\vars\var 5\LinkedIn-guardados\harvest_semanal.bat` (extractor + clasificador; log en `harvest.log`).
Requiere Edge en 9222 logueado como fedphd; si no, falla sin ruido y reintenta la semana siguiente.
- Ver/quitar: `Get-ScheduledTask -TaskName 'LinkedIn guardados fedphd (semanal)'` ·
  `Unregister-ScheduledTask -TaskName 'LinkedIn guardados fedphd (semanal)' -Confirm:$false`.
- Selector de autor validado 2026-06-27 (100% de 432): autor = primera línea del `<li>` (saltando
  «Estado: …» y bullets). Es el **20% volátil**: si LinkedIn cambia el markup, re-sondear el DOM.

## Ejemplos de invocación
- «Cosecha todos mis guardados de LinkedIn y agrúpalos por tema.»
- «¿Qué conceptos financieros tengo guardados que aún no estén en mis skills? Destílalos.»
- «Actualiza mi corpus de guardados de LinkedIn y dime los candidatos a skill nueva.»

## Vecindad en la red

Skills que dependen de esta y que antes no la citaban de vuelta:

- [[intereses-lkd-blockchain-fintech]]
- [[intereses-lkd-cognicion-metacognicion]]
- [[intereses-lkd-ia-agentes]]
- [[intereses-lkd-juridico-legislativo]]
- [[intereses-lkd-liderazgo-estrategia]]
- [[intereses-lkd-empresa-familiar-pyme]]
- [[intereses-lkd-finanzas-control]]

> Retroenlaces añadidos el 9-sep-2026 ([[regla-del-primer-tropiezo]] §10, movimiento «enlazar»).
