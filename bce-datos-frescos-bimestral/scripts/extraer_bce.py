# -*- coding: utf-8 -*-
"""
Extrae los INDICADORES ECONOMICOS del portal BCEData del Banco Central del Ecuador
(https://contenido.bce.fin.ec/) y los deja en:

  E:\\vars\\var 5\\BCE-datos\\bce_indicadores_YYYY-MM-DD.json   (snapshot crudo)
  E:\\vars\\var 5\\BCE-datos\\bce_ultimo.json                   (siempre el mas reciente)
  E:\\vars\\var 5\\BCE-datos\\bce_ultimo.md                     (tabla lista para leer)

Por que este portal y no www.bce.fin.ec:
  www.bce.fin.ec exige ACEPTAR una politica de privacidad antes de mostrar nada
  (banner bloqueante). contenido.bce.fin.ec (BCEData) sirve los indicadores sin
  ese muro: solo tiene un aviso de analitica no bloqueante. No se acepta ningun
  termino en nombre del usuario.

Uso:
  python extraer_bce.py                 # extrae y guarda
  python extraer_bce.py --comparar      # ademas compara contra el snapshot previo
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

URL = "https://contenido.bce.fin.ec/"
EDGE_PROFILE = Path.home() / ".notebooklm" / "browser_profile_edge"
DEST = Path(r"E:\vars\var 5\BCE-datos")

# Unidades que aparecen en las tarjetas del portal
UNIDAD = re.compile(
    r"^(Millones de USD|Millones USD FOB|Puntos B[aá]sicos|Porcentaje|USD / Onza Troy|"
    r"USD por barril|Indice|[ÍI]ndice|Puntos|USD|Porcentaje del PIB|Porcentaje-Trimestral)\s*-\s*"
    r"(Diaria|Mensual|Trimestral|Anual)$",
    re.I,
)
# Una fecha de referencia: "Julio 2026", "17 Agosto 2026", "IT 2026", "2025 (prel)"
FECHA = re.compile(
    r"^(\d{1,2}\s+)?(Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|"
    r"Octubre|Noviembre|Diciembre)\s+\d{4}$|^[IVX]{1,4}T\s*\d{4}$|^\d{4}(\s*\(prel\))?$",
    re.I,
)
VALOR = re.compile(r"^-?[\d.,]+$")


def extraer():
    from playwright.sync_api import sync_playwright

    filas = []
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(EDGE_PROFILE), channel="msedge", headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        pg.goto(URL, wait_until="networkidle", timeout=90000)
        pg.wait_for_timeout(4000)
        texto = pg.inner_text("body")
        ctx.close()

    lineas = [l.strip() for l in texto.split("\n")]
    lineas = [l for l in lineas if l and l != "..."]

    # El portal emite, por indicador: [simbolo] nombre / valor(es) / fecha / unidad-periodicidad
    i = 0
    while i < len(lineas):
        if UNIDAD.match(lineas[i]):
            unidad, periodicidad = [x.strip() for x in re.split(r"\s*-\s*", lineas[i], maxsplit=1)]
            fecha = lineas[i - 1] if i >= 1 and FECHA.match(lineas[i - 1]) else ""
            # hacia atras: valores hasta topar el nombre
            j = i - 2
            valores = []
            while j >= 0 and (VALOR.match(lineas[j]) or ":" in lineas[j]):
                valores.insert(0, lineas[j])
                j -= 1
            nombre = lineas[j] if j >= 0 else ""
            if nombre in ("$", "%", "I"):
                nombre = lineas[j - 1] if j >= 1 else nombre
            if nombre and fecha:
                filas.append({
                    "indicador": nombre,
                    "valor": valores[0] if len(valores) == 1 else valores,
                    "fecha_dato": fecha,
                    "unidad": unidad,
                    "periodicidad": periodicidad,
                })
        i += 1
    return filas


def guardar(filas):
    DEST.mkdir(parents=True, exist_ok=True)
    hoy = datetime.now().strftime("%Y-%m-%d")
    payload = {
        "fuente": URL,
        "portal": "BCEData - Series Estadisticas y Datos, Banco Central del Ecuador",
        "extraido_el": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "n_indicadores": len(filas),
        "indicadores": filas,
    }
    (DEST / f"bce_indicadores_{hoy}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (DEST / "bce_ultimo.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [f"# Indicadores BCE — extraido {payload['extraido_el']}",
          "", f"Fuente: {URL} (portal BCEData). {len(filas)} indicadores.", "",
          "| Indicador | Valor | Fecha del dato | Unidad | Periodicidad |",
          "|---|---:|---|---|---|"]
    for f in filas:
        v = f["valor"] if isinstance(f["valor"], str) else " · ".join(f["valor"])
        md.append(f"| {f['indicador']} | {v} | {f['fecha_dato']} | {f['unidad']} | {f['periodicidad']} |")
    (DEST / "bce_ultimo.md").write_text("\n".join(md), encoding="utf-8")
    return DEST / f"bce_indicadores_{hoy}.json"


def comparar(filas):
    """Compara contra el snapshot anterior mas reciente (distinto del de hoy)."""
    hoy = datetime.now().strftime("%Y-%m-%d")
    previos = sorted(DEST.glob("bce_indicadores_*.json"))
    previos = [p for p in previos if hoy not in p.name]
    if not previos:
        print("\n(no hay snapshot previo con el que comparar)")
        return
    ant = json.loads(previos[-1].read_text(encoding="utf-8"))
    antd = {x["indicador"]: x for x in ant["indicadores"]}
    print(f"\n=== CAMBIOS vs {previos[-1].name} ===")
    cambios = 0
    for f in filas:
        a = antd.get(f["indicador"])
        if a and (a["valor"] != f["valor"] or a["fecha_dato"] != f["fecha_dato"]):
            print(f"  • {f['indicador']}: {a['valor']} ({a['fecha_dato']}) -> {f['valor']} ({f['fecha_dato']})")
            cambios += 1
    if not cambios:
        print("  sin cambios")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comparar", action="store_true")
    a = ap.parse_args()

    filas = extraer()
    if not filas:
        print("ERROR: no se extrajo ningun indicador. El portal pudo cambiar de estructura.")
        sys.exit(1)

    print(f"Extraidos {len(filas)} indicadores:\n")
    for f in filas:
        v = f["valor"] if isinstance(f["valor"], str) else " · ".join(f["valor"])
        print(f"  {f['indicador']:<42} {v:>16}   {f['fecha_dato']}  ({f['periodicidad']})")

    if a.comparar:
        comparar(filas)

    ruta = guardar(filas)
    print(f"\nGuardado en: {ruta}")
    print(f"           : {DEST / 'bce_ultimo.md'}")


if __name__ == "__main__":
    main()
