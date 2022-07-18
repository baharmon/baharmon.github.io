---
title: Erosion in GRASS GIS
subtitle: A tutorial on erosion modeling in GRASS GIS.
description: A tutorial on erosion modeling in GRASS GIS.
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/discharge-with-landcover.png
usemathjax: true
---

![Shallow water flow discharge](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/discharge-with-landcover.png)

**Contents**
* TOC
{:toc}

---

## Erosion Modeling

This tutorial is an introduction to modeling erosion
with RUSLE3D, USPED, and SIMWE
in <i class="ms ms-grass-gis"></i> GRASS GIS.

This tutorial uses the <i class="ms ms-database"></i>
[Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
Download, extract, and move this geospatial dataset
for Governor's Island in New York City
to your `grassdata` directory.
Start <i class="ms ms-grass-gis"></i> GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
select `nyspf_governors_island` as your location,
and create a new mapset named `erosion`.

Start by setting the region, setting a mask,
and smoothing the terrain.
Zoom in on the landforms in the southwest of the island
and set the computational region.
Then set a mask to the vector map `shoreline` with the module
[r.mask](https://grass.osgeo.org/grass-stable/manuals/r.mask.html).
Smooth the digital elevation model using the module
[r.neighbors](https://grass.osgeo.org/grass-stable/manuals/r.neighbors.html)
to reduce noise from the lidar.

```
g.region n=189850 s=189100 e=978550 w=976850
r.mask vector=shoreline
r.neighbors -c input=elevation_2017 output=elevation size=5
r.colors -e map=elevation color=elevation
```
<!--
Erosion from shallow flows of water depends upon
rainfall, topographic parameters, soil parameters, and landcover.
-->

Derive landcover from a vegetation index such as
the Normalized Difference Vegetation Index (NDVI).
First use the module [i.vi](https://grass.osgeo.org/grass-stable/manuals/i.vi.html)
to compute NDVI with the red and near infrared channels
of the 2018 orthophotograph.
Then recode the map of NDVI as landcover.
Recode values below 0 as developed open space,
values between 0 and 0.2 as bare ground,
and values greater than 0.2 as grass.

```
-1:0:21:21
0:0.2:31:31
0.2:1:71:71
```
Set the color table to `nlcd`
to match the USGS National Landcover Dataset.

```
i.vi output=ndvi red=imagery_2018.1 nir=imagery_2018.4
r.recode input=ndvi output=roughness rules=landcover.txt
r.colors map=landcover@erosion color=nlcd
```


<!--
r.category
d.legend
-->

| Imagery 2018 |
|:---:|
| ![Imagery 2018](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/imagery.png) |

| Normalized Difference Vegetation Index |
|:---:|
| ![Normalized Difference Vegetation Index](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/ndvi.png) |

| Landcover from NDVI|
|:---:|
| ![Landcover from NDVI](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/landcover-from-ndvi.png) |

---

## RUSLE3D
3-Dimensional Revised Universal Soil Loss Equation (RUSLE 3D) model

R-factor from Panagos dataset

---

## USPED
the Unit Stream Power Erosion Deposition (USPED) model

---

## SIMWE

The Simulation of Water Erosion (SIMWE) model



[r.sim.water](https://grass.osgeo.org/grass-stable/manuals/r.sim.water.html)
[r.sim.sediment](https://grass.osgeo.org/grass-stable/manuals/r.sim.sediment.html)
