#!/usr/bin/env python3
"""Comprova que cada selector del CSS propi encara troba alguna cosa al lloc.

El problema que resol: el CSS propi depèn de l'estructura HTML que genera
Material. Quan es toca una opció del tema, aquesta estructura canvia i un
selector pot deixar d'aplicar-se **sense donar cap error**. La pàgina es
construeix, es publica, i l'estil simplement no hi és. Va passar en activar
`navigation.tabs`: les seccions del menú van baixar un nivell i el selector
dels ròtuls, que exigia ser fill directe de l'arrel, va morir en silenci.

`mkdocs build --strict` no ho detecta: per a MkDocs el CSS és un fitxer opac
que copia tal qual.

    python tools/comprova-estils.py

Llegeix docs/stylesheets/extra.css, n'extreu els selectors i comprova que
cadascun trobi almenys un element a les pàgines de site/. Torna 1 si n'hi ha
cap que no trobi res.

Cal haver construït el lloc abans (`mkdocs build`). Depèn de beautifulsoup4 i
soupsieve, que són a requirements-dev.txt i no a requirements.txt: no calen
per construir el lloc, només per comprovar-lo.
"""

from __future__ import annotations

import pathlib
import re
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Cal beautifulsoup4: pip install -r requirements-dev.txt")

ARREL = pathlib.Path(__file__).resolve().parent.parent
CSS = ARREL / "docs" / "stylesheets" / "extra.css"
SITE = ARREL / "site"

# Selectors que a propòsit encara no troben res, amb el motiu. Si un d'aquests
# comença a trobar elements, es diu però NO es falla: que algú comenci a fer
# servir un estil és una bona notícia, no un error que hagi d'aturar la
# publicació. Només cal recordar-se de treure'l d'aquí.
PREVISTOS_BUITS: dict[str, str] = {
    # De moment, cap. Els contenidors .iframe-wrap ja s'usen al mòdul 1.
}

# Pseudoclasses d'estat: no es poden comprovar sobre HTML estàtic, es treuen
# del selector abans de provar-lo.
ESTATS = re.compile(
    r"::?(hover|focus|focus-visible|focus-within|active|visited|target|"
    r"before|after|placeholder|selection|marker|first-line|first-letter)\b"
)

COMENTARIS = re.compile(r"/\*.*?\*/", re.DOTALL)


def selectors_de(css: str) -> list[str]:
    """Extreu els selectors del CSS, entrant dins dels blocs @media."""
    css = COMENTARIS.sub("", css)
    trobats: list[str] = []

    i = 0
    while i < len(css):
        obre = css.find("{", i)
        if obre == -1:
            break

        cap = css[i:obre].strip()
        # Final del bloc que correspon a aquesta obertura
        prof, j = 1, obre + 1
        while j < len(css) and prof:
            if css[j] == "{":
                prof += 1
            elif css[j] == "}":
                prof -= 1
            j += 1

        if cap.startswith("@"):
            if cap.startswith(("@media", "@supports")):
                trobats.extend(selectors_de(css[obre + 1:j - 1]))
            # @font-face, @import i companyia no duen selectors
        else:
            for s in cap.split(","):
                s = s.strip()
                if s:
                    trobats.append(s)

        i = j

    return trobats


def comprovables(selector: str) -> str | None:
    """Neteja el selector per poder-lo provar; None si no té sentit provar-lo."""
    net = ESTATS.sub("", selector).strip()
    return net or None


def main() -> int:
    if not SITE.is_dir():
        sys.exit("No hi ha site/. Executa abans: mkdocs build")

    css = CSS.read_text(encoding="utf-8")
    selectors = list(dict.fromkeys(selectors_de(css)))   # sense duplicats, en ordre
    if not selectors:
        sys.exit(f"No s'ha trobat cap selector a {CSS.relative_to(ARREL)}")

    pagines = sorted(SITE.rglob("*.html"))
    print(f"{len(selectors)} selectors contra {len(pagines)} pàgines\n")

    sopes = [BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser") for p in pagines]

    morts, ressuscitats = [], []

    for selector in selectors:
        prova = comprovables(selector)
        if prova is None:
            continue

        encerts = 0
        try:
            for sopa in sopes:
                encerts += len(sopa.select(prova))
                if encerts:
                    break
        except Exception as e:
            print(f"  ?  {selector}\n     no s'ha pogut provar: {e}")
            continue

        previst = selector in PREVISTOS_BUITS
        if encerts and previst:
            ressuscitats.append(selector)
            print(f"  ~  {selector}\n     ja troba elements: treu-lo de PREVISTOS_BUITS")
        elif encerts:
            print(f"  ok {selector}")
        elif previst:
            print(f"  -  {selector}  (buit a propòsit: {PREVISTOS_BUITS[selector]})")
        else:
            morts.append(selector)
            print(f"  X  {selector}\n     no troba cap element a tot el lloc")

    print()
    if morts:
        print(f"{len(morts)} selectors no s'apliquen a res:")
        for s in morts:
            print(f"  {s}")
        print("\nO l'estructura del tema ha canviat i s'han d'adaptar, o ja no")
        print("serveixen i s'han d'esborrar. Si és a posta, afegeix-los a")
        print("PREVISTOS_BUITS amb el motiu.")
        return 1

    if ressuscitats:
        print(f"Tot s'aplica. {len(ressuscitats)} selectors marcats com a buits ja")
        print("troben elements: treu-los de PREVISTOS_BUITS quan puguis.")
        return 0

    print("Tots els selectors troben elements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
