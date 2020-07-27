---
title: Terrain Analysis in GRASS GIS
subtitle: A tutorial on terrain analysis in GRASS GIS.
description: A tutorial on terrain analysis in GRASS GIS.
featured_image: /images/governors-island/surface.png
---

![Surface map with skyview shading](/images/governors-island/surface.png)

**Contents**
* TOC
{:toc}

---

# Dataset
Download and extract the [Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
This geospatial dataset contains
raster and vector data for
Governor's Island, New York City, USA.
The top level directory `nyspf_governors_island`
is a GRASS GIS location
for NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet
in US Surveyor's Feet.
Inside the location there is the `PERMANENT` mapset,
a license file, data record, readme file, workspace, color table,
category rules, and scripts for data processing.
Data sources include
[http://gis.ny.gov/](http://gis.ny.gov/),
[https://orthos.dhses.ny.gov/](https://orthos.dhses.ny.gov/)
and [https://data.cityofnewyork.us/](https://data.cityofnewyork.us/).

Create a directory on your computer called `grassdata`.
This will be your [GRASS GIS database](https://grass.osgeo.org/grass78/manuals/grass_database.html)
directory where you will store your GRASS locations and mapsets.
Move the location `nyspf_govenors_island` inside of your `grassdata` directory.


| 2018 imagery of Governor's Island, NYC |
|:---:|
| ![2018 imagery of Governor's Island, NYC](/images/governors-island/imagery-2018.png) |

---

# Start GRASS GIS
Start GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
select `nyspf_governors_island` as your location,
and create a new mapset called `terrain_analysis`.
While we will have access to reference data in the `PERMANENT` mapset,
all new data will be created in the new `terrain_analysis` mapset.
See this [guide to starting GRASS GIS](https://grass.osgeo.org/grass78/manuals/helptext.html).

---

# Computational Region
Set your computational region
to the raster map `elevation_2017` at 1 foot resolution with the module
[g.region](https://grass.osgeo.org/grass78/manuals/g.region.html).
Then set a mask to the vector map `shoreline` with the module
[r.mask](https://grass.osgeo.org/grass78/manuals/r.mask.html).
```
g.region raster=elevation_2017 res=1
r.mask vector=shoreline
```

Optionally zoom in and use the various zoom options dialog
in the graphical user interface (GUI) to
`Set computational region from display`.
Then save your custom region as `terrain`
using the various zoom options dialog
`Save computational region as named region`.

---

# Slope
Compute slope in degrees from the 2017 digital elevation model (DEM)
 with the module
[r.slope.aspect](https://grass.osgeo.org/grass78/manuals/r.slope.aspect.html)
and then add a legend.
```
r.slope.aspect -e elevation=elevation_2017 slope=slope_2017 format=degrees
d.legend raster=slope_2017
```

| Slope |
|:---:|
| ![](/images/governors-island/slope.png) |

---

# Categorized Slope
Create a categorized slope map
showing gentle, moderate, and steep slopes.
To reduce noise smooth the digital elevation model using the module
[r.neighbors](https://grass.osgeo.org/grass78/manuals/r.neighbors.html)
with a circular neighborhood with a 9 ft diameter.
Then re-compute the slope using
[r.slope.aspect](https://grass.osgeo.org/grass78/manuals/r.slope.aspect.html)
with the smoothed digital elevation model.
Reclassify the continuous slope data into discrete classes
using the module
[r.reclass](https://grass.osgeo.org/grass78/manuals/r.reclass.html).
```
r.neighbors -c input=elevation_2017 output=smoothed_elevation_2017 size=9
r.slope.aspect -e elevation=smoothed_elevation_2017 slope=smoothed_slope_2017 format=degrees
r.reclass input=smoothed_slope_2017 output=slope_classes_2017
```
with the following values:
```
0 thru 10 = 1
11 thru 20 = 2
21 thru 90 = 3
```
Then set a category for each class using the module
[r.category](https://grass.osgeo.org/grass78/manuals/r.category.html).
```
r.category map=slope_classes_2017 separator=pipe
````
with the following values:
```
1|Gentle
2|Moderate
3|Steep
```
Then set the color table with the module
[r.colors](https://grass.osgeo.org/grass78/manuals/r.colors.html)
and add a legend.
```
r.colors map=slope_classes_2017 color=viridis
d.legend raster=slope_classes_2017
```

| Categorized Slope |
|:---:|
| ![](/images/governors-island/categorized-slope.png) |

---

# Contours
Compute contours at 3 ft intervals
from the smoothed digital elevation model using the module
[r.contour](https://grass.osgeo.org/grass78/manuals/r.contour.html).
To further reduce noise, use the `cut` parameter
to specify the minimum number of points per contour curve.
```
r.contour input=smoothed_elevation_2017 output=contours_3ft step=3 cut=100
```

| Digital elevation model with 3 ft contours |
|:---:|
| ![Digital elevation model with 3 ft contours](/images/governors-island/contours.png) |

---

# Hillshade
Compute hillshading for the 2017 digital elevation model using the module
[r.relief](https://grass.osgeo.org/grass78/manuals/r.relief.html).
Set the `units` parameter to survey feet.
Then overlay the elevation map over the hillshade using the module
[r.shade](https://grass.osgeo.org/grass78/manuals/r.shade.html).
```
r.relief input=elevation_2017 output=relief_2017 zscale=3 units=survey
r.shade shade=relief_2017 color=elevation_2017 output=shaded_relief_2017 brighten=30
```

| Digital Elevation Model with Shaded Relief |
|:---:|
| ![Shaded relief map](/images/governors-island/shaded-relief.png) |

---

# Skyview Factor
Use the skyview factor,
a hillshading technique based on the openness of the terrain,
to better visualize the topography.
First install the addon `r.skyview` with the module
[g.extension](https://grass.osgeo.org/grass78/manuals/g.extension.html),
then compute the skyview factor using the addon module
[r.skyview](https://grass.osgeo.org/grass78/manuals/addons/r.skyview.html),
and then create a composite shaded relief map using the module
[r.shade](https://grass.osgeo.org/grass78/manuals/r.shade.html).
```
r.skyview input=surface_2017 output=skyview_2017 ndir=16
r.colors -e map=skyview_surface_2017 color=grey
r.relief input=surface_2017 output=surface_relief_2017 zscale=3 units=survey
r.shade shade=surface_relief_2017 color=surface_2017 output=shaded_surface_2017 brighten=50
r.shade shade=skyview_2017 color=shaded_surface_2017 output=composite_surface_2017 brighten=80
```

| Skyview Factor |
|:---:|
| ![Skyview factor](/images/governors-island/skyview.png) |

| Digital Surface Model with Skyview Shading |
|:---:|
| ![Surface map with skyview shading](/images/governors-island/composite-surface.png) |

---

# Cartography
To save a rendering of the elevation map with hillshading,
add the raster map `shaded_relief_2017` to the layer manager,
add the raster map `elevation_2017` above it at 36% opacity,
add the vector map `contours_3ft` above that at 50% opacity,
add the vector map `shoreline` above that with fill set to transparent,
and then add a legend, barscale, and north arrow.
Optionally add a cartographic grid with
[v.mkgrid](https://grass.osgeo.org/grass78/manuals/v.mkgrid.html).
```
d.legend raster=elevation_2017
d.northarrow style=fancy_compass
v.mkgrid map=grid box=250,250
```
Use the `Save display to file` button
to render the map as a `.png` file.

Optionally set the position, font, and font size for the legend.
This example uses the free, open source font
[Lato](https://www.latofonts.com/lato-free-fonts/).
Download and install the font before running
[d.legend](https://grass.osgeo.org/grass78/manuals/d.legend.html).
```
d.legend raster=elevation_2017 at=13,43,93.2,95.2 font=Lato-Regular fontsize=14
d.northarrow style=fancy_compass at=91,10.5 width=1 font=Lato-Regular fontsize=12
v.mkgrid map=grid box=250,250
v.clip input=grid clip=shoreline output=interior_grid
d.barscale -f -t style=solid at=82.45,6.25 length=250 segment=1 bgcolor=none font=Lato-Regular fontsize=12
d.text text="250 ft" color=black at=83.6,5 font=Lato-Regular size=1.25
```

| Shaded Relief with Cartographic Grid |
|:---:|
| ![Shaded relief map with cartographic grid](/images/governors-island/shaded-relief-grid.png) |

---

# Exercises
For practice, render
digital surface model, slope, and categorized slope maps with shaded relief.

| Digital Surface Model | Slope | Categorized Slope |
|:---:|:---:|:---:|
| ![Digital surface model with shaded relief](/images/governors-island/surface-contours.png) | ![Slope with shaded relief](/images/governors-island/shaded-slope.png) | ![Categorized slope with shaded relief](/images/governors-island/shaded-categorized-slope.png) |
