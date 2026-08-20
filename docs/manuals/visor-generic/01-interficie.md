# 1. Interfície i navegació

El visor s'inicia amb la Base de Referència de l'IDE Menorca i l'extensió completa de
l'illa. Aquest apartat descriu què hi ha a la pantalla i com moure-s'hi.

## 1.1. Les parts de la pantalla

<figure markdown>
  ![El visor amb tota l'illa de Menorca visible i els quinze elements de la interfície numerats amb globus grocs sobre la imatge](img/01-interficie-general.png){ .captura }
  <figcaption>Interfície per defecte del visor genèric.</figcaption>
</figure>

| # | Element | Ubicació |
|---|---|---|
| 1 | Mapa | Tota la superfície central |
| 2 | Panell de capes | Banda dreta |
| 3 | Quadre de cerca | Capçalera, al costat del logotip |
| 4 | Botons de zoom | Columna esquerra, a dalt |
| 5 | Extensió inicial | Columna esquerra |
| 6 | Pantalla completa | Columna esquerra |
| 7 | Panell d'eines | Columna esquerra |
| 8 | Street View | Columna esquerra |
| 9 | BirdEye | Columna esquerra |
| 10 | Llegenda | Columna esquerra |
| 11 | Mapa de situació | Columna esquerra, a baix |
| 12 | Indicador del sistema de coordenades i coordenades del cursor | Cantó inferior esquerre |
| 13 | Atribucions de les dades | Vora inferior, al centre |
| 14 | Escala gràfica | Vora inferior, a la dreta |
| 15 | Escala numèrica i mida de pantalla | Cantó inferior dret |

!!! note "Pendent de redactar"
    El document original no descriu els elements **9 (BirdEye)**, **10 (Llegenda)**,
    **11 (Mapa de situació)** ni **13 (Atribucions)**. Cal documentar-los.

## 1.2. Moure's pel mapa

Amb el ratolí:

| Acció | Com es fa |
|---|---|
| Desplaçar el mapa | Mantenir premut el botó esquerre i arrossegar cap a la direcció desitjada |
| Apropar-se a un punt concret | Doble clic sobre aquell punt |
| Apropar o allunyar | Rodeta del ratolí |

També es pot navegar amb els botons de zoom, descrits a continuació.

## 1.3. Botons de zoom

Els botons **+** i **−** de la columna esquerra apropen i allunyen el mapa.

<figure markdown>
  ![Els dos botons de zoom, quadrats i negres, amb els signes més i menys, apilats verticalment](img/02-botons-zoom.png){ .captura }
</figure>

## 1.4. Tornar a l'extensió inicial

El botó d'**extensió inicial**, amb la icona d'una casa, torna el mapa a la vista de
partida, on es veu tota l'illa de Menorca.

<figure markdown>
  ![Botó d'extensió inicial amb icona de casa](img/03-extensio-inicial.png){ .captura }
</figure>

!!! warning "Compte amb els límits d'escala"
    Si tens capes carregades amb un límit de visualització, en tornar a l'extensió
    inicial poden deixar de veure's. No és que s'hagin descarregat: senzillament, a
    aquella escala no es dibuixen. Consulta
    [la gestió de capes carregades](02-panell-capes.md#25-capes-carregades).

## 1.5. Pantalla completa

El botó de **pantalla completa** maximitza el visor i n'amaga la resta de la pàgina.
És especialment útil en pantalles petites i en dispositius mòbils.

Per sortir-ne, torna a prémer el botó o la tecla ++esc++.

<figure markdown>
  ![Els dos estats del botó de pantalla completa: negre quan s'hi entra, vermell quan ja s'hi és a dins](img/04-pantalla-completa.png){ .captura }
</figure>

## 1.6. Sistema de coordenades i coordenades del cursor

Al cantó inferior esquerre, un indicador mostra en tot moment el sistema de referència
de coordenades (CRS) actiu i les coordenades del punt on hi ha el cursor.

<figure markdown>
  ![Indicador de CRS mostrant EPSG:25831 i les coordenades x i y del cursor](img/05-indicador-crs.png){ .captura }
  <figcaption>L'indicador mostra el CRS actiu i les coordenades del cursor.</figcaption>
</figure>

En prémer el botó del sistema de referència s'obre un quadre que indica la projecció
actual del mapa i quins altres sistemes hi són compatibles. La projecció per defecte és
**ETRS89 / UTM zone 31N (EPSG:25831)**, i habitualment s'ofereixen també:

- WGS 84 (EPSG:4326)
- WGS 84 / Pseudo-Mercator (EPSG:3857)

Els sistemes disponibles depenen del mapa de fons que s'estigui utilitzant.

!!! tip "Relació amb els mapes de fons"
    Si tries un mapa de fons incompatible amb el CRS actual, el visor canvia
    automàticament al sistema compatible amb aquell mapa. Ho expliquem a
    [mapes de fons](02-panell-capes.md#22-mapes-de-fons).

## 1.7. Ajuda i idioma

A la capçalera del panell de capes hi ha l'enllaç **ajuda**, que obre un panell
informatiu amb l'accés al visualitzador antic i al canal de YouTube de la IDE Menorca,
on hi ha videotutorials.

A la dreta del mateix panell, els enllaços **ca**, **es** i **en** canvien l'idioma de
la interfície entre català, castellà i anglès. En prémer-los, el visor es refresca.

!!! warning "A verificar"
    L'enllaç al «visualitzador antic» encara existeix? Si el visor antic ja s'ha retirat,
    aquest paràgraf s'ha d'eliminar.
