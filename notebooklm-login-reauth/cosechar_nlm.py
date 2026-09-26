# -*- coding: utf-8 -*-
"""Cosecha el storage_state de NotebookLM desde los perfiles persistentes de Edge.
Escribe en profiles/default (que es el que lee el CLI) y en el perfil nombrado."""
import json, time, sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from playwright.sync_api import sync_playwright

CANDIDATOS = [
    Path.home() / ".notebooklm" / "profiles" / "mobijuesa360@gmail.com" / "browser_profile",
    Path.home() / ".notebooklm" / "browser_profile_edge",
    Path.home() / ".notebooklm-mobijuesa360@gmail.com" / "browser_profile",
]
DESTINOS = [
    Path.home() / ".notebooklm" / "profiles" / "default" / "storage_state.json",
    Path.home() / ".notebooklm" / "profiles" / "mobijuesa360@gmail.com" / "storage_state.json",
]

for perfil in CANDIDATOS:
    if not perfil.exists():
        print("(no existe) %s" % perfil.name); continue
    # soltar candado si quedó huérfano
    for lock in ("SingletonLock", "SingletonCookie", "SingletonSocket"):
        p = perfil / lock
        try:
            if p.exists() or p.is_symlink(): p.unlink()
        except Exception:
            pass
    try:
        with sync_playwright() as pw:
            ctx = pw.chromium.launch_persistent_context(
                str(perfil), channel="msedge", headless=True,
                args=["--disable-blink-features=AutomationControlled"])
            pg = ctx.pages[0] if ctx.pages else ctx.new_page()
            pg.goto("https://notebooklm.google.com/", wait_until="domcontentloaded", timeout=70000)
            time.sleep(9)
            url = pg.url
            vivo = not ("accounts.google.com" in url or "signin" in url.lower())
            st = ctx.storage_state()
            ncook = len(st.get("cookies", []))
            sid = any(c["name"] == "SID" for c in st.get("cookies", []))
            print("%-46s vivo=%-5s cookies=%-4d SID=%s  url=%s"
                  % (str(perfil)[-46:], vivo, ncook, sid, url[:58]))
            if vivo and sid:
                for d in DESTINOS:
                    d.parent.mkdir(parents=True, exist_ok=True)
                    d.write_text(json.dumps(st), encoding="utf-8")
                print("   -> ESCRITO en:", ", ".join(str(d.parent.name) for d in DESTINOS))
                ctx.close()
                raise SystemExit(0)
            ctx.close()
    except SystemExit:
        raise
    except Exception as e:
        print("%-46s ERROR %s" % (str(perfil)[-46:], str(e)[:110]))

print("NINGUNO VIVO")
raise SystemExit(2)
