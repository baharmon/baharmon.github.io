---
title: Hydrology in GRASS GIS
subtitle: A tutorial on hydrological modeling in GRASS GIS.
description: A tutorial on hydrological modeling in GRASS GIS.
featured_image: /images/governors-island/discharge-with-landcover.png
usemathjax: true
---

![Shallow water flow discharge](/images/governors-island/discharge-with-landcover.png)

**Contents**
* TOC
{:toc}

---

# Hydrological Modeling

This tutorial will introduce hydrological modeling
in <i class="ms ms-grass-gis"></i> GRASS GIS
using [r.watershed](https://grass.osgeo.org/grass78/manuals/r.watershed.html),
[r.sim.water](https://grass.osgeo.org/grass78/manuals/r.sim.water.html),
and [r.lake](https://grass.osgeo.org/grass78/manuals/r.lake.html).
Learn more about hydrology in GRASS on the
[grasswiki page](https://grasswiki.osgeo.org/wiki/Hydrological_Sciences).
<i class="ms ms-grass-gis"></i> GRASS GIS
includes many modules and addons
for hydrological modeling and analysis including:
* [r.watershed](https://grass.osgeo.org/grass78/manuals/r.watershed.html)
* [r.lake](https://grass.osgeo.org/grass78/manuals/r.lake.html)
* [r.lake.series](https://grass.osgeo.org/grass78/manuals/addons/r.lake.series.html)
* [r.sim.water](https://grass.osgeo.org/grass78/manuals/r.sim.water.html)
* [r.stream.extract](https://grass.osgeo.org/grass78/manuals/r.stream.extract.html)
* [r.stream.distance](https://grass.osgeo.org/grass78/manuals/addons/r.stream.distance.html)
* [r.stream.order](https://grass.osgeo.org/grass78/manuals/addons/r.stream.order.html)
* [r.filldir](https://grass.osgeo.org/grass78/manuals/r.fill.dir.html)
* [r.hydrodem](https://grass.osgeo.org/grass78/manuals/addons/r.hydrodem.html)
* [r.terraflow](https://grass.osgeo.org/grass78/manuals/r.terraflow.html)

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


smoothing
relief
skyview


```
g.region n=189850 s=189100 e=978550 w=976850 save=landforms
r.mask vector=shoreline
r.neighbors -c input=elevation_2017 output=elevation size=5
r.colors -e map=elevation color=elevation
r.relief input=elevation output=relief zscale=2 units=survey
r.shade shade=relief color=elevation output=shaded_relief brighten=40
g.extension extension=r.skyview
r.skyview input=elevation output=skyview ndir=16
r.shade shade=skyview color=shaded_relief output=composite_relief brighten=80
d.legend raster=elevation at=60,95,2,3.5 font=Lato-Regular fontsize=14
```

| Skyview Factor |
|:---:|
| ![Elevation](/images/governors-island/landforms-skyview.png) |

| Digital Elevation Model |
|:---:|
| ![Elevation](/images/governors-island/composite-relief.png) |

---

## Flow Accumulation
Compute flow accumulation with the module
[r.watershed](https://grass.osgeo.org/grass78/manuals/r.param.scale.html).

```
r.watershed -a -b --overwrite elevation=elevation accumulation=flow_accumulation
r.shade shade=relief color=flow_accumulation output=shaded_accumulation brighten=40
d.legend -l raster=flow_accumulation at=60,95,2,3.5 font=Lato-Regular fontsize=14
```

| Flow Accumulation |
|:---:|
| ![Flow Accumulation](/images/governors-island/shaded-flow-accumulation.png) |

Optionally layer the flow accumulation map
on top of the shaded or composite relief map.  
For the flow accumulation map use the values parameter
to set the range of values to display.
```
d.rast map=composite_relief
d.rast map=flow_accumulation values=100-1000000
```

---

## Shallow Water Flow

```
r.slope.aspect elevation=elevation dx=dx dy=dy
r.sim.water elevation=elevation dx=dx dy=dy rain_value=150 depth=depth discharge=discharge nwalkers=10000
r.shade shade=relief color=depth_with_landcover output=shaded_depth_with_landcover brighten=50
d.legend raster=depth_with_landcover at=60,95,2,3.5 font=Lato-Regular fontsize=14
```

| Shallow Water Flow Depth $$(m)$$|
|:---:|
| ![Shallow water flow shaded_depth](/images/governors-island/depth.png) |

| Shallow Water Flow Discharge $$(m^3/s)$$|
|:---:|
| ![Shallow water flow discharge](/images/governors-island/discharge.png) |

Optionally layer the depth or discharge map
on top of the shaded or composite relief map.  For
the depth or discharge maps use the values parameter
to set the range of values to display.
```
d.rast map=composite_relief
d.rast map=depth values=0.03-1
```

---

## Shallow Water Flow with Landcover

Create a new imagery group called `imagery_2018`
and a new imagery subgroup with the same name.
Click add, select the `PERMANENT` mapset,
and use the pattern `imagery_2018.*`
to add all the channels for the 2018 orthophotograph
to the imagery group.

```
i.cluster group=imagery_2018 subgroup=imagery_2018 signaturefile=signature classes=3
i.maxlik group=imagery_2018 subgroup=imagery_2018 signaturefile=signature output=classification
r.recode input=classification output=mannings rules=mannings.txt
```
For [r.recode](https://grass.osgeo.org/grass78/manuals/r.recode.html)
create a rules text file with the following lines
to recode class values to mannings values.
```
1:1:0.368:0.368
2:2:0.0404:0.0404
3:3:0.0113:0.0113
```
Then simulate shallow water flow
with spatially variable surface roughness
using the module
[r.sim.water](https://grass.osgeo.org/grass78/manuals/r.sim.water.html).
Set the `man` parameter to your mannings maps.
```
r.sim.water elevation=elevation dx=dx dy=dy rain_value=50 man=mannings depth=depth_with_landcover discharge=discharge_with_landcover
r.shade shade=relief color=depth output=shaded_depth brighten=40
d.legend raster=depth at=60,95,2,3.5 font=Lato-Regular fontsize=14


```

| Mannings Surface Roughness |
|:---:|
| ![Mannings](/images/governors-island/mannings.png) |

| Shallow Water Flow Depth $$(m)$$ with Landcover|
|:---:|
| ![Shallow water flow shaded_depth](/images/governors-island/depth-with-landcover.png) |

| Shallow Water Flow Discharge $$(m^3/s)$$ with Landcover|
|:---:|
| ![Shallow water flow discharge](/images/governors-island/discharge-with-landcover.png) |


---

## Shallow Water Flow Animation

```
r.sim.water -t --overwrite elevation=elevation dx=dx dy=dy depth=depth discharge=discharge nwalkers=10000 niterations=30 output_step=1
g.list type=raster pattern=discharge.* separator=comma
g.gui.animation raster=discharge.01,discharge.02,discharge.03,discharge.04,discharge.05,discharge.06,discharge.07,discharge.08,discharge.09,discharge.10,discharge.11,discharge.12,discharge.13,discharge.14,discharge.15,discharge.16,discharge.17,discharge.18,discharge.19,discharge.20,discharge.21,discharge.22,discharge.23,discharge.24,discharge.25,discharge.26,discharge.27,discharge.28,discharge.29,discharge.30
```

| Animated Shallow Water Flow Discharge |
|:---:|
| ![Shallow water flow discharge](/images/governors-island/discharge.gif) |

Optionally edit the animation to add the relief raster
below the series of discharge maps.
Set the opacity of the discharge maps to 80%.

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
