# -*- coding: utf-8 -*-
"""Descarga los PDF adjuntos de los estados de cuenta Produbanco (fedphd)."""
import sys, re, time
from pathlib import Path
from playwright.sync_api import sync_playwright

DEST = Path(r"E:\vars\var 11-11 Finanza Integral\10 Documentos de Respaldo\Estados de Cuenta\Produbanco 2026")
DEST.mkdir(parents=True, exist_ok=True)
# TIDs de estados de cuenta (Grupo Promerica) + notificacion envio
TIDS = ['19f28e5e23caa0fc','19e86165d9250daf','19deb5b790a2783f','19d6b5b5cd45445b',
        '19cb5513099afe73','19c24cf7971e3d6a','19b8bb3fd0a0c67e','19ae2efd531a06c7',
        '19f595e99b2e012e']
prof = Path.home() / ".notebooklm" / "browser_profile_fedphd"

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=str(prof), channel="msedge", headless=True,
        accept_downloads=True, args=["--disable-blink-features=AutomationControlled"])
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(45000)
    page.goto("https://mail.google.com/mail/u/0/#inbox", wait_until="load")
    page.wait_for_timeout(4000)
    ok=0
    for i,tid in enumerate(TIDS,1):
        try:
            page.evaluate(f"() => {{ window.location.hash = 'inbox/{tid}'; }}")
            page.wait_for_timeout(4500)
            # emision (para nombrar)
            emis = page.evaluate(r"""() => {
                const b=(document.querySelector('.a3s')||{}).innerText||'';
                const m=b.match(/(\d{4})\s*\/\s*(\d{2})\s*\/\s*(\d{2})/);
                return m ? (m[1]+'-'+m[2]+'-'+m[3]) : '';
            }""")
            href = page.evaluate(r"""() => {
                const a=document.querySelector('a[href*="view=att"]');
                return a? a.href : null;
            }""")
            if not href:
                print(f"[{i}] {tid}: sin adjunto"); continue
            dl = href
            if 'disp=' in dl: dl = re.sub(r'disp=[^&]*','disp=attd',dl)
            else: dl = dl + '&disp=attd'
            name = f"Estado_Produbanco_{emis or ('tid_'+tid[:8])}.pdf"
            with page.expect_download(timeout=45000) as di:
                page.evaluate("""(u)=>{const a=document.createElement('a');a.href=u;a.target='_self';
                    document.body.appendChild(a);a.click();a.remove();}""", dl)
            d=di.value
            dest=DEST/name
            # evitar sobrescribir mismos meses distintos hilos
            k=1
            while dest.exists(): dest=DEST/f"Estado_Produbanco_{emis or tid[:8]}_{k}.pdf"; k+=1
            d.save_as(str(dest))
            print(f"[{i}] {tid}: emision {emis or '?'} -> {dest.name}")
            ok+=1
        except Exception as e:
            print(f"[{i}] {tid}: ERROR {str(e)[:90]}")
    print("DESCARGADOS:", ok)
    ctx.close()
