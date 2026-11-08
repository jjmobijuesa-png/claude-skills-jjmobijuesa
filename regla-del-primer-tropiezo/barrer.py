# -*- coding: utf-8 -*-
"""
barrer.py — el barrido del inventario, automatizado (skill `regla-del-primer-tropiezo`).

Reemplaza los tres greps manuales del §3 por UN comando, y hace tres cosas que el
grep a mano no hacía y que costaron caro:

  1) EXPANDE EL SINTOMA A MECANISMOS (§4.1). «no encuentra el boton» se busca
     tambien como shadow dom / iframe / virtualizada / render diferido. El sintoma
     es local; el mecanismo transfiere.
  2) DEVUELVE EL FRAGMENTO UTIL, no la lista de archivos. El fallo tipico es
     obtener nombres y no leerlos. Aqui el texto viene en la salida.
  3) PRIORIZA las secciones «Como depurar si falla» y extrae COMANDOS Y RUTAS
     ejecutables cercanos a cada coincidencia: es lo que de verdad resuelve.

Uso:
    python barrer.py "notebooklm subir fuente"
    python barrer.py "401 sesion caducada" --todo          # sin recortar
    python barrer.py "selector vacio" --n 12               # mas archivos
    python barrer.py --mecanismos                          # ver la tabla

Salida: informe por consola, ordenado por puntaje. Pensado para leerse entero.
"""
from __future__ import annotations
import sys, os, re, argparse
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOME = Path(os.environ.get("USERPROFILE") or Path.home())
MEM = HOME / ".claude" / "projects" / "C--Users-datos-Downloads" / "memory"
SKILLS = HOME / ".claude" / "skills"
INDICE = MEM / "skills_index.md"
RED = MEM / "skills_network.md"
CONSTI = HOME / ".claude" / "CLAUDE.md"

# ── La tabla de mecanismos: el activo real de este script ─────────────────────
# sintoma (lo que se ve) -> mecanismos (lo que transfiere entre herramientas).
MECANISMOS: dict[str, list[str]] = {
    # sesiones, tokens, autenticacion
    r"auth|401|403|caduc|expir|sesion|session|login|token|cookie|credencial|csrf":
        ["storage_state", "perfil persistente", "cosechar", "reauth", "browser_profile",
         "profiles/default", "SingletonLock", "app-bound", "muro de autenticacion"],
    # automatizacion de navegador que no engancha
    r"selector|no encuentra|vacio|vacia|no aparece|click|clic|boton|button|dom|xpath|aria":
        ["shadow dom", "iframe", "virtualizada", "render diferido", "modal", "dialogo",
         "geometria", "coordenadas", "force=True", "query_selector", "cerrar modales"],
    # subidas y cargas
    r"subir|upload|cargar|adjunt|source add|fuente|file chooser|input":
        ["source add", "source wait", "source rename", "set_input_files", "expect_file_chooser",
         "idempotente", "carga masiva", "cargador", "deduplicar",
         # 12-oct-2026: el contenido del propio archivo puede romper la subida.
         "Data should not be empty", "fallo intermitente", "reintentar",
         "archivo de control", "discriminador"],
    # limites de transporte y volumen
    r"truncad|excedid|exceeded|limite|limit|bytes|too large|demasiado grande|timeout|cuelga|lento":
        ["tope", "cap", "MAX_RPC", "nlm_ask_big", "paginar", "chunk", "lote", "scroll",
         "stream", "headless", "spawn UNKNOWN"],
    # ofimatica por COM
    r"excel|word|access|xlsx|docx|formula|macro|vba|com":
        ["win32com", "DispatchEx", "CalculateFullRebuild", "ExportAsFixedFormat",
         "32-bit", "fuera de proceso", "A4", "centrar"],
    # lectura de documentos e imagenes
    r"pdf|escane|ocr|imagen|image|foto|frame|video|captura":
        ["rapidocr", "ffmpeg", "fotogramas", "media removed", "request limit",
         "page.pdf", "prefer_css_page_size"],
    # red y descargas
    r"descarg|download|fetch|http|url|dominio|redirig":
        ["edge-cdp", "webfetch", "canal msedge", "channel=\"msedge\"", "User-Agent", "CDP 9222"],
    # datos que se pierden o se pisan
    r"vacio|borr|piso|pisad|sobrescrib|perdid|cero resultados|0 resultados|congelad":
        ["candado antipisada", "snapshot", "creible", "LastTaskResult", "restaurar",
         "no sobrescribe"],
    # dinero, modelos, cifras que no cuadran
    r"cuadra|descuadr|van|tir|flujo|saldo|rojo|negativo|margen|cifra":
        ["dudar de los insumos", "referencia desplazada", "REF", "punto de equilibrio",
         "nunca en rojo", "aporte requerido", "capital recuperado", "costeo completo", "costo hundido",
         "balance cuadra por construcción"],
    # la misma cifra vale distinto en dos entregables (libro, PDF, lámina, gráfico)
    r"distint|no coincid|entregable|version|lamina|diapositiva|presentaci|pdf|mismo valor|mismos valores":
        ["fuente única", "fuente_v2.json", "cruce_v2", "gráfico nativo", "imagen insertada", "huella",
         "control-versiones-entregables", "vN (AAAA-MM-DD)"],
}

STOP = set("""de la el los las un una unos unas y o u que en al del con por para sin sobre
como cuando donde cual cuales es son esta estan ser fue fui no si se le lo me mi su sus
a ante bajo cabe contra desde entre hacia hasta segun tras the of and or to in on for with
it is are was be this that at by an""".split())

PESO = {"indice": 3.0, "red": 1.5, "memoria": 2.0, "skill": 2.0, "script": 1.6, "consti": 2.5}

RE_DEPURA = re.compile(r"c[oó]mo depurar|si falla|trampas|lo que no funciona|no reintentar|"
                       r"errores|problema|receta que funciona|candado", re.I)
RE_CMD = re.compile(r"^\s*(?:[\$>]\s*)?((?:python|py|notebooklm|npm|node|git|curl|grep|"
                    r"powershell|pwsh|Get-|Set-|&\s*\"|\"\$)[^\n]{4,200})")
RE_RUTA = re.compile(r"(?:[A-Za-z]:[\\/]|~[\\/]|\$HOME[\\/])[^\s\"'`,;:)\]]{6,160}"
                     r"\.(?:py|ps1|md|json|xlsx|exe|bat|csv|sql)")


def claves(texto: str) -> tuple[list[str], list[str]]:
    """Devuelve (literales, mecanismos) a partir del sintoma."""
    bruto = re.findall(r"[\wáéíóúüñ/_.\-]{3,}", texto.lower())
    lits = [t for t in bruto if t not in STOP]
    bajo = texto.lower()
    # Activar SOLO las familias con mas evidencia en el sintoma. Activarlas todas
    # diluye la senal: un sintoma con «html», «token» y «dominio» disparaba nueve
    # familias y 33 mecanismos, y entonces todo puntua y nada destaca.
    puntuadas = []
    for patron, lista in MECANISMOS.items():
        n = len(set(m.group(0) for m in re.finditer(patron, bajo)))
        if n:
            puntuadas.append((n, patron, lista))
    puntuadas.sort(key=lambda x: -x[0])
    mecs: list[str] = []
    for _, _, lista in puntuadas[:3]:
        mecs.extend(lista)
    # dedup conservando orden
    vistos, out = set(), []
    for m in mecs:
        k = m.lower()
        if k not in vistos:
            vistos.add(k); out.append(m)
    return lits, out


def archivos() -> list[tuple[Path, str]]:
    """(ruta, clase) de todo lo que compone el inventario."""
    out: list[tuple[Path, str]] = []
    if INDICE.exists(): out.append((INDICE, "indice"))
    if RED.exists(): out.append((RED, "red"))
    if CONSTI.exists(): out.append((CONSTI, "consti"))
    if MEM.is_dir():
        for p in sorted(MEM.glob("*.md")):
            if p not in (INDICE, RED):
                out.append((p, "memoria"))
    if SKILLS.is_dir():
        for p in sorted(SKILLS.rglob("*.md")):
            if "__pycache__" in p.parts or "_RnD" in p.parts:
                continue
            out.append((p, "skill"))
        for p in sorted(SKILLS.rglob("*.py")):
            if "__pycache__" in p.parts:
                continue
            out.append((p, "script"))
    return out


def leer(p: Path) -> list[str]:
    try:
        return p.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return []


def escanear(p: Path, clase: str, lits: list[str], mecs: list[str]):
    lineas = leer(p)
    if not lineas:
        return None
    lits_b = [t.lower() for t in lits]
    mecs_b = [m.lower() for m in mecs]
    golpes: list[tuple[int, float, str]] = []   # (nº linea, puntaje, texto)
    seccion = ""
    for i, ln in enumerate(lineas, 1):
        if ln.lstrip().startswith("#"):
            seccion = ln.strip("# ").strip()
        b = ln.lower()
        pl = sum(2.0 for t in lits_b if t in b)
        pm = sum(1.2 for m in mecs_b if m in b)
        if pl == 0 and pm == 0:
            continue
        pts = pl + pm
        if RE_DEPURA.search(seccion) or RE_DEPURA.search(b):
            pts *= 1.9                      # la solucion suele vivir aqui
        if RE_CMD.match(ln) or RE_RUTA.search(ln):
            pts *= 1.5                      # linea con comando o ruta ejecutable
        golpes.append((i, pts, ln.rstrip()))
    if not golpes:
        return None
    total = sum(g[1] for g in golpes) * PESO.get(clase, 1.0)
    # bonus por densidad: pocas lineas con mucho golpe valen mas que ruido disperso
    distintos = sum(1 for t in lits_b if any(t in g[2].lower() for g in golpes))
    total += distintos * 3.0
    return {"ruta": p, "clase": clase, "puntaje": total, "golpes": golpes,
            "n": len(lineas)}


def bloques(golpes, lineas_ctx: int, maximo: int):
    """Agrupa coincidencias cercanas para mostrar contexto legible."""
    top = sorted(golpes, key=lambda g: -g[1])[:maximo]
    nums = sorted({g[0] for g in top})
    grupos, actual = [], [nums[0]]
    for n in nums[1:]:
        if n - actual[-1] <= lineas_ctx * 2:
            actual.append(n)
        else:
            grupos.append(actual); actual = [n]
    grupos.append(actual)
    return grupos


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("sintoma", nargs="*", help="que fallo, en palabras llanas")
    ap.add_argument("--n", type=int, default=8, help="archivos a mostrar (def. 8)")
    ap.add_argument("--todo", action="store_true", help="no recortar los fragmentos")
    ap.add_argument("--mecanismos", action="store_true", help="imprimir la tabla y salir")
    a = ap.parse_args()

    if a.mecanismos:
        print("TABLA DE MECANISMOS (sintoma -> lo que transfiere)\n")
        for patron, lista in MECANISMOS.items():
            print(f"  [{patron}]\n      {', '.join(lista)}\n")
        return 0

    texto = " ".join(a.sintoma).strip()
    if not texto:
        ap.print_help(); return 2

    lits, mecs = claves(texto)
    print("=" * 78)
    print(f"BARRIDO DEL INVENTARIO  —  «{texto}»")
    print("=" * 78)
    print(f"literales : {', '.join(lits) or '(ninguno)'}")
    print(f"mecanismos: {', '.join(mecs) if mecs else '(ningun patron reconocido — §4.1 a mano)'}")

    fichas = []
    for p, clase in archivos():
        f = escanear(p, clase, lits, mecs)
        if f:
            fichas.append(f)
    fichas.sort(key=lambda f: -f["puntaje"])

    if not fichas:
        print("\nSIN COINCIDENCIAS. El inventario no cubre el caso: improvisar esta")
        print("permitido, y queda abierto el deber del §3 paso 6 (codificar lo aprendido).")
        return 1

    print(f"\n{len(fichas)} archivos con coincidencias. Los {min(a.n, len(fichas))} mejores:\n")
    ctx = 2 if not a.todo else 4
    maximo = 6 if not a.todo else 24
    cmds: list[str] = []
    rutas: list[str] = []

    for f in fichas[: a.n]:
        p = f["ruta"]
        try:
            rel = p.relative_to(HOME)
            etiqueta = f"~/{rel.as_posix()}"
        except ValueError:
            etiqueta = str(p)
        print("-" * 78)
        print(f"[{f['clase'].upper():7s}] {etiqueta}   (puntaje {f['puntaje']:.0f})")
        lineas = leer(p)
        for grupo in bloques(f["golpes"], ctx, maximo):
            ini, fin = max(1, grupo[0] - ctx), min(len(lineas), grupo[-1] + ctx)
            print(f"    ··· lineas {ini}-{fin} ···")
            for n in range(ini, fin + 1):
                ln = lineas[n - 1].rstrip()
                marca = ">" if n in grupo else " "
                print(f"   {marca}{n:5d}| {ln[:150]}")
                m = RE_CMD.match(ln)
                if m: cmds.append(m.group(1).strip())
                for r in RE_RUTA.findall(ln): rutas.append(r)

    def unicos(xs):
        v, o = set(), []
        for x in xs:
            if x not in v:
                v.add(x); o.append(x)
        return o

    cmds, rutas = unicos(cmds)[:14], unicos(rutas)[:14]
    if cmds:
        print("\n" + "=" * 78)
        print("COMANDOS DETECTADOS (verificar antes de ejecutar)")
        for c in cmds: print(f"  $ {c[:150]}")
    if rutas:
        print("\n" + "=" * 78)
        print("RUTAS DE SCRIPTS Y ARTEFACTOS")
        for r in rutas: print(f"  {r}")

    print("\n" + "=" * 78)
    print("SIGUIENTE PASO OBLIGATORIO (§3 paso 4): leer ENTERO el archivo mejor")
    print("puntuado antes de actuar. Los fragmentos de arriba no sustituyen la")
    print("lectura completa — ese fue el fallo fundacional del 9-sep-2026.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
