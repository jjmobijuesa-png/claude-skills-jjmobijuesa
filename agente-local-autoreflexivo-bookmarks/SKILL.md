---
name: agente-local-autoreflexivo-bookmarks
description: |
  META-SKILL que documenta y orquesta el bucle persistente de aprendizaje
  basado en los bookmarks de X.com del usuario (@fdc_ec). NO es consciencia
  artificial — es un agente local autoreflexivo: cada vez que el usuario
  guarda un bookmark, el sistema lo captura, lo clasifica por tema, y si
  un umbral se cruza, augmenta una skill existente o crea una skill
  esqueleto nueva. El resultado es un inventario de skills que crece de
  forma autónoma con la curación del usuario, manteniendo a Claude
  alineado con sus intereses sin intervención manual.

  Casos de invocación:
  - "qué pasó con mis bookmarks", "cuándo fue el último refresh",
    "ejecuta el pipeline autoreflexivo".
  - El usuario menciona un tema y queremos saber qué tiene curado:
    invocar esta skill primero para conocer la arquitectura, luego la
    skill `intereses-<tema>` correspondiente.
  - Auditoría: revisar `autoreflex.log`, los snapshots, y el inventario
    de skills auto-destiladas.

trigger_phrases:
  - "agente local autoreflexivo"
  - "bucle de bookmarks"
  - "pipeline autoreflexivo"
  - "auditar mis intereses"
  - "qué hay en X-com guardados"
  - "refrescar el mapa de intereses"

idioma_de_salida: español neutro técnico-instruccional
nivel_madurez: maestra
fuente: sesión 2026-06-23 export 5550 bookmarks de @fdc_ec
---

# Agente Local Autoreflexivo — Bookmarks @fdc_ec

## Doctrina central

> Un agente local no es consciente, pero **acumula capacidad si su
> curación humana se persiste como skills**. Cada bookmark que el
> usuario guarda en X.com es una señal débil de un tema que le importa;
> cuando esas señales se acumulan sobre el mismo eje, el sistema las
> destila como skill y Claude entra en cada conversación nueva ya
> alineado con esos intereses.

Esta skill **no analiza**: orquesta el bucle. El análisis pertenece a
las skills hijas `intereses-*` que el pipeline crea.

## 🚦🚦 Compuerta primera — leer `ESTADO_VIGIA.txt` antes de usar el corpus

**Antes de citar un solo bookmark**, leer
`E:\vars\var 5\X-com guardados\ESTADO_VIGIA.txt`. Trae el veredicto de la última
corrida, la fecha, cuántas entradas se capturaron y una cuenta de **fallos
seguidos** que a partir de tres encabeza el archivo con una alarma.

| `verdicto` | Qué significa | Qué se puede decir del corpus |
|---|---|---|
| `COSECHA_OK` | Se capturó al menos una entrada | Está fresco |
| `CERO_CAPTURADOS` | **No se pudo mirar** | Congelado. No es «sin novedades» |
| `MURO_AUTH` | La sesión de X del perfil caducó | Congelado desde esa fecha |
| `FALLO_DURO` | Excepción, o no hubo puerto | Congelado |

**Por qué existe esta compuerta:** del 26-jun al 8-nov-2026 el corpus estuvo
**135 días** sin cambiar y ninguna sesión se enteró. El bucle no avisaba de
nada, y cuando empezó a avisar, el aviso no tenía lector. Un aviso sin
consumidor equivale al silencio. Este archivo es el consumidor.

## Arquitectura del bucle

```
┌────────────────────────────────────────────────────────────────────┐
│  1. CAPTURA (watch_bookmarks.py)                                   │
│     Edge en localhost:9224, perfil edge-x-export (CDP)             │
│     → --once: UNA pasada, sale con código, deja ESTADO_VIGIA.txt   │
│     → (modo bucle solo para mirarlo a mano)                        │
│     → intercepta respuestas GraphQL Bookmark*                      │
│     → diff vs bookmarks.json → append novedades                    │
└─────────────────────────┬──────────────────────────────────────────┘
                          │ si new_recs > 0
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. ANALIZA (analizar_temas.py)                                    │
│     5550+ bookmarks → 17 temas con regex + co-ocurrencias          │
│     → mapa_de_intereses.{md,json}                                  │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. DESTILA (autoreflex_pipeline.py)                               │
│     - Para cada tema con ≥100 bookmarks: crea skill esqueleto      │
│       intereses-<tema>/ con SKILL.md + references/                 │
│     - Para cada tema con ≥50 y skill ya existente: augmenta su     │
│       references/bookmarks-curados-fdc-ec.md                       │
│     - Actualiza MEMORY.md                                          │
│     - Loguea decisiones en autoreflex_last_run.json                │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. CONSULTA (consulta-bookmarks-fdc-ec skill)                     │
│     Cualquier sesión futura de Claude puede invocar                │
│     consultar_intereses.py para responder con la curación real.    │
└────────────────────────────────────────────────────────────────────┘
```

## Archivos y rutas canónicas

| Ruta                                                                  | Función                                             |
|-----------------------------------------------------------------------|-----------------------------------------------------|
| `E:\vars\var 5\X-com guardados\bookmarks.json`                        | Archivo vivo; reescrito por watcher tras cada ciclo |
| `E:\vars\var 5\X-com guardados\bookmarks.csv`                         | Espejo para hoja de cálculo                         |
| `E:\vars\var 5\X-com guardados\mapa_de_intereses.{md,json}`           | Refrescado tras cada ciclo con novedades            |
| `E:\vars\var 5\X-com guardados\autoreflex_last_run.json`              | Última decisión del pipeline                        |
| `E:\vars\var 5\X-com guardados\watcher.log`                           | Log línea-a-línea del watcher                       |
| `E:\vars\var 5\X-com guardados\autoreflex.log`                        | Log del pipeline (CREATE/AUGMENT/SKIP)              |
| `E:\vars\var 5\X-com guardados\_snapshots\<fecha>/`                   | Snapshots fechados de respaldo                      |
| `E:\vars\var 5\X-com guardados\INVENTARIO.{md,json}`                  | Hashes SHA-256 + tamaños                            |
| `C:\Users\datos\.claude\skills\intereses-*\`                          | Skills hijas auto-destiladas                        |
| `E:\vars\var 5\X-com guardados\ESTADO_VIGIA.txt`                      | ⭐ Veredicto de la última corrida + fallos seguidos  |
| `E:\vars\var 5\X-com guardados\harvest_x_diario.bat`                  | ⭐ Lo que corre la tarea: dos compuertas y un código |
| `E:\vars\var 5\X-com guardados\harvest_x.log`                         | Registro de la envoltura (separado de `watcher.log`) |
| `E:\vars\var 5\X-com guardados\crear_tarea_vigia_x.ps1`               | Registra la tarea programada (lo corre el usuario)  |
| `E:\vars\var 5\X-com guardados\start_watch.bat`                       | Modo bucle, solo para mirarlo a mano                |
| `…\scripts\preflight_cdp.py` (skill `linkedin-guardados-fedphd`)      | Compuerta CDP compartida. Nunca mata Edge           |
| `_PELIGROSO_autostart_login.bat.desactivado`                          | 🚦 Desactivado 8-nov-2026. Mataba Edge. No reactivar |
| `_PELIGROSO_start_edge_debug.bat.desactivado`                         | 🚦 Desactivado 8-nov-2026. Mataba Edge. No reactivar |

## Cómo se invoca (operación humana)

### Caso 1 — Tras reiniciar el computador

**Nada que hacer.** La tarea programada «X-com vigia bookmarks fdc_ec
(diario)» corre a las 9:35 y levanta su propio Edge. LinkedIn va a las 9:15;
están escalonadas a propósito.

🚦 **El procedimiento viejo de esta sección era peligroso y ya no existe.**
Decía «doble-clic en `start_edge_debug.bat`». Ese archivo hacía
`taskkill /F /IM msedge.exe` y relanzaba Edge con
`--remote-debugging-port=9222` **sobre el perfil por defecto** — el indicador
que Chromium 136+ ignora en silencio. Es decir: mataba la sesión de Edge del
usuario, WhatsApp incluida, **y encima no abría el puerto**. El 8-nov-2026 se
desactivó junto con `autostart_login.bat`, que hacía lo mismo al iniciar
sesión; quedan con el nombre `_PELIGROSO_*.desactivado`. **No reactivarlos.**

Para levantar el puerto, siempre `preflight_cdp.py`, que nunca mata nada y
solo da el paso si el puerto **responde**.

### Caso 1-b — Correr la pasada a mano

```bash
powershell -Command "& cmd.exe /c 'E:\vars\var 5\X-com guardados\harvest_x_diario.bat'; $LASTEXITCODE"
```

🚦 Desde Git Bash **no**: MSYS convierte `/c` en `C:/`, `cmd` arranca
interactivo, no ejecuta nada y devuelve 0. Éxito falso perfecto
([[feedback_git_bash_convierte_barra_c]]).

### Caso 2 — Forzar un refresh manual

```bash
python "E:/vars/var 5/X-com guardados/autoreflex_pipeline.py" \
       --create-threshold 80 --augment-threshold 30
```

Baja los umbrales para que se generen skills en temas con menos
volumen. Útil para una corrida inicial o tras una purga.

### Caso 3 — Consultar un tema desde otra sesión de Claude

Cualquier sesión nueva puede llamar:

```bash
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --tema "geopolitica" --top 15
```

O invocar la skill hija directamente:
`Skill(intereses-geopolitica-soberania)`.

## Limitaciones honestas

- **No es consciencia.** Es un bucle persistente con memoria
  compartida. La diferencia importa: si el watcher muere, no "se
  duerme"; simplemente deja de capturar.
- **Una pasada al día, no cada 5 minutos.** Desde el 8-nov-2026 el modo de
  producción es `--once` por tarea programada. El bucle sigue existiendo para
  mirarlo a mano, pero no es lo que corre: **un bucle infinito no se puede
  vigilar ni reiniciar; si muere, muere en silencio** — y así estuvo 135 días.
- **Solo lee la cabecera del feed, y solo añade.** El archivo no se puede
  vaciar por esta vía (`archive = new_recs + archive`). El riesgo real no es
  perder el corpus: es **capturar cero en silencio**, que es lo que ahora
  distingue `ESTADO_VIGIA.txt`.
- **Si guardas muchos bookmarks en un día**, la cabecera puede no alcanzar;
  para un re-escaneo completo, `export_bookmarks.py`.
- **Sin LLM en el pipeline.** La clasificación es por regex sobre la
  taxonomía de `analizar_temas.py`. Si un tema nuevo emerge (ej.
  "kayaking") no se detecta hasta que el usuario lo añada a `THEMES`.

## Compuertas 🚦

1. **NO crear skills duplicadas.** El pipeline hace `if slug in existing: skip`.
2. **NO sobreescribir SKILL.md existentes.** Sólo añade `.md` en
   `references/`.
3. **NO mover/borrar bookmarks.json sin snapshot previo.** El usuario
   tiene 5.550 entradas curadas; perderlas es destruir años de criba.
4. **NO subir nada a la nube** desde este pipeline. Todo es local.
5. **Si la taxonomía cambia, re-correr `analizar_temas.py` antes del
   pipeline** — si no, las skills nuevas se generarán con cuentas top
   desactualizadas.
6. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
7. 🚦🚦 **NUNCA terminar el Edge dedicado cerrando su última pestaña.** El 14-nov-2026
   la cosecha entró bien a las 19:49 y a las 19:56 el veredicto era `MURO_AUTH`: al cerrar
   la última pestaña, Chromium se fue sin volcar al disco las cookies que X rota en cada
   uso, y en el perfil solo quedaron las de invitado. **`auth_token` y `ct0` se perdieron
   por el cierre, no por caducidad.** Lo normal es **dejar ese Edge abierto**: la compuerta
   lo reutiliza y no relanza nada. Si hay que cerrarlo, por `Browser.close` de CDP, que
   vuelca antes de salir — y nunca justo después de navegar por x.com.
8. 🚦 **El puerto a la escucha es necesario y NO suficiente.** Ese mismo día el puerto 9224
   respondía CDP, la sesión estaba viva y el vigía salió con **código 4**: `connect_over_cdp`
   venció a los 180 s **después** de conectar el websocket, porque Playwright se engancha a
   todos los objetivos y el perfil tenía **61** (unos 40 service workers de extensiones más
   la pestaña de bienvenida que cada extensión abre la primera vez que arranca el perfil).
   `preflight_cdp.py` cierra ahora esa hojarasca tras un lanzamiento propio y lo registra en
   el log. **Si vuelve a aparecer un código 4 con sesión buena, leer el recuento de objetivos
   antes de tocar nada más.**
9. 🚦 **No cambiar una sesión viva por una comprobación.** La avería 7 la causé probando la
   corrección de la 8. Antes de una prueba que toca el navegador, preguntarse qué se pierde
   si sale mal; si lo que se arriesga es la sesión, la prueba espera.

## Skills hijas auto-destiladas (estado al 2026-06-23)

Las 16 skills `intereses-*` creadas la primera corrida del pipeline:

- `intereses-geopolitica-soberania` (979 bookmarks)
- `intereses-educacion-aprendizaje` (917)
- `intereses-espiritualidad-religion` (759)
- `intereses-ia-llms` (722)
- `intereses-vida-masculina` (688)
- `intereses-productividad-habitos` (636)
- `intereses-liderazgo-estrategia` (610)
- `intereses-historia-arquetipos` (539)
- `intereses-negocios-emprendimiento` (507)
- `intereses-mentalidad-desarrollo` (472)
- `intereses-finanzas-mercados` (466)
- `intereses-salud-cuerpo` (438)
- `intereses-filosofia` (254)
- `intereses-blockchain-web3` (223)
- `intereses-geopolitica-latam` (156)
- `intereses-pensamiento-critico` (117)

Tema `intereses-tecnologia-programacion` (85) quedó debajo del umbral
de creación; aparecerá cuando supere 100.

## Cómo depurar si falla

Todo lo de aquí se midió el 8-nov-2026, reparando el vigía.

### `MURO_AUTH` — la sesión de X caducó

Lo único que pide mano humana. Se abre el Edge del puerto 9224 (lo levanta
`preflight_cdp.py --puerto 9224 --perfil C:\Users\datos\edge-x-export`), se
entra a x.com como **@fdc_ec** en esa ventana, y se vuelve a correr. El agente
**no** escribe la contraseña.

🚦 **La sesión de X no está donde parecía.** El perfil dedicado del 9222
(`browser_profile_edge`) tiene cookies de LinkedIn y **ninguna** de x.com. La
de X vive en `C:\Users\datos\edge-x-export`. Por eso el vigía tiene puerto
propio, igual que Telegram usa el 9223 ([[reference_telegram_cdp_tirr999]]).

🚦 **Cookies presentes no es sesión viva.** `edge-x-export` tenía cookies de
`.x.com` con fecha reciente y la sesión estaba muerta igual. Mismo mecanismo
que [[notebooklm-login-reauth]]: `auth check` pasa y la sesión no sirve. **La
única prueba es pedir la página y mirar qué devuelve.**

### RUTA B — trasplantar la sesión desde el Edge del usuario (preparada, SIN PROBAR)

Escrita el 14-nov-2026 y **detenida por orden del usuario antes de ejecutarse**: no
está probada, y hasta que lo esté, la ruta buena sigue siendo la de arriba —entrar a
mano en la ventana del perfil dedicado—. Se documenta porque el mecanismo es correcto
y la próxima vez no hay que volver a deducirlo.

**Para qué sirve:** evita que el usuario teclee la contraseña. La sesión de @fdc_ec
vive en su Edge de todos los días; a ese Edge **no se le puede enganchar CDP** —
Chromium 136+ ignora `--remote-debugging-port` en el perfil por defecto y el indicador
hay que darlo al arrancar ([[feedback_cdp_9222_ignorado_perfil_defecto]])—, así que lo
que se mueve no es el navegador: son las cookies.

| Guion (en `E:\vars\var 5\X-com guardados\`) | Qué hace |
|---|---|
| `trasplantar_sesion_x.py` | Copia el tarro de cookies del perfil del usuario, **lo poda a solo `x.com`** e instala eso más la clave `os_crypt` en `edge-x-export` |
| `comprobar_trasplante.py` | La comprobación barata: ¿`auth_token` trae valor legible y `/i/bookmarks` no redirige? |

**Las tres compuertas que lleva dentro, y por qué cada una:**

1. **Si hay cualquier Edge en marcha, para y no hace nada.** Con Edge vivo el tarro está
   tomado: `shutil.copy2` da `PermissionError` y `sqlite3` con `immutable=1` da
   `unable to open database file`. Una copia a medias es peor que ninguna. 🚦 Y ese
   «no pude mirar» **no es «no hay nada»** — misma trampa que la compuerta de cookies.
2. **Respaldo fechado de lo que se va a pisar, antes de pisarlo**
   (`edge-x-export\_respaldo_pre-trasplante_<sello>\`), que es la regla de
   [[feedback_set_e_no_aborta_y_rm_corre_igual]]: ningún paso destructivo detrás de uno
   sin comprobar.
3. **Solo viaja `x.com`.** El perfil del usuario tiene el tarro entero —banca, Google,
   todo—; se copia, se borran las filas que no son de `x.com` y se hace `VACUUM` antes
   de instalarlo. Un segundo perfil en la máquina con todas sus sesiones sería una
   brecha, no una comodidad.

**Lo que se mueve con las cookies y suele olvidarse:** la clave de cifrado. Los valores
están cifrados con `os_crypt` del `Local State` de origen, así que sin ella son ruido.
Se inyecta **solo ese campo** en el `Local State` del destino; sus preferencias no se
tocan. El cifrado ligado a la aplicación (Chromium 127+) impide que lo lea una
herramienta de terceros —de ahí el *Could not decrypt edge cookies* de
[[feedback_reauth_notebooklm_cosecha]]—, pero **no impide que lo lea Edge mismo**, que
es quien abre el perfil destino. Esa es la apuesta del mecanismo y es lo único que falta
por verificar.

**Riesgo residual honesto:** si el cifrado ligado a la aplicación no coopera en la ruta
nueva, el trasplante no sirve y se vuelve a la ruta A. No se pierde nada —el respaldo
está hecho y las cookies del destino eran de invitado—, pero **nadie lo ha comprobado
todavía**.

### Cómo se averigua qué pasó de verdad

Dos comprobaciones baratas, en este orden:

```python
# 1. ¿Qué cuentas tiene abiertas ese puerto? (a la sesión VIVA, por CDP)
#    No copiar el fichero Cookies: con Edge en marcha da PermissionError,
#    que significa «no pude mirar», NO «no hay nada».
ctx = p.chromium.connect_over_cdp("http://localhost:9224").contexts[0]
[c["domain"] for c in ctx.cookies() if "x.com" in c["domain"]]

# 2. ¿Qué mostró la pestaña? URL, título y texto del cuerpo.
pg.url; pg.title(); pg.inner_text("body")[:600]
```

La segunda fue la que cerró el diagnóstico: el texto era «Selecciona una opción
a continuación… Continuar con Google».

### 🚦 Detectar el muro por el PARÁMETRO, no por la ruta

La URL medida fue:

```
https://x.com/i/jf/onboarding/web?redirect_after_login=%2Fi%2Fbookmarks&mode=login
```

**No contiene `/flow/login` ni `/login`.** Mi primera lista de detección eran
rutas, y clasificó un muro de autenticación como `CERO_CAPTURADOS`. Lo
invariante es el parámetro (`redirect_after_login`, `mode=login`); la ruta X la
renombra. Constante `SENALES_DE_LOGIN` en `watch_bookmarks.py`.

### 🚦🚦 Y el muro tampoco se detecta en una página PÚBLICA — una URL pública no prueba nada

Corrección de la sección anterior, medida el 14-nov-2026 por la noche. Buscando
confirmar la sesión, pedí `https://x.com/fdc_ec` y la página **cargó completa
estando deslogueado**: nombre, 900 posts, 6.457 siguiendo, 878 seguidores, los
posts antiguos, y el muro únicamente como hoja al pie («Continuar con teléfono ·
Apple · Google»). La URL **no** redirigió, así que mi comprobación por parámetro
dictaminó «SESIÓN VIVA», y era falso.

**El parámetro solo delata el muro en una URL que exige sesión** (`/i/bookmarks`,
`/home`, `/notifications`). Un perfil público es visible para cualquiera: pedirlo
no distingue entrar de mirar.

La prueba barata y sin ambigüedad son **las cookies de la sesión viva, por CDP**:

```python
ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9224").contexts[0]
n = [c["name"] for c in ctx.cookies() if "x.com" in (c.get("domain") or "")]
viva = ("auth_token" in n) and ("ct0" in n)      # 'guest_id' solo NO es sesión
```

Ese día había 13 cookies de `.x.com` y **ninguna de las tres que importan**
(`auth_token`, `ct0`, `twid`): solo las de invitado. Encaja con la compuerta de
arriba —cookies presentes no es sesión viva— y le añade el otro filo: **ausencia
de las tres sí es sesión muerta, y es la lectura más barata que existe.** Pedir
una página solo decide si además se eligió una que exija entrar.

### 🚦 El `.bat` y el guion no pueden escribir en el MISMO registro

Costó un veredicto. El `.bat` redirigía con `>> watcher.log`, que en Windows
deja el archivo tomado; el `log()` del guion hacía `open("a")` sobre el mismo
archivo → `PermissionError` → la excepción subió hasta `__main__` → **el código
de salida pasó de 3 (sesión caducada) a 1 (fallo genérico)**.

Dos arreglos, los dos necesarios: la envoltura escribe en `harvest_x.log`, y
`log()` nunca deja que un registro ilegible tape el resultado. **Una línea de
registro perdida es una molestia; un veredicto enmascarado es una avería** —
pertenece a la familia de [[prueba-eliza-agente-que-trabaja]].

### `CERO_CAPTURADOS` con sesión viva

Entonces sí es el patrón GraphQL: `GRAPHQL_PATTERN` busca
`/graphql/<hash>/Bookmark`. Si X renombra la operación, no casa nada y no hay
error. Comprobarlo mirando las peticiones reales de la pestaña antes de tocar
el patrón.

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — la doctrina padre.
- [[consulta-bookmarks-fdc-ec]] — skill hermana para consultar.
- [[auditoria-cognitiva-reflexiva]] — para auditar al propio agente.
