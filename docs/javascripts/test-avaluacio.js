/* =========================================================================
   Aula IDE Menorca — el test d'avaluació dins la pàgina del mòdul 5

   El test és una pàgina a part (formacio/basic/test-curs-basic.html) que es
   mostra dins un iframe amb l'atribut data-aula-test. Aquest fitxer:
     - ajusta l'alçada de l'iframe a la del test, que en va avisant;
     - quan el test canvia de pregunta, puja la pàgina fins a dalt del test;
     - passa al test el tema clar o fosc que tingui triat la web.
   ========================================================================= */

(function () {
  "use strict";

  function iframes() {
    return document.querySelectorAll("iframe[data-aula-test]");
  }

  function tema() {
    return document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "light";
  }

  function aplicaTema(iframe) {
    try {
      iframe.contentDocument.documentElement.setAttribute("data-theme", tema());
    } catch (e) { /* encara no s'ha carregat */ }
  }

  window.addEventListener("message", function (e) {
    if (e.origin !== window.location.origin) return;
    var d = e.data;
    if (!d || d.font !== "aula-test") return;
    iframes().forEach(function (iframe) {
      if (iframe.contentWindow !== e.source) return;
      if (d.alcada) iframe.style.height = d.alcada + "px";
      if (d.amunt) {
        var capcalera = document.querySelector(".md-header");
        var marge = (capcalera ? capcalera.offsetHeight : 0) + 8;
        var dalt = iframe.getBoundingClientRect().top;
        if (dalt < marge) window.scrollTo(0, window.scrollY + dalt - marge);
      }
    });
  });

  function prepara() {
    iframes().forEach(function (iframe) {
      aplicaTema(iframe);
      iframe.addEventListener("load", function () { aplicaTema(iframe); });
    });
  }

  // Si es canvia el tema amb el botó de la capçalera, el test el segueix.
  new MutationObserver(function () {
    iframes().forEach(aplicaTema);
  }).observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(prepara);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", prepara);
  } else {
    prepara();
  }
})();
