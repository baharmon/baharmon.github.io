---
title: Hydrology in GRASS GIS
subtitle: A tutorial on hydrological modeling in GRASS GIS.
description: A tutorial on hydrological modeling in GRASS GIS.
featured_image: /images/governors-island/
---

![Flow Accumulation](/images/governors-island/shaded-flow-accumulation.png)

**Contents**
* TOC
{:toc}

---

## Hydrological Modeling

<i class="ms ms-grass-gis"></i> GRASS GIS
includes many modules and addons
for hydrological modeling including:
* [r.watershed](https://grass.osgeo.org/grass78/manuals/r.watershed.html)
* [r.lake](https://grass.osgeo.org/grass78/manuals/r.lake.html)
[r.lake.series](https://grass.osgeo.org/grass78/manuals/addons/r.lake.series.html)
* [r.sim.water](https://grass.osgeo.org/grass78/manuals/r.sim.water.html)
* [r.stream.extract](https://grass.osgeo.org/grass78/manuals/r.stream.extract.html)
* [r.stream.distance](https://grass.osgeo.org/grass78/manuals/addons/r.stream.distance.html)
* [r.stream.order](https://grass.osgeo.org/grass78/manuals/addons/r.stream.order.html)
* [r.filldir](https://grass.osgeo.org/grass78/manuals/r.fill.dir.html)
* [r.hydrodem](https://grass.osgeo.org/grass78/manuals/addons/r.hydrodem.html)
* [r.terraflow](https://grass.osgeo.org/grass78/manuals/r.terraflow.html)

[r.stream](https://grasswiki.osgeo.org/wiki/R.stream.*_modules)


This tutorial uses the
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
```
g.region n=189850 s=189100 e=978550 w=976850 save=landforms
r.mask vector=shoreline
```

| Digital Elevation Model |
|:---:|
| ![Elevation](/images/governors-island/southwestern-elevation.png) |

---

## Flow Accumulation

```
r.watershed -a -b elevation=elevation_2017 accumulation=flow_accumulation
r.neighbors -c input=elevation_2017 output=smoothed_elevation size=5
r.watershed -a -b --overwrite elevation=smoothed_elevation accumulation=flow_accumulation
r.relief --overwrite input=smoothed_elevation output=relief zscale=2 units=survey
r.shade --overwrite shade=relief color=flow_accumulation output=shaded_flow_accumulation brighten=40
d.legend -l raster=flow_accumulation at=60,95,2,4 font=Lato-Regular fontsize=14
```

| Flow Accumulation |
|:---:|
| ![Flow Accumulation](/images/governors-island/shaded-flow-accumulation.png) |

---

## Watersheds
The module
[r.watershed](https://grass.osgeo.org/grass78/manuals/r.param.scale.html)

```
r.watershed elevation=smoothed_elevation threshold=40000 basin=subwatersheds
r.to.vect -s input=subwatersheds output=subwatersheds type=area
d.vect map=subwatersheds color=white fill_color=none width=4
d.vect map=subwatersheds fill_color=none width=2
r.watershed elevation=smoothed_elevation threshold=120000 basin=watersheds
r.to.vect -s input=watersheds output=watersheds type=area
d.vect map=watersheds color=white fill_color=none width=6
d.vect map=watersheds fill_color=none width=4
```

| Watersheds |
|:---:|
| ![Watersheds](/images/governors-island/watersheds.png) |


---

## Stream Order

```
r.stream.extract elevation=smoothed_elevation accumulation=flow_accumulation threshold=500 stream_length=5 stream_raster=streams stream_vector=streams direction=flow_direction
r.stream.order stream_rast=streams direction=flow_direction elevation=smoothed_elevation accumulation=flow_accumulation stream_vect=stream_attributes
d.vect map=stream_attributes width_column=strahler size=0
v.colors map=stream_attributes use=attr column=strahler color=water
```


| Stream Order |
|:---:|
| ![Stream Order](/images/governors-island/stream-order.png) |


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
