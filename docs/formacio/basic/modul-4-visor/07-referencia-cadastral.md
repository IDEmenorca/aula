# 4.7.1. La referència cadastral

La **referència cadastral** és l'identificador oficial i obligatori dels béns
immobles a Espanya. Cada immoble en té una de sola, i serveix per situar-lo sense
ambigüitat a la cartografia del Cadastre.

És un codi alfanumèric de **20 caràcters**, que sempre es divideix en tres blocs:

| Posicions | Caràcters | Què identifica |
|---|---|---|
| 1–14 | 14 | La **parcel·la** (la finca) |
| 15–18 | 4 | El **bé immoble** dins de la parcel·la (número de càrrec) |
| 19–20 | 2 | Els **caràcters de control** |

El que canvia entre urbana i rústica és **com es construeixen els 14 primers
caràcters**. Els 4 següents i els 2 de control funcionen igual en tots dos casos.

!!! info "Com saber si és urbana o rústica?"
    Només cal mirar-ne l'estructura. Si comença per **2 dígits de província + 3
    de municipi + una lletra** (sector), és de tipus rústic. Si comença per **7
    dígits** (mançana i parcel·la) seguits de **2 lletres**, és de tipus urbà.

## Referència cadastral urbana

```text
7412801  EE9271A  0001  IF
'--+--'  '--+--'  '+-'  '+'
   |        |      |     '-- 2 caràcters de control
   |        |      '-------- 4 dígits: número de càrrec (immoble dins la parcel·la)
   |        '--------------- 7 caràcters: full del plànol parcel·lari
   '------------------------ 7 dígits: mançana (5) + parcel·la dins la mançana (2)
```

| Bloc | Longitud | Significat |
|---|---|---|
| Mançana | 5 dígits | Identifica la mançana on és la parcel·la |
| Parcel·la | 2 dígits | Número d'ordre de la parcel·la dins d'aquesta mançana |
| Full del plànol | 7 caràcters | Full cartogràfic on cau el centroide de la mançana (2 lletres + 4 dígits + 1 lletra) |
| Càrrec | 4 dígits | Número d'ordre de l'immoble dins de la parcel·la |
| Control | 2 lletres | Verificació de la resta del codi |

!!! info "Divisió horitzontal"
    Quan un edifici està dividit en pisos i locals (**propietat horitzontal**),
    tots els immobles comparteixen els mateixos 14 primers caràcters, perquè són
    a la mateixa parcel·la. Només es diferencien pel **número de càrrec** (i, per
    tant, pels caràcters de control, que en depenen).

Els **14 primers caràcters** (`7412801EE9271A`) identifiquen la parcel·la, que en
aquest cas és un edifici amb diversos immobles. Quan s'hi afegeix el número de
càrrec, cadascun dels immobles (habitatges, locals, garatges...) té la seva
pròpia referència de 20 caràcters:

| Referència completa | Càrrec | Immoble |
|---|---|---|
| `7412801EE9271A0001IF` | 0001 | Primer immoble de la parcel·la |
| `7412801EE9271A0002OG` | 0002 | Segon immoble |
| `7412801EE9271A0003PH` | 0003 | Tercer immoble |
| `7412801EE9271A0004AJ` | 0004 | Quart immoble |

## Referència cadastral rústica

```text
07  002  A  006  00140  0000  GQ
'+' '+'  |  '+'  '-+-'  '+-'  '+'
 |   |   |   |     |     |     '-- 2 caràcters de control
 |   |   |   |     |     '-------- 4 dígits: número de càrrec
 |   |   |   |     '-------------- 5 dígits: parcel·la dins del polígon
 |   |   |   '-------------------- 3 dígits: polígon
 |   |   '------------------------ 1 lletra: sector
 |   '---------------------------- 3 dígits: municipi
 '-------------------------------- 2 dígits: província
```

| Bloc | Longitud | Significat |
|---|---|---|
| Província | 2 dígits | Codi INE de la província |
| Municipi | 3 dígits | Codi INE del municipi |
| Sector | 1 lletra | Sector (lletra), lligat a la divisió parcel·lària del terme municipal, si n'hi ha |
| Polígon | 3 dígits | El terme municipal es divideix en polígons segons l'homogeneïtat de cultius, accidents geogràfics, etc. |
| Parcel·la | 5 dígits | Número de parcel·la dins del polígon |
| Càrrec | 4 dígits | Número d'ordre de l'immoble dins de la parcel·la |
| Control | 2 lletres | Verificació de la resta del codi |

**En rústic també existeix el concepte de divisió horitzontal.**

| Referència completa | Càrrec | Què representa |
|---|---|---|
| `07002A006001400000GQ` | 0000 | Primer càrrec de la parcel·la |
| `07002A006001400001HW` | 0001 | Segon càrrec (un altre immoble dins la mateixa parcel·la) |

Igual que en l'urbana, els 14 primers caràcters són idèntics i només canvien el
càrrec i el control.

!!! info "Els disseminats"
    Un **disseminat** és una parcel·la que, històricament, es va crear per
    **separar un habitatge o una construcció** (a camp obert) de la resta de la
    parcel·la rústica on es trobava. Aquestes parcel·les tenen una referència
    **d'estil urbà** (7 + 7 caràcters) i la seva referència comença per `00`.

    Fixa't que, tot i ser en sòl rústic, **no segueix l'estructura
    província-municipi-sector-polígon-parcel·la**: té forma de referència urbana,
    amb la marca de disseminat (`00...`) al començament.

!!! note "Només per documentar els existents"
    Amb el model de cartografia unificada rústica i urbana del Cadastre, **ja no
    es creen nous disseminats**. Una construcció no se segrega de la parcel·la
    rústica: es dibuixa dins d'ella. Els disseminats antics es mantenen per a les
    parcel·les ja donades d'alta, i quan aquests terrenys es desenvolupen
    urbanísticament es crea una mançana amb el disseminat dins la cartografia
    urbana.

!!! info "Una conseqüència pràctica"
    Una referència d'estil rústic no pot ser a la cartografia urbana, ni una
    d'estil urbà a la rústica, **excepte** els disseminats, que són l'excepció
    històrica.

??? info "Vols saber-ne més: els caràcters de control"
    Els dos últims caràcters permeten detectar errors de gravació en els 18
    anteriors. Es calculen amb un algorisme fix:

    1. **Primer caràcter de control (posició 19):** es prenen els 7 primers
       caràcters de la parcel·la + els 4 del càrrec (11 caràcters).
    2. **Segon caràcter de control (posició 20):** es prenen els 7 caràcters
       següents (posicions 8–14) + els 4 del càrrec (11 caràcters).
    3. Cada caràcter es converteix en un valor: els dígits valen el que indiquen
       i les lletres, la seva posició a l'alfabet (`A=1, B=2, ..., N=14, Ñ=15,
       O=16...`).
    4. Cada valor es multiplica pel **pes** de la seva posició (1 a 11):
       `13, 15, 12, 5, 4, 17, 9, 21, 3, 7, 1`.
    5. Se sumen tots els productes i es calcula el **residu de dividir entre 23**.
    6. Aquest residu és la posició de la lletra a la cadena
       `MQWERTYUIOPASDFGHJKLBZX` (començant a 0).

    **Exemple resolt: `07002A00600140` + `0000`**

    **Primer caràcter** (`07002A0` + `0000`):

    ```text
    Caràcter   0    7    0    0    2    A    0    0    0    0    0
    Valor      0    7    0    0    2    1    0    0    0    0    0
    Pes       13   15   12    5    4   17    9   21    3    7    1
    Producte   0  105    0    0    8   17    0    0    0    0    0
    ```

    Suma = 130 → 130 mod 23 = **15** → la lletra que ocupa la posició 15 de la
    cadena = **G**

    **Segon caràcter** (`0600140` + `0000`):

    Suma = 162 → 162 mod 23 = **1** → la lletra que ocupa la posició 1 = **Q**

    Control = **GQ**, i la referència completa és `07002A006001400000GQ`. ✓

    !!! example "Comprovació"
        Aquest algorisme reprodueix els caràcters de control de totes les
        referències d'aquesta pàgina: `GQ`, `HW`, `IF`, `OG` i `AJ`.

    Això vol dir que, si es canvia un sol caràcter de la referència, els de
    control deixen de quadrar i es detecta l'error.

## Resum comparatiu

| | Urbana | Rústica | Disseminat |
|---|---|---|---|
| Aspecte | `7412801EE9271A0001IF` | `07002A006001400000GQ` | `000500300FE01C` + càrrec + control |
| Ubicació | Mançana, parcel·la i full del plànol | Província, municipi, sector, polígon i parcel·la | Estil urbà, comença per `00` |
| 14 primers | Mançana (5) + parcel·la (2) + full (7) | Prov. (2) + mun. (3) + sector (1) + pol. (3) + parcel·la (5) | Estil urbà |
| Càrrec | 4 dígits | 4 dígits | 4 dígits |
| Control | 2 lletres | 2 lletres | 2 lletres |
| Es crea de nou? | Sí | Sí | **No** (només els històrics) |
