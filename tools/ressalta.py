# -*- coding: utf-8 -*-
"""Dibuixa requadres vermells de ressaltat sobre una captura.

Manté l'estil que ja tenen les captures del curs: vermell 222,0,0 i tres
píxels de gruix. Les coordenades són les de la vora exterior del requadre.

    python tools/ressalta.py docs/.../img/48-panell-imprimir.png 214,295,313,335

Es pot passar més d'un requadre. La imatge es modifica al seu lloc, o sigui
que convé tenir-la ja confirmada a Git abans d'executar-ho.
"""

import sys
from PIL import Image, ImageDraw

VERMELL = (222, 0, 0)
GRUIX = 3


def ressalta(cami, caixes):
    im = Image.open(cami).convert('RGB')
    dibuix = ImageDraw.Draw(im)
    for x0, y0, x1, y1 in caixes:
        dibuix.rectangle([x0, y0, x1, y1], outline=VERMELL, width=GRUIX)
    im.save(cami)
    return len(caixes)


def main(args):
    if len(args) < 2:
        sys.exit(__doc__)
    cami, caixes = args[0], []
    for brut in args[1:]:
        trossos = [int(n) for n in brut.split(',')]
        if len(trossos) != 4:
            sys.exit('Cada requadre vol quatre nombres: x0,y0,x1,y1 (rebut: %s)' % brut)
        caixes.append(trossos)
    n = ressalta(cami, caixes)
    print('%s: %d requadre%s' % (cami, n, 's' if n > 1 else ''))


if __name__ == '__main__':
    main(sys.argv[1:])
