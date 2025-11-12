---
title: Data
subtitle:
description:
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/baharmon-round.png
useleaflet: true
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
L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'png'
}).addTo(mymap);


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
$.getJSON("data/datasets.geojson",function(data){

  // add popups
  function onEachFeature(feature, layer) {
      layer.bindPopup("<b> Dataset: </b>" + feature.properties.dataset + "<br>" + "<b>Location: </b>" + feature.properties.location + "<br>" + "<b>Link: </b>" + "<a href=" + feature.properties.page + ">"+ feature.properties.page +"</a>");
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

## <i class="ms ms-txt"></i> Data Sources

[List of Geospatial Data Sources](geospatial-data-sources)

---

## <i class="ms ms-txt"></i> Book Dataset

[Computational Design Dataset](https://zenodo.org/doi/10.5281/zenodo.8191264)

---

## <i class="ms ms-cloud"></i> Point Clouds

[XYZ Server](https://xyz.cct.lsu.edu/) for point cloud visualization

[Cloud Garden](https://xyz.cct.lsu.edu/cloud-garden/) +
[<i class="ms ms-cloud"></i> Sketchfab](https://skfb.ly/pyp9U) +
[<i class="ai ai-doi"></i> Dataset](https://doi.org/10.5281/zenodo.15670829)

[Cloud Forest](https://zenodo.org/doi/10.5281/zenodo.8194066)

[Atlas of Heritage Trees](https://zenodo.org/doi/10.5281/zenodo.8353292)

---

## <i class="ms ms-grass-gis"></i> GRASS GIS Datasets

[Governor's Island Dataset for GRASS GIS](https://zenodo.org/doi/10.5281/zenodo.3940779)

[The Hills of Governor's Island Dataset for GRASS GIS](https://zenodo.org/doi/10.5281/zenodo.5248687)

[Hilltop Arboretum Landform Dataset for GRASS GIS](https://zenodo.org/doi/10.5281/zenodo.3749396)

[Landscape Evolution Dataset](https://zenodo.org/doi/10.5281/zenodo.2542928)

[Greater Panama Canal Zone Watershed Dataset](https://osf.io/d5h7s/)

[Global Dataset](https://zenodo.org/doi/10.5281/zenodo.3359631)

[Natural Earth Dataset](https://zenodo.org/doi/10.5281/zenodo.3762773)

[Sichuan Dataset](https://zenodo.org/doi/10.5281/zenodo.3359069)

[Louisiana Dataset](https://zenodo.org/doi/10.5281/zenodo.3359619)

[New Orleans Dataset](https://zenodo.org/doi/10.5281/zenodo.3359641)

---

## <i class="ms ms-qgis"></i> QGIS Datasets

[Governor's Island Dataset for QGIS](https://zenodo.org/doi/10.5281/zenodo.4044663)

[The Hills of Governor's Island Dataset for QGIS](https://zenodo.org/doi/10.5281/zenodo.5249090)

---

## <i class="ms ms-shp"></i> ArcGIS Datasets

[Governor's Island Dataset for ArcGIS](https://zenodo.org/doi/10.5281/zenodo.5249355)

[The Hills of Governor's Island Dataset for ArcGIS](https://zenodo.org/doi/10.5281/zenodo.5249789)

[Louisiana Geodatabase](https://zenodo.org/doi/10.5281/zenodo.3484054)

[New Orleans Geodatabase](https://zenodo.org/doi/10.5281/zenodo.3483790)


<!--
## <i class="ms ms-drone-quad-nano"></i> Drone Data
-->