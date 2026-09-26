---
name: access-db-local-connector
description: |
  Conector LOCAL a bases de datos Microsoft Access (.accdb/.mdb) desde Python,
  en esta máquina donde Python es 64-bit y Office/Access es 32-bit. Permite
  crear bases, listar tablas/consultas, ejecutar SQL (DDL/DML), traer cualquier
  SELECT a un pandas.DataFrame y exportar a XLSX/CSV. Úsala cuando haya que leer,
  consultar, transformar o alimentar una base Access del usuario.
trigger_phrases:
  - "trabajar una base de datos access"
  - "conéctate a la base access"
  - "lee la tabla de access"
  - "consulta el accdb"
  - "exporta la base access a excel"
idioma_de_salida: español
nivel: aplicada
dominio: datos / integración Office
metadata:
  version: 1.0
  fecha: 2026-09-25
  verificado_en: "Python 3.12 x64 + Office 2019 x86 (ProPlus/Access), esta máquina"
  relacionada: excel-formato-dolar-y-m2, modelo-excel-sistema-vivo, saneamiento-complementos-office, feedback_office_32bit_python_64bit_com
---

# Skill `access-db-local-connector`

## El problema que resuelve (mecanismo, no síntoma)
En esta máquina **Python = 64 bits** y **Office/Access = 32 bits**. Por eso:
- `pyodbc` de 64 bits **no ve** el driver "Microsoft Access Driver (*.mdb, *.accdb)" (que es de 32 bits) → *"driver not found / provider not registered"*.
- `ADODB.Connection` con `Microsoft.ACE.OLEDB.12.0/16.0` desde Python de 64 bits **falla** (COM in-process no cruza bits).
- Instalar el **ACE de 64 bits choca** con el Office de 32 bits (Microsoft lo bloquea).

**La única vía sin instalar nada y sin choque de bits** es automatizar **`Access.Application` por COM FUERA DE PROCESO**: Access corre como servidor COM independiente (LocalServer), así que un proceso de 64 bits SÍ puede manejar el Access de 32 bits. Requisitos que ya se cumplen aquí: **Access instalado** (`MSACCESS.EXE` en Office16 x86) + **pywin32**.

## Uso
```python
import sys; sys.path.insert(0, r"C:\Users\datos\.claude\skills\access-db-local-connector\scripts")
from access_connector import AccessDB

with AccessDB(r"D:\ruta\mi_base.accdb") as db:      # create=True para crear una nueva
    print(db.list_tables())                          # y list_queries()
    df = db.query("SELECT * FROM Clientes WHERE saldo > 0")   # SELECT -> DataFrame
    df = db.table("Ventas")                          # atajo de SELECT *
    db.execute("UPDATE Ventas SET estado='OK' WHERE id=5")    # DDL/DML
    db.to_excel("Ventas", r"D:\salida\ventas.xlsx")  # export nativo (a prueba de locale)
    db.to_csv("Ventas",  r"D:\salida\ventas.csv")    # export CSV vía pandas
```
Ejecutarlo siempre con el Python de 64 bits del sistema:
`C:\Users\datos\AppData\Local\Programs\Python\Python312\python.exe`.
Autoprueba de punta a punta: `python scripts\access_connector.py` (crea base temporal, inserta, consulta, exporta y cierra → imprime "CONECTOR VERIFICADO").

## Cómo depurar si falla
- **`TransferText` revienta** con *"el separador de campos coincide con el separador decimal"*: es la **configuración regional** (coma decimal en Ecuador). NO usar `TransferText`; usar `to_excel` (TransferSpreadsheet a XLSX) o `to_csv` (que exporta vía pandas). Ya resuelto en el módulo.
- **Ruido de pandas** `tslibs ... total_seconds` al leer fechas: los `datetime` de COM traen tz que rompe a pandas → el módulo los normaliza con `_clean` a `datetime` nativo. Si aparece con otro tipo, ampliar `_clean`.
- **`OpenCurrentDatabase` se cuelga o pide contraseña**: pasar la base sin abrir en Access a la vez; para bases protegidas, abrir con `visible=True` una vez y desbloquear, o parametrizar la contraseña.
- **Escritura del proyecto VBA bloqueada** ([[feedback_vba_injection_bloqueado]]): no aplica aquí — este conector usa DAO/DoCmd, no el modelo del proyecto VBA.
- Ante cualquier segundo fallo: [[regla-del-primer-tropiezo]] (barrer inventario antes del segundo intento).

## Alternativa (si se quiere ODBC/pandas puro)
Instalar un **Python de 32 bits** y ahí `pip install pyodbc`; entonces sí ve el driver Access de 32 bits y se puede `pandas.read_sql("...", pyodbc.connect(...))`. Más limpio para cargas SQL pesadas, pero exige ese intérprete aparte. El conector COM de arriba no requiere instalar nada.

## Relacionadas
[[excel-formato-dolar-y-m2]] · [[modelo-excel-sistema-vivo]] · [[saneamiento-complementos-office]] · [[feedback_office_32bit_python_64bit_com]]
