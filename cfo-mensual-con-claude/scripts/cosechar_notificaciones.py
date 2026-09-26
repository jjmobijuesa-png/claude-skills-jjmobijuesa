# -*- coding: utf-8 -*-
"""Cosecha notificaciones transaccionales Produbanco 2026 de fedphd -> JSON."""
import re, json, time
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(r"C:\Users\datos\AppData\Local\Temp\claude\C--Users-datos-Downloads\1e5f7d2c-d01a-49ef-b9a4-96feafbbf03a\scratchpad\notif_produbanco.json")
prof = Path.home()/".notebooklm"/"browser_profile_fedphd"

# tipos de notificacion que nos interesan (por asunto)
INTERES = re.compile(r'(Consumo tarjeta|Transferencia (enviada|Recibida|Ingresada|Acreditada)|Dep[oó]sito|Retiro de Efectivo|Pago de servicio|Pago Facturas|Pago Tel)', re.I)

with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir=str(prof),channel="msedge",headless=True,
        accept_downloads=False,args=["--disable-blink-features=AutomationControlled"])
    page=ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(40000)
    page.goto("https://mail.google.com/mail/u/0/#search/produbanco",wait_until="load")
    page.wait_for_timeout(4000)
    # recolectar TIDs+subject+date de varias paginas
    seen={}
    for pg in range(0,8):
        if pg>0:
            page.goto(f"https://mail.google.com/mail/u/0/#search/produbanco/p{pg+1}",wait_until="load")
            page.wait_for_timeout(3500)
        rows=page.evaluate(r"""()=>{
            const out=[];
            document.querySelectorAll('tr.zA').forEach(tr=>{
                const idEl=tr.querySelector('[data-legacy-thread-id]');
                const tid=idEl?idEl.getAttribute('data-legacy-thread-id'):'';
                const s=(tr.querySelector('.bog')||{}).innerText||'';
                const d=(tr.querySelector('.xW span, .xY span')||{});
                const date=d.getAttribute?(d.getAttribute('title')||d.innerText||''):'';
                if(tid) out.push({tid,subj:s,date});
            });
            return out;
        }""")
        new=0
        for r in rows:
            if r['tid'] not in seen:
                seen[r['tid']]=r; new+=1
        if new==0 and pg>0:
            break
    # filtrar por interes
    targets=[(t,v) for t,v in seen.items() if INTERES.search(v['subj'] or '')]
    print("Total hilos produbanco:",len(seen)," | notif transaccionales:",len(targets))

    data=[]
    for i,(tid,meta) in enumerate(targets,1):
        try:
            page.evaluate(f"()=>{{window.location.hash='inbox/{tid}';}}"); page.wait_for_timeout(2600)
            body=page.evaluate(r"""()=>{
                const b=(document.querySelector('.a3s')||{}).innerText||'';
                return b.replace(/\r/g,'');
            }""")
            def g(pat):
                m=re.search(pat, body, re.I); return m.group(1).strip() if m else ''
            rec={
                'tid':tid,'subj':meta['subj'],
                'fecha': g(r'Fecha y Hora:\s*([0-9]{1,2}/[A-Za-zé]+/[0-9]{4})'),
                'valor': g(r'(?:Valor|Monto):\s*(?:USD|\$)?\s*([\d.,]+)'),
                'establecimiento': g(r'Establecimiento:\s*(.+)'),
                'contacto': g(r'Contacto:\s*(.+)'),
                'banco_destino': g(r'Banco Destino:\s*(.+)'),
                'descripcion': g(r'Descripci[oó]n:\s*(.+)'),
                'deposito': g(r'dep[oó]sito de USD\s*([\d.,]+)'),
                'canal': g(r'Canal:\s*(.+)'),
            }
            data.append(rec)
            if i%20==0: print(f"  procesados {i}/{len(targets)}")
        except Exception as e:
            print("  err",tid,str(e)[:60])
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=1),encoding='utf-8')
    print("GUARDADO",OUT,"con",len(data),"notificaciones")
    ctx.close()
