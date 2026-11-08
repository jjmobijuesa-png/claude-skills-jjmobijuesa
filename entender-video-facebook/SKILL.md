---
name: entender-video-facebook
description: |
  Entiende un video de Facebook (o YouTube/otros) descargando su audio y
  transcribiéndolo LOCALMENTE: yt-dlp baja el audio, ffmpeg lo normaliza y
  faster_whisper lo transcribe. Devuelve metadatos (título, autor, duración,
  descripción/caption) + transcripción en un .md. Los videos PÚBLICOS de
  Facebook (share/v/<id>) NO requieren login. Úsala ante un enlace de video de
  Facebook cuyo contenido hay que comprender o destilar.
trigger_phrases:
  - "entiende este video de facebook"
  - "transcribe el video de facebook"
  - "qué dice este video"
  - "destila el enfoque de este video"
  - "analiza el reel"
idioma_de_salida: español
nivel: aplicada
dominio: ingesta de video / transcripción local
metadata:
  version: 1.0
  fecha: 2026-10-03
  verificado_en: "esta máquina — yt-dlp 2026.06.09 + ffmpeg 8.1.2 + faster_whisper (base): FB público, 90s→10s"
  relacionada: youtube-corpus-jjmobijuesa, feedback_video_links_auto_transcribe, feedback_leer_video_local_frames, feedback_solo_edge, humanizacion-texto-sin-firma-ia
---

# Skill `entender-video-facebook`

## Qué resuelve
Facebook no expone transcripción por API (a diferencia de YouTube). La vía fiable es
**descargar el audio y transcribirlo en local**. Los videos **públicos** de Facebook
(`facebook.com/share/v/<id>`) se leen **sin login**. Stack ya instalado aquí:
**yt-dlp** (módulo Python) + **ffmpeg** + **faster_whisper**.

## Uso
```powershell
$PY="C:\Users\datos\AppData\Local\Programs\Python\Python312\python.exe"
# Público (lo normal). --model small = mejor calidad ES; base = más rápido.
& $PY "C:\Users\datos\.claude\skills\entender-video-facebook\scripts\entender_video_facebook.py" `
      "https://www.facebook.com/share/v/<id>/" "C:\ruta\salida" --model small
# Solo probar: --seconds 90  (transcribe los primeros 90 s)
```
El script imprime META + MUESTRA y guarda `<fecha>_<titulo>.md` con metadatos,
descripción/caption y transcripción. Ejecutar con el **Python de 64 bits** del sistema.

## Cómo depurar si falla
- **`Could not copy Chrome cookie database`** al usar `--cookies edge`: el Edge del usuario
  está **abierto** y Chromium bloquea la BD de cookies. Para videos **privados**: cerrar Edge
  antes, o usar un **perfil Edge dedicado** logueado en Facebook (patrón `feedback_solo_edge`,
  como WhatsApp/Telegram) y exportar sus cookies. Para videos **públicos no hace falta** ninguna cookie.
- **Audio no descarga**: revisar que la URL sea del video (`/share/v/<id>/` o `/watch/?v=`); probar `-f best`.
- **Transcripción pobre** (nombres propios, tecnicismos): subir el modelo a `small` o `medium`;
  🚦 una síntesis sobre transcripción mala sale fluida y es ficción ([[feedback_gemini_notas_meet_idioma]]) → verificar contra el texto escrito antes de concluir.
- **`E:` no disponible**: la unidad puede no estar montada en la sesión; usar salida en `C:` o `G:`.

## Compuertas 🚦
- Facebook y toda red social: **solo lectura**. Nunca publicar, comentar, reaccionar ni enviar.
- La transcripción es insumo: **verificar** antes de citar como hecho.

## Relacionadas
[[youtube-corpus-jjmobijuesa]] (YouTube con captions oficiales) · [[feedback_video_links_auto_transcribe]] · [[feedback_leer_video_local_frames]] (video local por frames) · [[feedback_solo_edge]] · [[humanizacion-texto-sin-firma-ia]]
