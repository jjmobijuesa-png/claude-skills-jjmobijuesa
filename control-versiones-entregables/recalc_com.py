import win32com.client as w, os, sys
src=os.path.abspath(sys.argv[1]); dst=os.path.abspath(sys.argv[2])
xl=w.DispatchEx("Excel.Application"); xl.Visible=False; xl.DisplayAlerts=False
try:
    wb=xl.Workbooks.Open(src); xl.CalculateFull()
    for n,c in (("PyG","B14"),("PyG","B18"),("BALANCE GENERAL","B17"),("INDICADORES Y DECISIÓN","B14"),("INDICADORES Y DECISIÓN","B15"),("INDICADORES Y DECISIÓN","B26"),("RESUMEN FINANCIERO","G12")):
        print(n,c,wb.Worksheets(n).Range(c).Value)
    errs=0
    for ws in wb.Worksheets:
        ur=ws.UsedRange
        for cell in ur:
            v=cell.Text
            if isinstance(v,str) and v.startswith("#") and v.strip("#")!="": errs+=1; print("ERR",ws.Name,cell.Address,v) if errs<15 else None
    print("errores:",errs)
    wb.SaveAs(dst,51); wb.Close(False)
finally:
    xl.Quit()

