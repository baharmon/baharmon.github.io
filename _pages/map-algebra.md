---
title: Terrain Analysis
subtitle: A tutorial on terrain analysis in GIS.
description: A tutorial on terrain analysis in GIS.
featured_image: /images/
---

| 2018 imagery of Governor's Island, NYC |
|:---:|
| ![2018 imagery of Governor's Island, NYC](/images/governors_island/imagery_2018.png) |

## Map Algebra in GRASS GIS

1. [Dataset](#dataset)
1. [Start GRASS GIS](#start-grass-gis)
1. [Computational Region](#computational-region)
1. [](#)
1. [](#)
1. [](#)
1. [](#)
1. [](#)
1. [Exercises](#exercises)

#### Dataset
Download and extract the [Governor's Island Dataset for GRASS GIS]().
This geospatial dataset contains
raster and vector data for
Governor's Island, New York City, USA.
Move the location `nyspf_govenors_island` inside of your
[GRASS GIS database](https://grass.osgeo.org/grass78/manuals/grass_database.html)
directory named `grassdata`.

#### Start GRASS GIS
Start GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
select `nyspf_governors_island` as your location,
and create a new mapset called `map_algebra`.

#### Computational Region
Set your computational region
to the raster map `elevation_2017` at 1 foot resolution with the module
[g.region](https://grass.osgeo.org/grass78/manuals/g.region.html).
Then set a mask to the vector map `shoreline` with the module
[r.mask](https://grass.osgeo.org/grass78/manuals/r.mask.html).
Set your working directory to `nyspf_govenors_island`.
```
g.region raster=elevation_2017
r.mask vector=shoreline
```

#### Map Algebra
*Under Construction*

#### TODO
* Extract canopy height from landcover and difference between DEM and DSM
* Calculate biomass with r.volume and map algebra
* Calculate above ground carbon storage

#### Exercises
For practice...
