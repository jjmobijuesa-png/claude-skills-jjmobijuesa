# -*- coding: utf-8 -*-
"""
Entiende un video de Facebook (o YouTube/otros) descargando su audio con yt-dlp,
pasandolo a WAV con ffmpeg y transcribiendolo localmente con faster_whisper.
Guarda metadatos (titulo, autor, duracion, descripcion) + transcripcion en un .md.

Los videos PUBLICOS de Facebook (share/v/<id>) NO requieren login. Para privados,
pasar --cookies edge (requiere el Edge del usuario CERRADO: Chromium bloquea la BD
de cookies mientras corre; ver SKILL.md).

Uso:
  python entender_video_facebook.py "<url>" [carpeta_salida] [--seconds N] [--model small]
  --seconds N : transcribe solo los primeros N segundos (0 = todo, por defecto).
  --model     : tiny|base|small|medium (base=rapido; small=mejor calidad ES).
  --cookies edge : usa cookies del Edge para videos privados (Edge cerrado).
Verificado 2026-10-03: FB publico, base, 90s -> 10s de transcripcion.
"""
import os, sys, subprocess, tempfile, time
sys.stdout.reconfigure(encoding="utf-8")
PY = sys.executable

def run(cmd, timeout=600):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout)

def main():
    args = list(sys.argv[1:])
    if not args:
        print("uso: entender_video_facebook.py <url> [salida] [--seconds N] [--model small]"); return 1
    url = args[0]
    outdir = args[1] if len(args) > 1 and not args[1].startswith("--") else r"C:\Users\datos\Downloads\Videos-Facebook"
    seconds = 0; model_name = "small"; cookies = None
    for i, a in enumerate(args):
        if a == "--seconds": seconds = int(args[i+1])
        if a == "--model": model_name = args[i+1]
        if a == "--cookies": cookies = args[i+1]
    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="fbvid_")
    base = [PY, "-m", "yt_dlp", "--no-warnings"]
    if cookies: base += ["--cookies-from-browser", cookies]

    meta = run(base + ["--skip-download", "--print",
               "%(id)s\t%(title)s\t%(duration)s\t%(uploader)s\t%(description)s", url], 120)
    line = (meta.stdout or "").strip().split("\t")
    vid = line[0] if len(line) > 0 else "video"
    title = line[1] if len(line) > 1 else ""
    dur = line[2] if len(line) > 2 else ""
    uploader = line[3] if len(line) > 3 else ""
    descr = line[4] if len(line) > 4 else ""
    print(f"META id={vid} dur={dur}s autor={uploader}\n  titulo={title[:80]}")

    audio = os.path.join(tmp, "a.%(ext)s")
    dl = run(base + ["-f", "bestaudio/best", "-o", audio, url], 300)
    got = [f for f in os.listdir(tmp) if f.startswith("a.")]
    if not got:
        print("FALLO descarga audio:\n", dl.stderr[-900:]); return 2
    apath = os.path.join(tmp, got[0])

    wav = os.path.join(tmp, "a.wav")
    ff = ["ffmpeg", "-y", "-i", apath, "-ac", "1", "-ar", "16000"]
    if seconds > 0: ff += ["-t", str(seconds)]
    run(ff + [wav], 300)

    from faster_whisper import WhisperModel
    t0 = time.time()
    m = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, info = m.transcribe(wav, language="es", beam_size=1, vad_filter=True)
    text = " ".join(s.text.strip() for s in segments).strip()
    print(f"TRANSCRITO {len(text)} chars en {time.time()-t0:.0f}s (modelo {model_name})")

    safe = "".join(c for c in (title or vid)[:50] if c.isalnum() or c in " -_").strip() or vid
    fn = os.path.join(outdir, f"{time.strftime('%Y-%m-%d')}_{vid}_{safe}.md")
    with open(fn, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n- URL: {url}\n- Autor: {uploader} | Duracion: {dur}s | id: {vid}\n")
        f.write(f"- Transcripcion: {'primeros '+str(seconds)+'s' if seconds else 'completa'} (faster_whisper {model_name})\n\n")
        f.write("## Descripcion / caption\n\n" + (descr or "(sin texto)") + "\n\n## Transcripcion\n\n" + text + "\n")
    print("GUARDADO ->", fn)
    print("\n----- MUESTRA -----\n" + text[:800])
    return 0

if __name__ == "__main__":
    sys.exit(main())
