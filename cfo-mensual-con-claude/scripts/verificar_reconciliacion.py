# -*- coding: utf-8 -*-
import re, glob, os
from pypdf import PdfReader
DEST=r"E:\vars\var 11-11 Finanza Integral\10 Documentos de Respaldo\Estados de Cuenta\Produbanco 2026"
LINE=re.compile(r'^([A-ZÁÉÍÓÚÑ]{3,})\s+([A-Za-z]{3})\s+(\d{1,2})\s+(\d{4})\s+(\S+)\s+(.+?)\s+([\d.,]+)([+-])\s+([\d.,]+)\s+([\d.,]+)\s*$')
num=lambda s: float(s.replace(',',''))
for pdf in sorted(glob.glob(os.path.join(DEST,'Estado_Produbanco_2026-*.pdf'))):
    rd=PdfReader(pdf); txt=''
    for pg in rd.pages: txt+=(pg.extract_text() or '')+'\n'
    si=re.search(r'Saldo Inicial Contable:\s*([\d.,]+)',txt)
    sf=re.search(r'Saldo Final Contable:\s*([\d.,]+)',txt)
    si=num(si.group(1)) if si else None; sf=num(sf.group(1)) if sf else None
    n=0; deb=0.0; cre=0.0
    for ln in txt.splitlines():
        m=LINE.match(ln.strip())
        if not m: continue
        _,mon,day,yr,_,desc,val,sign,_,_=m.groups()
        a=num(val);
        if sign=='-':deb+=a
        else:cre+=a
        n+=1
    net=cre-deb
    exp=(sf-si) if (si is not None and sf is not None) else None
    okmark = 'OK' if (exp is not None and abs(net-exp)<0.05) else 'DESCUADRE'
    print(f'{os.path.basename(pdf)[:28]:28} | movs={n:3d} | deb={deb:8.2f} cre={cre:8.2f} net={net:8.2f} | SI={si} SF={sf} esperado={exp} -> {okmark}')
