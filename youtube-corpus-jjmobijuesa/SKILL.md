---
name: youtube-corpus-jjmobijuesa
description: |
  Acceso al corpus de YouTube del usuario jjmobijuesa@gmail.com:
  listar playlists privadas y públicas, extraer transcripciones de
  videos por playlist o por ID, y archivarlas como markdown listo
  para análisis por skills hijas (Pareto, mapa mental, MIT,
  inteligencia política).

  Stack: yt-dlp (lista playlists + videos, con cookies del Edge
  logueado) + youtube-transcript-api (descarga la transcripción
  oficial cuando existe). Resultados en
  `E:\vars\var 5\YouTube-jjmobijuesa\`.

  NO sustituye a notebooklm para curaduría temática del usuario:
  YouTube es la fuente de aprendizaje en formato video; NotebookLM
  es el espacio donde el usuario cura, etiqueta y conversa con sus
  fuentes.

trigger_phrases:
  - "lista mis playlists de YouTube"
  - "extrae transcripciones de la playlist"
  - "transcribir videos de YouTube"
  - "corpus YouTube jjmobijuesa"
  - "qué tengo guardado en YouTube"
  - "<cualquier link de video youtube/youtu.be compartido por el usuario>"

idioma_de_salida: español neutro técnico
nivel_madurez: aplicada
fuente: instalación 2026-06-26 (yt-dlp + youtube-transcript-api)
---

# YouTube — corpus jjmobijuesa@gmail.com

> **REGLA DE INVOCACIÓN AUTOMÁTICA (2026-07-04):** siempre que el usuario comparta
> un **link de video** (YouTube u otro), invocar esta skill de inmediato para
> extraer la transcripción y **usarla** en la tarea en curso + aprovechar la
> **memoria compartida** — nunca responder «no puedo ver video». Regla registrada en
> memoria como `feedback-video-links-auto-transcribe`.

## Doctrina

Esta skill convierte el corpus de YouTube del usuario en texto local
indexable. El video es una de las fuentes de aprendizaje más densas
que el usuario consume — esta skill captura la materia prima para
que otras skills (Pareto, mapas mentales, MIT, defensa apologética)
trabajen sobre transcripciones reales en vez de adivinar.

Tres principios:

1. **Cookies del Edge logueado.** No pedimos credenciales — leemos
   las cookies del perfil Edge que el usuario ya tiene autenticado
   en YouTube como jjmobijuesa@gmail.com.
2. **Pareto sobre la playlist.** Una playlist es ya una curación del
   usuario; las playlists con título descriptivo (no "Watch Later")
   son las que reciben transcripción primero.
3. **Persistencia obligatoria.** Cada video transcrito se guarda como
   markdown con metadatos en `transcripciones/<playlist>/`. Si el
   archivo ya existe, se omite por defecto.

## Cómo usarla

### 1. Listar playlists del usuario

```bash
python "C:/Users/datos/.claude/skills/youtube-corpus-jjmobijuesa/scripts/listar_playlists.py"
```

Genera:
- `E:\vars\var 5\YouTube-jjmobijuesa\playlists_index.json`
- `E:\vars\var 5\YouTube-jjmobijuesa\playlists_index.md`

### 2. Extraer transcripciones de una playlist

```bash
# Por URL completa
python "C:/Users/datos/.claude/skills/youtube-corpus-jjmobijuesa/scripts/extraer_transcripciones.py" \
       --playlist "https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxx"

# Por ID de playlist
python ".../extraer_transcripciones.py" --playlist PLxxxxxxxxxxxxxxx

# Limitar a primeros 10 videos
python ".../extraer_transcripciones.py" --playlist PLxxxx --limit 10

# Idiomas preferidos (en orden)
python ".../extraer_transcripciones.py" --playlist PLxxxx --idioma es,en,pt
```

Genera por playlist:
- `transcripciones/<titulo_playlist>/<titulo_video>__<video_id>.md`
- `transcripciones/<titulo_playlist>/_INDICE.json`

### 3. Extraer videos individuales

```bash
python ".../extraer_transcripciones.py" --videos abc123XYZ def456UVW
```

## Estructura de carpetas

```
E:\vars\var 5\YouTube-jjmobijuesa\
├── playlists_index.{json,md}      ← catálogo de playlists del usuario
└── transcripciones\
    ├── <playlist 1>\
    │   ├── <video 1>__<id>.md     ← transcripción + metadatos
    │   ├── <video 2>__<id>.md
    │   └── _INDICE.json           ← índice de la playlist
    └── <playlist 2>\...
```

## Cuándo combinarla con otras skills

| Skill | Uso |
|---|---|
| [[aprendizaje-pareto-juridico]] | Destila 20% accionable de un curso/playlist |
| [[mapa-mental-disertacion-juridica]] | Genera disertación basada en videos curados |
| [[metodo-mit-notebooklm-riguroso]] | Aplica método MIT a una serie de videos |
| [[llave-maestra-autoaprendizaje-ia]] | Detecta brechas y archiva nuevas skills derivadas |
| [[anthropic-skills:notebooklmskill]] | Sube transcripciones al cuaderno temático |

## Compuertas 🚦

1. **No grabar / no descargar el video MP4** — sólo transcripción. Si
   se necesita el audio, usar `yt-dlp` directo, no esta skill.
2. **No publicar transcripciones** de videos privados o restringidos
   fuera del computador local del usuario.
3. **Rate limit por defecto 1,5 s entre videos** — bajarlo invita a
   bloqueo temporal de YouTube.
4. **Cookies en Edge tienen TTL** — si yt-dlp devuelve error de auth,
   abrir YouTube en Edge, loguearse, reintentar.
5. **Transcripción no disponible ≠ error**: muchos videos no la
   exponen; se registra como `_Transcripción no disponible: <razon>_`
   y se sigue.
6. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cosechar un CANAL entero (9-nov-2026) 🚦

El guion **no acepta una URL de canal**: solo `--playlist` o `--videos`. Y
`--playlist` fuerza `cookiesfrombrowser('edge')` **incluso en contenido
público**, que es justo la avería más frecuente de esta skill. `--videos` sí
evita las cookies, pero escribe en `_manuales` **sin título**.

Receta probada sobre `@sofiaweb` (envoltorio que importa las funciones del
guion y lista el canal sin cookies):

```python
opts = {"quiet": True, "extract_flat": True, "ignoreerrors": True}   # SIN cookies
info = yt_dlp.YoutubeDL(opts).extract_info("https://www.youtube.com/@CANAL/videos", download=False)
```

### Tres trampas que cuestan el corpus entero

1. ⭐⭐ **El vídeo que importa puede estar SIN LISTAR.** En `@sofiaweb` la
   pestaña Videos no pasaba de hace cinco años, y el curso con IA —el único con
   el método nuevo— es de hace uno y **solo aparece en la pestaña Principal**.
   Un inventario hecho con `/videos` concluye que el canal lleva años parado y
   **pierde exactamente la pieza nueva**.
   **Comprobación:** abrir la raíz del canal y recoger los `watch?v=` del DOM;
   los que no estén en `/videos` son no listados y hay que añadirlos a mano.
2. ⭐ **Las listas traen vídeos que el canal no lista.** Todo el curso
   WooCommerce (#3 a #13) estaba solo en su playlist. **Cosechar por lista
   además de por canal**, y conservar el orden de la lista: ese orden **es el
   currículo**.
3. 🚦 **El orden de `/videos` no es el que se ve en el navegador.** Confirmar
   contra la página real antes de concluir nada sobre fechas.

### 🚦🚦 Bloqueo de IP — y por qué no se arregla con otra variante

Tras unas **78 peticiones seguidas**, YouTube corta por dirección IP:

| Vía | Qué devuelve | Qué parece |
|---|---|---|
| `youtube-transcript-api` | `RequestBlocked` / `IpBlocked` | «este vídeo no tiene transcripción» |
| URL `api/timedtext` de yt-dlp | `HTTP 429 Too Many Requests` | cero caracteres, lengua detectada |

⭐ **Las dos vías mueren con la misma IP caliente.** La segunda funcionó en una
sonda aislada y falló en tanda: **una sonda de un vídeo no prueba que la tanda
pase.** El remedio es **esperar**, no una tercera variante.

🚦 **Un cero por bloqueo y un cero por ausencia se ven idénticos en la salida y
significan lo contrario.** La única lectura válida es **el mensaje de error
real**, no el recuento. Si el guion guarda el error como dato en vez de
gritarlo, ya perdió la distinción.

### 🚦🚦 Candado antipisada — obligatorio

Mismo mecanismo que [[feedback_linkedin_corpus_pisado_por_cosecha_vacia]]:
**una cosecha fallida jamás sobrescribe una transcripción real.**

```python
def creible(destino, items):
    if items: return True, "cosecha con %d segmentos" % len(items)
    if not destino.exists(): return True, "sin transcripcion y no habia previo"
    if MARCA_VACIA in destino.read_text(encoding="utf-8"): return True, "el previo tambien estaba vacio"
    return False, "RECHAZADA: el previo tiene transcripcion real"
```

El 9-nov esto salvó 29 transcripciones (341.734 caracteres) que una tanda
bloqueada habría dejado en «no disponible». **Las carpetas que quedan con 0
transcripciones reales se borran**, o pasan por corpus.

### 🚦 Los subtítulos viejos no traen puntuación

Los automáticos de 2016-2021 llegan **sin puntos**. Cualquier análisis anclado
al punto (`[^.]{0,90}\.`) devuelve **cero en silencio** sobre ellos y normal
sobre los de 2025. **Muestrear por posición** (ventanas repartidas por el
minutaje) o normalizar a una línea antes de buscar patrones; el `grep` de
varias líneas también falla por el salto, no por ausencia.

### 🚦🚦 TEMA CERRADO por decisión del usuario — 14-nov-2026

**No se vuelve a intentar la cosecha de los capítulos bloqueados. Se trabaja con lo que
hay.** La decisión es del usuario, con estas palabras: «los cap de youtube cerrar ese tema,
nos quedamos con los que tenemos».

**Estado medido en disco ese día** (`E:\vars\var 5\YouTube-jjmobijuesa\transcripciones\`):

| Carpeta | `.md` | Con transcripción real | Marcados «no disponible» |
|---|---:|---:|---:|
| `Sofia Web - @sofiaweb` | 51 | **29** | 22 |
| `_manuales` | 62 | **32** | 30 |
| `DRLAROSA-biohacking` | 0 | 0 | 0 |
| **Total** | **113** | **61** | **52** |

**Qué significa esto para cualquier sesión futura:**

- 🚦 **Los 52 «no disponible» NO son un pendiente.** Son el corpus tal como queda. No
  reabrir la tanda, no bajar el ritmo y reintentar, no probar una tercera vía.
- 🚦 **Y no se pueden presentar como ausencia de subtítulos:** parte de esos ceros vinieron
  de **bloqueo por IP** (`RequestBlocked` / `429`), no de que el vídeo no los tuviera. Un
  cero por bloqueo y un cero por ausencia se ven idénticos y significan lo contrario; al
  citar el corpus se dice **61 transcripciones reales de 113 fichas**, no «113 vídeos».
- **Si alguna vez hace falta uno concreto**, se pide ese vídeo suelto y se anota por qué
  valía la pena; lo que queda cerrado es la **tanda**, no la herramienta.
- 🚦 La carpeta `DRLAROSA-biohacking` quedó con **cero** archivos. Existe y no aporta nada:
  borrarla o repoblarla es decisión del usuario, no del agente.

**Por qué queda escrito aquí y no en una lista de pendientes:** este pendiente vivió semanas
**solo en la conversación** y por eso reaparecía en cada relevo. Un pendiente que no está en
la skill que lo gobierna no está cerrado: está esperando que alguien lo recuerde.

## Cómo depurar si falla

- **`RequestBlocked` / `IpBlocked` / `HTTP 429`:** bloqueo por IP, no ausencia
  de subtítulos. **Esperar** (20 minutos o más) y bajar el ritmo a 15-20 s por
  vídeo. No probar una tercera biblioteca: la IP es la misma.
- **«0 transcripciones» en una tanda que antes funcionó:** leer el `error` del
  `_INDICE.json`, no el recuento. Y comprobar que el candado no dejó pasar
  escrituras vacías.
- **Un patrón que aparece en un vídeo y en ninguno más:** probablemente el
  resto son subtítulos sin puntuación. Ver la trampa anterior.
- `Sign in to confirm you're not a bot`: actualizar yt-dlp
  (`pip install -U yt-dlp`).
- `Could not copy Chrome cookie database`: bug conocido — Edge bloquea
  su SQLite mientras está corriendo. Tres workarounds:
  1. **Cookies a archivo** — instalar la extensión "Get cookies.txt
     LOCALLY", exportar como `cookies.txt`, y pasar
     `--cookies E:\vars\var 5\YouTube-jjmobijuesa\cookies.txt` al
     script en lugar de `--browser edge`.
  2. **Playlist pública** — si la playlist es pública, no necesita
     cookies. Pasarle la URL pública directa.
  3. **Cerrar Edge debug temporalmente** — invasivo (rompe watcher).
- `YouTubeTranscriptApi has no attribute get_transcript`: versión nueva
  del paquete (≥ 1.x) cambió la API a `.fetch()`. El script ya usa la
  nueva.
- `Video unavailable`: el video es privado o eliminado; se omite y
  se anota.
- Para depurar interactivo: añadir `verbose=True` en las opciones de
  yt-dlp.

## Smoke test verificado el 2026-06-26

- `python extraer_transcripciones.py --videos bOlroS23mN4` extrajo
  504 segmentos en español (19 152 chars) del video de NotebookLM /
  método MIT — el mismo que el usuario tiene como base de la skill
  `metodo-mit-notebooklm-riguroso`.

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — meta-doctrina del agente.
- [[perplexity-active-use]] — fuente complementaria (texto vs video).
