# -*- coding: utf-8 -*-
"""
xlsx_to_a4_pdf.py
Clean one or more .xlsx workbooks and export them as a SINGLE A4-portrait PDF,
merging all sheets in the given order. Uses Microsoft Excel via COM for
high-fidelity page setup and native PDF export, then pypdf to merge.

See SKILL.md for usage.
"""
import sys, os, re, json, argparse, tempfile

# ---- text cleaning ---------------------------------------------------------
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF"   # pictographs / emoji
    "\U00002600-\U000027BF"    # misc symbols + dingbats (warning, check, cross)
    "\U00002B00-\U00002BFF"    # arrows/stars block (decorative)
    "\U0000FE00-\U0000FE0F"    # variation selectors
    "\U0000231A-\U0000231B"    # watch
    "\U000023E0-\U000023FF]"   # clock/timer technical symbols (incl. stopwatch)
)
# source-citation residue: lowercase letters/dots inside brackets, e.g. [grepalma]
CITE = re.compile(r"\s*\[[a-z]+(?:[._\-][a-z0-9]+)*\]")


def col_letter(n: int) -> str:
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def clean_text(s: str) -> str:
    s2 = EMOJI.sub("", s)
    s2 = CITE.sub("", s2)
    s2 = re.sub(r"[ \t]{2,}", " ", s2)
    # tidy "( word" left after removing an emoji right after an open paren
    s2 = s2.replace("( ", "(").replace(" )", ")")
    return s2.strip()


# ---- Excel constants -------------------------------------------------------
XL_PORTRAIT, XL_LANDSCAPE = 1, 2
XL_PAPER_A4 = 9
XL_TYPE_PDF = 0
XL_OPENXML = 51


def process(files, out_pdf, cleaned_dir, replacements, maxw, orientation, tmpdir,
            fill_units=100.0):
    import win32com.client as win32

    excel = win32.DispatchEx("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False
    excel.ScreenUpdating = False
    orient = XL_PORTRAIT if orientation == "portrait" else XL_LANDSCAPE
    pdfs = []
    try:
        for f in files:
            f = os.path.abspath(f)
            base = os.path.splitext(os.path.basename(f))[0]
            repl = replacements.get(os.path.basename(f), {})
            wb = excel.Workbooks.Open(f)
            try:
                for ws in wb.Worksheets:
                    # 1) remove all shapes / pictures / wordart
                    try:
                        for i in range(ws.Shapes.Count, 0, -1):
                            ws.Shapes.Item(i).Delete()
                    except Exception:
                        pass

                    ur = ws.UsedRange
                    nrows = int(ur.Rows.Count)
                    ncols = int(ur.Columns.Count)
                    r0 = int(ur.Row)
                    c0 = int(ur.Column)

                    # 2) clean text + apply per-cell replacements, and track the
                    #    bounding box of cells that actually hold content (so we
                    #    can drop trailing empty columns/rows from the print area)
                    min_r = min_c = 10 ** 9
                    max_r = max_c = -1
                    for rr in range(1, nrows + 1):
                        for cc in range(1, ncols + 1):
                            cell = ur.Cells(rr, cc)
                            v = cell.Value
                            if v is None or (isinstance(v, str) and v == ""):
                                continue
                            ar = r0 + rr - 1
                            ac = c0 + cc - 1
                            if ar < min_r: min_r = ar
                            if ar > max_r: max_r = ar
                            if ac < min_c: min_c = ac
                            if ac > max_c: max_c = ac
                            if not isinstance(v, str) or not v:
                                continue
                            addr = "%s%d" % (col_letter(ac), ar)
                            if addr in repl:
                                nv = repl[addr]
                                cell.Value = "" if nv == "__CLEAR__" else nv
                            else:
                                nv = clean_text(v)
                                if nv != v:
                                    cell.Value = nv

                    if max_c < 0:   # empty sheet
                        continue

                    # 3) layout / fit (operate on the content columns only)
                    ws.Cells.EntireColumn.AutoFit()
                    for ac in range(min_c, max_c + 1):
                        col = ws.Columns(ac)
                        try:
                            if col.ColumnWidth > maxw:
                                col.ColumnWidth = maxw
                                col.WrapText = True
                        except Exception:
                            pass
                    # fill the printable width: if the content columns are
                    # narrower than the A4 printable area, scale them up
                    # proportionally so the table reads across the full width.
                    if fill_units and fill_units > 0:
                        try:
                            total = 0.0
                            for ac in range(min_c, max_c + 1):
                                total += float(ws.Columns(ac).ColumnWidth)
                            if total > 0 and total < fill_units:
                                factor = min(fill_units / total, 3.0)
                                if factor > 1.02:
                                    for ac in range(min_c, max_c + 1):
                                        col = ws.Columns(ac)
                                        col.ColumnWidth = float(col.ColumnWidth) * factor
                        except Exception:
                            pass
                    ws.Cells.EntireRow.AutoFit()

                    # restrict the print area to the real content bounding box
                    try:
                        ws.PageSetup.PrintArea = "%s%d:%s%d" % (
                            col_letter(min_c), min_r, col_letter(max_c), max_r)
                    except Exception:
                        pass

                    ps = ws.PageSetup
                    ps.Orientation = orient
                    ps.PaperSize = XL_PAPER_A4
                    ps.Zoom = False
                    ps.FitToPagesWide = 1
                    ps.FitToPagesTall = False
                    ps.LeftMargin = excel.InchesToPoints(0.4)
                    ps.RightMargin = excel.InchesToPoints(0.4)
                    ps.TopMargin = excel.InchesToPoints(0.5)
                    ps.BottomMargin = excel.InchesToPoints(0.5)
                    ps.HeaderMargin = excel.InchesToPoints(0.2)
                    ps.FooterMargin = excel.InchesToPoints(0.2)
                    ps.CenterHorizontally = True
                    ps.PrintGridlines = False
                    ps.CenterFooter = "&P de &N"

                # 4) save cleaned xlsx copy
                if cleaned_dir:
                    os.makedirs(cleaned_dir, exist_ok=True)
                    cleaned_path = os.path.abspath(
                        os.path.join(cleaned_dir, base + " (limpio).xlsx"))
                    wb.SaveAs(cleaned_path, FileFormat=XL_OPENXML)

                # 5) export to per-file PDF
                pdf_tmp = os.path.abspath(os.path.join(tmpdir, base + ".pdf"))
                wb.ExportAsFixedFormat(XL_TYPE_PDF, pdf_tmp)
                pdfs.append(pdf_tmp)
            finally:
                wb.Close(SaveChanges=False)
    finally:
        excel.Quit()

    # 6) merge in order
    from pypdf import PdfReader, PdfWriter
    writer = PdfWriter()
    for p in pdfs:
        for page in PdfReader(p).pages:
            writer.add_page(page)
    os.makedirs(os.path.dirname(os.path.abspath(out_pdf)), exist_ok=True)
    with open(out_pdf, "wb") as fh:
        writer.write(fh)
    return out_pdf, pdfs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", required=True,
                    help="xlsx paths in order, separated by ';'")
    ap.add_argument("--out", required=True, help="output merged PDF path")
    ap.add_argument("--cleaned-dir", default=None,
                    help="dir to save cleaned .xlsx copies")
    ap.add_argument("--replacements", default=None,
                    help="JSON file with per-cell replacements")
    ap.add_argument("--maxw", type=float, default=48.0)
    ap.add_argument("--orientation", choices=["portrait", "landscape"],
                    default="portrait")
    ap.add_argument("--fill-units", type=float, default=100.0,
                    help="target total column width (in char units) to fill the "
                         "printable width; 0 disables width-fill. Default 100 (A4).")
    ap.add_argument("--tmp", default=None, help="temp dir for per-file PDFs")
    args = ap.parse_args()

    files = [p.strip() for p in args.inputs.split(";") if p.strip()]
    for f in files:
        if not os.path.exists(f):
            print("MISSING INPUT:", f, file=sys.stderr)
            sys.exit(2)

    replacements = {}
    if args.replacements:
        with open(args.replacements, "r", encoding="utf-8") as fh:
            replacements = json.load(fh)

    tmpdir = args.tmp or tempfile.mkdtemp(prefix="xlsx2pdf_")
    os.makedirs(tmpdir, exist_ok=True)

    out, pdfs = process(files, args.out, args.cleaned_dir, replacements,
                        args.maxw, args.orientation, tmpdir, args.fill_units)

    from pypdf import PdfReader
    npages = len(PdfReader(out).pages)
    print("OK  ->", out)
    print("Pages:", npages)
    for p in pdfs:
        print("  section:", os.path.basename(p))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
