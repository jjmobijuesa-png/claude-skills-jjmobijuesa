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

idioma_de_salida: español neutro técnico
nivel_madurez: aplicada
fuente: instalación 2026-06-26 (yt-dlp + youtube-transcript-api)
---

# YouTube — corpus jjmobijuesa@gmail.com

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

## Cómo depurar si falla

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
