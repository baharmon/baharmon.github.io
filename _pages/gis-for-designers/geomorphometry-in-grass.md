---
title: Geomorphometry in GRASS GIS
subtitle: A tutorial on quantitative terrain analysis in GRASS GIS.
description: A tutorial on quantitative terrain analysis in GRASS GIS.
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/geomorphons.png
---

![Geomorphons](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/shaded-geomorphons.png)

**Contents**
* TOC
{:toc}

---

## Geomorphometry

Geomorphometry is the quantitative analysis of topography.
Geomorphometric analyses include slope, aspect, curvature,
topographic indices, and landforms.
<i class="ms ms-grass-gis"></i> GRASS GIS
includes many modules and addons for geomorphometric analysis including:

* [r.param.scale](https://grass.osgeo.org/grass-stable/manuals/r.param.scale.html)
* [r.slope.aspect](https://grass.osgeo.org/grass-stable/manuals/r.slope.aspect.html)
* [r.geomorphon](https://grass.osgeo.org/grass-stable/manuals/r.geomorphon.html)
* [r.topidx](https://grass.osgeo.org/grass-stable/manuals/r.topidx.html)
* [r.convergence](https://grass.osgeo.org/grass-stable/manuals/addons/r.convergence.html)
* [r.terrain.texture](https://grass.osgeo.org/grass-stable/manuals/addons/r.terrain.texture.html)
* [r.vector.ruggedness](https://grass.osgeo.org/grass-stable/manuals/addons/r.vector.ruggedness.html)
* [r.northerness.easterness](https://grass.osgeo.org/grass74/manuals/addons/r.northerness.easterness.html)

In this tutorial we will use the modules
[r.param.scale](https://grass.osgeo.org/grass-stable/manuals/r.param.scale.html)
and
[r.geomorphon](https://grass.osgeo.org/grass-stable/manuals/r.geomorphon.html)
to automatically classify the landforms on Governor's Island.
We will also use the addon module
[r.convergence](https://grass.osgeo.org/grass-stable/manuals/addons/r.convergence.html)
to compute the topographic convergence index and classify landforms.
This tutorial uses the
[Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
Download, extract, and move this geospatial dataset
for Governor's Island in New York City
to your `grassdata` directory.

Start <i class="ms ms-grass-gis"></i> GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
select `nyspf_governors_island` as your location,
and create a new mapset called `geomorphometry`.
Zoom in on the landforms in the southwest of the island.
Either set the computation from the display
using the various zoom options dropdown or
run [g.region](https://grass.osgeo.org/grass-stable/manuals/g.region.html)
and set the boundaries for the region. Save the region.
Then set a mask to the vector map `shoreline` with the module
[r.mask](https://grass.osgeo.org/grass-stable/manuals/r.mask.html).
```
g.region n=189850 s=189100 e=978550 w=976850 save=landforms
r.mask vector=shoreline
```

| Digital Elevation Model |
|:---:|
| ![Elevation](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/southwestern-elevation.png) |

---

## Topographic Parameters
The module
[r.param.scale](https://grass.osgeo.org/grass-stable/manuals/r.param.scale.html)
calculates the morphometric parameters of topography
using differential calculus.
Terrain is parameterized based on
the first and second order partial derivatives
of the quadratic surfaces fit to a moving window using least squares.
The scale of the morphometric parameterization
depends on the size of the moving window.
Parameters include slope, aspect, curvature, and morphometric features.
Morphometric features, i.e. landforms, are defined
by the relationship of a cell to its neighbors
in terms of convexity and concavity,
the second derivatives of the topographic surface.
[r.param.scale](https://grass.osgeo.org/grass-stable/manuals/r.param.scale.html)
can identify six general landforms -
peaks, ridges, passes, planes, channels, and pits.
Use the module
[r.param.scale](https://grass.osgeo.org/grass-stable/manuals/r.param.scale.html)
to automatically classify landforms.
Set the moving window size to an odd number.
```
r.param.scale input=elevation_2017 output=landforms size=33 method=feature --overwrite
```

| Landforms |
|:---:|
| ![Landforms](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/landforms.png) |

Try running
[r.param.scale](https://grass.osgeo.org/grass-stable/manuals/r.param.scale.html)
with different moving window sizes.
Either change the name of the output map or set the `--overwrite` flag.
Add a [legend](https://grass.osgeo.org/grass-stable/manuals/d.legend.html).
Note how this module characterizes most of the landforms here
as either ridges or channels.

---

## Geomorphons

The module
[r.geomorphon](https://grass.osgeo.org/grass-stable/manuals/r.geomorphon.html)
automatically recognizes and classifies landforms using machine vision.
Landforms are classified as either
flats, peaks, ridges, shoulders, spurs, slopes, hollows,
footslope, valleys, or pits
based on their visibility from 8 cardinal and ordinal directions.
Geomorphons has been used for diverse application such as
characterizing [submarine dunes on the ocean floor](https://doi.org/10.3390/geosciences8010028)
and creating [global landform maps](https://doi.org/10.1038/s41597-020-0479-6).

| Landforms |
|:---:|
| ![Landforms](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/geomorphons-legend.png) |

Classify landforms using
[r.geomorphon](https://grass.osgeo.org/grass-stable/manuals/r.geomorphon.html).
Experiment with the `search`, `skip`, and `flat` parameters.
The search radius determines the scale of the landform features,
the flatness threshold set the angle at which ground is considered flat,
and the skip radius eliminates small landforms, reducing noise.
To better visualize the landforms
compute shaded relief from the digital elevation model using
[r.relief](https://grass.osgeo.org/grass-stable/manuals/r.relief.html).
Set the units to US survey feet
and optionally the vertical scale to 2 or higher.
Then drape a map of landforms over the shaded relief using
[r.shade](https://grass.osgeo.org/grass-stable/manuals/r.relief.html).
```
g.region region=landforms
r.geomorphon elevation=elevation_2017 forms=geomorphons search=36 skip=6 flat=12 --overwrite
r.relief input=elevation_2017 output=relief_2017 zscale=2 units=survey
r.shade shade=relief_2017 color=geomorphons output=shaded_geomorphons brighten=45
```

| Geomorphons with Shaded Relief |
|:---:|
| ![Geomorphons](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/shaded-geomorphons.png) |

Note how
[r.geomorphon](https://grass.osgeo.org/grass-stable/manuals/r.geomorphon.html)
has clearly identified the ridge lines and their peaks and
has classified the pathways as either valleys or footslopes.

---

## Landform Extraction

Use map algebra to extract the ridges from either map of landforms.
In the raster map calculator, use an `if, then, else` statement.
If cells in the geomorphons raster equal 3,
then write a value of 1 in the new raster,
else write null values.
```
r.mapcalc expression="ridges = if(geomorphons==3,1,null())"
```

Set a color for the maps of ridges.
Right click on ridges layer in the layer manager
and choose set color interactively.
Assign a category value with
[r.category](https://grass.osgeo.org/grass-stable/manuals/r.category.html).
In the `Define` tab enter category value directly as
`1|ridge`

```
r.category map=ridges separator=pipe
```

| Ridges |
|:---:|
| ![Ridges](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/ridges.png) |

To make a simpler, cleaner vector map of the ridges,
first convert the raster map to a vector using the module
[r.to.vect](https://grass.osgeo.org/grass-stable/manuals/r.to.vect.html).
Then remove small areas from the vector map with the module
[v.clean](https://grass.osgeo.org/grass-stable/manuals/v.clean.html).
All areas smaller than the threshold parameter will be removed.
Then simplify the boundaries of the areas using
[v.generalize](https://grass.osgeo.org/grass-stable/manuals/v.generalize.html)
with the `reumann` method.
Smooth the  boundaries of the areas using
[v.generalize](https://grass.osgeo.org/grass-stable/manuals/v.generalize.html)
with the `snakes` or `hermite` method.
Remove the intermediate cleaned and simplified maps with
[g.remove](https://grass.osgeo.org/grass-stable/manuals/g.remove.html).
Add a vector legend for the ridges with
[d.legend.vect](https://grass.osgeo.org/grass-stable/manuals/d.legend.vect.html).
```
r.to.vect -s input=ridges output=ridges type=area
v.clean input=ridges output=ridges_cleaned type=point,line,area tool=rmarea thres=2
v.generalize input=ridges_cleaned type=area output=ridges_generalized method=reumann threshold=2
v.generalize input=ridges_generalized type=area output=ridges method=snakes threshold=2 alpha=1 beta=1 --overwrite
g.remove -f type=vector name=ridges_cleaned,ridges_generalized
d.legend.vect at=2,95 font=Lato-Regular fontsize=14
```

| Vector Ridges |
|:---:|
| ![Vector Ridges](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/vector-ridges.png) |

---

## Topographic Convergence
Valleys and ridges can be identified from
the convergence and divergence of the topography.
Use [g.extension](https://grass.osgeo.org/grass-stable/manuals/g.extension.html)
to install the addon module
[r.convergence](https://grass.osgeo.org/grass-stable/manuals/addons/r.convergence.html).
Compute the convergence index of the terrain with
[r.convergence](https://grass.osgeo.org/grass-stable/manuals/addons/r.convergence.html)
with a moving window size of 15 cells.
In the resulting raster
values from 1 to 100 are convergent, 0 is planar,
and values from -1 to -100 are divergent.
```
g.extension extension=r.convergence
r.convergence -c input=elevation_2017 output=convergence window=15 weights=standard
```

| Topographic Convergence |
|:---:|
| ![Topographic Convergence](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/convergence.png) |


Use map algebra to extract ridges from areas of topographic divergence.
In the raster map calculator, use an `if, then, else` statement.
If cells in the convergence raster are less than or equal to a threshold,
then write a value of 1 in the new raster,
else write null values.
The threshold for ridges should be a negative value between -1 and -100.
Experiment to find the right threshold.
This example uses a threshold of -15.
Then convert the raster map to a vector using the module
[r.to.vect](https://grass.osgeo.org/grass-stable/manuals/r.to.vect.html),
remove small areas from the vector map with the module
[v.clean](https://grass.osgeo.org/grass-stable/manuals/v.clean.html),
simplify the boundaries of the areas using
[v.generalize](https://grass.osgeo.org/grass-stable/manuals/v.generalize.html),
and then smooth the  boundaries of the areas using
[v.generalize](https://grass.osgeo.org/grass-stable/manuals/v.generalize.html).
Remove the intermediate maps with
[g.remove](https://grass.osgeo.org/grass-stable/manuals/g.remove.html).
Add a vector legend for the ridgelines with
[d.legend.vect](https://grass.osgeo.org/grass-stable/manuals/d.legend.vect.html).

```
r.mapcalc expression="ridgelines = if(convergence <= -15, 1, null())"
r.to.vect -s input=ridgelines output=ridgelines type=area
v.clean input=ridgelines output=ridges_cleaned type=point,line,area tool=rmarea thres=75
v.generalize input=ridges_cleaned type=area output=ridges_generalized method=reumann threshold=2
v.generalize input=ridges_generalized type=area output=ridgelines method=snakes threshold=2 alpha=1 beta=1 --overwrite
g.remove -f type=vector name=ridges_cleaned,ridges_generalized
d.legend.vect at=2,95 font=Lato-Regular fontsize=14
```

| Ridges Derived from Topographic Divergence |
|:---:|
| ![Ridges](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/vector-ridgelines.png) |
