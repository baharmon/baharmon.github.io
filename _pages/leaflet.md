---
title: Leaflet
subtitle:
description:
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/
useleaflet: true
---

## Leaflet Map of London

&nbsp;
<style>
#map { height: 500px; }
</style>

<div id="map"></div>

<script>
var mymap = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
maxZoom: 18,
id: 'mapbox/streets-v11',
tileSize: 512,
zoomOffset: -1,
accessToken: 'pk.eyJ1IjoiYmFoYXJtb24iLCJhIjoiY2tnYnF1eW14MGpqejJ0cXFjbnI2c3k1biJ9.fFlwJv9wUEpKPAtSopLIyw'
}).addTo(mymap);
</script>

---

## Stamen Toner

&nbsp;
<style>
#toner-map { height: 500px; }
</style>

<div id="toner-map"></div>

<script>

// create map
var mymap = L.map('toner-map').setView([30.411804, -91.180910], 12);
L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'png'
}).addTo(mymap);

// create custom markers
var customIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-black.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});
L.marker([30.411804, -91.180910], {icon: customIcon}).addTo(mymap);


// create map markers
const fontAwesomeIcon = L.divIcon({
  html: '<i style="font-size:36px; color:black" class="ms ms-grass-gis"></i>',
  iconSize: [20, 20],
  className: 'myDivIcon'
});

L.marker([30.4, -91.1], {
    icon: fontAwesomeIcon
  }).addTo(mymap)
  .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')

</script>

---

## Project Map with Sidebar

&nbsp;
<style>
#project-map { height: 500px; }
</style>

<div id="project-map"></div>

<div id="sidebar">
</div>

<script
  src="https://code.jquery.com/jquery-3.5.1.min.js"
  integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
  crossorigin="anonymous"></script>

<script>

// create map
var mymap = L.map('project-map').setView([30.411804, -91.180910], 8);
L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'png'
}).addTo(mymap);

// create custom markers
var customIcon = new L.Icon({
  iconUrl: '/images/baharmon-round.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [100, 100],
  iconAnchor: [25, 100],
  popupAnchor: [1, -34],
  shadowSize: [100, 100]
});
var myLocation = L.marker([30.411804, -91.180910], {icon: customIcon}).addTo(mymap);

// create custom markers
var markerIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-black.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

// load GeoJSON from an external file
$.getJSON("data/projects.geojson",function(data){

  // add popups
  function onEachFeature(feature, layer) {
      layer.bindPopup("<b> Project: </b>" + feature.properties.project + "<br>" + "<b>Location: </b>" + feature.properties.location + "<br>" + "<b>Link: </b>" + "<a href=" + feature.properties.page + ">"+ feature.properties.page +"</a>");

      sidebar.setContent("<b> Project: </b>" + feature.properties.project + "<br>" + "<b>Location: </b>" + feature.properties.location + "<br>" + "<b>Link: </b>" + "<a href=" + feature.properties.page + ">"+ feature.properties.page +"</a>");

  }   

  // add GeoJSON layer to the map once the file is loaded
  L.geoJSON(data, {
    pointToLayer: function (feature, latlng) {
			return L.marker(latlng, {icon: markerIcon});
		},
    onEachFeature: onEachFeature
  }).addTo(mymap).on('click', function () {
              sidebar.toggle();
          });
});

// sidebar
var sidebar = L.control.sidebar('sidebar', {
    position: 'left'
});
mymap.addControl(sidebar);

</script>
