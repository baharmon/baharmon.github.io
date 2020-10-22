---
title: Watersheds in GRASS GIS
subtitle: A tutorial on watershed analysis in GRASS GIS.
description: A tutorial on watershed analysis in GRASS GIS.
featured_image: /images/
---

![Watersheds](/images/tunica-hills/elevation-with-streams.png)

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

## Terrain Acquisition

This tutorial uses the
[...](...).
Download, extract, and move this geospatial dataset
for ...
to your `grassdata` directory.

Start <i class="ms ms-grass-gis"></i> GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
select `...` as your location,
and create a new mapset called `hydrology`.
Zoom in on the landforms in the southwest of the island.
Either set the computation from the display using the various zoom options dropdown or run [g.region](https://grass.osgeo.org/grass78/manuals/g.region.html) and set the boundaries for the region. Save the region.

Use
[g.extension](https://grass.osgeo.org/grass78/manuals/g.extension.html)
to install the addon module
[r.in.usgs](https://grass.osgeo.org/grass78/manuals/addons/r.in.usgs.html).


To work with lower resolution data
set the resolution of the region to 30m
with [g.region](https://grass.osgeo.org/grass78/manuals/g.region.html)
and import the national elevation dataset
at 1 arcsecond resolution with
[r.in.usgs](https://grass.osgeo.org/grass78/manuals/addons/r.in.usgs.html).
To work with higher resolution data
set the resolution of the region to 10m
with [g.region](https://grass.osgeo.org/grass78/manuals/g.region.html)
and import the national elevation dataset
at 1/3 arcsecond resolution with
[r.in.usgs](https://grass.osgeo.org/grass78/manuals/addons/r.in.usgs.html).

```
g.region n=3432678.24028746 s=3420115.23940805 e=646814.51098306 w=634251.50105829 res=30 save=tunica_hills
g.extension extension=r.in.usgs
r.in.usgs product=ned output_name=elevation output_directory=usgs ned_dataset=ned1sec resampling_method=bilinear
r.relief input=elevation output=relief zscale=3
r.shade shade=relief color=elevation output=shaded_relief brighten=30
d.legend raster=elevationat=60,95,2,4 font=Lato-Regular fontsize=14
```

| Digital Elevation Model |
|:---:|
| ![Elevation](/images/tunica-hills/elevation.png) |

---

## Watershed Delineation
 ... the module
[r.watershed](https://grass.osgeo.org/grass78/manuals/r.watershed.html)

Basins
```
r.watershed -a -b elevation=elevation threshold=10000 basin=basins
r.to.vect -s input=basins output=basins type=area
v.extract input=basins cats=3 output=basin
d.vect map=basin color=white fill_color=none width=3
```

Watersheds
```
r.mask vector=basin
r.watershed -a -b elevation=elevation threshold=1000 basin=watersheds
r.to.vect -s input=watersheds output=watersheds type=area
d.vect map=watersheds color=white fill_color=none width=1
```

| Watersheds |
|:---:|
| ![Watersheds](/images/tunica-hills/masked-watersheds.png) |


Optionally layer masked and unmasked shaded relief maps
to visualize the topography inside and outside of the basin.
First set the mask to the basin
with [r.mask](https://grass.osgeo.org/grass78/manuals/r.mask.html),
then
with [r.mapcalc](https://grass.osgeo.org/grass78/manuals/r.mapcalc.html)
use map algebra to create a masked version of the shaded relief.
Set the opacity of the original shaded relief map to 50%.
```
r.mask vector=basin
r.mapcalc expression="masked_relief = shaded_relief"
r.mask -r
```

---

## Flow Accumulation

```
r.mask vector=basin
r.watershed -a -b elevation=elevation threshold=10000 accumulation=flow_accumulation
r.shade shade=relief color=flow_accumulation output=shaded_accumulation brighten=80
d.legend -l raster=flow_accumulation at=60,95,2,3.5 font=Lato-Regular fontsize=14
```

| Flow Accumulation |
|:---:|
| ![Flow Accumulation](/images/tunica-hills/flow-accumulation.png) |

---

## Stream Order

```
r.stream.extract elevation=elevation accumulation=flow_accumulation threshold=200 stream_raster=stream_raster stream_vector=stream_vector direction=flow_direction
r.stream.order stream_rast=stream_raster direction=flow_direction elevation=elevation accumulation=flow_accumulation stream_vect=stream_attributes
d.vect map=stream_attributes width_column=strahler size=0
v.colors map=stream_attributes use=attr column=strahler color=water
```


| Stream Order |
|:---:|
| ![Stream Order](/images/tunica-hills/stream-order.png) |


| Shaded Relief with Stream Network |
|:---:|
| ![Shaded relief with streams](/images/tunica-hills/elevation-with-streams.png) |
