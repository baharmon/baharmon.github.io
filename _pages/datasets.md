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

[Computational Design Dataset](https://zenodo.org/records/8254075)

---

## <i class="ms ms-cloud"></i> Point Clouds

[XYZ Server](https://xyz.cct.lsu.edu/) for point cloud visualization

[Atlas of Heritage Trees](https://zenodo.org/records/8353293)

[Cloud Forest](https://zenodo.org/records/8210022)

---

## <i class="ms ms-grass-gis"></i> GRASS GIS Datasets

[Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/5248419/)

[The Hills of Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/5248688/)

[Hilltop Arboretum Landform Dataset for GRASS GIS](http://doi.org/10.5281/zenodo.3749397)

[Landscape Evolution Dataset](https://github.com/baharmon/landscape_evolution_dataset)

[Greater Panama Canal Zone Watershed Dataset](https://osf.io/d5h7s/)

[Global Dataset](https://doi.org/10.5281/zenodo.3359632)

[Natural Earth Dataset](https://doi.org/10.5281/zenodo.3968936)

[Sichuan Dataset](https://doi.org/10.5281/zenodo.3359645)

[Louisiana Dataset](https://doi.org/10.5281/zenodo.3359620)

[New Orleans Dataset](https://doi.org/10.5281/zenodo.3359642)

---

## <i class="ms ms-qgis"></i> QGIS Datasets

[Governor's Island Dataset for QGIS](https://zenodo.org/record/5248629)

[The Hills of Governor's Island Dataset for QGIS](https://zenodo.org/record/5249091)

---

## <i class="ms ms-shp"></i> ArcGIS Datasets

[Governor's Island Dataset for ArcGIS](https://zenodo.org/record/5249356)

[The Hills of Governor's Island Dataset for ArcGIS](https://zenodo.org/record/5249790)

[Louisiana Geodatabase](https://doi.org/10.5281/zenodo.3484055)

[New Orleans Geodatabase](https://doi.org/10.5281/zenodo.3484059)


<!--
## <i class="ms ms-drone-quad-nano"></i> Drone Data
-->