# Aula IDE Menorca

Cursos de formació i manuals d'usuari de les eines del projecte IDE Menorca.

Codi font del portal, mantingut pel Departament de Cartografia del
**Consell Insular de Menorca**.

TODO: *El lloc publicat: <https://formacio.ide.cime.es> (pendent de confirmar el
subdomini definitiu — vegeu [DEPLOY.md](DEPLOY.md))*

Està fet amb [MkDocs](https://www.mkdocs.org/) i el tema
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), i es
publica automàticament a GitHub Pages a cada canvi a la branca `main`.

## Aixecar el lloc en local

Cal Python 3.9 o superior i Git.

```bash
git clone https://github.com/IDEmenorca/aula.git
cd aula

python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1

pip install -r requirements.txt
mkdocs serve
```

El lloc queda disponible a <http://127.0.0.1:8000>. Es recarrega tot sol cada
vegada que deses un fitxer.

Per comprovar el que farà el desplegament (enllaços trencats inclosos):

```bash
mkdocs build --strict
```

### Si toques el tema o el CSS

`mkdocs build` copia `docs/stylesheets/extra.css` sense mirar-se'l. Si canvies
una opció de `theme.features`, l'HTML que genera Material canvia i un selector
del CSS propi pot deixar d'aplicar-se **sense cap error**: el lloc es publica,
simplement sense aquell estil.

Per detectar-ho:

```bash
pip install -r requirements-dev.txt
mkdocs build
python tools/comprova-estils.py
```

Comprova que cada selector del CSS propi encara trobi algun element. També
s'executa a cada desplegament, després de la construcció.

## Com contribuir

Els canvis no es fan mai directament a `main`:

1. Crea una branca: `git switch -c contingut/modul-4-navegacio`
2. Edita els fitxers Markdown dins de `docs/`
3. Comprova-ho en local amb `mkdocs serve`
4. Fes commit i puja la branca: `git push -u origin la-teva-branca`
5. Obre un *pull request* i demana revisió

Quan el PR es fusiona a `main`, GitHub Actions reconstrueix i publica el lloc
en un parell de minuts.

## Organització dels fitxers

```
docs/
├── index.md              portada
├── formacio/             cursos (bàsic, intermedi)
├── manuals/              manuals d'usuari dels visors
├── stylesheets/          estils propis
└── CNAME                 domini personalitzat
```

**Regla d'imatges:** cada secció desa les seves captures en una subcarpeta
`img/` al seu costat (per exemple `docs/formacio/basic/modul-4-visor/img/`),
mai en una carpeta global. Així es pot moure o esborrar una secció sencera
sense deixar imatges òrfenes.

La navegació del menú es defineix explícitament a `mkdocs.yml`, a la clau
`nav`. Si afegeixes una pàgina nova, has d'afegir-la també allà: si no,
`mkdocs build --strict` fallarà.
