# -*- coding: utf-8 -*-
"""
armar_semana.py — arma la carpeta «Sem ven NN» del informe semanal de ventas QVP.

Crea la carpeta de la semana y sus siete subcarpetas de area, clasifica cada
archivo e imagen segun el patron detectado en la semana 44, los mueve a su
subcarpeta y escribe el acta de procedencia FUENTES_Semana_NN.md.

Uso (interprete del sistema: tiene rapidocr-onnxruntime):
    python armar_semana.py --semana 45
    python armar_semana.py --semana 45 --aplicar
    python armar_semana.py --semana 45 --origen "C:/Users/datos/Downloads" --aplicar

Sin --aplicar solo muestra el plan. NUNCA sobrescribe: si el destino existe,
avisa y deja el archivo donde estaba.
"""
import argparse
import datetime as dt
import os
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = pathlib.Path(
    r"C:\Users\datos\Dropbox\7 Quevepalma\1 WAR ROOM QVP\Entregables\I Inf Sem Ventas"
)

# Los nombres se replican TAL CUAL de la semana 44, erratas incluidas
# («finaciera» sin la «n»). No corregirlos: romperia el emparejamiento.
AREAS = [
    "area comercial",
    "area compra de fruta",
    "area compra de materiales",
    "area control de calidad",
    "area de mantenimiento",
    "area finaciera y cartera",
    "area logistica",
]
SIN_CLASIFICAR = "_sin_clasificar"

# Reglas por NOMBRE DE ARCHIVO: deterministas, mandan sobre el OCR.
REGLAS_NOMBRE = [
    (r"seguimiento\s+precio", "area comercial"),
    (r"comite\s+ejecutivo", "area comercial"),
    (r"propuesta|surveydata|estudio[_ ]?mercado|planta[_ ]?jabon", "area comercial"),
    (r"precios?\s+aceite|competencia", "area comercial"),
    (r"macro.*cartera|control\s+semanal\s+de\s+cartera", "area finaciera y cartera"),
    (r"\bcartera\b", "area finaciera y cartera"),
    (r"\blogistica\b|\bacopios?\b", "area logistica"),
    (r"\bcalidad\b", "area control de calidad"),
    (r"mantenimiento", "area de mantenimiento"),
    (r"compra\s+de\s+fruta|palma|racimo", "area compra de fruta"),
    (r"materiales|insumos", "area compra de materiales"),
    (r"neg\s+|negociacion|oriental", "area comercial"),
]

# TITULOS del reporte, con peso 6: mandan sobre todo lo demas. Se buscan en el
# texto NORMALIZADO (sin espacios ni signos) porque el OCR pega las palabras:
# «INDICADORESDECALIDAD», «PROGRAMACIONDEVENTAS».
# Varias entradas son la grafia que DEVUELVE el OCR, no la correcta («logstica»,
# «flujodecaia», «acopos»). Es deliberado: se verificaron contra las 32 imagenes
# de la semana 44. Al anadir una nueva, anadir tambien lo que el OCR lea.
TITULOS = {
    "area comercial": ["programaciondeventas", "programadespachos", "preciosdeventa",
                       "seguimientoprecio", "resultadodeventas", "cumplimientodeventas",
                       "preciosdelacompetencia", "comiteejecutivo", "estudiodemercado",
                       "prefactibilidad", "plantadejabones", "surveydata",
                       "evaluacioncomparativ", "dospropuestas", "proponente",
                       "alianzacomercial", "ventasvspresupuesto"],
    "area finaciera y cartera": ["controlsemanaldecartera", "resumendecartera",
                                 "estadodecartera", "flujodecaja", "flujodecaia",
                                 "cuentasporcobrar", "recuperaciondecartera",
                                 "totaldeingresos", "totaldeegresos", "saldoinicial",
                                 "sobregiro", "interesxmora", "interespormora",
                                 "diasdecredito"],
    "area compra de fruta": ["compradefruta", "compradepalma", "reportedecompra",
                             "recepciondefruta", "tasadeextraccion", "compracrudo",
                             "costeoevoluci", "preciodelafruta"],
    "area compra de materiales": ["comprasacumuladas", "comprassemanal",
                                  "anticiposacumulados", "consumodecombustible",
                                  "ordendecompra", "resumengeneral"],
    "area control de calidad": ["indicadoresdecalidad", "fueraespecificacion",
                                "fueradeespecificacion", "controldecalidad",
                                "noconformidad", "fallasnodetectadas",
                                "indicadordefallas", "seguimientosemanal"],
    "area de mantenimiento": ["indicadoresdemantenimiento", "plandemantenimiento",
                              "mantenimientopreventivo", "ordendetrabajo",
                              "trabajospendientes", "serviciosytrabajos"],
    "area logistica": ["acopios", "acopos", "logisticasemana", "logsticasemana",
                       "frutatransportada", "transportadaporvehiculos",
                       "controldevueltas", "mermadeproductos",
                       "despachadovsrecepcion", "despachadovsrrecepcion"],
}

# Palabras del CONTENIDO (OCR). peso 3 = decide; peso 1 = acompana.
CLAVES = {
    "area comercial": {
        3: ["oleina", "oleína", "disebaj", "alto oleico", "gondola", "góndola",
            "precio de venta", "ventas programadas", "programa de ventas",
            "estearina", "aceite de palmiste", "jaboneria", "jabonería", "cupo",
            "cumplimiento de ventas", "presupuesto de ventas"],
        1: ["precio", "cliente", "tonelada", "margen", "colombia", "venta",
            "credito", "crédito", "contado", "competencia", "producto"],
    },
    "area finaciera y cartera": {
        3: ["cartera", "vencido", "cobranza", "flujo de caja", "antiguedad",
            "antigüedad", "recuperacion", "recuperación", "por vencer",
            "saldo por cobrar", "tesoreria", "tesorería", "mora", "egresos",
            "ingresos", "sobregiro", "saldo inicial"],
        1: ["saldo", "dias", "días", "banco", "pago", "meta", "cobro", "deuda"],
    },
    "area compra de fruta": {
        3: ["compra de fruta", "racimo", "rff", "fruta fresca", "proveedor de fruta",
            "precio de la fruta", "tasa de extraccion", "tasa de extracción",
            "guineensis", "hibrido", "híbrido", "crudo", "costeo"],
        1: ["fruta", "palma", "proveedor", "tonelada", "extraccion", "extracción"],
    },
    "area compra de materiales": {
        3: ["compra de materiales", "requisicion", "requisición", "orden de compra",
            "insumos", "repuestos", "bodega", "stock", "combustible", "anticipos",
            "compras acumuladas", "compras semanal"],
        1: ["material", "proveedor", "compra", "existencia", "quimico", "químico",
            "insumo", "galones", "consumo"],
    },
    "area control de calidad": {
        3: ["no conformidad", "acidez", "humedad", "impureza", "dobi",
            "control de calidad", "indice de peroxido", "índice de peróxido",
            "analisis de laboratorio", "análisis de laboratorio", "turbidez",
            "fallas no detectadas", "especificacion", "especificación"],
        1: ["calidad", "muestra", "norma", "parametro", "parámetro", "laboratorio",
            "falla", "tendencia"],
    },
    "area de mantenimiento": {
        3: ["mantenimiento preventivo", "mantenimiento correctivo", "orden de trabajo",
            "disponibilidad de equipos", "paradas", "mtbf", "mttr",
            "plan de mantenimiento"],
        1: ["mantenimiento", "equipo", "caldera", "maquina", "máquina", "falla",
            "cumplimiento"],
    },
    "area logistica": {
        3: ["vueltas", "placa", "flota", "transportista", "acopio", "merma",
            "fruta transportada", "viajes", "vehiculos", "vehículos",
            "interno/externo", "flete"],
        1: ["transporte", "camion", "camión", "ruta", "carga", "despacho", "km"],
    },
}

RE_WA = re.compile(
    r"WhatsApp\s+Image\s+(\d{4})-(\d{2})-(\d{2})\s+at\s+(\d{1,2})\.(\d{2})\.(\d{2})\s*([AP]M)",
    re.I,
)
EXT_IMG = {".jpeg", ".jpg", ".png", ".webp"}
EXT_DOC = {".xlsx", ".xlsm", ".xls", ".pptx", ".ppt", ".pdf", ".docx", ".csv", ".mp4", ".txt"}


def limites_iso(anio, semana):
    lun = dt.date.fromisocalendar(anio, semana, 1)
    return lun, lun + dt.timedelta(days=6)


def fecha_captura(p):
    m = RE_WA.search(p.name)
    if m:
        a, me, d, h, mi, s, ampm = m.groups()
        h = int(h) % 12 + (12 if ampm.upper() == "PM" else 0)
        return dt.datetime(int(a), int(me), int(d), h, int(mi), int(s))
    return dt.datetime.fromtimestamp(p.stat().st_mtime)


_ocr = None


def texto_ocr(p):
    """Devuelve el texto de una imagen. '' si no se pudo leer."""
    global _ocr
    if p.suffix.lower() not in EXT_IMG:
        return ""
    try:
        if _ocr is None:
            from rapidocr_onnxruntime import RapidOCR
            _ocr = RapidOCR()
        res, _t = _ocr(str(p))
        return " ".join(r[1] for r in res) if res else ""
    except Exception as e:  # OCR ausente o imagen ilegible: no es fatal
        print("   [aviso] OCR fallo en %s: %s" % (p.name, e))
        return ""


def clasificar(p, texto):
    """(area, motivo, puntajes). area None = va a _sin_clasificar."""
    bajo = p.name.lower()
    for patron, area in REGLAS_NOMBRE:
        if re.search(patron, bajo):
            return area, "nombre de archivo ~ /%s/" % patron, {}
    if not texto:
        return None, "sin texto legible (documento binario o OCR vacio)", {}
    t = texto.lower()
    # el OCR pega las palabras: se compara tambien contra el texto normalizado
    norm = re.sub(r"[^a-z0-9]", "", t)
    punt = {}
    for area, grupos in CLAVES.items():
        s = 6 * sum(1 for w in TITULOS.get(area, []) if w in norm)
        for peso, palabras in grupos.items():
            s += peso * sum(1 for w in palabras if w in t)
        punt[area] = s
    orden = sorted(punt.items(), key=lambda kv: -kv[1])
    (a1, p1), (a2, p2) = orden[0], orden[1]
    if p1 >= 3 and (p1 - p2) >= 2:
        return a1, "OCR: %s=%d, 2do %s=%d" % (a1, p1, a2, p2), punt
    return None, "ambiguo (%s=%d vs %s=%d): leer la imagen a ojo" % (a1, p1, a2, p2), punt


def candidatos(destino, origen):
    """Archivos sueltos a clasificar: raiz de I Inf Sem Ventas, raiz de la
    carpeta de la semana, _sin_clasificar, y el --origen si se dio."""
    vistos, out = set(), []
    fuentes = [RAIZ, destino, destino / SIN_CLASIFICAR]
    if origen:
        fuentes.insert(0, pathlib.Path(origen))
    for d in fuentes:
        if not d.is_dir():
            continue
        for p in sorted(d.iterdir()):
            if not p.is_file() or p.resolve() in vistos:
                continue
            if p.suffix.lower() not in EXT_IMG | EXT_DOC:
                continue
            if p.name.startswith(("QVP_", "FUENTES_", "~$", ".")):
                continue
            vistos.add(p.resolve())
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--semana", type=int, required=True)
    ap.add_argument("--anio", type=int, default=dt.date.today().year)
    ap.add_argument("--origen", default=None,
                    help="carpeta extra donde buscar los archivos descargados de WhatsApp")
    ap.add_argument("--raiz", default=None, help="otra raiz (para pruebas)")
    ap.add_argument("--aplicar", action="store_true", help="sin esto solo muestra el plan")
    a = ap.parse_args()

    global RAIZ
    if a.raiz:
        RAIZ = pathlib.Path(a.raiz)
    lun, dom = limites_iso(a.anio, a.semana)
    destino = RAIZ / ("Sem ven %d" % a.semana)
    print("Semana %d de %d  ·  %s a %s" % (a.semana, a.anio, lun, dom))
    print("Destino: %s" % destino)
    print("Modo: %s\n" % ("APLICAR" if a.aplicar else "solo plan (anada --aplicar)"))

    if a.aplicar:
        for sub in [""] + AREAS:
            (destino / sub).mkdir(parents=True, exist_ok=True)

    arch = candidatos(destino, a.origen)
    if not arch:
        print("No hay archivos sueltos que clasificar.")
        print("Revise donde quedaron las descargas de WhatsApp y use --origen.")
        return

    plan, fuera, dudosos = [], [], []
    for p in arch:
        t = texto_ocr(p)
        area, motivo, _ = clasificar(p, t)
        f = fecha_captura(p)
        if not (lun <= f.date() <= dom):
            fuera.append((p, f))
        dest = destino / (area or SIN_CLASIFICAR) / p.name
        plan.append((p, dest, area, motivo, f, t[:160]))
        if area is None:
            dudosos.append(p)

    anch = max(len(p.name) for p, *_ in plan)
    for p, dest, area, motivo, f, _s in plan:
        print("%-*s -> %-24s  %s" % (anch, p.name, area or SIN_CLASIFICAR, motivo))

    print("\n%d archivo(s). Sin clasificar: %d." % (len(plan), len(dudosos)))
    if fuera:
        print("AVISO — fecha fuera de la semana %d (%s a %s):" % (a.semana, lun, dom))
        for p, f in fuera:
            print("   %s  (%s)" % (p.name, f.strftime("%Y-%m-%d %H:%M")))
    if dudosos:
        print("AVISO — lea a ojo estas imagenes y muevalas a mano; el OCR no decide:")
        for p in dudosos:
            print("   %s" % p.name)

    if not a.aplicar:
        return

    movidos = []
    for p, dest, area, motivo, f, muestra in plan:
        if p.resolve() == dest.resolve():
            continue
        if dest.exists():
            print("   [omitido] ya existe en destino: %s" % dest.name)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(p), str(dest))
        movidos.append((dest, area, motivo, f, muestra))
    print("\nMovidos: %d" % len(movidos))

    acta = destino / ("FUENTES_Semana_%d.md" % a.semana)
    lineas = [
        "# Procedencia de las fuentes — Semana %d (%s a %s)" % (a.semana, lun, dom),
        "",
        "**Origen unico de todo el material de esta carpeta:** WhatsApp de la cuenta",
        "**+593 99 387 9355**, chats **«Bs Inmobiliaria Mobijuesa»** y",
        "**«Alfredo Sevilla Ventas QVP»**, en las fechas de la semana %d." % a.semana,
        "",
        "Las imagenes son fotografias de los reportes semanales que cada area publica en",
        "esos chats; los .xlsx/.xlsm/.pptx/.pdf son los adjuntos de los mismos chats.",
        "No hay ninguna fuente de fuera de WhatsApp en esta carpeta.",
        "",
        "| Archivo | Subcarpeta | Capturado | Por que ahi |",
        "|---|---|---|---|",
    ]
    for dest, area, motivo, f, muestra in sorted(movidos, key=lambda x: (x[1] or "", x[0].name)):
        lineas.append("| %s | %s | %s | %s |" % (
            dest.name, area or SIN_CLASIFICAR, f.strftime("%Y-%m-%d %H:%M"),
            motivo.replace("|", "/")))
    lineas += ["", "_Acta generada por `armar_semana.py` el %s._" %
               dt.datetime.now().strftime("%Y-%m-%d %H:%M")]
    acta.write_text("\n".join(lineas), encoding="utf-8")
    print("Acta de procedencia: %s" % acta)


if __name__ == "__main__":
    main()
