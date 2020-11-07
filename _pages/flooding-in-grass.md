---
title: Flooding in GRASS GIS
subtitle: A tutorial on flooding in GRASS GIS.
description: A tutorial on flooding in GRASS GIS.
featured_image: /images/governors-island/
usemathjax: true
---

![Shallow water flow discharge](/images/governors-island/discharge-with-landcover.png)

**Contents**
* TOC
{:toc}


---

## Dataset

This tutorial uses the <i class="ms ms-database"></i>
[Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
Download, extract, and move this geospatial dataset
for Governor's Island in New York City
to your `grassdata` directory.

Start <i class="ms ms-grass-gis"></i> GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
select `nyspf_governors_island` as your location,
and create a new mapset called `hydrology`.
Zoom in on the landforms in the southwest of the island.
Either set the computation from the display using the various zoom options dropdown or run [g.region](https://grass.osgeo.org/grass78/manuals/g.region.html) and set the boundaries for the region. Save the region.
Then set a mask to the vector map `shoreline` with the module
[r.mask](https://grass.osgeo.org/grass78/manuals/r.mask.html).
The digital elevation model from lidar
has substantial noise that would impact hydrological simulations.
To reduce this noise
smooth the digital elevation model using the module
[r.neighbors](https://grass.osgeo.org/grass78/manuals/r.neighbors.html)
with a moving window size of 5.
Optionally make the moving window circular with flag `-c`.

```
g.region n=189850 s=189100 e=978550 w=976850 save=landforms
r.mask vector=shoreline
r.neighbors -c input=elevation_2017 output=elevation size=5
```

---

## Flooding
[r.lake](https://grass.osgeo.org/grass78/manuals/r.lake.html)

```
r.lake elevation=smoothed_elevation water_level=11.5 lake=flooding coordinates=978381.33268,189447.513474
d.legend raster=flooding at=60,95,2,4 font=Lato-Regular fontsize=14
```

| Flooding |
|:---:|
| ![Flooding](/images/governors-island/flooding.png) |

[r.lake.series](https://grass.osgeo.org/grass78/manuals/addons/r.lake.series.html)

```
r.lake.series --overwrite elevation=smoothed_elevation output=flooding start_water_level=9.8 end_water_level=12 water_level_step=.1 coordinates=978378.671875,189465.703125
```

```
g.gui.animation
```

| Flooding Animation |
|:---:|
| ![Flood Animation](/images/governors-island/flooding.gif) |
