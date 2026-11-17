# 4.7. Treballar amb el cadastre

## Objectiu

En acabar sabràs carregar la cartografia cadastral, localitzar una parcel·la al
visor i obrir-ne la fitxa oficial al Cadastre.

## Passos

1. **Carregar la cartografia cadastral.** És a les capes disponibles, dins
   **Ordenació del territori i cadastre → Cadastre**
   ([4.5](05-capes-tematiques.md)). Carrega-hi **`Catastro`**: és la que dibuixa
   la cartografia cadastral sencera. Les altres del grup —`PARCELA`, `CONSTRU`,
   `MASA`…— són peces soltes, per a usos més concrets.

    !!! note "Captura pendent — `img/47-capa-cadastre.png`"
        El cadastre carregat sobre una ortofoto d'un nucli urbà, amb les
        parcel·les dibuixades a sobre de les teulades.

        Peu de foto previst: *La cartografia cadastral dibuixa els límits de les parcel·les sobre el terreny.*

2. **Buscar per referència cadastral.** El quadre de cerca de la capçalera —el
   mateix de la [4.4](04-localitzar-coordenades.md)— accepta referències
   cadastrals. Escriu-ne una i el visor s'hi situa.

3. **Consultar una parcel·la.** Fes clic a sobre, com a la
   [4.6](06-consulta-atributs.md). El requadre no treu cap taula d'atributs: el
   que et dona és la **referència cadastral**, i és un **enllaç**.

    !!! note "Captura pendent — `img/47-dades-parcella.png`"
        El requadre de resultats d'una parcel·la, amb la referència cadastral
        emmarcada.

        Peu de foto previst: *La referència cadastral és, alhora, l'enllaç que obre la fitxa oficial.*

4. **Obrir la fitxa oficial.** L'enllaç obre la Seu Electrònica del Cadastre
   **en una pestanya nova**, amb les dades d'aquella parcel·la. No perds el
   mapa: el visor es queda obert a la pestanya d'abans.

    !!! tip "El visor situa, el Cadastre certifica"
        El visor et serveix per **trobar** la parcel·la i veure-la en context.
        El document amb validesa oficial surt de la **Seu Electrònica del
        Cadastre**, no d'aquí.

!!! warning "La cartografia cadastral ve de fora"
    No és de l'IDE Menorca: la serveix la Direcció General del Cadastre. Per
    això no es pot descarregar en vectorial des del visor, a diferència de les
    capes pròpies.

## Exercici pràctic

1. Carrega la cartografia cadastral.
2. Busca la referència **`7552201FE0175S`** al quadre de cerca.
3. Fes clic sobre la parcel·la: en surt la referència cadastral.
4. Obre la fitxa oficial amb l'enllaç.
5. Compara l'adreça que dona el Cadastre amb el que veus al mapa.

!!! tip "L'edifici el coneixes"
    És la plaça de la Biosfera, 5, de Maó: la seu del Consell Insular de
    Menorca.

---

!!! tip "Al manual de referència"
    El manual encara no té cap apartat de cadastre. Mentrestant, la càrrega de
    capes es descriu a
    [2.3. Buscar i afegir capes](../../../manuals/visor-generic/02-panell-capes.md#23-buscar-i-afegir-capes).
