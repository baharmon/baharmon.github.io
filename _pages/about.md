---
title: About
subtitle:
description:
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/baharmon-round.png
useleaflet: true
---

## Brendan Harmon
**Associate Professor of Landscape Architecture**

<!--<i class="fa fa-university"></i>-->
[Louisiana State University](https://design.lsu.edu/faculty/brendan-harmon/)

[<i class="fa fa-graduation-cap"></i> Curriculum Vitae](https://github.com/baharmon/curriculum-vitae/raw/master/baharmon-cv.pdf)

Brendan is a spatial scientist and computational designer. His work explores the entanglement of ecology and technology. Brendan’s current research programs include the design of robotic processes for planting and sensing landscapes, experiments in the use of point cloud modeling as a new creative medium, and documentary projects that use emerging technologies to preserve a record of our disappearing natural and cultural heritage. His past research programs included building resilience to climate change, erosion and landscape evolution modeling, the geochemistry of tropical rivers, drone data analytics for computational ecology, and development of a tangible interface for geospatial modeling. He is committed to open science and open education as global foundations for equitable access to knowledge. Brendan hosts a collection of 3D scanned heritage landscapes at [https://xyz.cct.lsu.edu](https://xyz.cct.lsu.edu). 

<i class="fab fa-youtube"></i>
[Youtube](youtube.com/@baharmon) 
&middot; 
<i class="fab fa-github"></i>
[GitHub](https://github.com/baharmon/) 
&middot; 
<i class="ai ai-orcid"></i>
[OrcID](http://orcid.org/0000-0002-6218-9318) 
&middot; 
<i class="ai ai-researchgate"></i>
[ResearchGate](https://www.researchgate.net/profile/Brendan_Harmon2) 
&middot; 
<i class="ai ai-osf"></i>
[Open Science Framework](https://osf.io/xhvp4/) 

<i class="fas fa-cube"></i>
[Sketchfab](https://sketchfab.com/baharmon) 
&middot; 
<i class="fa fa-cloud"></i>
[XYZ Point Cloud Collection](https://xyz.cct.lsu.edu)

&nbsp;
<style>
#toner-map { height: 500px; }
</style>

<div id="toner-map">
</div>

<script
  src="https://code.jquery.com/jquery-3.5.1.min.js"
  integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
  crossorigin="anonymous">
</script>


<script>

// create map
var mymap = L.map('toner-map').setView([30.411804, -91.180910], 8);
L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'png'
}).addTo(mymap);

// create custom markers
var customIcon = new L.Icon({
  iconUrl: 'https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/baharmon-round.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [100, 100],
  iconAnchor: [25, 100],
  popupAnchor: [1, -34],
  shadowSize: [100, 100]
});
var myLocation = L.marker([30.411804, -91.180910], {icon: customIcon}).addTo(mymap);
myLocation.bindPopup("<b>Brendan Harmon</b> <br> Louisiana State University <br> Baton Rouge, Louisiana, USA");
myLocation.setZIndexOffset(-1000)

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
  }   

  // add GeoJSON layer to the map once the file is loaded
  geojson = L.geoJSON(data, {
    pointToLayer: function (feature, latlng) {
			return L.marker(latlng, {icon: markerIcon});
		},
    onEachFeature: onEachFeature
  }).addTo(mymap)
  mymap.fitBounds(geojson.getBounds());
});

</script>
