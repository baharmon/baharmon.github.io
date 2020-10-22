---
title: Leaflet
subtitle:
description:
featured_image: /images/
---

# Leaflet
Webmapping with Leaflet

---

## Leaflet Map of London

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

<style>
#toner-map { height: 500px; }
</style>

<div id="toner-map"></div>

<script>

// create map
var mymap = L.map('toner-map').setView([30.411804, -91.180910], 12);
L.tileLayer.provider('Stamen.Toner').addTo(mymap);

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

## Leaflet Map as iframe

<iframe width="560" height="315" src="https://baharmon.github.io/maps" frameborder="0" allowfullscreen></iframe>

---
