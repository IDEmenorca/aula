# Pla de publicació

Com es publica l'Aula IDE Menorca, què està fet i què queda per fer.

**Estat a 20 d'agost de 2026:** el lloc ja es publica automàticament i és accessible a
<https://idemenorca.github.io/aula/>. El que queda és passar-lo al subdomini propi.

---

## 1. Com funciona la publicació

A cada canvi que arriba a `main`, GitHub Actions executa
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml):

1. Descarrega el codi amb l'historial complet (`fetch-depth: 0`).
2. Instal·la les dependències fixades a `requirements.txt`.
3. Construeix el lloc amb `mkdocs build --strict`.
4. Puja el resultat com a artefacte de Pages i el desplega.

No hi ha branca `gh-pages` ni ningú escriu al repositori. Fem servir el **mètode
d'artefacte d'Actions**, que és el que recomana GitHub actualment.

> **`--strict` atura la construcció davant de qualsevol avís**: un enllaç intern
> trencat, una imatge que no existeix, una pàgina que no és a la `nav`. És deliberat:
> val més que falli la publicació que no publicar el lloc amb enllaços morts. Si el
> desplegament falla, mira't primer aquest pas.

---

## 2. Fet

- [x] Estructura del lloc, configuració de MkDocs i tema.
- [x] Workflow de desplegament.
- [x] Repositori creat a <https://github.com/IDEmenorca/aula>.
- [x] **Pages activat** amb origen «GitHub Actions».
- [x] Primer desplegament correcte.

---

## 3. Queda per fer

### 3.1. Confirmar el subdomini

Tot aquest document assumeix **`formacio.ide.cime.es`**, que encara **no està
confirmat**. Si finalment és un altre, canvia'l a tots els passos següents.

### 3.2. Demanar el registre DNS

Aquest pas va **primer**, abans de tocar res a GitHub. Demana-ho a qui gestioni la zona
`cime.es` amb aquestes dades exactes:

| Camp | Valor |
|---|---|
| Tipus de registre | `CNAME` |
| Nom / Host | `formacio.ide` |
| Valor / Destinació | `idemenorca.github.io.` |
| TTL | 3600 (o el que tinguin per defecte) |

Tres precisions que estalvien mal d'entendre's:

- El nom del registre és **`formacio.ide`**, no el domini sencer. La majoria de gestors
  de DNS hi afegeixen `.cime.es` automàticament. Si el seu els demana el nom complet,
  llavors sí: `formacio.ide.cime.es`.
- La destinació és **`idemenorca.github.io`**, el compte d'organització, **sense**
  `/aula`. Un registre DNS apunta a una màquina, no a una carpeta.
- El **punt final** de `idemenorca.github.io.` és correcte i important en molts
  sistemes: indica que el nom és absolut. Si el seu gestor no l'accepta, que el treguin.

> **No demanis registres `A`.** Els registres `A` amb les IP de GitHub només calen per a
> dominis d'arrel (`cime.es`). Per a un subdomini, el `CNAME` és el correcte i
> l'aconsellat: si GitHub canvia d'infraestructura, no s'ha de tocar res.

**Quant triga.** El registre sol propagar-se en minuts, però formalment pot arribar a
les 24 hores, i fins a 48 si la zona té TTL alts. Mentrestant el lloc segueix funcionant
per la URL de `github.io`: no hi ha tall de servei.

Per comprovar si ja hi és:

```bash
nslookup formacio.ide.cime.es
```

Ha de respondre amb `idemenorca.github.io`. Mentre digui que no troba el nom, encara no
ha propagat.

### 3.3. Configurar el domini a GitHub

**Només quan el `nslookup` respongui.** Si ho fas abans, GitHub deixarà la verificació
pendent i haurà de reintentar-ho.

1. Ves a <https://github.com/IDEmenorca/aula/settings/pages>.
2. A **Custom domain**, escriu `formacio.ide.cime.es` i prem **Save**.
3. GitHub comprova el DNS. Si el registre hi és, surt una marca verda.

> **No cal crear cap fitxer `CNAME` al repositori.** N'hi havia un a `docs/CNAME` i es
> va eliminar: amb el mètode d'artefacte d'Actions, GitHub **ignora** aquest fitxer i
> agafa el domini només d'aquesta pantalla. El fitxer feia creure que el domini estava
> configurat quan no ho estava.

### 3.4. Esperar el certificat HTTPS

Un cop verificat el domini, GitHub demana automàticament un certificat a Let's Encrypt.

- **Triga entre uns minuts i una hora.** Mentrestant, a la mateixa pantalla surt
  «Certificate not yet created» i la casella **Enforce HTTPS** està desactivada i grisa.
- Quan el certificat estigui llest, **marca «Enforce HTTPS»**. A partir d'aquell moment
  tot el trànsit `http://` es redirigeix a `https://`.
- Si passades unes hores el certificat no arriba, sol ser perquè el DNS encara no
  propagava del tot quan es va desar el domini. Solució: treu el domini personalitzat,
  desa, torna'l a posar i desa.

> **No marquis «Enforce HTTPS» abans que el certificat existeixi**: deixaries el lloc
> inaccessible fins que es generés.

### 3.5. Actualitzar `site_url`

A [`mkdocs.yml`](mkdocs.yml), `site_url` apunta ja a `https://formacio.ide.cime.es/`.
Si el subdomini definitiu és un altre, canvia'l: d'aquí surten els enllaços canònics i
el `sitemap.xml`.

---

## 4. Verificació final

Quan tot estigui fet, comprova aquestes cinc coses:

| Què | Com |
|---|---|
| El domini resol | `nslookup formacio.ide.cime.es` respon `idemenorca.github.io` |
| El lloc carrega | <https://formacio.ide.cime.es> obre la portada |
| HTTPS funciona | El cadenat del navegador, sense avisos de certificat |
| `http` redirigeix | `curl -sI http://formacio.ide.cime.es` retorna `301` cap a `https` |
| La URL antiga redirigeix | <https://idemenorca.github.io/aula/> porta al subdomini nou |

I dins del lloc: que el menú lateral surti sencer, que el cercador trobi text en català,
que les imatges dels manuals es vegin i que el commutador clar/fosc funcioni.

---

## 5. Si el desplegament falla

Mira'l a <https://github.com/IDEmenorca/aula/actions> i identifica **quina de les dues
feines** ha fallat: «Construeix el lloc» o «Desplega a GitHub Pages».

### Falla «Construeix el lloc»

El problema és al contingut. Reprodueix-lo en local, que dóna el mateix error:

```bash
mkdocs build --strict
```

| Missatge | Causa |
|---|---|
| `contains a link '...' but the target is not found` | Enllaç intern o imatge que no existeix. Comprova el nom i el camí |
| `The following pages exist in the docs directory but are not included in the nav` | Has afegit una pàgina i no l'has posada a la `nav` de `mkdocs.yml` |
| `Config value 'plugins': The "..." plugin is not installed` | Falta el connector a `requirements.txt` |
| Error del connector de dates | El `checkout` ha perdut el `fetch-depth: 0` |

### Falla «Desplega a GitHub Pages»

El problema és de configuració, no de contingut.

| Símptoma | Causa |
|---|---|
| Error de permisos o «Pages site not found» | Pages no està activat amb origen «GitHub Actions» a Settings → Pages |
| «Missing environment» | Falta l'entorn `github-pages`. Es crea sol en activar Pages |
| Error de token | Falten els permisos `pages: write` i `id-token: write` al workflow |

### El desplegament diu que ha anat bé però el lloc no es veu

Gairebé sempre és el domini personalitzat: està configurat a Settings → Pages però el
DNS encara no resol, i llavors la URL de `github.io` redirigeix a un domini que no
existeix. Comprova-ho amb `nslookup`. Mentre s'arregla, es pot treure el domini
personalitzat i el lloc torna a `idemenorca.github.io/aula/`.

---

## 6. Publicar un canvi de contingut

El dia a dia, un cop tot això estigui fet:

```bash
git switch -c contingut/el-que-sigui
# edita els fitxers de docs/
mkdocs serve                 # comprova-ho a http://127.0.0.1:8000
mkdocs build --strict        # comprova que passarà a CI
git add -A && git commit -m "..."
git push -u origin contingut/el-que-sigui
```

Obre un *pull request*. En fusionar-lo a `main`, el lloc es reconstrueix i es publica
en un parell de minuts.
