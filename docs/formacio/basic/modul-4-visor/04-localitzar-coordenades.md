# 4.4. Localitzar i obtenir coordenades

## Objectiu

En acabar sabràs trobar un lloc pel nom i obtenir les coordenades de qualsevol
punt del mapa.

## Passos

1. **Cercar un lloc pel nom.** El quadre de cerca és a la capçalera. Accepta
   municipis, nuclis, carrers i **referències cadastrals**. Tria un resultat de
   la llista i el visor s'hi situa.

    !!! note "Captura pendent — `img/44-cercador.png`"
        El quadre de cerca amb text escrit i la llista de resultats desplegada
        a sota.

        Peu de foto previst: *El cercador troba municipis, nuclis, carrers i referències cadastrals.*

2. **Obtenir les coordenades d'un punt.** Fes clic sobre el mapa. El visor et
   dóna sempre el sistema de referència, les **coordenades** i l'**elevació**
   del punt. Si allà hi ha elements d'alguna capa carregada, hi afegeix la
   seva informació a sota.

    !!! note "Captura pendent — `img/44-coordenades-punt.png`"
        El quadre amb el sistema de referència, les coordenades x i y i
        l'elevació del punt consultat.

        Peu de foto previst: *Fent clic en un punt buit, el visor en dóna les coordenades i l'altitud del terreny.*

3. **Llegir les coordenades del cursor.** Al cantó inferior esquerre hi ha un
   indicador que va mostrant, en temps real, el sistema de referència actiu i
   les coordenades d'allà on tens el ratolí.

4. **Canviar el sistema de coordenades.** Prem l'indicador del cantó inferior
   esquerre. S'obre un quadre amb la projecció actual i les compatibles.

    El visor treballa per defecte en **ETRS89 / UTM zone 31N (EPSG:25831)**, que
    és l'oficial a les Illes Balears i dóna les coordenades en **metres**. En
    canviar a **WGS 84 (EPSG:4326)**, el mateix punt passa a expressar-se en
    **graus**.

## Exercici pràctic

1. Cerca un **carrer de Ferreries** al quadre de cerca.
2. Fes **clic sobre un edifici** i apunta'n les coordenades i l'elevació.
3. Canvia el sistema de coordenades a **WGS 84** i torna a mirar el mateix
   punt: els números passen de metres a graus, però el lloc és el mateix.
4. Torna a **ETRS89 / UTM 31N**.

---

!!! tip "Al manual de referència"
    [1.6. Sistema de coordenades i coordenades del cursor](../../../manuals/visor-generic/01-interficie.md#16-sistema-de-coordenades-i-coordenades-del-cursor)
