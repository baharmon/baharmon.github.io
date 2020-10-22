---
title: About
subtitle:
description:
featured_image: /images/baharmon-round.png
---

<style>
#toner-map { height: 500px; }
</style>

<div id="toner-map"></div>

<script
  src="https://code.jquery.com/jquery-3.5.1.min.js"
  integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
  crossorigin="anonymous"></script>

<script>

// create map
var mymap = L.map('toner-map').setView([30.411804, -91.180910], 8);
L.tileLayer.provider('Stamen.Toner').addTo(mymap);

// create custom markers
var customIcon = new L.Icon({
  iconUrl: '/images/baharmon-round.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [100, 100],
  iconAnchor: [25, 100],
  popupAnchor: [1, -34],
  shadowSize: [100, 100]
});
L.marker([30.411804, -91.180910], {icon: customIcon}).addTo(mymap);

// L.geoJSON(geojsonFeature).addTo(mymap);

// load GeoJSON from an external file
$.getJSON("data/projects.geojson",function(data){
  // add GeoJSON layer to the map once the file is loaded
  L.geoJson(data).addTo(mymap);
});


</script>

## Brendan Harmon

Assistant Professor of Landscape Architecture

[<i class="fa fa-university"></i> Louisiana State University](https://design.lsu.edu/faculty/brendan-harmon/)

[<i class="fa fa-graduation-cap"></i> Curriculum Vitae](https://github.com/baharmon/curriculum-vitae/blob/master/baharmon_cv.pdf)

---

## Research Interests

* Geographic information systems
* Geospatial modeling and simulation
* Generative design
* Digital fabrication
* Robotics

---

## Links

<i class="fab fa-github"></i>
[GitHub](https://github.com/baharmon/)

<i class="ai ai-osf"></i>
[Open Science Framework](https://osf.io/xhvp4/)

<i class="ai ai-orcid"></i>
[OrcID](http://orcid.org/0000-0002-6218-9318)

<i class="ai ai-researchgate"></i>
[ResearchGate](https://www.researchgate.net/profile/Brendan_Harmon2)

<i class="ai ai-academia"></i>
[Academia](http://lsu.academia.edu/BrendanHarmon)

<i class="fas fa-cube"></i>
[Sketchfab](https://sketchfab.com/lsu-landscape-architecture)
