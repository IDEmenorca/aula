# 8. Fitxers propis

A més de les capes del catàleg, el visor pot obrir fitxers de cartografia del
teu ordinador i dibuixar-los damunt el mapa.

## 8.1. On es carreguen

La secció **Afegir mapes** és al final del panell de capes, sota **Capes
disponibles**. Té dues pestanyes:

| Pestanya | Per a què serveix |
|---|---|
| **Afegir WMS** | Connectar un servei de mapes extern a partir de la seva adreça |
| **Obrir arxiu** | Carregar un fitxer de l'ordinador |

<figure markdown>
  ![La secció Afegir mapes desplegada al final del panell de capes, amb les pestanyes Afegir WMS i Obrir arxiu](img/100-afegir-mapes.png){ .captura }
  <figcaption>Afegir mapes, al final del panell de capes, serveix tant per a serveis com per a fitxers.</figcaption>
</figure>

!!! note "Pendent: la pestanya Afegir WMS"
    Aquest apartat només descriu **Obrir arxiu**. La càrrega de serveis WMS
    externs encara no s'ha documentat.

## 8.2. Formats admesos i maneres de carregar

Des de la pestanya **Obrir arxiu**, el visor accepta **KML**, **GML**, **GPX**,
**GeoJSON**, **TopoJSON**, **WKT**, **Shapefile** i **GeoPackage**, també
comprimits en **ZIP**.

<figure markdown>
  ![La pestanya Obrir arxiu seleccionada, amb el text dels formats admesos i el botó Obrir arxiu](img/101-obrir-arxiu.png){ .captura }
  <figcaption>La pestanya Obrir arxiu diu quins formats accepta i de quines maneres.</figcaption>
</figure>

Hi ha tres maneres de carregar-lo, i totes tres van a parar al mateix lloc:

1. Triar-lo amb el botó **Obrir arxiu**.
2. Aferrar-lo des del porta-retalls.
3. Arrossegar-lo damunt l'àrea del mapa.

El sistema de coordenades del fitxer no importa: el visor el reprojecta.

## 8.3. Com es comporta un fitxer carregat

El fitxer apareix a **Capes carregades** amb el nom del fitxer, i s'hi queda
encara que recarreguis la pàgina.

<figure markdown>
  ![Un fitxer carregat, amb la seva fila a Capes carregades i el requadre d'atributs de l'element on s'ha fet clic](img/102-atributs-fitxer.png){ .captura }
  <figcaption>La fila d'un fitxer propi no porta les mateixes icones que la d'una capa del catàleg.</figcaption>
</figure>

La seva fila no porta les mateixes icones que les de
[2.5. Capes carregades](02-panell-capes.md#25-capes-carregades):

| Icona | Nom | Què fa |
|---|---|---|
| Fletxa avall sobre una safata | **Descarregar** | Torna a treure el fitxer en el format que triis |
| Casella | **Visibilitat** | Activa o desactiva la visualització |
| Barra lliscant | **Control de transparència** | Igual que a qualsevol capa |
| Fletxes verticals | **Canviar l'ordre** | Prem i arrossega amunt o avall |

No hi són, en canvi, la **informació de la capa**, el **zoom a l'extensió de la
capa** ni les **consultes**.

La fila **Selecció per** del final del panell surt **apagada**. Tot i així, un
clic damunt un element del fitxer n'obre el requadre amb la taula d'atributs.

## 8.4. Tornar a descarregar el fitxer

La icona de descàrrega de la fila del fitxer el torna a treure en **KML**,
**GML**, **GeoJSON**, **WKT**, **Shapefile** o **GeoPackage**. És una manera de
convertir de format sense sortir del visor.

L'eina **Descarregar** del panell d'eines
([3.3. Descarregar](03-eines/03-descarregar.md)) **no** baixa els fitxers
propis: només treballa amb les capes del catàleg. Amb un fitxer teu carregat i
cap capa del catàleg, avisa que no hi ha capes carregades.

!!! warning "A verificar: on va a parar el fitxer i quant pot pesar"
    No s'ha comprovat si el fitxer es queda al navegador o es puja a algun
    servidor, ni si hi ha cap límit de mida. És el primer que preguntarà qui
    hi vulgui posar dades que no són públiques.
