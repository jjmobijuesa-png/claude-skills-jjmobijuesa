"""Validador post-generacion para documentos Word.

Escanea un .docx y reporta:
- Anchos de tabla vs ancho util de la seccion
- Tablas con autofit (red flag)
- Tablas sin centrar
- Tablas que se desbordan
- Recomendacion de rotar a landscape si > 80% de tablas exceden portrait

Uso:
    python page_layout_validator.py archivo.docx
"""
import sys
from pathlib import Path
from docx import Document
from docx.shared import Emu


EMU_PER_CM = 360000


def emu_to_cm(emu):
    if emu is None: return None
    return emu / EMU_PER_CM


def validate(doc_path):
    p = Path(doc_path)
    if not p.exists():
        print(f"ERROR: no existe {p}")
        return 1
    doc = Document(p)
    print(f"Validando: {p.name}")
    print("=" * 70)

    issues = []
    table_overflows = 0
    total_tables = 0
    landscape_tables_in_portrait = 0

    for s_idx, section in enumerate(doc.sections):
        page_w = emu_to_cm(section.page_width)
        page_h = emu_to_cm(section.page_height)
        ml = emu_to_cm(section.left_margin)
        mr = emu_to_cm(section.right_margin)
        mt = emu_to_cm(section.top_margin)
        mb = emu_to_cm(section.bottom_margin)
        usable_w = page_w - ml - mr if page_w and ml is not None and mr is not None else None
        is_portrait = page_h > page_w

        print(f"\nSeccion {s_idx + 1}:")
        print(f"  Pagina: {page_w:.2f} x {page_h:.2f} cm "
              f"({'PORTRAIT' if is_portrait else 'LANDSCAPE'})")
        print(f"  Margenes: top={mt:.2f} bottom={mb:.2f} left={ml:.2f} right={mr:.2f} cm")
        print(f"  Ancho util: {usable_w:.2f} cm")

    print("\nTablas:")
    for t_idx, table in enumerate(doc.tables):
        total_tables += 1
        # Sumar anchos de columna
        col_widths = []
        for col in table.columns:
            w = emu_to_cm(col.width) if col.width else None
            col_widths.append(w)
        total_w = sum(w for w in col_widths if w is not None)

        # Centrada?
        alignment = table.alignment
        centered = (alignment is not None and "CENTER" in str(alignment))

        # Autofit?
        autofit = table.autofit

        # Comparar con ancho util de la primera seccion (la mas comun)
        first_section = doc.sections[0]
        page_w_s = emu_to_cm(first_section.page_width)
        ml_s = emu_to_cm(first_section.left_margin)
        mr_s = emu_to_cm(first_section.right_margin)
        usable_w_s = page_w_s - ml_s - mr_s
        is_portrait_s = emu_to_cm(first_section.page_height) > page_w_s

        overflow = total_w > usable_w_s + 0.05  # tolerancia 0.5mm

        status = "OK"
        flags = []
        if autofit:
            flags.append("autofit=True")
        if not centered:
            flags.append("sin centrar")
        if overflow:
            flags.append(f"DESBORDE +{(total_w - usable_w_s):.2f}cm")
            table_overflows += 1

        if is_portrait_s and total_w > 17.5:
            landscape_tables_in_portrait += 1

        if flags:
            status = "WARNING: " + ", ".join(flags)
            issues.append((t_idx, total_w, status))

        col_w_str = ", ".join(f"{w:.1f}" if w is not None else "?" for w in col_widths)
        print(f"  Tabla {t_idx + 1:>3}: {len(table.rows)}r x {len(table.columns)}c "
              f"| anchos=[{col_w_str}] cm | total={total_w:.2f} cm | {status}")

    print("\n" + "=" * 70)
    print("RESUMEN")
    print(f"  Total de tablas: {total_tables}")
    print(f"  Tablas con problemas: {len(issues)}")
    print(f"  Tablas que se desbordan: {table_overflows}")
    if table_overflows > 0 and total_tables > 0 and table_overflows / total_tables > 0.8:
        print("  RECOMENDACION: > 80% de tablas se desbordan en PORTRAIT — considerar LANDSCAPE.")
    if len(issues) == 0:
        print("  RESULTADO: TODOS LOS CUADROS ESTAN ENCUADRADOS. Documento listo para entrega.")
        return 0
    else:
        print("  RESULTADO: HAY PROBLEMAS — ver detalle arriba.")
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(validate(sys.argv[1]))
