# -*- coding: utf-8 -*-
"""
Script de referencia de la skill aceptar-revisiones-docx-y-comentarios.

Acepta track changes (w:ins, w:del, w:rPrChange, w:moveFrom/To, etc.),
elimina comentarios y aplica las recomendaciones sustantivas del revisor
sobre DOCX revisados.

ESTRATEGIA DUAL:
  - Documentos SIN comentarios → limpieza vía regex sobre XML (rápida).
  - Documentos CON comentarios o estructura compleja → vía Word COM
    (más robusto, maneja TCs cruzados que romperían la limpieza regex).

USO:
    Modificar SRC_DIR / DST_DIR / COMENTARIOS_SUSTANTIVOS_POR_ARCHIVO
    para ajustar al caso concreto y ejecutar.
"""
import re
import shutil
import sys
import time
import zipfile
from pathlib import Path
from docx import Document
from docx2pdf import convert as d2p_convert

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ======================================================================
# CONFIGURACIÓN POR CASO (ajustar)
# ======================================================================
SRC_DIR = Path(r"C:\Users\datos\Dropbox\var 91\Neg Inm\1 Proy Belen 2026"
               r"\Tokenizacion Activos Reales - RWA\Matriz de Acuerdos\JRPFM"
               r"\Proyecto Marco Regulatorio Asamblea\00a Carta a Instancias"
               r"\Propuestas por Asesor Asamblea")  # fuente con TC + comentarios
DST_DIR = Path(r"C:\Users\datos\Dropbox\var 91\Neg Inm\1 Proy Belen 2026"
               r"\Tokenizacion Activos Reales - RWA\Matriz de Acuerdos\JRPFM"
               r"\Proyecto Marco Regulatorio Asamblea\00a Carta a Instancias"
               r"\Cartas Listas para Envio")  # destino limpio
SHORT_TMP = Path(r"C:\Users\datos\.notebooklm-extractos\revisiones_tmp")
SHORT_TMP.mkdir(parents=True, exist_ok=True)


# ======================================================================
# ACCIONES SUSTANTIVAS (interpretación de comentarios)
# ======================================================================
def eliminar_seccion_iv_b012(docx_path: Path):
    """B-012: eliminar sección IV PROPUESTA DE ARQUITECTURA INTER-COMISION.

    El revisor (Andrés) marcó: 'No considero apropiado sugerir los procesos
    internos de decisión, la asamblea tiene su mecanismo de gobernanza y el
    que un actor externo lo proponga puede ser contraproducente.'

    Elimina párrafos desde 'IV. PROPUESTA DE ARQUITECTURA INTER-COMISION'
    hasta el final de 'Ley anti-lavado de activos digitales.- ...' inclusive.
    """
    doc = Document(str(docx_path))
    patterns = [
        r"IV\.\s*PROPUESTA\s*DE\s*ARQUITECTURA\s*INTER[- ]COMISI[OÓ]N",
        r"La\s+FBSE\s+somete\s+a\s+su\s+consideraci[oó]n\s+la\s+siguiente\s+arquitectura\s+de\s+coordinaci[oó]n\s+inter[- ]comisi[oó]n",
        r"Plano\s*I\s*-\s*LOFPD\.\-\s*Aprobaci[oó]n\s+conjunta",
        r"Plano\s*II\s*-\s*Reforma\s+COMYF\s*/\s*LMV\s*/\s*COPLAFIP\.\-\s*Competencia",
        r"Plano\s*III\s*-\s*Reglamento\s+operativo\s+IBPP\s*/\s*EcuaLedger\s+Sober[ae]ma\.\-\s*Competencia",
        r"Ley\s+anti[- ]lavado\s+de\s+activos\s+digitales\.\-\s*Competencia\s+primaria",
    ]
    to_remove = []
    for p in doc.paragraphs:
        t = p.text or ""
        for pat in patterns:
            if re.search(pat, t, re.IGNORECASE | re.DOTALL):
                to_remove.append(p)
                break
    for p in to_remove:
        el = p._element
        el.getparent().remove(el)
    doc.save(str(docx_path))
    return len(to_remove)


COMENTARIOS_SUSTANTIVOS_POR_ARCHIVO = {
    "B-011_Comision_Regimen_Economico_y_Tributario.docx": [],  # cosméticos
    "B-012_Comision_Soberania_Integral.docx": [eliminar_seccion_iv_b012],
    "B-013_Consejo_de_Administracion_Legislativa_CAL.docx": [],
    "B-014_Ministerio_de_Telecomunicaciones_MINTEL.docx": [],
    "B-015_Presidencia_de_la_Republica.docx": [],
}


# ======================================================================
# ESTRATEGIA 1: Vía Word COM (la más robusta — usa Word para todo)
# ======================================================================
def accept_revisions_via_word(src: Path, dst: Path):
    """Usa Word COM para abrir el doc, aceptar todas las revisiones,
    eliminar todos los comentarios y guardar limpio. La estrategia más
    robusta — Word maneja correctamente todos los casos extremos.

    Trabaja en un short-path temporal para evitar el límite de 255 chars.
    """
    import pythoncom
    import win32com.client

    name = src.stem
    short_src = SHORT_TMP / f"{name}_in.docx"
    short_dst = SHORT_TMP / f"{name}_out.docx"
    shutil.copy(str(src), str(short_src))
    time.sleep(0.5)

    pythoncom.CoInitialize()
    word = win32com.client.gencache.EnsureDispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0  # wdAlertsNone
    try:
        doc = word.Documents.Open(str(short_src), ConfirmConversions=False)
        # Aceptar todas las revisiones
        n_rev = doc.Revisions.Count
        if n_rev:
            doc.Revisions.AcceptAll()
        # Eliminar todos los comentarios
        n_cm = doc.Comments.Count
        if n_cm:
            while doc.Comments.Count > 0:
                doc.Comments.Item(1).Delete()
        # Guardar como nuevo DOCX limpio (16 = wdFormatXMLDocument)
        doc.SaveAs2(str(short_dst), FileFormat=16)
        doc.Close(SaveChanges=0)
        print(f"    [Word COM] revisiones aceptadas: {n_rev}  comentarios eliminados: {n_cm}")
    finally:
        word.Quit()
        pythoncom.CoUninitialize()

    # Copiar de vuelta
    shutil.copy(str(short_dst), str(dst))
    short_src.unlink(missing_ok=True)
    short_dst.unlink(missing_ok=True)


# ======================================================================
# ESTRATEGIA 2: Vía XML/Regex (rápida, solo para casos simples)
# ======================================================================
def accept_track_changes_xml(doc_xml: str) -> str:
    """Acepta todas las revisiones a nivel XML.

    Útil cuando los TCs no cruzan límites de párrafo y no hay comments.xml.
    """
    # 1) Eliminar w:del y w:moveFrom completos
    for tag in ("w:del", "w:moveFrom"):
        doc_xml = re.sub(rf"<{tag}\s[^>]*>.*?</{tag}>", "", doc_xml, flags=re.DOTALL)
        doc_xml = re.sub(rf"<{tag}\s[^/]*?/>", "", doc_xml)
    # 2) Mantener contenido de w:ins y w:moveTo
    for tag in ("w:ins", "w:moveTo"):
        doc_xml = re.sub(
            rf"<{tag}\s[^>]*>(.*?)</{tag}>", r"\1", doc_xml, flags=re.DOTALL
        )
    # 3) Eliminar todos los *Change (revisiones de formato)
    for tag in (
        "w:rPrChange",
        "w:pPrChange",
        "w:sectPrChange",
        "w:tblPrChange",
        "w:trPrChange",
        "w:tcPrChange",
        "w:tblGridChange",
        "w:numberingChange",
        "w:cellIns",
        "w:cellDel",
        "w:cellMerge",
    ):
        doc_xml = re.sub(
            rf"<{tag}\s[^>]*>.*?</{tag}>", "", doc_xml, flags=re.DOTALL
        )
        doc_xml = re.sub(rf"<{tag}\s[^/]*?/>", "", doc_xml)
    # 4) Rangos huérfanos
    for tag in (
        "w:moveFromRangeStart",
        "w:moveFromRangeEnd",
        "w:moveToRangeStart",
        "w:moveToRangeEnd",
        "w:customXmlInsRangeStart",
        "w:customXmlInsRangeEnd",
        "w:customXmlDelRangeStart",
        "w:customXmlDelRangeEnd",
    ):
        doc_xml = re.sub(rf"<{tag}\s[^/]*?/>", "", doc_xml)
    return doc_xml


def docx_to_pdf_via_short(docx_path: Path):
    """Convierte a PDF usando path corto."""
    name = docx_path.stem
    short_docx = SHORT_TMP / f"{name}.docx"
    short_pdf = SHORT_TMP / f"{name}.pdf"
    pdf_path = docx_path.with_suffix(".pdf")
    shutil.copy(str(docx_path), str(short_docx))
    time.sleep(0.5)
    d2p_convert(str(short_docx), str(short_pdf))
    time.sleep(0.5)
    shutil.copy(str(short_pdf), str(pdf_path))
    short_docx.unlink(missing_ok=True)
    short_pdf.unlink(missing_ok=True)
    print(f"    PDF OK: {pdf_path.name}")


def has_comments_or_complex_tracking(src: Path) -> bool:
    """Determina si conviene usar Word COM (presencia de comments.xml o muchos TCs)."""
    with zipfile.ZipFile(src, "r") as z:
        names = z.namelist()
        if "word/comments.xml" in names:
            return True
        # Si tiene más de 20 inserciones/deleciones, ir por COM (más seguro)
        doc = z.read("word/document.xml").decode("utf-8", errors="replace")
        n_ins = len(re.findall(r"<w:ins\s", doc))
        n_del = len(re.findall(r"<w:del\s", doc))
        if n_ins + n_del > 20:
            return True
    return False


def process_simple_xml(src: Path, dst: Path):
    """Procesamiento simple vía XML para docs sin comentarios y pocos cambios."""
    with zipfile.ZipFile(src, "r") as zin:
        items = {name: zin.read(name) for name in zin.namelist()}
    doc_xml = items.get("word/document.xml", b"").decode("utf-8", errors="replace")
    doc_xml = accept_track_changes_xml(doc_xml)
    items["word/document.xml"] = doc_xml.encode("utf-8")
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in items.items():
            zout.writestr(name, data)


def process(src: Path, dst: Path, sustantive_actions: list):
    """Procesa un DOCX."""
    print(f"\n>>> {src.name}")
    if not src.exists():
        print(f"    [NO EXISTE]")
        return
    use_com = has_comments_or_complex_tracking(src)
    print(f"    Estrategia: {'Word COM' if use_com else 'XML/regex'}")
    if use_com:
        accept_revisions_via_word(src, dst)
    else:
        process_simple_xml(src, dst)
    # Aplicar acciones sustantivas (sobre el dst ya limpio)
    for action in sustantive_actions:
        try:
            n = action(dst)
            print(f"    [acción {action.__name__}] {n} párrafos eliminados")
        except Exception as e:
            print(f"    [acción {action.__name__}] ERROR: {e}")
    # Convertir a PDF
    try:
        docx_to_pdf_via_short(dst)
    except Exception as e:
        print(f"    WARN PDF: {str(e)[:120]}")


if __name__ == "__main__":
    print("=" * 70)
    print("ACEPTAR REVISIONES DOCX + COMENTARIOS (estrategia dual)")
    print("=" * 70)
    for fname, actions in COMENTARIOS_SUSTANTIVOS_POR_ARCHIVO.items():
        src = SRC_DIR / fname
        dst = DST_DIR / fname
        process(src, dst, actions)
    print("\n" + "=" * 70)
    print("FIN")
    print("=" * 70)
