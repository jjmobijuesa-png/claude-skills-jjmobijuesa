# -*- coding: utf-8 -*-
"""Compuerta de arranque para cualquier automatizacion por CDP sobre Edge.

POR QUE EXISTE (8-nov-2026)
---------------------------
Desde Chromium 136 el indicador `--remote-debugging-port` **se ignora en
silencio** cuando Edge usa el perfil por defecto. Esta casa tuvo la cosecha de
guardados de LinkedIn congelada 132 dias informando exito, porque el indicador
estaba en la linea de ordenes y el puerto no existia. La comprobacion valida no
es el indicador: es **el puerto a la escucha y respondiendo CDP**.

QUE HACE
--------
1. Comprueba que algo escucha en el puerto Y que responde `/json/version`
   (un puerto abierto por otra cosa no sirve).
2. Si no responde, mira si Edge ya esta corriendo con ESE perfil:
   - Si lo esta, NO lo mata y NO relanza: avisa y sale con 5. Matar Edge se
     llevaria por delante las sesiones del usuario (WhatsApp, LinkedIn).
   - Si no lo esta, lanza Edge minimizado con el perfil dedicado y espera.
3. Vuelve a comprobar. Sale 0 solo si el puerto responde CDP de verdad.

CODIGOS DE SALIDA
-----------------
  0  puerto a la escucha y respondiendo CDP
  4  no se pudo levantar el puerto (lanzamos Edge y no respondio)
  5  Edge esta abierto con el perfil dedicado PERO sin el puerto: cerrarlo

USO
---
  python preflight_cdp.py                      # puerto 9222, perfil por defecto de la casa
  python preflight_cdp.py --puerto 9223 --perfil "C:\\Users\\datos\\.telegram-fdc"
  python preflight_cdp.py --no-lanzar          # solo comprobar, nunca lanzar
"""
import argparse
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PERFIL_CASA = r"C:\Users\datos\browser_profile_edge"


def responde_cdp(puerto, timeout=2.0):
    """True solo si el puerto escucha Y habla CDP. Devuelve (ok, detalle)."""
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect(("127.0.0.1", puerto))
    except Exception as e:
        return False, u"nada escucha en %d (%s)" % (puerto, type(e).__name__)
    finally:
        try:
            s.close()
        except Exception:
            pass
    try:
        with urllib.request.urlopen("http://127.0.0.1:%d/json/version" % puerto,
                                    timeout=timeout) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
        return True, d.get("Browser", "?")
    except Exception as e:
        return False, u"el %d escucha pero NO habla CDP (%s)" % (puerto, type(e).__name__)


def edge_usando_perfil(perfil):
    """PIDs de msedge que ya usan ese --user-data-dir (sin PowerShell: wmic cayo,
    asi que se usa CIM via powershell -NoProfile, y si falla se devuelve None
    = 'no lo se', que NO es lo mismo que 'no hay ninguno')."""
    ps = (
        "Get-CimInstance Win32_Process -Filter \"Name='msedge.exe'\" | "
        "Where-Object { $_.CommandLine -like '*user-data-dir*' -and "
        "$_.CommandLine -like '*%s*' } | ForEach-Object { $_.ProcessId }"
        % os.path.basename(perfil)
    )
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60)
        if r.returncode != 0:
            return None
        return [int(x) for x in r.stdout.split() if x.strip().isdigit()]
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puerto", type=int, default=9222)
    ap.add_argument("--perfil", default=PERFIL_CASA)
    ap.add_argument("--espera", type=int, default=35, help="segundos a esperar tras lanzar")
    ap.add_argument("--no-lanzar", action="store_true", help="solo comprobar")
    a = ap.parse_args()

    ok, det = responde_cdp(a.puerto)
    if ok:
        print(u"PREFLIGHT OK  puerto %d responde CDP  (%s)" % (a.puerto, det))
        return 0

    print(u"PREFLIGHT  %s" % det)
    if a.no_lanzar:
        print(u"PREFLIGHT FALLO  (--no-lanzar): no se intenta levantar Edge.")
        return 4

    pids = edge_usando_perfil(a.perfil)
    if pids:
        print(u"PREFLIGHT FALLO  Edge YA esta abierto con el perfil dedicado "
              u"(pid %s) pero SIN el puerto %d."
              % (", ".join(str(p) for p in pids), a.puerto))
        print(u"   No se mata Edge: se llevaria las sesiones del usuario.")
        print(u"   Cierre esa ventana y vuelva a abrirla con:")
        print(u"   \"%s\" --remote-debugging-port=%d --user-data-dir=\"%s\""
              % (EDGE, a.puerto, a.perfil))
        return 5
    if pids is None:
        print(u"   aviso: no pude saber si Edge usa ese perfil; intento lanzar igual.")

    if not os.path.isfile(EDGE):
        print(u"PREFLIGHT FALLO  no encuentro msedge.exe en %s" % EDGE)
        return 4

    print(u"PREFLIGHT  lanzando Edge minimizado con el perfil dedicado...")
    # Sin shell=True: la ventana se minimiza por STARTUPINFO, que ademas NO roba
    # el foco (SW_SHOWMINNOACTIVE). A las 9:15 de la manana eso importa.
    SW_SHOWMINNOACTIVE = 7
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = SW_SHOWMINNOACTIVE
    subprocess.Popen(
        [EDGE,
         "--remote-debugging-port=%d" % a.puerto,
         "--user-data-dir=%s" % a.perfil,
         "--no-first-run",
         "--no-default-browser-check",
         "about:blank"],
        startupinfo=si,
        close_fds=True,
    )

    t0 = time.time()
    while time.time() - t0 < a.espera:
        time.sleep(2)
        ok, det = responde_cdp(a.puerto)
        if ok:
            print(u"PREFLIGHT OK  puerto %d responde CDP tras %.0fs  (%s)"
                  % (a.puerto, time.time() - t0, det))
            return 0
    print(u"PREFLIGHT FALLO  lance Edge y el puerto %d sigue sin responder tras %ds -> %s"
          % (a.puerto, a.espera, det))
    return 4


if __name__ == "__main__":
    sys.exit(main())
