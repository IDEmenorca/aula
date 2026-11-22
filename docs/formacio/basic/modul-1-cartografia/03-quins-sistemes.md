# 1.3. Quins sistemes de coordenades hi ha?

De sistemes de coordenades n'hi ha moltíssims. Segons quin sigui el propòsit que
tinguis i la zona del món on siguis, en faràs servir un o un altre.

<figure markdown>
  ![Dotze mapes del món dibuixats amb projeccions diferents: Mercator, ortogràfica, Robinson, Gall-Peters, azimutal polar, Mollweide, interrompuda de Goode, cònica, Peirce quincuncial, gnomònica, Eckert IV i Dymaxion](img/03-projeccions-del-mon.jpg){ .captura }
  <figcaption>Dotze maneres de dibuixar el mateix món. Cap no és la correcta.</figcaption>
</figure>

Per entendre-ho millor, mirem de classificar-los. La primera distinció que hem de
fer és entre els **sistemes geogràfics** i els **sistemes projectats**. Resumint:
els geogràfics defineixen les coordenades **en angles** des d'un punt de
referència; els projectats les defineixen per parells de coordenades amb
**unitats de distància** des d'un punt de referència.

<figure markdown>
  ![Quadre comparatiu entre sistemes geogràfics i projectats: com funcionen, de què depenen i quins avantatges i inconvenients tenen](img/04-geografics-i-projectats.jpg){ .captura }
  <figcaption>Els geogràfics situen punts amb graus; els projectats els passen a un pla en metres.</figcaption>
</figure>

## Exercici: com creix Espanya si puja cap al nord

Aquesta és una eina que t'hem preparat per veure com canviaria la mida d'Espanya
si estigués a una altra latitud.

- [ ] Arrossega Espanya cap amunt i cap avall i mira com li canvia la mida.
- [ ] Fixa't en l'escala i l'àrea aparents que et diu el requadre de la dreta.
- [ ] Deixa-la a l'altura d'Escandinàvia i mira quantes vegades més grossa s'hi
  veu.
- [ ] Torna-la a l'origen amb el botó.

<div id="mapa-espanya-wrap">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>
#mapa-espanya { height: 500px; width: 100%; }
#mapa-espanya .info { background: #fff; padding: 6px 10px; border-radius: 4px; font: 13px/1.4 system-ui, sans-serif; box-shadow: 0 1px 4px rgba(0,0,0,.3); }
#mapa-espanya .info button { margin-top: 4px; cursor: pointer; }
#mapa-espanya .espanya { cursor: grab; }
#mapa-espanya .logo-ide { background: rgba(255,255,255,.85); border-radius: 50%; padding: 3px; box-shadow: 0 1px 4px rgba(0,0,0,.3); line-height: 0; }
#mapa-espanya .logo-ide img { width: 64px; height: 64px; display: block; }
</style>
<div id="mapa-espanya"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
const SPAIN = [
  [43.79,-7.69],[43.55,-6.60],[43.66,-5.85],[43.47,-4.90],[43.47,-3.80],
  [43.40,-3.00],[43.34,-2.30],[43.38,-1.79],[43.28,-1.45],[43.03,-1.32],
  [42.97,-0.75],[42.79,-0.53],[42.70,-0.05],[42.80,0.65],[42.85,0.70],
  [42.62,1.40],[42.48,1.45],[42.45,1.95],[42.35,2.45],[42.45,3.17],
  [42.32,3.32],[41.90,3.20],[41.65,2.80],[41.38,2.18],[41.10,1.25],
  [40.72,0.85],[40.36,0.40],[39.47,-0.32],[38.73,0.23],[38.34,-0.48],
  [37.63,-0.69],[37.55,-1.30],[36.83,-2.45],[36.72,-2.19],[36.74,-3.52],
  [36.72,-4.42],[36.50,-5.00],[36.11,-5.35],[36.00,-5.60],[36.53,-6.29],
  [36.95,-6.43],[37.21,-7.40],[37.55,-7.43],[38.02,-7.30],[38.45,-7.25],
  [38.88,-6.98],[39.20,-7.05],[39.66,-7.53],[40.20,-7.00],[40.85,-6.85],
  [41.15,-6.80],[41.50,-6.30],[41.80,-6.55],[41.95,-7.00],[42.05,-8.00],
  [41.88,-8.87],[42.25,-8.85],[42.88,-9.27],[43.25,-9.00],[43.37,-8.40],
  [43.50,-8.25]
];
const R = 6371008.8, RAD = Math.PI / 180, DEG = 180 / Math.PI;
const ORIGIN = L.latLng(40.2, -3.7);
function bearingDist(a, b) {
  const p1 = a.lat * RAD, p2 = b.lat * RAD, dl = (b.lng - a.lng) * RAD;
  const y = Math.sin(dl) * Math.cos(p2);
  const x = Math.cos(p1) * Math.sin(p2) - Math.sin(p1) * Math.cos(p2) * Math.cos(dl);
  const h = Math.sin((p2 - p1) / 2) * Math.sin((p2 - p1) / 2) + Math.cos(p1) * Math.cos(p2) * Math.sin(dl / 2) * Math.sin(dl / 2);
  return { brng: Math.atan2(y, x), d: 2 * R * Math.asin(Math.sqrt(h)) };
}
function destination(a, brng, d) {
  const dd = d / R, p1 = a.lat * RAD, l1 = a.lng * RAD;
  const p2 = Math.asin(Math.sin(p1) * Math.cos(dd) + Math.cos(p1) * Math.sin(dd) * Math.cos(brng));
  const l2 = l1 + Math.atan2(Math.sin(brng) * Math.sin(dd) * Math.cos(p1), Math.cos(dd) - Math.sin(p1) * Math.sin(p2));
  return L.latLng(p2 * DEG, ((l2 * DEG + 540) % 360) - 180);
}
const rel = SPAIN.map(function (p) { return bearingDist(ORIGIN, L.latLng(p[0], p[1])); });
const shape = function (c) { return rel.map(function (r) { return destination(c, r.brng, r.d); }); };
const map = L.map('mapa-espanya', { zoomControl: false }).setView([45, -3.7], 4);
// Logo IDE Menorca (cantonada superior esquerra, abans del control de zoom)
const logo = L.control({ position: 'topleft' });
logo.onAdd = function () {
  const div = L.DomUtil.create('div', 'logo-ide');
  div.innerHTML = '<img src="../img/logo-ide.png" alt="IDE Menorca" title="IDE Menorca">';
  L.DomEvent.disableClickPropagation(div);
  return div;
};
logo.addTo(map);
L.control.zoom({ position: 'topleft' }).addTo(map);
// Mapa base: OpenStreetMap (cal que el navegador enviï el Referer: referrerPolicy 'origin')
const osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  referrerPolicy: 'origin',
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
// Només s'usa si OSM bloqueja la pàgina (dades també d'OpenStreetMap)
const cartoFallback = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
  subdomains: 'abcd', maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
});
let osmBlocked = false;
function comprovaOSM() {
  fetch('https://tile.openstreetmap.org/0/0/0.png', { referrerPolicy: 'origin' })
    .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); })
    .catch(function (err) {
      console.warn('OpenStreetMap bloqueja o no respon:', err);
      osmBlocked = true;
      map.removeLayer(osm);
      cartoFallback.addTo(map);
      cartoFallback.bringToBack();
      info.update();
    });
}
L.polygon(shape(ORIGIN), { color: '#555', weight: 1, dashArray: '4 4', fill: false, interactive: false }).addTo(map);
let center = ORIGIN, grab = null;
const poly = L.polygon(shape(center), { color: '#c0392b', weight: 2, fillColor: '#e74c3c', fillOpacity: 0.45, className: 'espanya' }).addTo(map);
const handle = L.marker(center, { draggable: true, title: 'Arrossega per moure' }).addTo(map);
const info = L.control({ position: 'topright' });
info.onAdd = function () {
  this._div = L.DomUtil.create('div', 'info');
  L.DomEvent.disableClickPropagation(this._div);
  this.update();
  return this._div;
};
info.update = function () {
  const k = 1 / Math.cos(center.lat * RAD);
  this._div.innerHTML = '<b>Arrossega Espanya pel mapa</b><br>Latitud del centre: ' + center.lat.toFixed(1) + '°<br>Escala lineal aparent: ×' + k.toFixed(2) + '<br>Àrea aparent: ×' + (k * k).toFixed(2) + (osmBlocked ? '<br><small>OSM bloqueja aquesta pàgina (falta el Referer): es fa servir CARTO.</small>' : '') + '<br><button id="reset-espanya">Tornar a l\'origen</button>';
  const b = this._div.querySelector('#reset-espanya');
  if (b) b.onclick = function () { move(ORIGIN); handle.setLatLng(center); };
};
info.addTo(map);
function move(c) {
  center = L.latLng(Math.max(-75, Math.min(80, c.lat)), c.lng);
  poly.setLatLngs(shape(center));
  info.update();
}
poly.on('mousedown', function (e) {
  grab = { dlat: center.lat - e.latlng.lat, dlng: center.lng - e.latlng.lng };
  map.dragging.disable();
  L.DomEvent.preventDefault(e.originalEvent);
});
map.on('mousemove', function (e) {
  if (!grab) return;
  move(L.latLng(e.latlng.lat + grab.dlat, e.latlng.lng + grab.dlng));
  handle.setLatLng(center);
});
document.addEventListener('mouseup', function () {
  if (grab) { grab = null; map.dragging.enable(); }
});
handle.on('drag', function (e) { move(e.target.getLatLng()); });
comprovaOSM();
})();
</script>
</div>

Això passa perquè la projecció **Web Mercator** és una projecció **conforme**: és
a dir, està dissenyada per conservar els angles i les formes locals, però a canvi
sacrifica la mida —l'àrea— a mesura que ens allunyem de l'equador. Més endavant
ho expliquem, ara no t'hi capfiquis.

??? info "Vols saber-ne més: com es produeix aquest efecte"
    És un efecte matemàtic i geomètric, i surt de tres coses:

    1. **L'estirament dels meridians.** A la Terra real, les línies de longitud
       s'ajunten a mesura que s'acosten als pols, fins que es toquen en un sol
       punt. En un mapa pla de Mercator, en canvi, es dibuixen com a línies
       rectes completament paral·leles. Això obliga a «estirar» horitzontalment
       els territoris propers als pols perquè ocupin tota l'amplada del mapa.

    2. **Compensació vertical per mantenir la forma.** Si només s'estirés el mapa
       horitzontalment, un cercle prop dels pols quedaria aixafat com un oval. Per
       evitar-ho i mantenir la propietat de ser conforme —que un cercle continuï
       sent un cercle i que els angles de navegació siguin exactes—, la projecció
       aplica exactament el mateix factor d'estirament en sentit vertical, i va
       separant cada vegada més els paral·lels de latitud.

    3. **El resultat.** Com que un cercle real s'estira tant d'ample com d'alt en
       la mateixa proporció —a raó d'1 / cos(latitud)—, conserva la forma rodona,
       però l'àrea es multiplica exponencialment:

        - A **0°**, a l'equador, el factor d'escala és 1: la mida real.
        - A **60°** de latitud, com Escandinàvia o el Canadà, l'escala es duplica,
          el doble d'ample i el doble d'alt, i el cercle ocupa **4 vegades més
          àrea** al mapa.
        - A **80°**, com Groenlàndia o l'Antàrtida, l'escala es multiplica gairebé
          per 6: el cercle sembla **més de 30 vegades més gran** del que és.
        - Als **90°**, als pols, la distorsió tendeix a l'infinit. Per això Web
          Mercator talla el mapa cap als 85° de latitud.

        <figure markdown>
          ![Mapamundi amb cercles vermells de la mateixa mida real col·locats a latituds diferents: minúsculs a l'equador i enormes prop dels pols](img/05-distorsio-web-mercator.jpg){ .captura }
          <figcaption>Tots aquests cercles tenen la mateixa mida real.</figcaption>
        </figure>

    Aquesta és la raó per la qual a les aplicacions de mapes web Groenlàndia
    sembla tan grossa com tota l'Àfrica, quan en realitat l'Àfrica és unes 14
    vegades més gran.
