# 3.1. Dibuixar i mesurar

Aquesta eina permet dibuixar punts, línies i polígons sobre el mapa. Els elements
dibuixats porten associada la seva informació geogràfica: coordenades, longitud o
superfície. També es poden descarregar.

!!! note "Captura pendent — `img/20-dibuixar-panell.png`"
    Panell Dibuixar i medir amb les pestanyes de punts, línies i polígons.

    Peu de foto previst: *L'eina s'organitza en tres pestanyes, una per tipus de geometria.*

## Pestanya de punts

Dibuixa punts sobre el mapa i en mostra les **coordenades** i l'**elevació**. Es pot
canviar el color del traç, el color del farciment, l'opacitat i el gruix.

| Botó | Acció |
|---|---|
| Llapis | Començar l'edició |
| Creu | Cancel·lar l'edició |

!!! note "Captura pendent — `img/21-punts.png`"
    Pestanya de punts amb els controls de color, gruix i les coordenades del punt.

## Pestanya de línies

Dibuixa línies i en mostra la **longitud**. Es pot canviar el color i el gruix del traç,
i desfer o refer trams mentre dibuixes.

| Botó | Acció |
|---|---|
| Llapis | Començar l'edició |
| Fletxa antihorària | Desfer el darrer vèrtex dibuixat |
| Fletxa horària | Refer el darrer vèrtex esborrat |
| Marca de verificació | Acabar el dibuix (també amb doble clic) |
| Creu | Cancel·lar la darrera edició |

### Perfil d'elevació

En dibuixar una línia apareix el seu **perfil d'elevació**, amb el desnivell acumulat
positiu i negatiu.

!!! note "Captura pendent — `img/22-perfil-elevacio.png`"
    Panell de perfil d'elevació amb la corba del terreny i el desnivell.

    Peu de foto previst: *El perfil mostra el desnivell al llarg de la línia dibuixada.*

El botó amb la icona de muntanyes activa i desactiva el panell del perfil. L'alçada i
l'amplada del panell s'ajusten amb els controls del lateral dret, de la part inferior i
del cantó inferior dret.

## Pestanya de polígons

Dibuixa polígons i en mostra la **superfície** i el **perímetre**. Es pot canviar el
color i el gruix del traç, el color i l'opacitat del farciment, i desfer o refer vèrtexs.

Els botons són els mateixos que a la pestanya de línies.

!!! note "Captura pendent — `img/23-poligons.png`"
    Pestanya de polígons mostrant àrea i perímetre del polígon dibuixat.

## Eines comunes als tres tipus

Aquestes eines estan disponibles en tot moment, sigui quina sigui la pestanya activa.

| Botó | Acció |
|---|---|
| Mà | **Seleccionar** un o diversos elements. Per seleccionar-ne més d'un, mantén premuda la tecla ++shift++ |
| Goma | **Esborrar** els elements seleccionats |
| **A** | **Etiquetar**: afegeix text a cada entitat seleccionada, amb color i mida triables |
| Ull | **Amagar o mostrar** tots els elements dibuixats |
| Fletxa avall | **Descarregar** els elements dibuixats |
| Paperera | **Esborrar-ho tot**, amb confirmació prèvia |

### Modificar una geometria ja dibuixada

Un cop seleccionada una entitat, se'n pot canviar la forma: prem i arrossega un vèrtex
per moure'l, o arrossega un punt intermedi per crear-ne un de nou.

!!! note "Captura pendent — `img/24-modificar-geometria.png`"
    Polígon abans i després de moure un vèrtex per modificar-ne la forma.

### Descarregar el que has dibuixat

!!! note "Captura pendent — `img/25-descarregar-dibuix.png`"
    Diàleg de descàrrega del dibuix amb l'opció d'incloure elevacions i els formats disponibles.

El diàleg permet **incloure les elevacions**. En línies i polígons hi ha, a més, l'opció
d'interpolar coordenades per obtenir l'elevació dels punts intermedis, no només dels
vèrtexs.

Els formats oferts en aquest diàleg són: KML, GML, GeoJSON, WKT, GPX, Shapefile i
GeoPackage.

!!! warning "A verificar: quins formats hi ha realment"
    El manual original no és coherent en aquest punt. Aquí en llista set; a
    [descàrrega vectorial](03-descarregar.md) diu que «són quatre»; a
    [selecció gràfica](../04-seleccio-grafica.md) n'enumera sis. Cal comprovar al visor
    quins formats ofereix cada eina i corregir els tres apartats.

!!! tip "El dibuix no es descarrega amb les capes"
    L'eina de [descàrrega vectorial](03-descarregar.md) **no** inclou el que hagis
    dibuixat. Per obtenir el dibuix has de fer servir el botó de descàrrega d'aquesta
    mateixa eina.
