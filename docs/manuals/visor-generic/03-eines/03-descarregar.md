# 3.3. Descarregar

Aquesta eina ofereix dues descàrregues diferents: una **imatge** del mapa o les **dades
vectorials** de les capes carregades.

!!! note "Captura pendent — `img/40-descarregar-panell.png`"
    Panell Descarregar amb les pestanyes Imatge del mapa i Capes vectorials.

## Imatge del mapa

Genera un PNG o un JPEG amb tot el que es veu al visor: capes carregades visibles,
mapes de fons, serveis WMS i fitxers carregats.

Permet incloure un **codi QR** que enllaça amb la vista del mapa que ha generat la
imatge.

!!! note "Captura pendent — `img/41-descarregar-imatge.png`"
    Pestanya d'imatge del mapa amb el selector de format i la casella del codi QR.

## Capes vectorials

Descarrega les entitats que intersequen amb l'àrea que estàs visualitzant.

!!! warning "Només el que es veu"
    Es descarreguen únicament les capes **carregades i amb la visibilitat activada**. Les
    capes carregades però amagades no es descarreguen. I no es descarrega la capa
    sencera, només els elements visibles a l'extensió actual: per obtenir-la tota, fes
    servir el botó d'informació **i** de la capa al panell de capes carregades.

!!! note "Captura pendent — `img/42-descarregar-vectorial.png`"
    Pestanya de capes vectorials amb el selector de format.

### Què no es pot descarregar

- Capes de fons.
- Dades ràster: ortofotos, mapes en relleu, mapes base, cartografia topogràfica i
  imatges de satèl·lit.
- Capes carregades mitjançant serveis WMS.
- Capes que no siguin propietat del Consell Insular o dels ajuntaments. Les d'altres
  nodes IDE (IDEIB, Cadastre, Costes i altres) no es descarreguen.
- El que hagis dibuixat amb l'eina de [dibuixar i mesurar](01-dibuixar-mesurar.md), que
  té el seu propi botó de descàrrega.

### Formats disponibles

| Format | Descripció |
|---|---|
| **GML** | Dades geogràfiques en dues dimensions, en llenguatge de marques basat en XML. Estàndard de l'OGC |
| **GeoJSON** | Dades espacials basades en JSON |
| **KML** | Dades espacials en tres dimensions, en XML. Obre's amb Google Earth |
| **Shapefile** | Format d'ESRI molt estès. Es descarrega un ZIP amb els fitxers `.shp`, `.shx`, `.dbf` i `.prj`, més un `.cst` amb la codificació de caràcters |

!!! warning "A verificar: quins formats hi ha realment"
    El manual original diu que en aquesta eina «són quatre», però a
    [dibuixar i mesurar](01-dibuixar-mesurar.md) n'enumera set i a
    [selecció gràfica](../04-seleccio-grafica.md) sis. Cal comprovar-ho al visor.

Un cop triat el format, prem **Descarregar**. Es genera un fitxer ZIP o KMZ amb la
informació, agrupada per servei.

### Missatges d'error

| Situació | Missatge |
|---|---|
| No hi ha capes carregades, o totes tenen la visibilitat desactivada | «No hi ha capes carregades» |
| Se supera el màxim d'elements descarregables (**1.000**) | «Massa elements per al servei IDEMenorca. Faci zoom sobre el mapa per seleccionar una àrea més petita o redueixi el nombre de capes carregades» |
| No hi ha entitats a l'àrea visible | «No hi ha dades: no s'han trobat entitats disponibles per a descarregar» |

!!! tip "Si superes el límit d'elements"
    Tens dues sortides: apropar-te per reduir l'àrea, o descarregar menys capes alhora.

!!! note "Capes amagades per escala"
    Si una capa no es dibuixa perquè estàs fora del seu rang d'escala, es pot descarregar
    igualment, sempre que no superi el màxim d'elements.

La icona d'informació al costat del botó **Descarregar** obre un quadre d'ajuda amb
aquestes mateixes condicions.
