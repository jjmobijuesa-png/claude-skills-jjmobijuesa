# -*- coding: utf-8 -*-
"""FUENTE ÚNICA de cifras v2: lee el libro entregado (valores guardados por Excel) y calcula las cuotas de referencia.
Todo entregable que cite una cifra (láminas, PDF, mensajes) la toma de fuente_v2.json. Nada se teclea a mano."""
import sys, io, glob, json, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import openpyxl

D = r"G:\Mi unidad\3 Urbanización San Sebastian\02 Financiero\Presupuesto Definitivo v1\00 ENTREGABLES - v2"
XL = glob.glob(D + r"\PRESUPUESTO GENERAL*v2.1*.xlsx")[0]
wb = openpyxl.load_workbook(XL, data_only=True)


def lab(ws, texto, col=2, exacto=False):
    for row in wb[ws].iter_rows():
        for c in row:
            if isinstance(c.value, str) and (c.value.strip() == texto if exacto else c.value.strip().startswith(texto)):
                return wb[ws].cell(c.row, col).value
    raise KeyError(f"{ws}: «{texto}»")


def fm(x, d=0): return ("−$" if x < 0 else "$") + f"{abs(x):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
def fn(x, d=2): return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
def fp(x, d=1): return f"{x*100:.{d}f}".replace(".", ",") + " %"


I, RF = "INDICADORES Y DECISIÓN", "RESUMEN FINANCIERO"
SBU = lab("PARAMETROS", "SBU 2026"); ENT = lab("PARAMETROS", "Entrada del comprador %")
PVD = lab("PARAMETROS", "PVP $/m² vendible"); PVC = lab("PARAMETROS", "PVP $/m² — casas")
TOPE = SBU * lab("PARAMETROS", "Tope bono Yapa (SBU del precio)")


def pmt(pv, i, n): return pv * (i / 12) / (1 - (1 + i / 12) ** -n)
def cuota_dep(p, sbu, n): return pmt(p * (1 - ENT) - SBU * sbu, 0.0299, n)    # BIESS CrediCasa 2,99 %
def cuota_casa(p, n): return pmt(p * (1 - ENT), 0.0499, n)                     # Miti-Miti 4,99 %


# tipologías de la hoja DEPARTAMENTOS (área vendible) y VIVIENDAS
ws = wb["DEPARTAMENTOS"]; tip = {}
for r in range(4, ws.max_row):
    dorm, a, dest = ws.cell(r, 6).value, ws.cell(r, 7).value, ws.cell(r, 10).value
    if dorm and isinstance(a, (int, float)):
        k = f"{dorm}|{a}"; t = tip.setdefault(k, dict(dorm=dorm, area=a, pvp=a * PVD, venta=0, renta=0)); t["venta" if dest == "Venta" else "renta"] += 1
ws = wb["VIVIENDAS"]; casas = {}
for r in range(4, ws.max_row):
    a = ws.cell(r, 3).value
    if isinstance(a, (int, float)): casas.setdefault(a, 0); casas[a] += 1
d1, d2, d3, t2 = 43.14 * PVD, 61.33 * PVD, 64.68 * PVD, 60.0 * PVD
c95, c112 = 95 * PVC, 112 * PVC
Q = dict(d1_21_30=cuota_dep(d1, 21, 360), d1_14_30=cuota_dep(d1, 14, 360), d1_14_20=cuota_dep(d1, 14, 240),
         d2_14_30=cuota_dep(d2, 14, 360), d2_14_20=cuota_dep(d2, 14, 240), d3_14_30=cuota_dep(d3, 14, 360), d3_14_20=cuota_dep(d3, 14, 240),
         c95_30=cuota_casa(c95, 360), c95_25=cuota_casa(c95, 300), c112_30=cuota_casa(c112, 360), c112_25=cuota_casa(c112, 300))
ARR = 417.80
v = dict(
    ventas=lab(RF, "SUBTOTAL INGRESOS", 7), neta=lab("PyG", "UTILIDAD NETA"), uai=lab("PyG", "UTILIDAD ANTES DE IMPUESTOS"),
    capital=lab("PyG", "Capital invertido recuperado"), retorno=lab("PyG", "RETORNO TOTAL"), margen=lab("PyG", "margen neto s/ventas"),
    margen_sin_iva=lab("PyG", "margen neto s/ventas SIN"), tir=lab(I, "TIR anual", exacto=True), van=lab(I, "VAN a la tasa"),
    payback=lab(I, "Payback (meses)"), aporte=lab(I, "Aporte propio de arranque"), pico=lab(I, "Pico del crédito BDE"),
    linea=lab(I, "Límite de la línea BDE"), umbrales=lab(I, "Umbrales cumplidos"), decision=lab(I, "DECISIÓN DE ARRANQUE"),
    u_margen=lab(I, "Margen neto mínimo"), u_tir=lab(I, "TIR anual mínima"), u_van=lab(I, "Tasa de descuento"), u_pb=lab(I, "Payback máximo"),
    interes=lab("FLUJO DE CAJA", "Interés total BDE"), cancela=lab("FLUJO DE CAJA", "Mes en que se cancela"),
    caja_min=lab("CAJA 5 INDICADORES", "FCL acumulado mínimo"), canon=lab("PARAMETROS", "Canon de alquiler"),
    renta_bruta=lab("ALQUILERES", "Renta bruta anual"), rend_bruto=lab("ALQUILERES", "Rendimiento BRUTO"), rend_neto=lab("ALQUILERES", "Rendimiento NETO s/valor"),
    val_ret=lab("ALQUILERES", "Valor de mercado"), sbu=SBU, tope=TOPE, bono14=SBU * 14, bono21=SBU * 21, pvd=PVD, pvc=PVC,
    pvp_d1=d1, pvp_d2=d2, pvp_d3=d3, pvp_t2=t2, pvp_c95=c95, pvp_c112=c112, arriendo=ARR,
    area_t1_edif=sum(t['area'] * (t['venta'] + t['renta']) for t in tip.values() if t['area'] != 60.0) / 4,
    **{f"q_{k}": x for k, x in Q.items()})
v["area_t1"] = v["area_t1_edif"] * 4; v["area_t2"] = 60.0 * 12 * 3; v["area_dep"] = v["area_t1"] + v["area_t2"]
v["media_t1"] = v["area_t1"] / 72; v["pvp_medio_t1"] = v["media_t1"] * PVD
v["ahorro_arriendo"] = ARR - round(Q["d2_14_20"])
v["sens"] = {wb["SENSIBILIDAD"].cell(r, 1).value: dict(neta=wb["SENSIBILIDAD"].cell(r, 3).value, margen=wb["SENSIBILIDAD"].cell(r, 4).value,
             tir=wb["SENSIBILIDAD"].cell(r, 5).value, pico=wb["SENSIBILIDAD"].cell(r, 7).value, ok=wb["SENSIBILIDAD"].cell(r, 10).value)
             for r in range(4, 16) if wb["SENSIBILIDAD"].cell(r, 1).value}
v["casas"] = {str(int(k)): n for k, n in casas.items()}
# textos ya formateados (lo único que copian las láminas)
F = dict(margen=fp(v["margen"]), tir=fp(v["tir"]), van_m=fm(v["van"] / 1e6, 2) + " M", van=fm(v["van"]), payback=f"{v['payback']} meses",
         aporte=fm(v["aporte"]), pico=fm(v["pico"]), pico_m=fm(v["pico"] / 1e6, 2) + " M", linea_m=fm(v["linea"] / 1e6, 2) + " M",
         neta=fm(v["neta"]), retorno=fm(v["retorno"]), capital=fm(v["capital"]), ventas=fm(v["ventas"]), tope=fm(TOPE),
         bono14=fm(v["bono14"]), bono21=fm(v["bono21"]), d1=fm(d1), d2=fm(d2), d3=fm(d3), t2=fm(t2), c95=fm(c95), c112=fm(c112),
         q_desde=fm(round(Q["d1_21_30"])), q_max=fm(round(Q["d3_14_20"])), q_d2_20=fm(round(Q["d2_14_20"])), q_d2_30=fm(round(Q["d2_14_30"])),
         q_d3_30=fm(round(Q["d3_14_30"])), ing_min_dep=fm(round(Q["d1_14_20"] / .4)), ing_max_dep=fm(round(Q["d3_14_20"] / .4)),
         q_c95_30=fm(round(Q["c95_30"])), ing_c95=f"{fm(round(Q['c95_30']/.4))} a {fm(round(Q['c95_25']/.4))}",
         q_c112_30=fm(round(Q["c112_30"])), ing_c112=f"{fm(round(Q['c112_30']/.4))} a {fm(round(Q['c112_25']/.4))}",
         ahorro=fm(v["ahorro_arriendo"]), area_t1=fn(v["area_t1"]), area_t2=fn(v["area_t2"]), area_dep=fn(v["area_dep"]),
         media_t1=fn(v["media_t1"]), pvp_medio_t1=fm(round(v["pvp_medio_t1"])), canon=fm(v["canon"]), cancela=v["cancela"],
         umbrales=v["umbrales"], u_margen=fp(v["u_margen"], 0), u_tir=fp(v["u_tir"], 0), u_pb=f"{v['u_pb']} m",
         interes=fm(v["interes"]), rend_bruto=fp(v["rend_bruto"]), rend_neto=fp(v["rend_neto"]), caja_min=fm(v["caja_min"]))
out = dict(libro=os.path.basename(XL), v=v, f=F)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fuente_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
for k, x in F.items(): print(f"{k:<14} {x}")
