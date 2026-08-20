# Captures pendents

Llista generada automàticament amb `python tools/captures.py --llista`.
No l'editis a mà: es regenera.

Queden **34 captures** per fer.

## Com afegir-les

1. Fes la captura del visor.
2. Desa-la amb **exactament** el nom i a **exactament** la carpeta que
   indica la columna «Fitxer». Les carpetes ja existeixen.
3. Executa `python tools/captures.py --insereix`.
4. Comprova-ho amb `mkdocs serve` i fes el commit.

No cal fer-les totes de cop: l'script insereix les que hi hagi i deixa
la resta com a marcadors.

> **Consell.** Fes les captures amb la finestra prou ampla i sense dades
> personals a la vista. Retalla-les a l'element que es descriu: una captura
> de pantalla sencera per ensenyar un botó no s'entén.

## `docs/manuals/visor-generic/01-interficie.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/img/01-interficie-general.png` | El visor acabat d'obrir, amb tota l'illa visible i els **quinze elements numerats** amb globus sobre la imatge, en el mateix ordre de la taula de sota. És la captura més important del manual: convé fer-la a pantalla ampla i que s'hi llegeixin bé els números |
| `docs/manuals/visor-generic/img/02-botons-zoom.png` | Detall retallat dels botons de zoom: dos botons quadrats negres, **+** i **−**, apilats verticalment |
| `docs/manuals/visor-generic/img/03-extensio-inicial.png` | Botó d'extensió inicial amb icona de casa |
| `docs/manuals/visor-generic/img/04-pantalla-completa.png` | Els dos estats del botó de pantalla completa: negre quan s'hi entra, vermell quan ja s'hi és a dins |
| `docs/manuals/visor-generic/img/05-indicador-crs.png` | Indicador de CRS mostrant EPSG:25831 i les coordenades x i y del cursor |

## `docs/manuals/visor-generic/02-panell-capes.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/img/10-capcalera-panell.png` | Capçalera del panell amb l'enllaç d'ajuda i els selectors d'idioma ca, es i en |
| `docs/manuals/visor-generic/img/11-control-lliscant.png` | Control lliscant entre l'ortofoto de 2021 i el mapa base de l'IDE Menorca |
| `docs/manuals/visor-generic/img/12-avis-crs.png` | Miniatura d'un mapa de fons amb el símbol de fletxa que indica un CRS diferent |
| `docs/manuals/visor-generic/img/13-graella-mapes-fons.png` | Graella de miniatures amb tots els mapes de fons disponibles |
| `docs/manuals/visor-generic/img/14-arbre-capes.png` | Arbre de capes amb un node desplegat i el cursor en forma de mà sobre una capa |
| `docs/manuals/visor-generic/img/15-cercador-capes.png` | Cercador de capes amb resultats agrupats per servei |
| `docs/manuals/visor-generic/img/16-canviar-tema.png` | Finestra de canvi de tema amb les icones dels temes disponibles |
| `docs/manuals/visor-generic/img/17-capes-carregades.png` | Llista de capes carregades amb les icones de cada capa |

## `docs/manuals/visor-generic/03-eines/01-dibuixar-mesurar.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/03-eines/img/20-dibuixar-panell.png` | Panell Dibuixar i medir amb les pestanyes de punts, línies i polígons |
| `docs/manuals/visor-generic/03-eines/img/21-punts.png` | Pestanya de punts amb els controls de color, gruix i les coordenades del punt |
| `docs/manuals/visor-generic/03-eines/img/22-perfil-elevacio.png` | Panell de perfil d'elevació amb la corba del terreny i el desnivell |
| `docs/manuals/visor-generic/03-eines/img/23-poligons.png` | Pestanya de polígons mostrant àrea i perímetre del polígon dibuixat |
| `docs/manuals/visor-generic/03-eines/img/24-modificar-geometria.png` | Polígon abans i després de moure un vèrtex per modificar-ne la forma |
| `docs/manuals/visor-generic/03-eines/img/25-descarregar-dibuix.png` | Diàleg de descàrrega del dibuix amb l'opció d'incloure elevacions i els formats disponibles |

## `docs/manuals/visor-generic/03-eines/02-imprimir.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/03-eines/img/30-imprimir-panell.png` | Panell Imprimir amb els camps de títol, disseny, mida i la casella del codi QR |
| `docs/manuals/visor-generic/03-eines/img/31-imprimir-previsualitzacio.png` | Previsualització dinàmica amb el marc ajustable de l'àrea d'impressió. El manual original no en té cap imatge, tot i ser el pas on l'usuari es queda encallat més sovint |

## `docs/manuals/visor-generic/03-eines/03-descarregar.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/03-eines/img/40-descarregar-panell.png` | Panell Descarregar amb les pestanyes Imatge del mapa i Capes vectorials |
| `docs/manuals/visor-generic/03-eines/img/41-descarregar-imatge.png` | Pestanya d'imatge del mapa amb el selector de format i la casella del codi QR |
| `docs/manuals/visor-generic/03-eines/img/42-descarregar-vectorial.png` | Pestanya de capes vectorials amb el selector de format |

## `docs/manuals/visor-generic/03-eines/04-compartir.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/03-eines/img/50-compartir-panell.png` | Panell Compartir amb les icones de correu, QR, Facebook, X i marcador, i les pestanyes Compartir enllaç i Insertar mapa |
| `docs/manuals/visor-generic/03-eines/img/51-insertar-mapa.png` | Pestanya Insertar mapa amb el codi de l'etiqueta iframe i el botó de copiar |

## `docs/manuals/visor-generic/04-seleccio-grafica.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/img/60-barra-seleccio.png` | Barra de selecció amb els botons per punt, per línia i per recinte sota una capa carregada |
| `docs/manuals/visor-generic/img/61-requadre-resultats.png` | Requadre de resultats amb les taules d'atributs agrupades per capa i els objectes ressaltats al mapa |
| `docs/manuals/visor-generic/img/62-perfil-entitat.png` | Perfil d'elevació d'un tram del camí de cavalls al costat de la seva taula d'atributs |

## `docs/manuals/visor-generic/05-consultes.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/img/70-boto-consultes.png` | Botó de consultes ressaltat a la fila d'una capa carregada |
| `docs/manuals/visor-generic/img/71-consulta-dialeg.png` | Diàleg de consulta alfanumèrica amb el desplegable d'atributs, els criteris i la caixa de valor |
| `docs/manuals/visor-generic/img/72-resultats-consulta.png` | Taula de resultats d'una consulta amb els elements ressaltats en vermell sobre el mapa |
| `docs/manuals/visor-generic/img/73-filtre-espacial.png` | Diàleg de consulta amb l'atribut the_geom seleccionat i els criteris interseca i dins |

## `docs/manuals/visor-generic/06-street-view.md`

| Fitxer | Què ha de mostrar |
|---|---|
| `docs/manuals/visor-generic/img/80-icona-street-view.png` | Icona de Google Street View a la columna d'eines del visor |
