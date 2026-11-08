# -*- coding: utf-8 -*-
"""Validador de consistencia de TODOS los entregables de una versión: libro ⇄ PDF ⇄ presentación.
Fuente única = libro guardado por Excel (vía fuente_v2.json). Una cifra = un valor en todos los documentos.
Uso: python cruce_v2.py   → imprime la matriz concepto × documento y termina con TODO CUADRA o la lista de fallas."""
import sys, io, glob, re, os, json, hashlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import openpyxl, fitz
from pptx import Presentation

SP = os.path.dirname(os.path.abspath(__file__))
D = r"G:\Mi unidad\3 Urbanización San Sebastian\02 Financiero\Presupuesto Definitivo v1\00 ENTREGABLES - v2"
XL = glob.glob(D + r"\PRESUPUESTO GENERAL*v2.1*.xlsx")[0]
J = json.load(open(os.path.join(SP, "fuente_v2.json"), encoding="utf-8")); v, f = J["v"], J["f"]
wb = openpyxl.load_workbook(XL, data_only=True)
fallas = []
assert J["libro"] == os.path.basename(XL), "fuente_v2.json no corresponde al libro entregado: regenerarla"


def lab(ws, texto, col=2, exacto=False):
    for row in wb[ws].iter_rows():
        for c in row:
            if isinstance(c.value, str) and (c.value.strip() == texto if exacto else c.value.strip().startswith(texto)):
                return wb[ws].cell(c.row, col).value
    raise KeyError(f"{ws}: «{texto}»")


def igual(nombre, vals, tol=0.005):   # al centavo
    vs = [x for x in vals if x is not None]; ok = max(vs) - min(vs) <= tol
    print(f"{'OK ' if ok else 'FALLA'} {nombre:<42} " + " | ".join(f"{x:,.2f}" for x in vs))
    if not ok: fallas.append(nombre)


# ================= 1. coherencia interna del libro =================
print("== 1. LIBRO:", os.path.basename(XL))
RF, I, S_ = "RESUMEN FINANCIERO", "INDICADORES Y DECISIÓN", wb["SENSIBILIDAD"]
DEP, VIV = wb["DEPARTAMENTOS"], wb["VIVIENDAS"]
ventas = lab(RF, "SUBTOTAL INGRESOS", 7); neta = lab(RF, "UTILIDAD NETA", 7)
cap = lab(RF, "Suelo (terreno propio)", 7) + lab(RF, "Urbanización ejecutada", 7)
igual("Ventas", [ventas, lab("PyG", "Ingresos por venta"), wb["CRONOGRAMA ENTREGAS"]["K11"].value,
                 DEP.cell(DEP.max_row, 12).value + VIV.cell(VIV.max_row, 6).value, S_["B4"].value])
igual("Utilidad neta", [neta, lab("PyG", "UTILIDAD NETA"), lab("BALANCE GENERAL", "Utilidad neta del proyecto"), S_["C4"].value])
igual("Utilidad antes de impuestos", [lab(RF, "UTILIDAD ANTES DE IMPUESTOS", 7), lab("PyG", "UTILIDAD ANTES DE IMPUESTOS")])
igual("Impuesto a la renta", [lab(RF, "(−) Impuesto a la renta", 7), -lab("PyG", "(−) Impuesto a la renta")])
igual("Capital invertido", [cap, lab("PyG", "Capital invertido recuperado"),
      lab("BALANCE GENERAL", "Capital en especie: terreno") + lab("BALANCE GENERAL", "Capital en especie: urbanización")])
igual("Retorno = capital + utilidad", [lab(RF, "Retorno al propietario", 7), lab("PyG", "RETORNO TOTAL"), lab(I, "Retorno total al propietario"), cap + neta])
igual("Margen neto", [lab("PyG", "margen neto s/ventas"), lab(I, "Margen neto s/ventas"), S_["D4"].value, neta / ventas], tol=1e-6)
igual("TIR anual", [lab(I, "TIR anual", exacto=True), S_["E4"].value], tol=1e-6)
igual("VAN @15%", [lab(I, "VAN a la tasa"), S_["F4"].value])
igual("Pico BDE", [lab(I, "Pico del crédito BDE"), lab("FLUJO DE CAJA", "Pico del crédito BDE"), S_["G4"].value])
igual("Aporte propio", [lab(I, "Aporte propio de arranque"), lab("FLUJO DE CAJA", "Aporte propio de arranque"),
                        lab("BALANCE GENERAL", "Aporte propio de arranque"), lab("PRIMERA ETAPA", "Aporte propio de caja"), S_["H4"].value])
igual("Interés BDE", [lab(RF, "Gasto financiero", 7), -lab("PyG", "(−) Gasto financiero BDE"), lab("FLUJO DE CAJA", "Interés total BDE")])
igual("9 deptos capitalizados", [-lab(RF, "(−) Costo capitalizado", 7), lab("PyG", "(+) Costo capitalizado"),
                                 lab("BALANCE GENERAL", "Propiedad de inversión"), lab("ALQUILERES", "Costo capitalizado (balance)")])
igual("Valor 9 deptos retenidos", [lab("PRIMERA ETAPA", "Valor comercial"), lab("ALQUILERES", "Valor de mercado")])
igual("Renta bruta = 9 × canon × 12", [lab("ALQUILERES", "Renta bruta anual"), 9 * lab("PARAMETROS", "Canon de alquiler") * 12])
igual("Control del balance = 0", [lab("BALANCE GENERAL", "CONTROL"), 0])
igual("Caja final (flujo = balance)", [lab("FLUJO DE CAJA", "Caja final"), lab("BALANCE GENERAL", "Caja y bancos")])
igual("Construcción", [lab(RF, "SUBTOTAL CONSTRUCCIÓN", 7), wb["CRONOGRAMA ENTREGAS"]["J11"].value,
                       DEP.cell(DEP.max_row, 11).value + VIV.cell(VIV.max_row, 5).value])
igual("Etapa 1: ventas", [lab(RF, "SUBTOTAL INGRESOS", 8), lab("PRIMERA ETAPA", "Ventas 1.ª etapa")])
ws = wb[RF]; malas = 0
for i in range(9, ws.max_row + 1):
    g = ws.cell(i, 7).value; ets = [ws.cell(i, j).value for j in range(8, 15)]
    if isinstance(g, (int, float)) and all(isinstance(x, (int, float)) for x in ets) and "impuesto" not in str(ws.cell(i, 2).value).lower():
        if abs(sum(ets) - g) > 1: malas += 1; print("   fila", i, ws.cell(i, 2).value, g, sum(ets))
igual("RESUMEN: filas con Σ etapas ≠ total", [malas, 0])
_pv = wb["PLAN DE VENTAS"]
igual("Reservas antes de feb-27 = 0", [sum(_pv.cell(rw, 7).value or 0 for rw in range(4, 7)), 0])
igual("Ventas después de oct-28 = 0", [sum(_pv.cell(rw, 7).value or 0 for rw in range(28, 31)), 0])
import motor_v2 as _M   # el motor que generó el libro debe dar lo mismo al centavo
_r = _M.run()
igual("Motor = libro: utilidad neta", [_r["NETA"], neta])
igual("Motor = libro: VAN @15%", [_r["VAN15"], lab(I, "VAN a la tasa")])
igual("Motor = libro: TIR anual", [_r["TIR"], lab(I, "TIR anual", exacto=True)], tol=1e-9)
igual("Motor = libro: costos totales", [_r["COSTOS"] + _r["INT"], lab(RF, "COSTOS TOTALES", 7)])
igual("Motor = libro: pico BDE", [_r["PICO"], lab(I, "Pico del crédito BDE")])
igual("Motor = libro: aporte propio", [_r["APORTE"], lab(I, "Aporte propio de arranque")])
igual("Plan de ventas: Σ meses = ventas", [lab("PLAN DE VENTAS", "TOTAL", 7), ventas])
igual("Plan de ventas: Σ entradas 5 % = 5 % de ventas", [lab("PLAN DE VENTAS", "TOTAL", 9), 0.05 * ventas])
igual("Fuente única = libro", [abs(v["neta"] - neta) + abs(v["pico"] - lab(I, "Pico del crédito BDE")) + abs(v["tir"] - lab(I, "TIR anual", exacto=True)), 0], tol=1e-6)


# ================= 2. textos de cada documento =================
def norm(t):  # «$ 1.923.761», «−$ 1.923.761» y «$1.923.761» comparan igual; mayúsculas no importan
    return re.sub(r"\s+", " ", t.replace("\xa0", " ")).replace("$ ", "$").replace("−", "-").lower()


def txt_pdf(clave): return norm("".join(pg.get_text() for pg in fitz.open(glob.glob(D + "\\" + clave + "*v2.1*.pdf")[0])))


dig = lambda x, d=0: f"{abs(x):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
PPT = glob.glob(D + r"\Presentacion*v2.1*.pptx")[0]; prs = Presentation(PPT)
def txt_lam(i):
    out = []
    for sh in prs.slides[i - 1].shapes:
        if sh.has_text_frame: out.append(sh.text_frame.text)
        if sh.has_table: out += [c.text for r in sh.table.rows for c in r.cells]
        if sh.has_chart:   # los gráficos nativos son un canal de datos aparte: categorías y valores también se validan
            pl = sh.chart.plots[0]; out += list(pl.categories)
            out += ["$" + dig(x) if x == round(x) else "$" + dig(x, 2) for se in pl.series for x in se.values]
    return norm(" ".join(out))


# láminas de imagen: el HTML de origen es su texto; la huella prueba que la imagen insertada es ese render
IMG = {7: "cuadro_slide_v2", 20: "decision_slide_v2"}
print("\n== 2. LÁMINAS DE IMAGEN")
for i, n in IMG.items():
    pic = next(sh for sh in prs.slides[i - 1].shapes if sh.shape_type == 13)
    same = hashlib.sha1(pic.image.blob).hexdigest() == hashlib.sha1(open(os.path.join(SP, n + ".png"), "rb").read()).hexdigest()
    print(f"{'OK ' if same else 'FALLA'} lámina {i}: imagen insertada = render de {n}.html")
    if not same: fallas.append(f"lámina {i}: imagen distinta del render")
def txt_img(i):
    h = open(os.path.join(SP, IMG[i] + ".html"), encoding="utf-8").read()
    return norm(re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", "", h, flags=re.S)).replace("&gt;", ">").replace("&nbsp;", " "))


DOCS = {"PDF general": txt_pdf("Resumen Ejecutivo A4 - Presupuesto General"), "PDF etapa 1": txt_pdf("Resumen Ejecutivo A4 - Primera Etapa"),
        "PDF precios": txt_pdf("Lista de Precios por Unidad"), **{f"lám {i}": txt_lam(i) for i in range(1, len(prs.slides) + 1) if i not in IMG},
        **{f"lám {i} (img)": txt_img(i) for i in IMG}}
dig = lambda x, d=0: f"{abs(x):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
pct = lambda x: f"{x*100:.1f}".replace(".", ",") + " %"
e1 = lambda k: lab(RF, k, 8)
C = {  # concepto → (valor del libro formateado, documentos donde DEBE aparecer)
 "Ventas": (dig(v["ventas"]), ["PDF general", "PDF precios"]),
 "Utilidad neta": (dig(v["neta"]), ["PDF general", "lám 20 (img)"]),
 "Capital invertido": (dig(v["capital"]), ["PDF general", "lám 20 (img)"]),
 "Retorno al propietario": (dig(v["retorno"]), ["PDF general", "lám 20 (img)"]),
 "Margen neto": (pct(v["margen"]), ["PDF general", "lám 20 (img)"]),
 "TIR anual": (pct(v["tir"]), ["PDF general", "lám 20 (img)"]),
 "VAN @15 %": (dig(v["van"]), ["lám 20 (img)"]),
 "VAN (millones)": (dig(v["van"] / 1e6, 2) + " m", ["PDF general", "lám 20 (img)"]),
 "Payback": (f"{v['payback']} meses", ["PDF general", "lám 20 (img)"]),
 "Umbrales cumplidos": (v["umbrales"], ["PDF general", "lám 20 (img)"]),
 "Aporte propio": (dig(v["aporte"]), ["PDF general", "PDF etapa 1", "lám 20 (img)"]),
 "Pico BDE": (dig(v["pico"]), ["PDF general"]),
 "Pico BDE (millones)": (dig(v["pico"] / 1e6, 2) + " m", ["lám 20 (img)"]),
 "Cancelación BDE": (v["cancela"], ["PDF general", "lám 20 (img)"]),
 "Interés BDE": (dig(v["interes"]), ["PDF general"]),
 "Etapa 1: ventas": (dig(e1("SUBTOTAL INGRESOS")), ["PDF etapa 1"]),
 "Etapa 1: costos": (dig(e1("COSTOS TOTALES")), ["PDF etapa 1"]),
 "Etapa 1: resultado": ("-$" + dig(lab("PRIMERA ETAPA", "RESULTADO CONTABLE")), ["PDF etapa 1"]),
 "Valor 9 deptos": (dig(v["val_ret"]), ["PDF etapa 1"]),
 "Tope bono 135 SBU": (dig(v["tope"]), ["PDF precios", "lám 6", "lám 7 (img)"]),
 "Bono 14 SBU": (dig(v["bono14"]), ["PDF precios", "lám 5", "lám 7 (img)", "lám 12"]),
 "PVP 1 dorm.": (dig(v["pvp_d1"]), ["PDF precios", "lám 5", "lám 7 (img)"]),
 "PVP 2 dorm.": (dig(v["pvp_d2"]), ["PDF precios", "lám 7 (img)"]),
 "PVP 3 dorm.": (dig(v["pvp_d3"]), ["PDF precios", "lám 5", "lám 6", "lám 7 (img)"]),
 "PVP tipo 2": (dig(v["pvp_t2"]), ["PDF precios", "lám 6", "lám 7 (img)"]),
 "PVP casa 95": (dig(v["pvp_c95"]), ["PDF precios", "lám 4", "lám 7 (img)", "lám 9"]),
 "PVP casa 112": (dig(v["pvp_c112"]), ["PDF precios", "lám 4", "lám 7 (img)", "lám 10"]),
 "Área vendible deptos": (dig(v["area_dep"], 2), ["lám 6", "lám 7 (img)"]),
 "Canon renta Fase 1": ("$" + dig(v["canon"]), ["lám 15", "lám 7 (img)"]),
 "Cuota depto desde": (f["q_desde"], ["lám 2", "lám 5", "lám 11"]),
 "Cuota 2 dorm. 20 a.": (f["q_d2_20"], ["lám 11"]),
 "Cuota 3 dorm. 20 a. (gráfico)": (f["q_max"], ["lám 11", "lám 5"]),
 "Arriendo medio zona": ("$417,80", ["lám 2", "lám 11"]),
 "Ingreso mín. deptos": (f"{f['ing_min_dep']} a {f['ing_max_dep']}", ["lám 5"]),
 "Cuota casa 95": (f["q_c95_30"], ["lám 9"]),
 "Ingreso mín. casa 95": (f["ing_c95"], ["lám 9"]),
 "Cuota casa 112": (f["q_c112_30"], ["lám 10"]),
 "Ingreso mín. casa 112": (f["ing_c112"], ["lám 10"]),
 "Casas 95 m² (unid.)": (f"{v['casas']['95']} unid", ["lám 4"]),
 "Casas 112 m² (unid.)": (f"{v['casas']['112']} unid", ["lám 4"]),
}
print("\n== 3. MATRIZ CONCEPTO × DOCUMENTO (valor del libro buscado en cada documento)")
for k, (val, docs) in C.items():
    res = []
    for dname in dict.fromkeys(docs):
        ok = norm(val) in DOCS[dname]; res.append(f"{dname}:{'✔' if ok else '✘'}")
        if not ok: fallas.append(f"{k} en {dname} ({val})")
    print(f"   {k:<24} {val:<18} " + "  ".join(res))

VIEJOS = ["2.713.5", "5.013.5", "14.144.5", "10.526.3", "1.553.2", "1.309.962", "50,2 %", "19,2 %", "19,18 %", "1,31 m",
          "61.012", "63.093", "52.897", "4.392,88", "2.271,33", "6.664,21", "$201", "$295", "$710", "$738", "$284", "$134",
          "$216", "$224", "$1.253", "$1.475", "$280", "21 hojas", "libro v2 recalculado", "del libro v2. ", "» v2 ·", "(2026-10-30)", "m² privado", "área privada", "áreas no vendibles", "1.923.761", "4.297.178", "682.834", "617.038", "3.214.783", "3,21 m", "alícuota y bono incluidos", "aporte propio fresco de $0",
          "capital propio fresco", "utilidad escondida", "nunca en rojo", "4/4 umbrales", "con capital propio"]
print("\n== 4. CIFRAS O CONCEPTOS DE LA v1 QUE NO DEBEN QUEDAR")
hall = [(dn, x) for dn, t in DOCS.items() for x in VIEJOS if norm(x) in t]
for dn, x in hall: print(f"   FALLA «{x}» sigue en {dn}"); fallas.append(f"v1 «{x}» en {dn}")
if not hall: print("   OK  ninguna")
print("\nRESULTADO:", "TODO CUADRA" if not fallas else f"{len(fallas)} FALLAS → {fallas}")
sys.exit(1 if fallas else 0)
