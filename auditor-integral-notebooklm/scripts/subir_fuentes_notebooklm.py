# -*- coding: utf-8 -*-
"""Cargador GENERICO e idempotente de fuentes a un cuaderno de NotebookLM.

Generaliza `E:\\vars\\var 5\\Universidad-Abierta\\subir_aula_notebooklm.py`, que estaba
atado al manifiesto del Aula. Cambio esencial (11-oct-2026): invoca el CLI a traves
del envoltorio `war_room_tmp/nlm_dominio.py`, porque el `notebooklm.exe` sin parchear
aborta con «CSRF token not found» desde que NotebookLM se mudo a notebook.google.com.

Uso:
    python subir_fuentes_notebooklm.py --nb <notebook_id> <archivo_o_glob> [...]
    python subir_fuentes_notebooklm.py --nb f214f670-... "C:/ruta/*.pdf" --prefijo "[CIARCU] "
    python subir_fuentes_notebooklm.py --nb <id> ... --dry            # solo planificar

Garantias:
  * Idempotente: consulta `source list --json` y omite lo ya presente, indexando por
    titulo Y por nombre de archivo (`--title` se IGNORA al subir archivos: la fuente
    nace con el nombre del PDF, y hay que renombrarla despues).
  * Limpia la «fuente muerta»: si `source add` corta con AssertionError, queda una
    fuente en estado 5 «preparing» que nunca se procesa; se borra y se reintenta.
  * Tolera la salida sucia del CLI: `--json` viene con lineas «Matched:»/WARNING
    delante, asi que el objeto se extrae con `raw_decode`.
  * Registra todo en `<carpeta del primer archivo>/_subidas_nlm.json`.

Ver [[auditor-integral-notebooklm]] y [[reference_cuaderno_asesoria_ecualedger_fbse]].
"""
from __future__ import annotations
import argparse, glob, json, os, subprocess, sys, time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VENV_PY = Path.home() / ".notebooklm-venv" / "Scripts" / "python.exe"
ENVOLTORIO = Path.home() / "war_room_tmp" / "nlm_dominio.py"
EXE = Path.home() / ".notebooklm-venv" / "Scripts" / "notebooklm.exe"
PERFIL = "mobijuesa360@gmail.com"


def base_cmd() -> list[str]:
    """El envoltorio de dominio si existe; si no, el exe pelado (puede fallar)."""
    if VENV_PY.exists() and ENVOLTORIO.exists():
        return [str(VENV_PY), str(ENVOLTORIO), "--profile", PERFIL]
    return [str(EXE), "--profile", PERFIL]


def run(args: list[str], timeout: int = 600) -> tuple[int, str]:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        r = subprocess.run(base_cmd() + args, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout, env=env)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return 99, "TIMEOUT local del subprocess"


def parse_json(out: str):
    """Extrae el JSON de una salida sucia del CLI.

    14-nov-2026: la version anterior tomaba el PRIMER `{` o `[` de la salida. El CLI
    imprime `WARNING ... [req=abc123]` antes del JSON cuando reintenta un RPC, asi que
    ese `[` ganaba y `raw_decode` fallaba. El fallo NO se veia: `fuentes()` lo atrapaba,
    devolvia {} y **se perdia la idempotencia en silencio** — habria vuelto a subir una
    fuente ya presente, duplicandola. Ahora se prueban varios puntos de arranque y se
    exige que el resultado tenga forma de listado.
    """
    candidatos_json = []
    for marca in ("\n{", "\n["):          # el JSON del CLI empieza en su propia linea
        p = out.find(marca)
        while p >= 0:
            candidatos_json.append(p + 1)
            p = out.find(marca, p + 1)
    if out[:1] in ("{", "["):
        candidatos_json.insert(0, 0)
    for k in sorted(candidatos_json):
        try:
            d = json.JSONDecoder().raw_decode(out[k:])[0]
        except Exception:
            continue
        if isinstance(d, list) or (isinstance(d, dict) and "sources" in d):
            return d
    raise ValueError("sin JSON con forma de listado en la salida (%d candidatos probados)"
                     % len(candidatos_json))


def fuentes(nb: str) -> dict:
    rc, out = run(["source", "list", "-n", nb, "--json"])
    if rc != 0:
        print("  [aviso] no pude listar fuentes:", out[-220:].replace("\n", " "))
        return {}
    try:
        d = parse_json(out)
    except Exception as e:
        print("  [aviso] JSON de fuentes ilegible:", e)
        return {}
    lista = d.get("sources", d) if isinstance(d, dict) else d
    out_d = {}
    for s in lista or []:
        t = (s.get("title") or "").strip()
        if t:
            out_d[t] = s
    return out_d


def ids_vivos(ya: dict) -> set:
    """Los ids de fuente que de verdad estan en el cuaderno ahora mismo."""
    return {(v.get("id") or "") for v in ya.values() if v.get("id")}


def ya_por_registro(f: str, log: list, vivos: set):
    """Devuelve el id si este PDF ya esta subido y procesado, segun el registro.

    Sobrevive al renombrado de la fuente, que es lo que rompia la idempotencia por
    titulo: el registro guarda la RUTA del PDF, que no cambia cuando el titulo si.
    """
    objetivo = os.path.normcase(os.path.abspath(f))
    for e in reversed(log or []):
        if e.get("estado") != "listo" or not e.get("source_id"):
            continue
        arch = e.get("archivo") or ""
        if os.path.normcase(os.path.abspath(arch)) == objetivo and e["source_id"] in vivos:
            return e["source_id"]
    return None


def limpiar_muerta_por_nombre(nb: str, f: str) -> str:
    """Borra la fuente muerta que deja un `add` roto sin JSON (no hay id que usar).

    Se identifica por el nombre del archivo y por NO estar `ready`. La confirmacion
    es volver a listar: el `delete` de este CLI miente en las dos direcciones.
    """
    nombre, raiz = Path(f).name, Path(f).stem
    rc, out = run(["source", "list", "-n", nb, "--json"])
    if rc != 0:
        return "sin_limpiar(no_pude_listar)"
    try:
        d = parse_json(out)
    except Exception as e:
        return "sin_limpiar(%s)" % e
    lista = d.get("sources", d) if isinstance(d, dict) else d
    muertas = [x for x in (lista or [])
               if (x.get("status") or "").lower() != "ready"
               and (nombre in (x.get("title") or "") or raiz in (x.get("title") or ""))]
    if not muertas:
        return "sin_muerta"
    borradas = []
    for x in muertas:
        run(["source", "delete", x["id"], "-n", nb, "-y"])
        borradas.append(x["id"][:8])
    rc2, out2 = run(["source", "list", "-n", nb, "--json"])
    sigue = False
    if rc2 == 0:
        try:
            d2 = parse_json(out2)
            l2 = d2.get("sources", d2) if isinstance(d2, dict) else d2
            sigue = any(x.get("id") in [m["id"] for m in muertas] for x in (l2 or []))
        except Exception:
            sigue = True
    return ("NO_SE_BORRO:" if sigue else "limpiada:") + ",".join(borradas)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nb", required=True, help="id del cuaderno")
    ap.add_argument("patrones", nargs="+", help="archivos o globs")
    ap.add_argument("--prefijo", default="", help="prefijo para el titulo de la fuente")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--espera", type=int, default=300, help="segundos de source wait")
    a = ap.parse_args()

    archivos: list[str] = []
    for pat in a.patrones:
        if any(c in pat for c in "*?["):
            archivos.extend(sorted(glob.glob(pat)))
        elif os.path.isdir(pat):
            archivos.extend(sorted(glob.glob(os.path.join(pat, "*.pdf"))))
        else:
            archivos.append(pat)
    archivos = [f for f in archivos if os.path.isfile(f)]
    if not archivos:
        print("sin archivos que subir"); return 2

    print(f"CUADERNO : {a.nb}")
    print(f"ARCHIVOS : {len(archivos)}")
    for f in archivos:
        print(f"   {os.path.getsize(f)/1024:8.0f} KB  {os.path.basename(f)[:84]}")

    ya = fuentes(a.nb)
    vivos = ids_vivos(ya)
    print(f"\nfuentes ya presentes: {len(ya)}")

    log_path = Path(archivos[0]).parent / "_subidas_nlm.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else []

    if a.dry:
        for f in archivos:
            t = (a.prefijo + Path(f).stem)[:200]
            sid_reg = ya_por_registro(f, log, vivos)
            if sid_reg:
                print(f"   = ya esta (registro {sid_reg[:8]})  {t}")
            elif t in ya or Path(f).name in ya:
                print(f"   = ya esta (titulo)  {t}")
            else:
                print(f"   + subiria  {t}")
        return 0
    ok = omitidas = fallos = 0

    for f in archivos:
        titulo = (a.prefijo + Path(f).stem)[:200]
        nombre = Path(f).name
        sid_reg = ya_por_registro(f, log, vivos)
        if sid_reg:
            print(f"  = ya esta (registro {sid_reg[:8]}, aunque el titulo haya cambiado)")
            omitidas += 1
            continue
        if titulo in ya:
            print(f"  = ya esta          {titulo[:72]}"); omitidas += 1; continue
        if nombre in ya:
            sid_prev = ya[nombre].get("id")
            if sid_prev:
                run(["source", "rename", sid_prev, titulo, "-n", a.nb])
                print(f"  ~ renombrada       {titulo[:72]}")
            omitidas += 1
            continue

        t0 = time.time()
        rc, out = run(["source", "add", f, "-n", a.nb, "--type", "file",
                       "--timeout", str(a.espera), "--json"], timeout=a.espera + 600)
        sid = None
        try:
            d = parse_json(out)
            sid = d.get("source_id") or d.get("id") or (d.get("source") or {}).get("id")
        except Exception:
            pass

        estado = "add_ok" if rc == 0 else "add_error"
        if rc == 0 and sid:
            rc2, _ = run(["source", "wait", sid, "-n", a.nb,
                          "--timeout", str(a.espera), "--interval", "3"],
                         timeout=a.espera + 120)
            estado = {0: "listo", 1: "fallo_procesando", 2: "timeout"}.get(rc2, f"rc{rc2}")
            if estado == "listo":
                run(["source", "rename", sid, titulo, "-n", a.nb])
        elif rc != 0 and sid:
            # la subida rota deja una fuente muerta en estado 5: borrarla
            run(["source", "delete", sid, "-n", a.nb, "-y"])
            estado = "add_error_limpiado"
        elif rc != 0 and not sid:
            # 14-nov-2026: el `add` corto con AssertionError sin imprimir JSON, asi que
            # no hay id y la rama de arriba no se ejecutaba: la fuente muerta se quedaba
            # en «preparing». Se busca por nombre entre las que no estan `ready`.
            estado = "add_error_" + limpiar_muerta_por_nombre(a.nb, f)

        marca = "OK " if estado == "listo" else "FAL"
        extra = "" if rc == 0 else "   " + out[-160:].replace("\n", " ")
        print(f"  {marca} {estado:18s} {titulo[:62]}  ({time.time()-t0:.0f}s){extra}")
        if estado == "listo":
            ok += 1
        else:
            fallos += 1
        log.append({"titulo": titulo, "archivo": f, "source_id": sid,
                    "estado": estado, "salida": out[-400:]})
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")

    fin = fuentes(a.nb)
    print(f"\nRESUMEN: {ok} subidas · {omitidas} ya estaban · {fallos} fallidas")
    print(f"fuentes en el cuaderno al cierre: {len(fin)}")
    print(f"registro: {log_path}")
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
