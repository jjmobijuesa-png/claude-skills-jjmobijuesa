# -*- coding: utf-8 -*-
"""
Auditor estático LOCAL de skills antes de instalarlas.

Inspirado en SkillSpector (NVIDIA, open-source). Una skill es CÓDIGO
EJECUTABLE que corre con TU mismo acceso: puede leer tus variables de
entorno, tus API keys, tus cookies, y enviarlas a un servidor. Antes de
copiar una skill de GitHub a ~/.claude/skills/, se AUDITA.

Uso:
    python auditar_skill.py "<ruta a skill: carpeta, archivo, o .zip>"

Salida: hallazgos por categoría + puntaje de riesgo 0-100 + veredicto:
    SEGURO (0-19) · PRECAUCIÓN (20-59) · NO INSTALAR (60-100)

NO ejecuta el código auditado. Solo lo lee. Complementa (no reemplaza)
a SkillSpector y a la revisión humana.
"""
import sys, re, zipfile, tempfile, shutil
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# (categoría, peso, regex, descripción)
RULES = [
    ("credenciales", 18, r"os\.environ|getenv|process\.env|%[A-Z_]+%|\$env:", "lee variables de entorno (posibles API keys)"),
    ("credenciales", 22, r"\.aws/credentials|\.ssh/|id_rsa|cookies\.txt|storage_state|\.netrc|credentials\.json", "accede a archivos de credenciales conocidos"),
    ("exfiltracion", 20, r"requests\.(post|put)|urllib\.request|httpx\.|fetch\(|XMLHttpRequest|socket\.socket|net\.connect", "hace llamadas de red salientes"),
    ("exfiltracion", 15, r"curl\s+-|Invoke-WebRequest|Invoke-RestMethod|wget\s+http", "descarga/sube datos por shell"),
    ("ejecucion", 20, r"\beval\(|\bexec\(|subprocess\.(call|run|Popen)|os\.system|child_process|Runtime\.exec", "ejecuta código o comandos del sistema"),
    ("destructivo", 25, r"rm\s+-rf|Remove-Item.*-Recurse|shutil\.rmtree|format\s|del\s+/[sf]|rd\s+/s", "operaciones de borrado destructivo"),
    ("ofuscacion", 18, r"base64\.b64decode|atob\(|FromBase64String|\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}", "cadenas ofuscadas / base64 ejecutable"),
    ("persistencia", 15, r"schtasks|crontab|New-ScheduledTask|Startup\\|Run\\.*reg add|LaunchAgents", "instala persistencia / autoarranque"),
    ("red-dura", 22, r"https?://(?!github\.com|raw\.githubusercontent|pypi\.org|nvidia|anthropic|microsoft)[a-z0-9.-]+", "URL a host externo no reconocido"),
]

TEXT_EXT = {".py",".js",".ts",".sh",".bat",".cmd",".ps1",".mjs",".cjs",".json",".yml",".yaml",".md",".txt",".rb",".go",".pl"}

def scan_text(path, rel):
    findings = []
    try:
        txt = Path(path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return findings
    for cat, weight, pat, desc in RULES:
        for m in re.finditer(pat, txt, re.I):
            line = txt.count("\n", 0, m.start()) + 1
            snippet = txt.splitlines()[line-1].strip()[:100] if line-1 < len(txt.splitlines()) else ""
            findings.append((cat, weight, desc, rel, line, snippet))
    return findings

def audit(target):
    target = Path(target)
    tmp = None
    if target.suffix.lower() == ".zip":
        tmp = Path(tempfile.mkdtemp())
        with zipfile.ZipFile(target) as z: z.extractall(tmp)
        root = tmp
    elif target.is_file():
        root = target.parent
        files = [target]
    else:
        root = target
    if target.is_dir() or tmp:
        files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_EXT]

    all_f = []
    for f in files:
        rel = str(f.relative_to(root)) if (root in f.parents or root == f.parent) else f.name
        all_f += scan_text(f, rel)

    # puntaje: suma de pesos únicos por (categoria) con tope
    by_cat = {}
    for cat, w, desc, rel, ln, sn in all_f:
        by_cat.setdefault(cat, 0)
        by_cat[cat] = min(by_cat[cat] + w, 40)  # tope por categoría
    score = min(sum(by_cat.values()), 100)

    print(f"=== Auditoría estática de: {target.name} ===")
    print(f"Archivos de código revisados: {len(files)}\n")
    if not all_f:
        print("  Sin patrones de riesgo detectados por reglas estáticas.")
    else:
        cats = {}
        for cat, w, desc, rel, ln, sn in all_f:
            cats.setdefault((cat, desc), []).append(f"{rel}:{ln}  {sn}")
        for (cat, desc), hits in sorted(cats.items(), key=lambda x: -len(x[1])):
            print(f"  [{cat.upper()}] {desc}  ({len(hits)} coincidencia/s)")
            for h in hits[:4]:
                print(f"       - {h}")
    verd = "SEGURO" if score < 20 else ("PRECAUCION" if score < 60 else "NO INSTALAR")
    print(f"\nPUNTAJE DE RIESGO: {score}/100  ->  VEREDICTO: {verd}")
    print("Recuerda: esto es un filtro estático. Para código con red/credenciales,")
    print("leer el archivo completo o pasar SkillSpector antes de instalar.")
    if tmp: shutil.rmtree(tmp, ignore_errors=True)
    return score, verd

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    audit(sys.argv[1])
