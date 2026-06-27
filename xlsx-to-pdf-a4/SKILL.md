---
name: xlsx-to-pdf-a4
description: "Convert each sheet of an .xlsx or .xls workbook to a separate A4-landscape PDF, one PDF per sheet, with auto-sized font and pagination for long sheets. Use when you need to feed Excel data into a system that only accepts PDFs (e.g. NotebookLM, which rejects xlsx/csv uploads), or when you want each sheet as a printable A4 page. Triggers: 'convert Excel to PDF', 'each sheet to PDF', 'xlsx to A4 PDF', 'subir Excel a NotebookLM' (since NotebookLM doesn't accept xlsx, this is the workaround), 'convertir hojas a PDF'. Optionally tags each PDF with a PBC code prefix in the filename and embeds the tag in the header."
user-invocable: true
---

# Excel → A4-landscape PDF (one PDF per sheet)

NotebookLM accepts PDF and DOCX but not XLSX, XLS, or CSV. Other systems may have similar restrictions. This skill renders each sheet of a workbook as a standalone A4-landscape PDF that any downstream system can ingest.

## Setup

- Python with `openpyxl` (.xlsx), `xlrd==1.2.0` (.xls), and `reportlab`. Install once:
  ```bash
  pip install openpyxl "xlrd==1.2.0" reportlab
  ```

## What it produces

For each workbook, one PDF per sheet, named:
```
<output_prefix>_<workbook_stem>_<sheet_name>.pdf
```

Each PDF has:
- A4 landscape page size (297 × 210 mm)
- Header: optional category line + workbook title + sheet name
- Table of all the sheet's data, with header row in dark navy and body in light grey grid
- Auto font size based on column count: ≤6 cols → 9pt, ≤10 → 7pt, ≤14 → 6pt, more → 5pt
- Pagination: long sheets are split into chunks of 60 rows per page with the header row repeated

## Usage

```bash
python convert.py \
    --input "workbook.xlsx" \
    --output-dir "./out" \
    [--prefix "PBC-A5"] \
    [--header-tag "BLOQUE A - Registros Contables"]
```

The `--prefix` is prepended to each output filename so the PDFs auto-sort into groups in any source list. The `--header-tag` appears as a subheading on each page.

## Files in this skill

- `scripts/convert.py` — the converter. Handles both .xlsx and .xls; trims trailing blank rows; survives non-ASCII content.

## Limits and edge cases

- Cells with formulas are read with `data_only=True` (openpyxl) which uses the last cached value. If the workbook was never opened in Excel after the formula was added, the cache may be empty — open the file in Excel once and re-save.
- Sheets with merged cells render flat (the merged value appears only in the top-left cell, other cells show empty).
- Sheets with more than ~3,000 rows produce PDFs of 500KB+ and may exceed NotebookLM's per-source rate limit on the first upload — retry once if the first add fails.
- Cells with embedded images, charts, or pivot tables: only the table values are extracted; visual elements are lost. Use a print-to-PDF route from Excel itself if visuals matter.

## Why one PDF per sheet (and not one multi-page PDF)

For ingestion into systems like NotebookLM where each PDF becomes a separately retrievable source, one-per-sheet gives more granular citation and the AI can quote a specific sheet without dragging in unrelated tabs.
