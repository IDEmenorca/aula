#!/usr/bin/env python3
"""Extreu les imatges incrustades d'un PDF, per poder-les revisar i col·locar.

S'usa per recuperar les captures dels manuals antics en PDF. No forma part de
la construcció del lloc: depèn de PyMuPDF, que a propòsit NO és a
requirements.txt perquè no cal per fer `mkdocs build`.

    pip install pymupdf
    python tools/extreu-imatges-pdf.py _origen/manual-visor-generic.pdf sortida/

Deixa a la carpeta de sortida un fitxer per imatge, anomenat
`pNN-iMM-AMPLADAxALCADA.png`, i escriu un inventari per pantalla. Els noms
duen la pàgina i la mida perquè després es puguin identificar i reanomenar
segons l'esquema de CAPTURES.md.

No reanomena ni col·loca res automàticament: quina imatge correspon a quin
apartat s'ha de decidir mirant-les.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

try:
    import pymupdf
except ImportError:  # noms antics de la biblioteca
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit("Cal PyMuPDF: pip install pymupdf")


def extreu(pdf: pathlib.Path, sortida: pathlib.Path, minim: int) -> int:
    sortida.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)

    desades = 0
    descartades = 0

    print(f"{pdf.name}: {doc.page_count} pàgines\n")
    print(f"{'fitxer':<34} {'mida':<12} {'bytes':>9}")
    print("-" * 58)

    for num in range(doc.page_count):
        for idx, info in enumerate(doc[num].get_images(full=True), start=1):
            xref = info[0]
            try:
                base = doc.extract_image(xref)
            except Exception as e:                      # imatge malmesa
                print(f"  p{num + 1:02d} i{idx:02d}: no s'ha pogut extreure ({e})")
                continue

            dades = base["image"]
            ample, alt = base.get("width", 0), base.get("height", 0)

            # Les icones minúscules no serveixen com a captura.
            if ample < minim or alt < minim:
                descartades += 1
                continue

            nom = f"p{num + 1:02d}-i{idx:02d}-{ample}x{alt}.{base['ext']}"
            desti = sortida / nom
            desti.write_bytes(dades)
            print(f"{nom:<34} {f'{ample}x{alt}':<12} {len(dades):>9,}")
            desades += 1

    doc.close()
    print("-" * 58)
    print(f"{desades} imatges desades a {sortida}")
    if descartades:
        print(f"{descartades} descartades per ser més petites de {minim} px")
    return 0 if desades else 1


def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("pdf", type=pathlib.Path, help="PDF d'origen")
    p.add_argument("sortida", type=pathlib.Path, help="carpeta on deixar les imatges")
    p.add_argument("--minim", type=int, default=60,
                   help="descarta les imatges més petites d'aquests píxels (per defecte 60)")
    a = p.parse_args()

    if not a.pdf.is_file():
        sys.exit(f"No hi ha cap fitxer a {a.pdf}")
    return extreu(a.pdf, a.sortida, a.minim)


if __name__ == "__main__":
    sys.exit(main())
