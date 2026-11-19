# -*- coding: utf-8 -*-
"""Dibuixa requadres vermells de ressaltat sobre una captura.

Manté l'estil que ja tenen les captures del curs: vermell 222,0,0 i tres
píxels de gruix. Les coordenades són les de la vora exterior del requadre.

    python tools/ressalta.py docs/.../img/48-panell-imprimir.png 214,295,313,335

Es pot passar més d'un requadre. Si un requadre acaba amb «@x,y», s'hi afegeix
una pastilla numerada en aquell punt; la numeració segueix l'ordre dels
requadres de la línia d'ordres, començant per l'1:

    python tools/ressalta.py img.png 4,4,856,70@600,37 14,80,66,530@40,326

La imatge es modifica al seu lloc, o sigui que convé tenir-la ja confirmada a
Git abans d'executar-ho.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

VERMELL = (222, 0, 0)
GRUIX = 3
RADI = 12
LLETRES = ('C:/Windows/Fonts/arialbd.ttf', 'C:/Windows/Fonts/arial.ttf')


def tipografia(mida):
    for cami in LLETRES:
        if os.path.exists(cami):
            return ImageFont.truetype(cami, mida)
    return ImageFont.load_default()


def ressalta(cami, caixes):
    im = Image.open(cami).convert('RGB')
    dibuix = ImageDraw.Draw(im)
    lletra = tipografia(16)
    for n, (x0, y0, x1, y1, pastilla) in enumerate(caixes, start=1):
        dibuix.rectangle([x0, y0, x1, y1], outline=VERMELL, width=GRUIX)
        if pastilla is None:
            continue
        cx, cy = pastilla
        dibuix.ellipse([cx - RADI, cy - RADI, cx + RADI, cy + RADI], fill=VERMELL)
        dibuix.text((cx, cy), str(n), fill=(255, 255, 255), font=lletra, anchor='mm')
    im.save(cami)
    return len(caixes)


def llegeix(brut):
    pastilla = None
    if '@' in brut:
        brut, punt = brut.split('@', 1)
        trossos = [int(n) for n in punt.split(',')]
        if len(trossos) != 2:
            sys.exit('La pastilla vol dos nombres: @x,y (rebut: %s)' % punt)
        pastilla = tuple(trossos)
    trossos = [int(n) for n in brut.split(',')]
    if len(trossos) != 4:
        sys.exit('Cada requadre vol quatre nombres: x0,y0,x1,y1 (rebut: %s)' % brut)
    return trossos + [pastilla]


def main(args):
    if len(args) < 2:
        sys.exit(__doc__)
    cami, caixes = args[0], [llegeix(b) for b in args[1:]]
    n = ressalta(cami, caixes)
    print('%s: %d requadre%s' % (cami, n, 's' if n > 1 else ''))


if __name__ == '__main__':
    main(sys.argv[1:])
