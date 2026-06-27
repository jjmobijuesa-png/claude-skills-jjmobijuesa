# -*- coding: utf-8 -*-
"""
Lista todas las playlists del canal de YouTube de jjmobijuesa@gmail.com
usando yt-dlp con cookies extraídas del perfil Edge logueado.

Salida:
  E:\\vars\\var 5\\YouTube-jjmobijuesa\\playlists_index.json
  E:\\vars\\var 5\\YouTube-jjmobijuesa\\playlists_index.md

Uso:
  python listar_playlists.py
  python listar_playlists.py --browser edge --refresh
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import yt_dlp

OUT_DIR = Path(r"E:\vars\var 5\YouTube-jjmobijuesa")
OUT_DIR.mkdir(parents=True, exist_ok=True)

JSON_PATH = OUT_DIR / "playlists_index.json"
MD_PATH = OUT_DIR / "playlists_index.md"


def list_user_playlists(cookies_browser=None, cookies_file=None):
    """Lista playlists del usuario logueado. Acepta cookies de browser
    (puede fallar si Edge está corriendo) o archivo Netscape generado
    por harvest_cookies.py (recomendado)."""
    url = "https://www.youtube.com/feed/playlists"
    opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
        "playlistend": 200,
        "ignoreerrors": True,
    }
    if cookies_file:
        opts["cookiefile"] = str(cookies_file)
    elif cookies_browser:
        opts["cookiesfrombrowser"] = (cookies_browser, None, None, None)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser", default=None,
                    help="Navegador del que leer cookies (edge/chrome/firefox). NO usar si Edge está corriendo.")
    ap.add_argument("--cookies-file", default=r"E:\vars\var 5\YouTube-jjmobijuesa\cookies.txt",
                    help="Archivo Netscape generado por harvest_cookies.py (recomendado)")
    args = ap.parse_args()

    cookies_file = args.cookies_file if Path(args.cookies_file).exists() else None
    if cookies_file:
        print(f"Listando playlists con cookies-file: {cookies_file}")
    elif args.browser:
        print(f"Listando playlists con cookies de {args.browser}...")
    else:
        print("AVISO: sin cookies — sólo verá playlists públicas")
    try:
        info = list_user_playlists(args.browser, cookies_file)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(2)

    # Normalizar estructura: info['entries'] suele tener playlists
    entries = info.get("entries", []) if isinstance(info, dict) else []
    playlists = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        # En /feed/playlists cada entry es _type='url' con URL de playlist
        url_ = e.get("url") or ""
        if "playlist?list=" in url_ or e.get("_type") == "playlist":
            playlists.append({
                "id": e.get("id"),
                "title": e.get("title") or e.get("playlist_title"),
                "url": url_,
                "n_videos": e.get("playlist_count") or e.get("n_entries"),
                "uploader": e.get("uploader"),
                "channel": e.get("channel"),
                "raw_type": e.get("_type"),
            })

    out = {
        "extracted_at": datetime.now().isoformat(),
        "browser_cookies": args.browser,
        "playlists_count": len(playlists),
        "playlists": playlists,
        "raw_top_level": {k: info.get(k) for k in ("id", "title", "uploader", "channel") if isinstance(info, dict)},
    }
    JSON_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"JSON: {JSON_PATH}")

    md = [f"# Playlists de jjmobijuesa@gmail.com\n",
          f"_Extraído {datetime.now().strftime('%Y-%m-%d %H:%M')} con cookies de {args.browser}._\n",
          f"Total playlists: **{len(playlists)}**\n",
          "| # | Título | Videos | URL |",
          "|---|--------|-------:|-----|"]
    for i, p in enumerate(playlists, 1):
        md.append(f"| {i} | {p.get('title') or '(sin título)'} | {p.get('n_videos') or '?'} | {p.get('url') or ''} |")
    MD_PATH.write_text("\n".join(md), encoding="utf-8")
    print(f"Markdown: {MD_PATH}")
    print(f"Playlists detectadas: {len(playlists)}")


if __name__ == "__main__":
    main()
