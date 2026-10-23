# 4.5. Buscar i carregar capes temàtiques

## Objectiu

En acabar sabràs trobar una capa d'informació, carregar-la al mapa i ajustar
com es veu.

## Passos

1. **Obrir el panell de capes disponibles.** És a la banda dreta, sota els
   mapes de fons. La informació hi està organitzada per temes:

    - Ordenació del territori i cadastre
    - Urbanisme i habitabilitat
    - Turisme, cultura i patrimoni
    - Medi ambient, agricultura i caça
    - Equipaments i infraestructures públiques
    - Cartografia històrica (Cartoteca)
    - Bases i mapes topogràfics

    <figure markdown>
      ![El panell de capes disponibles amb un dels temes desplegat i les seves capes a la vista](img/45-arbre-capes.png){ .captura }
      <figcaption>Les capes estan agrupades per temes; cada tema es desplega amb el botó del costat.</figcaption>
    </figure>

2. **Trobar una capa per l'arbre.** Desplega els temes fins a arribar a la capa
   que vols i fes-hi clic per carregar-la.

    L'arbre té quatre nivells —tema, servei, grup de capes i capa— o sigui que
    sovint hauràs de desplegar unes quantes vegades abans d'arribar a allò que
    es pot carregar.

    El cursor t'indica on ets: quan es converteix en una **mà**, allò es pot
    afegir al mapa; si es queda en forma de **selecció de text**, encara ets en
    un nivell intermedi i l'has de desplegar. Les capes que ja has carregat
    surten **ressaltades en verd**.

3. **Trobar una capa pel cercador.** Si ja saps què busques, la **lupa** del
   costat de «Capes disponibles» és més ràpida que anar desplegant temes.

    Escriu-hi tres caràcters i començarà a donar resultats. Busca tant al nom
    de la capa com a la seva descripció, i et diu de quin servei surt cadascuna.

4. **Gestionar les capes carregades.** Les que has afegit apareixen al panell
   **Capes carregades**, cadascuna amb les seves eines:

    | Eina | Per a què |
    |---|---|
    | Casella | Amagar i tornar a mostrar la capa sense treure-la |
    | **i** | Veure d'on surt la capa, qui la manté i amb quines condicions |
    | Marc amb fletxa | Ajustar el mapa a l'extensió de la capa |
    | Lupa | Consultar la capa per atributs. Ho veuràs a la [4.6](06-consulta-atributs.md) |
    | Barra lliscant | Fer-la més transparent per veure què hi ha a sota |
    | Fletxes verticals | Canviar l'ordre: quina capa tapa quina |
    | Creu, a dalt a la dreta | Treure la capa del mapa |

    A sota hi ha una fila de **selecció** —per punt, per línia o per recinte—
    que serveix per triar elements sobre el mapa. No actua sobre una sola
    capa: busca a **totes les que tinguis carregades**. També la veuràs a la
    [4.6](06-consulta-atributs.md).

    <figure markdown>
      ![El panell de capes carregades amb un parell de capes i les icones de cadascuna visibles](img/45-capes-carregades.png){ .captura }
      <figcaption>Cada capa carregada porta les seves eines de visibilitat, transparència i ordre.</figcaption>
    </figure>

    !!! tip "Si una capa surt en gris"
        Vol dir que a l'escala on ets no es dibuixa. Apropa't i tornarà a
        aparèixer.

## Exercici pràctic

1. Carrega la **Zonificació de la Reserva de la Biosfera**. És a quatre nivells
   de fondària, i cal desplegar-los un per un:

    ```text
    Medi ambient, agricultura i caça          ← tema
      Medi ambient, agricultura i caça (IDE menorca)   ← servei
        Reserva de la Biosfera                ← grup de capes
          Zonificació de la Reserva de la Biosfera     ← la capa
    ```
2. Posa de mapa de fons una **ortofoto**: veuràs que la capa tapa el terreny.
3. Amb la **barra lliscant** de la capa, baixa-li la transparència fins a veure
   la fotografia a sota.
4. Prova la **casella** per amagar-la i tornar-la a mostrar.
5. Treu-la del mapa amb la **creu**.

---

!!! tip "Al manual de referència"
    [2.3. Buscar i afegir capes](../../../manuals/visor-generic/02-panell-capes.md#23-buscar-i-afegir-capes)
    i [2.5. Capes carregades](../../../manuals/visor-generic/02-panell-capes.md#25-capes-carregades)
