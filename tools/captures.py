#!/usr/bin/env python3
"""Gestiona els marcadors de captura pendent del lloc.

Cada captura que falta és una admonició dins d'una pàgina:

    !!! note "Captura pendent - `img/13-graella.png`"
        Descripció del que ha de mostrar la captura.

        Peu de foto previst: *Text del peu*

Aquest script fa dues coses:

    python tools/captures.py --llista
        Escriu CAPTURES.md a l'arrel: la llista ordenada de totes les captures
        que falten, amb la ruta exacta on ha d'anar cada fitxer. És el document
        per a qui hagi de fer les captures.

    python tools/captures.py --insereix
        Per a cada marcador, mira si el fitxer d'imatge ja existeix. Si hi és,
        substitueix el marcador pel bloc <figure> corresponent. Si no, el deixa
        estar. Es pot executar tantes vegades com calgui, a mesura que van
        arribant captures.

    python tools/captures.py --insereix --prova
        Igual, però només diu què faria, sense tocar cap fitxer.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ARREL = pathlib.Path(__file__).resolve().parent.parent
DOCS = ARREL / "docs"

TITOL = re.compile(r'^!!! note "Captura pendent [—-] `(?P<src>[^`]+)`"\s*$')
PEU = re.compile(r"^\s*Peu de foto previst: \*(?P<peu>.+)\*\s*$")


class Marcador:
    def __init__(self, pagina, inici, fi, src, descripcio, peu):
        self.pagina = pagina          # Path de la pàgina .md
        self.inici = inici            # índex de la primera línia del bloc
        self.fi = fi                  # índex següent al bloc
        self.src = src                # p. ex. "img/13-graella.png"
        self.descripcio = descripcio
        self.peu = peu

    @property
    def desti(self) -> pathlib.Path:
        """Ruta absoluta on ha d'anar el fitxer d'imatge."""
        return (self.pagina.parent / self.src).resolve()

    @property
    def existeix(self) -> bool:
        return self.desti.is_file()

    @property
    def ordre(self) -> tuple:
        """Ordena per número del nom de fitxer; els numero jo en escriure'ls."""
        nom = pathlib.PurePosixPath(self.src).name
        m = re.match(r"(\d+)", nom)
        return (int(m.group(1)) if m else 9999, str(self.pagina))

    def bloc_figura(self) -> list[str]:
        linies = [
            "<figure markdown>",
            f"  ![{self.descripcio}]({self.src})" + "{ .captura }",
        ]
        if self.peu:
            linies.append(f"  <figcaption>{self.peu}</figcaption>")
        linies.append("</figure>")
        return linies


def llegeix(pagina: pathlib.Path) -> list[str]:
    return pagina.read_text(encoding="utf-8").split("\n")


def marcadors_de(pagina: pathlib.Path) -> list[Marcador]:
    linies = llegeix(pagina)
    trobats = []
    i = 0
    while i < len(linies):
        m = TITOL.match(linies[i])
        if not m:
            i += 1
            continue

        # El cos de l'admonició són les línies indentades que segueixen,
        # incloent-hi línies en blanc intercalades.
        j = i + 1
        cos = []
        while j < len(linies):
            linia = linies[j]
            if linia.strip() == "":
                # Blanc: només forma part del bloc si després ve més indentació.
                seguent = linies[j + 1] if j + 1 < len(linies) else ""
                if seguent.startswith("    "):
                    cos.append(linia)
                    j += 1
                    continue
                break
            if not linia.startswith("    "):
                break
            cos.append(linia)
            j += 1

        descripcio, peu = [], None
        for linia in cos:
            p = PEU.match(linia)
            if p:
                peu = p.group("peu").strip()
            elif linia.strip():
                descripcio.append(linia.strip())

        text = " ".join(descripcio).strip()
        if text.endswith("."):
            text = text[:-1]

        trobats.append(
            Marcador(pagina, i, j, m.group("src"), text, peu)
        )
        i = j
    return trobats


def tots() -> list[Marcador]:
    trobats = []
    for pagina in sorted(DOCS.rglob("*.md")):
        trobats.extend(marcadors_de(pagina))
    trobats.sort(key=lambda x: x.ordre)
    return trobats


def fes_llista() -> int:
    marcadors = tots()
    if not marcadors:
        print("No queda cap captura pendent.")
        return 0

    per_pagina: dict[pathlib.Path, list[Marcador]] = {}
    for m in marcadors:
        per_pagina.setdefault(m.pagina, []).append(m)

    linies = [
        "# Captures pendents",
        "",
        "Llista generada automàticament amb `python tools/captures.py --llista`.",
        "No l'editis a mà: es regenera.",
        "",
        f"Queden **{len(marcadors)} captures** per fer.",
        "",
        "## Com afegir-les",
        "",
        "1. Fes la captura del visor.",
        "2. Desa-la amb **exactament** el nom i a **exactament** la carpeta que",
        "   indica la columna «Fitxer». Les carpetes ja existeixen.",
        "3. Executa `python tools/captures.py --insereix`.",
        "4. Comprova-ho amb `mkdocs serve` i fes el commit.",
        "",
        "No cal fer-les totes de cop: l'script insereix les que hi hagi i deixa",
        "la resta com a marcadors.",
        "",
        "> **Consell.** Fes les captures amb la finestra prou ampla i sense dades",
        "> personals a la vista. Retalla-les a l'element que es descriu: una captura",
        "> de pantalla sencera per ensenyar un botó no s'entén.",
        "",
    ]

    for pagina in sorted(per_pagina, key=lambda p: per_pagina[p][0].ordre):
        rel = pagina.relative_to(ARREL).as_posix()
        linies.append(f"## `{rel}`")
        linies.append("")
        linies.append("| Fitxer | Què ha de mostrar |")
        linies.append("|---|---|")
        for m in per_pagina[pagina]:
            desti = m.desti.relative_to(ARREL).as_posix()
            estat = " ✅" if m.existeix else ""
            linies.append(f"| `{desti}`{estat} | {m.descripcio} |")
        linies.append("")

    desti = ARREL / "CAPTURES.md"
    desti.write_text("\n".join(linies), encoding="utf-8", newline="\n")
    print(f"Escrit {desti.relative_to(ARREL)} amb {len(marcadors)} captures.")
    return 0


def fes_insercio(prova: bool) -> int:
    inserides = 0
    pendents = 0

    for pagina in sorted(DOCS.rglob("*.md")):
        marcadors = marcadors_de(pagina)
        llestos = [m for m in marcadors if m.existeix]
        pendents += len(marcadors) - len(llestos)
        if not llestos:
            continue

        linies = llegeix(pagina)
        # De baix a dalt, per no invalidar els índexs.
        for m in sorted(llestos, key=lambda x: x.inici, reverse=True):
            linies[m.inici:m.fi] = m.bloc_figura()
            print(f"  {m.src}  ->  {pagina.relative_to(ARREL).as_posix()}")
            inserides += 1

        if not prova:
            pagina.write_text("\n".join(linies), encoding="utf-8", newline="\n")

    if inserides == 0:
        print("Cap imatge nova trobada al disc.")
    else:
        verb = "S'inseririen" if prova else "Inserides"
        print(f"\n{verb} {inserides} captures.")
    print(f"En queden {pendents} de pendents.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--llista", action="store_true",
                   help="genera CAPTURES.md amb les captures que falten")
    g.add_argument("--insereix", action="store_true",
                   help="insereix les captures que ja siguin al disc")
    p.add_argument("--prova", action="store_true",
                   help="amb --insereix: només diu què faria")
    a = p.parse_args()

    if a.llista:
        return fes_llista()
    return fes_insercio(a.prova)


if __name__ == "__main__":
    sys.exit(main())
