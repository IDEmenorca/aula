# Mòdul 1. Conceptes bàsics de cartografia i dades geogràfiques

## 1. Conceptes Generals sobre Projeccions Geogràfiques

**La Terra no és plana!!** Si algú us n'intenta convèncer aixequeu-vos i marxeu corrents sens ni dir adeu! :-) Tampoc és una esfera perfecta. La Terra és un **geoide** (superfície d'igual equipotencial gravitatòria) i per a respresentar-lo fem servir un **el·lipsoide de revolució**. 

I com que la terra no és plana el problema apareix quan volem representar aquesta superfície tridimensional i corba (la Terra) sobre un pla bidimensional (un mapa, un plànol o una pantalla d'ordinador). Per a fer-ho hem d'utilitzar una **projecció cartogràfica**.

[<iframe width="560" height="315" src="https://www.youtube.com/embed/kIID5FDi2JQ?si=jWLze-QRUzfoIG0D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>](https://youtu.be/kIID5FDi2JQ?si=GPyb61XEmwI5JEQz)

<img width="1024" height="559" alt="imagen" src="https://github.com/user-attachments/assets/95d863a3-9a86-4f10-961d-29ab5e932ac5" />


### 1.1. El problema de la distorsió és que els amplis poden petar si toques a volum molt alt.
Qualsevol projecció implica necessàriament una deformació o distorsió d'alguna de les propietats geomètriques. Cap mapa pot conservar simultàniament totes les propietats:

*   **Projeccions Conformes:** Mantenen la fidelitat dels **angles** i les formes de petites regions. Són les utilitzades en navegació i en la cartografia oficial.
*   **Projeccions Equivalents:** Mantenen les **superfícies** o àrees de forma proporcional, però deformen els angles i les formes.
*   **Projeccions Equidistants:** Mantenen les **distàncies** al llarg de determinades línies o des d'un punt central.

### 1.2. Sistemes de Referència Espacial (CRS) i Datums
Per situar un punt a la Terra necessitem un **Sistema de Referència Espacial** (*Spatial Reference System* - SRS/CRS):
*   **Coordenades Geogràfiques:** Expressades en graus de **Latitud** ($\phi$) i **Longitud** ($\lambda$).
*   **Coordenades Projectades / Cartesianes:** Expressades en metres sobre un pla ($X, Y$ o *Easting, Northing*).
*   **Datum:** Paràmetre de referència que defineix la posició de l'el·lipsoide respecte al centre de la Terra. Canviar de datum implica un canvi significatiu en les coordenades d'un mateix punt.

---

## 2. Projeccions Geogràfiques Oficials a Espanya i Menorca

A l'estat espanyol i en l'àmbit de la Comunitat Autònoma de les Illes Balears, la normativa vigent (*Real Decreto 1071/2007*) estableix el sistema de referència geodesic oficial.

### 2.1. El Sistema ETRS89
*   **Sistema de Referència Oficial:** **ETRS89** (*European Terrestrial Reference System 1989*).
*   **El·lipsoide de referència:** **GRS80**.
*   *Nota històrica:* Abans de la normativa de 2007 s'utilitzava el datum **ED50** (*European Datum 1950*). Aquest canvi va suposar un desplaçament d'uns **200 metres cap al sud-oest** en les coordenades de les Illes Balears. Qualsevol cartografia antiga en ED50 ha de ser reprojectada a ETRS89 abans de ser incorporada a un SIG municipal.

### 2.2. La Projecció UTM (Universal Transverse Mercator)
La projecció oficial per a cartografia terrestre a Espanya és la **UTM**:
*   És una projecció **cilíndrica, transversal i conforma**.
*   Divideix la Terra en **60 husos** (zones de 6° de longitud cadascun).
*   **L'arxipèlag balear (inclosa Menorca) es troba integrament en el Hús 31 North (31N).**

### 2.3. Codificació EPSG Oficial per a Menorca
En els programes de SIG (QGIS, ArcGIS, visualitzadors web), els sistemes de referència s'identifiquen mitjançant codis del **EPSG** (*European Petroleum Survey Group*):

| Nom del Sistema / Projecció | Codi EPSG | Ús / Àmbit |
| :--- | :--- | :--- |
| **ETRS89 / UTM zone 31N** | **EPSG:25831** | **Oficial per a treball i cartografia vectorial/Ràster a Menorca** |
| WGS 84 (Geogràfiques - graus) | EPSG:4326 | Ús global, GPS de camp, estàndards web |
| WGS 84 / Pseudo-Mercator | EPSG:3857 | Capes base web (Google Maps, OpenStreetMap, Carto) |
| ED50 / UTM zone 31N | EPSG:23031 | **OBSOLET.** Només per a cartografia històrica anterior a 2007 |

> **Atenció per a tècnics locals:** En carregar dades cartogràfiques als visors municipals o QGIS, comproveu sempre que la capa estigui definida en **EPSG:25831**. Barrejar EPSG:23031 (ED50) amb EPSG:25831 (ETRS89) provocat que els edificis o parcel·les apareguin "desplaçats" uns 200 metres a la mar o sobre la finca del veí.

---

## 3. Cartografia Bàsica vs. Cartografia Temàtica

A l'administració local treballem contínuament amb dos grans tipus de informació cartogràfica:

### 3.1. Cartografia Bàsica
La cartografia bàsica és aquella que s'obté mitjançant processos directes d'observació i mesurament de la superfície terrestre (topografia, fotogrametria). Serveix de suport fonamental per a qualsevol altra representació territorial.

*   **Característiques:**
    *   Proporciona la referència geomètrica i espacial del territori.
    *   Inclou elements naturals i artificials permanents: relleu (corbes de nivell), xarxa hidrogràfica, edificacions, xarxa viària, límits administratius.
    *   És d'interès general i serveix de base per a totes les administracions.
*   **Exemples a Menorca:**
    *   **BTN100 / BTN25:** Base Topogràfica Nacional (IGN).
    *   **Mapa Topogràfic de Menorca** (1:1.000 / 1:5.000) elaborat pel Consell Insular de Menorca.
    *   **Cartografia Cadastral Urbana i Russa** (Direcció General del Cadastre).

### 3.2. Cartografia Temàtica
La cartografia temàtica utilitza la cartografia bàsica com a fons de referència per a representar fenòmens, dades o conceptes específics d'un tema concret (social, econòmic, mediambiental, jurídic).

*   **Característiques:**
    *   Centrada en un aspecte o variable particular.
    *   Combina informació geogràfica amb atributs alfanumèrics.
    *   Fundamental per a la presa de decisions polítiques i tècniques.
*   **Exemples a Menorca:**
    *   **Plànol de Qualificació Urbanística del PGOU** d'un ajuntament (Maó, Ciutadella, Alaior, etc.).
    *   **Mapa d'Espais Naturals Protegits (ANLE/PRUG de s'Albufera des Grau)**.
    *   **Mapa del Camí de Cavalls (GR-223)** amb punts d'interès turístic i d'emergència.
    *   **Mapes de Risc d'Inundabilitat** (INUNCAT / ARPSI en barrancs com el de Algendar).
    *   **Mapa de Coberta Vegetal i Usos del Sol** de Menorca.

---

## 4. Ortofotografies i el Procés de Creació (Vol Fotogramètric)

### 4.1. Què és una Ortofoto?
Una **ortofoto** (o ortofotografia) és una imatge aèria rectificada mètricament. 

A diferència d'una fotografia aèria convencional (on existeixen deformacions causades per la perspectiva de la càmera i les diferències d'elevació del terreny), en una ortofoto **tots els punts tenen la mateixa escala** i la mateixa validesa mètrica que un mapa topogràfic.

$$	ext{Ortofoto} = 	ext{Fotografia Aèria} + 	ext{Ortorectificació (eliminació de la perspectiva i efecte del relleu)}$$

*   En una ortofoto es poden **mesurar distàncies, àrees i angles directament** sobre la imatge amb total precisió.

### 4.2. Com es crea una Ortofoto? El Procés Fotogramètric Passo a Passo

La creació d'una ortofoto d'alta resolució (per exemple, les ortofotos del projecte **PNOA** o les pròpies del Consell Insular) segueix les següents fases:

```
[1. Planejament del Vol] ──> [2. Execució del Vol i Captura] ──> [3. Punts de Control Terrestre (GCP)]
                                                                               │
[6. Generació Ortofoto Final] <── [5. Ortorectificació i Mosaicat] <── [4. Aerotriangulació i MDE]
```

1.  **Planificació i Execució del Vol Fotogramètric:**
    *   Un avió o drons equipat amb una càmera fotogramètrica mètrica realitza passades paral·leles sobre el territori.
    *   Es garanteix un **recobriment (encavalcament)** entre fotos: normalment un **60-80% de recobriment longitudinal** (al llarg de la línia de vol) i un **30-50% transversal** (entre línies paral·leles). Això permet la visió estereoscòpica (3D).
2.  **Mesura de Punts de Control Terrestre (GCP - Ground Control Points):**
    *   Equips de topògrafs mesuren amb GPS/GNSS de alta precisió punts clarament identificables a terra (creus pintades, cantonades de murs de pedra seca, fites).
    *   Aquests punts serveixen per a ancorar les imatges a les coordenades reals en el sistema **ETRS89 UTM 31N**.
3.  **Aerotriangulació i Ajust de Bloc:**
    *   Mitjançant càlculs matemàtics, es determinen exactament la posició ($X, Y, Z$) i l'orientació de la càmera en el moment de cada dispar.
4.  **Generació del Model Digital de l'Elevació (MDE / MDT):**
    *   A partir del parell d'imatges estereoscòpiques (o mitjançant sensors LiDAR aerotransportats), es genera un model 3D del terreny (MDT) que recull les altituds i pendents del territori.
5.  **Ortorectificació:**
    *   Aquest és el pas clau. S'aplica el MDT a cada píxel de la fotografia original per eliminar el desplaçament provocat pel relleu i la inclinació de l'objectiu. El píxel es projecta ortogonalment sobre el pla cartogràfic.
6.  **Mosaicat i Anivellament de Color:**
    *   Es combinen centenars o milers d'ortofotos individuals per formar un mosaic continu de tota la illa de Menorca, ajustant la lluminositat i el balanç de colors per evitar línies de tall visibles.

---

## 5. Exemples d'Aplicació Pràctica a Menorca

Per a un funcionari local de Menorca, la combinació d'aquests conceptes s'aplica diàriament en la gestió pública:

### Exemple 1: Verificació d'Infrafraccions Urbanístiques o Edificació en Sòl Rústic
*   **Eina:** Visualizador de la **IDE Menorca** (SITIBSA / Consell Insular).
*   **Procediment:** Es compara l'ortofoto PNOA actual amb ortofotos històriques (p. ex. vol de 1956, ortofoto de 2002, 2010, 2022).
*   **Aplicació:** Permet comprovar si un paret de pedra, una piscina o una ampliació d'un habitatge rural a **Alaior** o **Sant Lluís** es va construir abans o després de l'entrada en vigor de la Llei d'Espais Naturals (LEN) o del PGOU municipal.

### Exemple 2: Delimitació d'un camí públic (Camí de Cavalls / Camins Municipals)
*   **Capes utilitzades:** 
    *   *Cartografia Bàsica:* Linia de camins del Mapa Topogràfic de Menorca.
    *   *Cartografia Temàtica:* Llista de camins del Catàleg Municipal de Camins + Capa del Cadastre (parcel·lari).
    *   *Ortofoto:* Ortofoto recent de 10 cm/píxel.
*   **Projecció:** Totes les capes carregades en **EPSG:25831**. Permet mesurar l'amplada real de la traça del camí i detectar invasions de la propietat privada sobre el camí públic.

---

## 6. Exercicis Pràctics i de Consolidació de Coneixements

A continuació es presenten 4 exercicis pràctics pensats per als tècnics i administratius locals. Podeu intentar resoldre'ls i comprovar les solucions a la secció posterior.

---

### Qüestionari d'Exercicis

#### Exercici 1: Gestió de Projeccions en un projecte municipal
Un topògraf entrega a l'Ajuntament de Ciutadella un arxiu CAD (`.dwg`) amb el projecte de reforma d'una plaça urbana. Quan el tècnic municipal carrega el fitxer sobre el visor geogràfic de la IDE Menorca (que treballa en ETRS89 UTM 31N), la plaça apareix desplaçada uns 200 metres endins del mar.
1.  Quin és el motiu més probable d'aquest desplaçament?
2.  Quin codi EPSG té l'arxiu original del topògraf i quin codi EPSG hauria de tenir?

#### Exercici 2: Distingir Cartografia Bàsica i Temàtica
Classifica els següents productes cartogràfics utilitzats a l'Ajuntament de Maó en **Cartografia Bàsica (CB)** o **Cartografia Temàtica (CT)**:
1.  Full 1:5.000 del Mapa Topogràfic de les Illes Balears amb corbes de nivell cada 5 metres.
2.  Plànol del PGOU que mostra la classificació del sòl (Sòl Urbà, Sòl Abalorable, Sòl Rústic Protegit).
3.  Capa vectorial de punts de contenidors de recollida selectiva i les seves rutes de recollida.
4.  Capa d'edificacions i línies d'illa de cases del Cadastre.
5.  Mapa de zones d'alta vulnerabilitat d'aqüífers a Menorca per contaminació de nitrats.

#### Exercici 3: Mesurament en Ortofoto vs. Fotografia Aèria
L'àrea de Medi Ambient vol calcular la superfície d'una bassa d'aigua situada al fons d'un barranc profund (com el Barranc de Algendar). 
1.  Per què NO és correcte mesurar la superfície directament sobre una fotografia aèria obliqua o no rectificada?
2.  Quina propietat té l'ortofoto que sí que permet mesurar aquesta superfície amb garanties jurídiques i tècniques?

#### Exercici 4: Elecció de Sistema de Coordenades
Reps un correu d'un ciutadà que vol informar de la caiguda d'un arbre al Camí de Cavalls. Et dona les següents coordenades obtingudes amb el seu telèfon mòbil: `39.8872º N, 4.2541º E`.
1.  Quin tipus de coordenades són i en quin codi EPSG solen estar basades les dades de GPS mòbil?
2.  Què hauries de fer per poder dibuixar aquest punt de manera exacta sobre el SIG municipal en ETRS89 UTM 31N?

---

## 7. Solucions i Respostes als Exercicis

### Solució a l'Exercici 1
1.  **Motiu del desplaçament:** L'arxiu entregat pel topògraf utilitza el sistema antic de referència **ED50** (*European Datum 1950*). A les Illes Balears, la diferència entre el sistema antic ED50 i l'oficial actual ETRS89 és d'aproximadament **200 metres en direcció Sud-Oest / Nord-Est**.
2.  **Codis EPSG:** L'arxiu del topògraf està en **EPSG:23031** (ED50 / UTM zone 31N). Per solucionar-ho, el tècnic ha de reprojectar o transformar l'arxiu al sistema oficial **EPSG:25831** (ETRS89 / UTM zone 31N).

### Solució a l'Exercici 2
1.  Mapa Topogràfic 1:5.000: **Cartografia Bàsica (CB)**. (Descriu la geometria i el relleu real del terreny).
2.  Plànol de classificació de sòl del PGOU: **Cartografia Temàtica (CT)**. (Representa un fenomen jurídic/administratiu sobre la base territorials).
3.  Capa de contenidors de residus: **Cartografia Temàtica (CT)**. (Informació sectorial de serveis municipals).
4.  Capa d'edificacions i línies de Cadastre: **Cartografia Bàsica (CB)**. (Serveix de base mètrica de la parcel·la i l'edificació).
5.  Mapa de vulnerabilitat d'aqüífers: **Cartografia Temàtica (CT)**. (Anàlisi mediambiental temàtic).

### Solució a l'Exercici 3
1.  **Fotografia aèria no rectificada:** Té efectes de perspectiva i distorsió provocats per l'orografia del barranc (les zones més altes semblen més grans i les zones fondes queden comprimides o desplaçades per la inclinació dels raigs visuals respecte del centre de la lent). La mesura d'àrees sobre aquesta imatge donaria un error significatiu.
2.  **Propietat de l'Ortofoto:** L'ortofoto ha passat per un procés d'**ortorectificació** utilitzant un Model Digital del Terreny (MDT). S'han corregit totes les distorsions de perspectiva i relleu, transformant la projecció central en una **projecció ortogonal**. Per tant, té una escala uniforme a tota la imatge i permet mesurar distàncies i superfícies directament amb la mateixa precisió que un mapa topogràfic.

### Solució a l'Exercici 4
1.  **Tipus de coordenades:** Són **coordenades geogràfiques** (Latitud i Longitud) expressades en graus decimals. El estàndard de la majoria de receptors GPS de dispositius mòbils i aplicacions web és el datum **WGS84** (**EPSG:4326**).
2.  **Acció en el SIG municipal:** Al programari SIG (ex. QGIS), s'ha de crear un punt introduint les coordenades X, Y en EPSG:4326 (Longitud `4.2541`, Latitud `39.8872`) i posteriorment sol·licitar al programa que el transformi/reprojecti al CRS del projecte municipal (**EPSG:25831 - ETRS89 UTM 31N**). Pràcticament tots els SIG moderns fan aquesta conversió al vol (*reprojection on-the-fly*).
