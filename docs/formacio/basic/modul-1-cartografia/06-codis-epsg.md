# 1.6. Els codis EPSG

Són codis identificadors numèrics que designen de manera inequívoca cada sistema
de coordenades. El nom ve de l'antic *European Petroleum Survey Group*, i avui el
manté l'IOGP, l'*International Association of Oil & Gas Producers*.

S'han convertit en una mena d'estàndard per conveni perquè resulten molt útils,
especialment perquè els programes de cartografia i els serveis web puguin
referir-se a un sistema de manera inequívoca. Per exemple, `EPSG:25831`
substitueix la descripció completa d'ETRS89 / UTM 31N.

Els més habituals a Espanya són aquests.

## Sistemes geogràfics, en graus

| Codi | Sistema |
|---|---|
| `4326` | WGS84 — GPS, GeoJSON, Leaflet |
| `4258` | ETRS89 — oficial a Espanya des del 2007 |
| `4230` | ED50 — antic, en cartografia anterior al 2007 |

## Projectats oficials, ETRS89 / UTM

| Codi | Zona | On s'usa |
|---|---|---|
| `25829` | 29N | Galícia i oest peninsular |
| `25830` | 30N | La major part de la península |
| `25831` | 31N | Catalunya, **Balears —Menorca inclosa—** i est peninsular |

Els antics, en ED50 / UTM, són `23029`, `23030` i `23031` —zones 29N, 30N i
31N—, presents en cartografia anterior.

## Per a mapes web

| Codi | Sistema | Per a què |
|---|---|---|
| `3857` | Web Mercator | El d'OpenStreetMap, Google i la majoria de mapes en línia. **No és adequat per mesurar**, per les deformacions d'àrea i distància |
| `3035` | ETRS89 LAEA Europa | Equivalent, usat per a estadístiques europees |

??? info "Vols saber-ne més: per què ho van inventar unes petrolieres"
    La raó principal va ser **evitar errors i ambigüitats en intercanviar dades
    de posició entre empreses i països**. Bé, no, un moment: la raó principal va
    ser perquè tenien un problema i mooooooolts diners i recursos per dedicar a
    trobar-hi una solució.

    **El context**

    Als anys 80, les petrolieres europees feien prospeccions sísmiques,
    perforacions i gasoductes, sobretot al mar del Nord, que implicaven diversos
    països. Cada país tenia el seu datum, el seu el·lipsoide i les seves
    projeccions, i cada empresa els anomenava a la seva manera. Això provocava
    problemes:

    - **Noms ambigus.** «UTM zona 31» no deia si era amb ED50, WGS84 o un altre
      datum, i una diferència de datum pot suposar desenes o centenars de metres.
    - **Paràmetres dispersos o inconsistents.** No hi havia un lloc comú amb les
      definicions i les fórmules de transformació.
    - **Risc econòmic i de seguretat.** Un error de posició en un pou o una
      canonada és molt costós.

    **La solució**

    L'any 1985 es va crear el grup EPSG per recollir en una **única base de
    dades** les definicions de datums, el·lipsoides, projeccions i
    transformacions, i per assignar a cadascun un **codi numèric únic**. Un
    número és curt, no depèn de l'idioma, no s'interpreta de dues maneres i un
    programa el pot llegir fàcilment.

    **Per què es va imposar**

    Com que era públic, coherent i ben documentat, el van adoptar els programes
    de cartografia i els estàndards geogràfics —PROJ, GDAL, OGC, QGIS— i avui és
    la referència de facto per identificar sistemes de coordenades.

## Exercici: el far de Cavalleria en tres sistemes

Ara sí. Aquest el faràs al visor.

- [ ] Obre el [visor de l'IDE Menorca](https://ide.cime.es/visor) i fixa't que a
  baix a l'esquerra hi ha un selector del sistema de referència.
- [ ] Modifica'l i observa com canvien les coordenades en passar el cursor pel
  mapa. També en fer clic sobre el mapa.
- [ ] Troba les coordenades del **far de Cavalleria** en els tres sistemes de
  referència disponibles.
