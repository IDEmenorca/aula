# 4.9. Visualitzar fitxers de cartografia al visor IDE Menorca

## Objectiu

En acabar sabràs carregar al visor un fitxer de cartografia teu, consultar-ne
els atributs i tornar-lo a descarregar en un altre format.

## Passos

1. **Obrir «Afegir mapes».** És a baix de tot del panell de capes. Té dues
   pestanyes: **Afegir WMS**, per a serveis, i **Obrir arxiu**, per als fitxers
   del teu ordinador.

    <figure markdown>
      ![El panell de capes amb la secció Afegir mapes desplegada, on es veuen les pestanyes Afegir WMS i Obrir arxiu](img/49-afegir-mapes.png){ .captura }
      <figcaption>Afegir mapes, a baix de tot del panell de capes, serveix tant per a serveis com per a fitxers.</figcaption>
    </figure>

2. **Carregar el fitxer.** Hi ha tres camins i tots tres van a parar al mateix
   lloc: triar-lo des de la pestanya **Obrir arxiu**, aferrar-lo des del
   porta-retalls, o **arrossegar-lo damunt el mapa**.

    <figure markdown>
      ![La pestanya Obrir arxiu emmarcada i seleccionada, amb el text dels formats admesos a sota](img/49-obrir-arxiu.png){ .captura }
      <figcaption>La segona pestanya d'Afegir mapes és la dels fitxers, i hi diu quins formats accepta.</figcaption>
    </figure>

    Admet **KML**, **GML**, **GPX**, **GeoJSON**, **TopoJSON**, **WKT**,
    **Shapefile** i **GeoPackage**, també comprimits en **ZIP**.

3. **No et preocupis pel sistema de coordenades.** El visor reprojecta el
   fitxer ell mateix: tant se val que vingui en 25831, en 4326 o en ED50.

4. **Consultar els atributs.** La fila **Selecció per** et sortirà apagada, però
   fes clic damunt un element igualment: els atributs surten.

    <figure markdown>
      ![Un fitxer carregat al visor, amb la fila Selecció per emmarcada i apagada, i el requadre dels atributs de l'element on s'ha fet clic](img/49-atributs-fitxer.png){ .captura }
      <figcaption>Encara que la fila de selecció surti apagada, el clic sobre l'element en retorna els atributs.</figcaption>
    </figure>

5. **Descarregar-lo en un altre format.** La fila del fitxer té una **icona de
   descàrrega pròpia** que el torna a treure en KML, GML, GeoJSON, WKT,
   Shapefile o GeoPackage. És una manera ràpida de convertir de format sense
   sortir del visor.

    !!! warning "L'eina Descarregar no el baixa"
        La del panell d'eines només treballa amb les capes del catàleg. Si hi
        vas amb un fitxer teu carregat, et dirà que no hi ha capes carregades.
        Per baixar-lo, la icona de la seva pròpia fila.

6. **El fitxer es queda.** Si recarregues la pàgina, continua carregat.

## Exercici pràctic

Aquest exercici tanca el cercle: treure dades del visor i tornar-les-hi a
posar.

1. Dibuixa un polígon damunt el mapa amb l'eina de dibuix
   ([4.3](03-mesurar-dibuixar.md)).
2. Descarrega'l en **GeoJSON**.
3. Torna'l a carregar al visor, arrossegant-lo damunt el mapa.
4. Comprova que surt a **Capes carregades** amb el nom del fitxer.
5. Recarrega la pàgina: hi ha de continuar.
6. Descarrega'l un altre cop, ara des de la icona de la seva fila, i tria
   **Shapefile**.

!!! tip "És el que faràs amb la cartografia del teu ajuntament"
    El mateix camí serveix per mirar al visor un fitxer que t'hagin passat o
    que hagis preparat tu, i veure'l damunt la cartografia de l'illa.

---

!!! tip "Al manual de referència"
    El manual encara no té cap apartat sobre carregar fitxers propis. Els
    formats de descàrrega es descriuen a
    [3.3. Descarregar](../../../manuals/visor-generic/03-eines/03-descarregar.md).
