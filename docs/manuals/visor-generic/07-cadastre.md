# 7. El cadastre

La cartografia cadastral no és de l'IDE Menorca: la serveix la **Direcció General
del Cadastre**. El visor la carrega com una capa més, però la consulta d'una
parcel·la no es comporta com la de la resta de capes: en comptes d'una taula
d'atributs, en retorna la **referència cadastral** en forma d'enllaç a la Seu
Electrònica del Cadastre.

## 7.1. Carregar la cartografia cadastral

Les capes del cadastre són a **Capes disponibles**, dins **Ordenació del
territori i cadastre → Cadastre**.

<figure markdown>
  ![El desplegable del cadastre amb la capa Catastro emmarcada, i les parcel·les dibuixades sobre el mapa](img/90-capes-cadastre.png){ .captura }
  <figcaption>La capa Catastro dibuixa la cartografia cadastral sencera.</figcaption>
</figure>

La capa **`Catastro`** dibuixa la cartografia cadastral sencera: és la que es
carrega habitualment. Les altres del grup són les capes individuals que
`Catastro` reuneix, amb el nom que els dona el servei del Cadastre:

`CONSTRU`, `TXTCONSTRU`, `SUBPARCE`, `TXTSUBPARCE`, `PARCELA`, `TXTPARCELA`,
`MASA`, `TXTMASA`, `EJES`, `LIMITES`, `TEXTOS` i `ELEMLIN`.

## 7.2. Trobar una parcel·la per la seva referència

El quadre de cerca de la capçalera, el mateix que troba municipis, nuclis,
carrers, camins i topònims, accepta també **referències cadastrals**. En
escriure'n una, el visor s'hi situa.

## 7.3. Consultar una parcel·la

Amb la capa carregada, un clic sobre una parcel·la obre el requadre de resultats
de la [selecció gràfica](04-seleccio-grafica.md). A dalt hi surten, com sempre,
el sistema de referència, les coordenades i l'elevació del punt; a sota, en
comptes d'una taula d'atributs, hi ha la **referència cadastral de la parcel·la**
com a enllaç.

<figure markdown>
  ![El requadre de resultats d'una parcel·la, amb la referència cadastral emmarcada](img/91-referencia-parcella.png){ .captura }
  <figcaption>La referència cadastral és, alhora, l'enllaç que obre la fitxa oficial.</figcaption>
</figure>

L'enllaç obre la **Seu Electrònica del Cadastre** en una pestanya nova, amb les
dades d'aquella parcel·la. El visor es queda obert a la pestanya d'abans.

!!! note "Només s'hi pot imprimir"
    Aquest requadre no porta els botons de descarregar ni de compartir que tenen
    les capes pròpies: només el d'imprimir.

## 7.4. Què certifica cada cosa

El visor serveix per **situar** la parcel·la i veure-la en context. El document
amb validesa oficial surt de la **Seu Electrònica del Cadastre**, no del visor.
