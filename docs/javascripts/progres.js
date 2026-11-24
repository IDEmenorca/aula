/* =========================================================================
   Aula IDE Menorca — progrés de lectura dels cursos

   Què fa:
     - Marca una secció com a llegida quan el final de la pàgina apareix a la
       pantalla. Al menú de l'esquerra hi surt una ✓.
     - Desa les caselles dels exercicis. Si una secció té totes les caselles
       marcades, al menú hi surten dues ✓.
     - Al costat del títol de cada mòdul hi posa quantes seccions se n'han
       llegit: «3/9».
     - Els botons amb l'atribut data-progres-reinicia="basic" (o "mig")
       esborren el progrés d'aquell curs.

   Només compta les pàgines de /formacio/. Tot es desa al localStorage del
   navegador: no surt res de l'ordinador de l'alumne. Si el navegador no deixa
   desar-hi res (finestra privada, dades bloquejades), el lloc funciona igual,
   només que sense marques.

   El tema té la navegació instantània activada: les pàgines es canvien sense
   recarregar. Per això tot es torna a aplicar cada vegada que el tema emet
   document$, que és el senyal que fa servir per avisar que hi ha pàgina nova.
   ========================================================================= */

(function () {
  "use strict";

  var CLAU = "aula-ide-progres-v1";

  /* --- Desar i llegir --------------------------------------------------- */

  function llegeix() {
    try {
      var dades = JSON.parse(window.localStorage.getItem(CLAU));
      if (dades && typeof dades === "object") {
        dades.llegides = dades.llegides || {};
        dades.caselles = dades.caselles || {};
        return dades;
      }
    } catch (e) { /* sense localStorage o dades malmeses: es comença de zero */ }
    return { llegides: {}, caselles: {} };
  }

  function desa(dades) {
    try {
      window.localStorage.setItem(CLAU, JSON.stringify(dades));
    } catch (e) { /* no es pot desar: les marques només duren aquesta visita */ }
  }

  /* --- Camins ----------------------------------------------------------- */

  // Totes les adreces es comparen pel camí absolut i acabat en barra, que és
  // la forma que tenen les pàgines amb use_directory_urls.
  function normalitza(cami) {
    cami = cami.replace(/index\.html$/, "");
    return cami.charAt(cami.length - 1) === "/" ? cami : cami + "/";
  }

  function camiDe(href) {
    return normalitza(new URL(href, window.location.href).pathname);
  }

  function esDeCurs(cami) {
    return cami.indexOf("/formacio/") !== -1;
  }

  // Una secció és una pàgina que comença per dues xifres: 01-navegacio/...
  // La presentació de cada mòdul no compta per al comptador.
  function esSeccio(cami) {
    return /\/\d\d-[^/]+\/$/.test(cami);
  }

  function exerciciFet(dades, cami) {
    var c = dades.caselles[cami];
    if (!c || !c.length) return false;
    for (var i = 0; i < c.length; i++) if (!c[i]) return false;
    return true;
  }

  /* --- Menú de l'esquerra ----------------------------------------------- */

  function posaMarca(enllac, text, titol) {
    var vella = enllac.querySelector(":scope > .progres-marca");
    if (vella) vella.remove();
    if (!text) return;
    var marca = document.createElement("span");
    marca.className = "progres-marca";
    marca.textContent = text;
    marca.title = titol;
    var icona = enllac.querySelector(":scope > .md-nav__icon");
    enllac.insertBefore(marca, icona);
  }

  function decoraMenu(dades) {
    // Cada pàgina del menú: un <li> amb un enllaç directe que no és cap ancora
    // de l'índex de la pàgina. La pàgina activa també hi té una etiqueta.
    // L'índex de la pàgina oberta (.md-nav--secondary) no compta: amb la
    // navegació instantània, els seus enllaços poden arribar amb el camí
    // sencer davant de l'ancora, i semblarien la pàgina mateixa.
    var items = document.querySelectorAll(".md-sidebar--primary li.md-nav__item");
    items.forEach(function (li) {
      if (li.closest(".md-nav--secondary")) return;
      var a = li.querySelector(":scope > a.md-nav__link");
      if (!a || new URL(a.getAttribute("href"), window.location.href).hash) return;
      var cami = camiDe(a.getAttribute("href"));
      li.dataset.progresCami = cami;
      if (!esDeCurs(cami)) return;

      var text = "", titol = "";
      if (exerciciFet(dades, cami)) {
        text = "✓✓"; titol = "Llegida i amb l'exercici fet";
      } else if (dades.llegides[cami]) {
        text = "✓"; titol = "Llegida";
      }
      li.querySelectorAll(":scope > .md-nav__link").forEach(function (enllac) {
        posaMarca(enllac, text, titol);
      });
    });

    // Comptador als mòduls i als subgrups (com la 4.7, amb la 4.7.1 i la
    // 4.7.2): el porta tot grup que tingui alguna secció penjada directament,
    // i compta totes les seccions de dins, també les dels subgrups. El grup del
    // curs no en porta, perquè dins només hi té mòduls.
    var grups = document.querySelectorAll(".md-sidebar--primary li.md-nav__item--nested");
    grups.forEach(function (grup) {
      var etiqueta = grup.querySelector(":scope > label.md-nav__link, :scope > a.md-nav__link");
      var llista = grup.querySelector(":scope > nav > ul.md-nav__list");
      if (!etiqueta || !llista) return;

      var directa = false;
      llista.querySelectorAll(":scope > li.md-nav__item").forEach(function (li) {
        var cami = li.dataset.progresCami;
        if (cami && esDeCurs(cami) && esSeccio(cami)) directa = true;
      });

      var total = 0, fetes = 0;
      if (directa) {
        llista.querySelectorAll("li.md-nav__item").forEach(function (li) {
          if (li.closest(".md-nav--secondary")) return;
          var cami = li.dataset.progresCami;
          if (!cami || !esDeCurs(cami) || !esSeccio(cami)) return;
          total++;
          if (dades.llegides[cami] || exerciciFet(dades, cami)) fetes++;
        });
      }

      var vell = etiqueta.querySelector(":scope > .progres-comptador");
      if (vell) vell.remove();
      if (!total) return;

      var comptador = document.createElement("span");
      comptador.className = "progres-comptador" + (fetes === total ? " progres-comptador--complet" : "");
      comptador.textContent = fetes + "/" + total;
      comptador.title = fetes + " de " + total + " seccions llegides";
      etiqueta.insertBefore(comptador, etiqueta.querySelector(":scope > .md-nav__icon"));
    });
  }

  /* --- Final de la pàgina ------------------------------------------------ */

  var observador = null;

  function vigilaFinal(cami) {
    if (observador) { observador.disconnect(); observador = null; }
    if (!esDeCurs(cami) || !("IntersectionObserver" in window)) return;

    var article = document.querySelector(".md-content__inner");
    if (!article) return;
    var sentinella = document.createElement("div");
    sentinella.className = "progres-sentinella";
    sentinella.setAttribute("aria-hidden", "true");
    article.appendChild(sentinella);

    observador = new IntersectionObserver(function (entrades) {
      if (!entrades.some(function (e) { return e.isIntersecting; })) return;
      var dades = llegeix();
      if (!dades.llegides[cami]) {
        dades.llegides[cami] = Date.now();
        desa(dades);
        decoraMenu(dades);
      }
      observador.disconnect();
      observador = null;
    });
    observador.observe(sentinella);
  }

  /* --- Caselles dels exercicis ------------------------------------------ */

  function caselles() {
    return Array.prototype.slice.call(
      document.querySelectorAll(".md-content .task-list-item input[type=checkbox]")
    );
  }

  function preparaCaselles(cami) {
    if (!esDeCurs(cami)) return;
    var llista = caselles();
    if (!llista.length) return;

    // Es recupera l'estat només si la pàgina té les mateixes caselles que quan
    // es va desar; si s'hi n'han afegit o tret, l'estat vell ja no hi encaixa.
    var desades = llegeix().caselles[cami];
    if (desades && desades.length === llista.length) {
      llista.forEach(function (c, i) { c.checked = !!desades[i]; });
    }

    llista.forEach(function (c) {
      c.addEventListener("change", function () {
        var dades = llegeix();
        dades.caselles[cami] = caselles().map(function (x) { return x.checked; });
        desa(dades);
        decoraMenu(dades);
      });
    });
  }

  /* --- Reiniciar --------------------------------------------------------- */

  var NOMS = { basic: "del curs bàsic", mig: "del curs mitjà" };

  function preparaReinici() {
    document.querySelectorAll("[data-progres-reinicia]").forEach(function (boto) {
      boto.addEventListener("click", function () {
        var curs = boto.getAttribute("data-progres-reinicia");
        var nom = NOMS[curs] || "d'aquest curs";
        if (!window.confirm("Segur que vols esborrar el progrés " + nom + "? No es pot desfer.")) return;

        var dades = llegeix();
        var prefix = "/formacio/" + curs + "/";
        ["llegides", "caselles"].forEach(function (tipus) {
          Object.keys(dades[tipus]).forEach(function (cami) {
            if (cami.indexOf(prefix) !== -1) delete dades[tipus][cami];
          });
        });
        desa(dades);
        decoraMenu(dades);
        boto.textContent = "Progrés esborrat";
        boto.disabled = true;
      });
    });
  }

  /* --- Cada pàgina nova -------------------------------------------------- */

  function enCadaPagina() {
    var cami = normalitza(window.location.pathname);
    decoraMenu(llegeix());
    preparaCaselles(cami);
    preparaReinici();
    vigilaFinal(cami);
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(enCadaPagina);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enCadaPagina);
  } else {
    enCadaPagina();
  }
})();
