# -*- coding: utf-8 -*-
"""
Extrae transcripciones de los videos de una playlist (o de una lista de
video IDs) en YouTube y los guarda como .md en
E:\\vars\\var 5\\YouTube-jjmobijuesa\\transcripciones\\<playlist>\\.

Estrategia:
  1. yt-dlp lista los videos de la playlist (con cookies de Edge si es
     privada).
  2. youtube-transcript-api obtiene la transcripción de cada video
     (sin auth, funciona en públicos; en privados / restringidos
     puede fallar — se registra como "transcripción no disponible").

Uso:
  python extraer_transcripciones.py --playlist <URL_o_ID>
  python extraer_transcripciones.py --playlist <URL> --idioma es,en
  python extraer_transcripciones.py --videos VIDEO_ID1 VIDEO_ID2
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
try:
    from youtube_transcript_api._errors import (
        TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
    )
except Exception:
    # Versiones nuevas exportan distintas excepciones
    TranscriptsDisabled = Exception
    NoTranscriptFound = Exception
    VideoUnavailable = Exception

_YT_API = YouTubeTranscriptApi()

OUT_ROOT = Path(r"E:\vars\var 5\YouTube-jjmobijuesa\transcripciones")
OUT_ROOT.mkdir(parents=True, exist_ok=True)


def safe_name(s):
    return re.sub(r"[^\w\-_. ]", "_", (s or ""))[:120].strip() or "untitled"


def list_playlist_videos(url_or_id, cookies_browser="edge"):
    if not url_or_id.startswith("http"):
        url = f"https://www.youtube.com/playlist?list={url_or_id}"
    else:
        url = url_or_id
    opts = {
        "quiet": True, "no_warnings": True,
        "extract_flat": True,
        "cookiesfrombrowser": (cookies_browser, None, None, None),
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    title = info.get("title", "playlist")
    entries = info.get("entries", []) or []
    videos = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        videos.append({
            "id": e.get("id"),
            "title": e.get("title"),
            "url": e.get("url") or f"https://www.youtube.com/watch?v={e.get('id')}",
            "duration": e.get("duration"),
            "uploader": e.get("uploader"),
        })
    return title, videos


def fetch_transcript(video_id, languages=("es", "en")):
    """API nueva de youtube-transcript-api ≥ 1.x.
    Devuelve (lang, snippets_list_of_dicts) o (None, {error}).
    """
    try:
        t = _YT_API.fetch(video_id, languages=list(languages))
        items = [{"text": s.text, "start": getattr(s, "start", None),
                  "duration": getattr(s, "duration", None)} for s in t.snippets]
        return t.language_code, items
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        return None, {"error": type(e).__name__}
    except Exception as e:
        return None, {"error": str(e)}


def transcript_to_text(items):
    if not items or not isinstance(items, list):
        return ""
    return "\n".join(it.get("text", "") for it in items)


def write_md(playlist_dir, video, lang, items):
    fname = f"{safe_name(video.get('title') or video['id'])}__{video['id']}.md"
    target = playlist_dir / fname
    body = [
        f"# {video.get('title') or video['id']}",
        f"",
        f"- **video_id**: `{video['id']}`",
        f"- **url**: <{video['url']}>",
        f"- **uploader**: {video.get('uploader') or '?'}",
        f"- **duration_s**: {video.get('duration') or '?'}",
        f"- **transcript_lang**: {lang or 'no disponible'}",
        f"- **extracted_at**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"---",
        f"",
    ]
    if items and isinstance(items, list):
        body.append(transcript_to_text(items))
    else:
        err = items.get("error") if isinstance(items, dict) else "sin datos"
        body.append(f"_Transcripción no disponible: {err}_")
    target.write_text("\n".join(body), encoding="utf-8")
    return target


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--playlist", help="URL o ID de la playlist")
    ap.add_argument("--videos", nargs="+", help="Lista de video IDs (omitir --playlist)")
    ap.add_argument("--browser", default="edge",
                    help="Navegador para cookies (sólo si playlist privada)")
    ap.add_argument("--idioma", default="es,en",
                    help="Idiomas preferidos por orden, separados por coma")
    ap.add_argument("--limit", type=int, default=0,
                    help="Limitar nº de videos por playlist (0 = todos)")
    ap.add_argument("--delay", type=float, default=1.5,
                    help="Pausa en segundos entre videos (rate limit)")
    args = ap.parse_args()

    langs = tuple(s.strip() for s in args.idioma.split(",") if s.strip())

    if args.playlist:
        title, videos = list_playlist_videos(args.playlist, args.browser)
        if args.limit:
            videos = videos[:args.limit]
        pdir = OUT_ROOT / safe_name(title)
        pdir.mkdir(parents=True, exist_ok=True)
        print(f"Playlist: {title} → {pdir}")
        print(f"Videos: {len(videos)}")
        index = []
        for i, v in enumerate(videos, 1):
            print(f"  [{i}/{len(videos)}] {v.get('title') or v['id']} ...", flush=True)
            lang, items = fetch_transcript(v["id"], langs)
            target = write_md(pdir, v, lang, items)
            index.append({
                "video_id": v["id"],
                "title": v.get("title"),
                "url": v["url"],
                "lang": lang,
                "available": isinstance(items, list),
                "file": target.name,
            })
            time.sleep(args.delay)
        (pdir / "_INDICE.json").write_text(
            json.dumps({"playlist": title, "videos": index}, ensure_ascii=False, indent=2),
            encoding="utf-8")
        ok = sum(1 for x in index if x["available"])
        print(f"\nResumen: {ok}/{len(index)} con transcripción.")
        return

    if args.videos:
        pdir = OUT_ROOT / "_manuales"
        pdir.mkdir(parents=True, exist_ok=True)
        for vid in args.videos:
            print(f"  → {vid} ...", flush=True)
            lang, items = fetch_transcript(vid, langs)
            write_md(pdir, {"id": vid, "title": None,
                            "url": f"https://www.youtube.com/watch?v={vid}",
                            "uploader": None, "duration": None}, lang, items)
            time.sleep(args.delay)
        return

    ap.print_help()


if __name__ == "__main__":
    main()
