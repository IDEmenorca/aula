# 5.3. Eines bàsiques

## Objectiu

En acabar aquesta secció sabràs entrar al visor restringit, reconèixer-ne les
parts i trobar un lloc amb les eines del menú **Localitzar**.

## Entrar al visor

1. **Obre la pàgina d'entrada:** <https://ide.cime.es/sitmun/inicio.jsp>.

2. **Escriu l'usuari i la contrasenya** a **Accés Privat** i prem **Entrar**.

    <figure markdown>
      ![Pàgina d'entrada de l'IDE Menorca amb els quadres Accés Públic i Accés Privat; el d'Accés Privat, amb les caselles Usuari i Contrasenya i els botons Entrar i Modificar contrasenya, ressaltat](img/03-entrar.png){ .captura }
      <figcaption>L'usuari i la contrasenya del curs te'ls donarem a classe.</figcaption>
    </figure>

3. **Tria l'aplicació i el territori.** Si el teu usuari només en té un de
   cada, no cal triar: el visor hi entra directament.

    <figure markdown>
      ![Pantalla de selecció amb els desplegables Selecciona una aplicació, amb Restringit_edicio_arbrat, i Selecciona un territori, amb Ciutadella, i el missatge carregant](img/03-aplicacio.png){ .captura }
      <figcaption>Amb l'usuari del curs no cal triar res.</figcaption>
    </figure>

## La vista inicial

<figure markdown>
  ![Vista inicial del visualitzador de consulta de capes restringides, amb quatre zones ressaltades i numerades: 1, els menús Localitzar i Eines i el quadre On vols anar?; 2, el menú Capes de Fons; 3, l'arbre de capes de la dreta; 4, la barra d'eines de baix amb l'escala](img/03-vista-inicial.png){ .captura }
  <figcaption>Les parts del visor restringit.</figcaption>
</figure>

1. **A dalt a l'esquerra:** els menús **Localitzar** i **Eines**, i el quadre
   **On vols anar?**, que és un cercador general.
2. **A dalt a la dreta:** el menú **Capes de Fons**.
3. **A la dreta:** l'arbre de capes, amb les pestanyes **Abre**, **Afegir
   capes** i **Llegenda**.
4. **A baix:** la barra d'eines i l'escala.

## Localitzar

El menú **Localitzar** té cinc eines. Cadascuna s'obre en una finestra petita
damunt el mapa. Aquí en veurem quatre: la **Llista de Municipis** també hi és,
però no la veurem.

<figure markdown>
  ![Menú Localitzar desplegat, ressaltat amb el número 1, amb les opcions Infraestructures i equipaments, Llista de Municipis, Guia de carrers, Topònims i Localització de coordenades; al costat, la finestra Infraestructures i equipaments, ressaltada amb el número 2, amb la cerca salut i dos centres de salut a la llista](img/03-localitzar-infraestructures.png){ .captura }
  <figcaption>El menú Localitzar i la cerca d'infraestructures i equipaments.</figcaption>
</figure>

| Eina | Per trobar... | Com |
|---|---|---|
| **Infraestructures i equipaments** | Un equipament | Escriu el nom a **Nom a buscar** i prem **Cerca**. Marca'n un o més a la llista i prem **Centrar**: el mapa t'hi porta i els marca. **Tots** els marca tots |
| **Guia de carrers** | Una adreça | Municipi, nucli, carrer i portal. Cada nivell té el seu botó **Centrar** |
| **Topònims** | Un lloc pel seu nom | Escriu-ne un tros, tria'l de la llista i prem **Centrar**. A la llista hi surt el nom, el tipus i el municipi |
| **Localització de coordenades** | Un punt | Escriu la X i la Y en ETRS89 31N i prem **Accepta** |

!!! tip "Només t'hi porta"
    Llevat d'**Infraestructures i equipaments**, aquestes eines no deixen cap
    marca al mapa: només t'hi porten.

<div class="figures-costat" markdown>
<figure markdown>
  ![Finestra Guia de carrers amb municipi Ciutadella, nucli Cala Blanca, carrer Baladre, passatge, i portal 10, cadascun amb el botó Centrar](img/03-localitzar-carrers.png){ .captura }
  <figcaption>Guia de carrers</figcaption>
</figure>
<figure markdown>
  ![Finestra Topònims amb sal escrit al quadre Nom a buscar i la llista de llocs que ho contenen, amb el nom, el tipus i el municipi](img/03-localitzar-toponims.png){ .captura }
  <figcaption>Topònims</figcaption>
</figure>
<figure markdown>
  ![Finestra Localització de coordenades amb les caselles X i Y en ETRS89 31N i el botó Accepta](img/03-localitzar-coordenades.png){ .captura }
  <figcaption>Localització de coordenades</figcaption>
</figure>
</div>

!!! info "Un sol sistema de referència"
    Al visor restringit, les coordenades només es poden escriure en ETRS89 31N.
    Al visor genèric en pots triar tres
    ([4.6](../modul-4-visor-generic/06-localitzadors.md)).

## Exercici: troba-ho al visor restringit

- [ ] Entra al visor restringit amb l'usuari del curs.
- [ ] **Infraestructures i equipaments**: cerca **salut**, marca el **Centre de
  Salut Verge del Toro** i prem **Centrar**. A quin municipi és?
- [ ] **Guia de carrers**: troba l'adreça de la teva feina.
- [ ] **Topònims**: troba **Cala Cabra Salada**. De quin municipi és?
- [ ] **Localització de coordenades**: ves a X 570261, Y 4433650. Quin far hi
  trobes?
- [ ] **On vols anar?**: escriu-hi el nom d'un lloc que coneguis.
