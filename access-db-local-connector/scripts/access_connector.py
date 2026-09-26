# -*- coding: utf-8 -*-
"""
Conector local a Microsoft Access (.accdb/.mdb) para Python 64-bit + Office 32-bit.
Mecanismo: automatiza Access.Application por COM FUERA DE PROCESO (cruza el bit-gap
que bloquea a pyodbc/ADODB in-process). Requiere: Access instalado + pywin32.

API:
  with AccessDB(ruta, create=False, visible=False) as db:
      db.list_tables()            -> [str]
      db.list_queries()           -> [str]
      db.execute(sql)             -> None  (DDL/DML: CREATE/INSERT/UPDATE/DELETE)
      db.query(sql)               -> pandas.DataFrame  (SELECT arbitrario, vía DAO)
      db.table(nombre)            -> pandas.DataFrame  (SELECT * FROM [nombre])
      db.to_excel(objeto, xlsx)   -> exporta tabla/consulta a XLSX (a prueba de locale)
      db.to_csv(objeto, csv)      -> exporta a CSV vía pandas (locale-safe)

Verificado 2026-09-25 en esta máquina (Python 3.12 x64 + Office 2019 x86).
"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
import datetime
import pythoncom
import pywintypes
import win32com.client as win32
import pandas as pd

def _clean(v):
    # COM devuelve fechas como pywintypes.TimeType con tz que rompe a pandas -> a datetime nativo
    if isinstance(v, pywintypes.TimeType):
        return datetime.datetime(v.year, v.month, v.day, v.hour, v.minute, v.second)
    return v

class AccessDB:
    def __init__(self, path, create=False, visible=False):
        self.path = os.path.abspath(path); self.create = create
        self.visible = visible; self.app = None
    def __enter__(self):
        pythoncom.CoInitialize()
        self.app = win32.DispatchEx("Access.Application")  # DispatchEx = instancia propia
        self.app.Visible = self.visible
        if self.create:
            if os.path.exists(self.path): os.remove(self.path)
            self.app.NewCurrentDatabase(self.path)
        else:
            self.app.OpenCurrentDatabase(self.path)
        return self
    def __exit__(self, *a):
        try:
            if self.app is not None:
                try: self.app.CloseCurrentDatabase()
                except Exception: pass
                self.app.Quit(2)  # acQuitSaveNone
        finally:
            self.app = None; pythoncom.CoUninitialize()
    def _db(self): return self.app.CurrentDb()
    def list_tables(self):
        db = self._db(); out = []
        for i in range(db.TableDefs.Count):
            n = db.TableDefs(i).Name
            if not n.startswith("MSys") and not n.startswith("~"): out.append(n)
        return out
    def list_queries(self):
        db = self._db(); return [db.QueryDefs(i).Name for i in range(db.QueryDefs.Count)
                                 if not db.QueryDefs(i).Name.startswith("~")]
    def execute(self, sql):
        # dbFailOnError=128; DAO ejecuta DDL y DML sin diálogos de advertencia
        self._db().Execute(sql, 128)
    def query(self, sql):
        db = self._db(); rs = db.OpenRecordset(sql)
        cols = [rs.Fields(i).Name for i in range(rs.Fields.Count)]
        rows = []
        if not rs.EOF:
            rs.MoveFirst()
            while not rs.EOF:
                rows.append([_clean(rs.Fields(i).Value) for i in range(len(cols))])
                rs.MoveNext()
        rs.Close()
        return pd.DataFrame(rows, columns=cols)
    def table(self, name):
        return self.query("SELECT * FROM [%s]" % name)
    def to_excel(self, objeto, ruta_xlsx):
        # acExport=1 ; acSpreadsheetTypeExcel12Xml=10 ; a prueba de configuración regional
        self.app.DoCmd.TransferSpreadsheet(1, 10, objeto, os.path.abspath(ruta_xlsx), True)
        return ruta_xlsx
    def to_csv(self, objeto, ruta_csv):
        # locale-safe: exporta vía DAO->pandas (evita el choque coma decimal/coma campo del TransferText)
        self.table(objeto).to_csv(ruta_csv, index=False, encoding="utf-8-sig")
        return ruta_csv

# ---------------- AUTOPRUEBA de punta a punta ----------------
if __name__ == "__main__":
    tmp = os.path.join(os.environ.get("TEMP","."), "_prueba_conector.accdb")
    print("1) Crear base y tabla...")
    with AccessDB(tmp, create=True) as db:
        db.execute("CREATE TABLE Ventas (id COUNTER PRIMARY KEY, producto TEXT(50), monto CURRENCY, fecha DATETIME)")
        db.execute("INSERT INTO Ventas (producto, monto, fecha) VALUES ('Agua 20L', 1.50, #2026-09-25#)")
        db.execute("INSERT INTO Ventas (producto, monto, fecha) VALUES ('Canasta',  4.00, #2026-09-25#)")
        db.execute("INSERT INTO Ventas (producto, monto, fecha) VALUES ('Recarga',  1.00, #2026-09-24#)")
        print("   tablas:", db.list_tables())
        print("2) SELECT -> DataFrame:")
        print(db.query("SELECT producto, monto FROM Ventas WHERE monto >= 1.5 ORDER BY monto DESC").to_string(index=False))
        print("   total:", db.query("SELECT SUM(monto) AS total FROM Ventas").iloc[0,0])
        db.to_excel("Ventas", os.path.join(os.environ.get("TEMP","."), "_prueba_ventas.xlsx"))
        db.to_csv("Ventas", os.path.join(os.environ.get("TEMP","."), "_prueba_ventas.csv"))
        print("3) Export XLSX+CSV OK")
    print("4) Cerrado limpio. CONECTOR VERIFICADO.")
    try: os.remove(tmp)
    except Exception: pass
