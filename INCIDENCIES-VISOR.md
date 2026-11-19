# Incidències detectades al visor

Coses del **visor**, no d'aquest lloc web, que han anat sortint mentre
redactàvem el curs i el manual. Es recullen aquí per no perdre-les; corregir-les
és feina de qui manté el visor.

**No es publica**: és un document de treball del repositori.

---

## Interfície

| On | Què passa |
|---|---|
| Panell de capes carregades | En carregar una **segona** capa, el panell creix i empeny la resta cap avall. L'arbre de capes disponibles queda tallat per sota i «Afegir mapes» surt de la vista. Amb una sola capa, el panell es veu bé |

---

## Mapes de fons

| On | Què passa |
|---|---|
| Graella de mapes de fons | Els dos mapes **CARTO** —dark i light— no funcionen. S'han de treure de la graella. Mentrestant ja s'han tret de les explicacions: del curs (4.2) i del llistat del manual (2.2) |

---

## Traduccions

| On | Què passa | Hauria de dir |
|---|---|---|
| Fila de selecció, dins del panell de capes carregades | Amb la interfície en **castellà** surt **«Selection by»**, en anglès. Falta la cadena traduïda | «Selección por» |
| Panell d'eines, en **català** | L'eina es diu **«Dibuixar i medir»**. «Medir» és un castellanisme | «Dibuixar i mesurar» |
| Panell **Imprimir**, en **castellà** | El desplegable **Diseño** ofereix **«Horitzontal»**, en català | «Horizontal» |
| Diàleg de descàrrega d'entitats, amb les elevacions marcades i l'opció d'interpolar activada | Al voltant del camp de la distància hi surten les claus internes **«interpolateEveryXMeters.1»** i **«interpolateEveryXMeters.2»** en comptes del text traduït | Alguna cosa com «Interpola un punt cada [20] metres» |
| Mateix diàleg, en **català** | El botó de confirmar diu **«Si»**, sense accent | «Sí» |
| Pestanya **Obrir arxiu** de «Afegir mapes» | La llista de formats no diu el mateix a cada idioma: en **català** hi surt **GPX** i no hi surt **KMZ**; en **castellà**, al revés | La mateixa llista als dos idiomes |

En **català** la mateixa cadena surt bé, «Selecció per». El problema és només a
la versió castellana.

---

## Funcions que té IDENA i aquí no

El visor està fet amb l'API SITNA, la mateixa que el visor d'IDENA de Navarra.
Comparant els dos manuals han sortit diferències que potser interessa igualar.

| Funció | A IDENA | Aquí |
|---|---|---|
| Copiar al porta-retalls les coordenades d'un punt consultat | Sí | No hi ha cap botó |
| Copiar al porta-retalls els atributs d'un element seleccionat | Sí | No hi ha cap botó |

Referència: [manual del visor d'IDENA](https://idena.navarra.es/navegar/pdf/manual.pdf),
edició de setembre del 2026, apartat 13.

---

## Pendent de comprovar

| Què | Per què importa |
|---|---|
| Si els botons de selecció **per línia** i **per recinte** necessiten que la capa tingui WFS, o només que hi hagi alguna capa carregada | IDENA diu que cal WFS. Aquí s'ha provat amb dues capes que en tenen, o sigui que no s'ha pogut descartar. Caldria provar-ho amb una capa que només tingui WMS |
