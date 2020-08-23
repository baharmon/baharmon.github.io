---
title: Using GRASS in GQIS
subtitle:
description: Using GRASS inside of QGIS.
featured_image: /images/
---

![GRASS in QGIS](/images/governors-island/hillshade-style.jpg)

**Contents**
* TOC
{:toc}

---

# Rationale

Processing in GRASS (scientific GIS, terrain and lidar)

Cartography in QGIS

QGIS' great interface (GUI)

Streamlined workflow

---

# GRASS Plugins

<i class="ms ms-qgis"></i> GRASS

<i class="ms ms-grass-gis"></i> QGIS

[GRASS GIS Integration](https://docs.qgis.org/3.10/en/docs/user_manual/grass_integration/grass_integration.html)

---

# GRASS Datasets

Download and extract the [Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
The top level directory `nyspf_governors_island`
is a GRASS GIS location
for NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet
in US Surveyor's Feet.
Inside the location there is the `PERMANENT` mapset,
a license file, data record, readme file, workspace, color table,
category rules, and scripts for data processing.
Create a directory on your computer called `grassdata`.
This will be your [GRASS GIS database](https://grass.osgeo.org/grass78/manuals/grass_database.html)
directory where you will store your GRASS locations and mapsets.
Move the location `nyspf_govenors_island` inside of your `grassdata` directory.

Browse to your `grassdata` directory in the browser panel
on the left side of the QGIS window.
Optionally right click and select
`add as favorite` to create a shortcut.
Expand your `grassdata` directory and
browse to find the GRASS location.
There will be a both
a directory with a <i class="ms ms-directory"></i> icon
and a GRASS location with a <i class="ms ms-grass-gis"></i> icon
named `nyspf_governors_island`.
Expand the location
<i class="ms ms-grass-gis"></i> `nyspf_governors_island`
and select the <i class="ms ms-grass-gis"></i> `PERMANENT` mapset.

Expand the mapset
and add some data to your layer manager and map.
First try adding the
<i class="ms ms-polygon"></i> `shoreline` vector.
Expand the <i class="ms ms-database"></i> shoreline database
and double click on the
<i class="ms ms-polygon"></i>
shoreline area to add it.
If a datum transformation dialog appears, click cancel.
while the default coordinate reference system
for a new project is WGS 84 (EPSG 4326),
the project CRS will automatically switch
to that of the first layer added.
In this case the CRS will be
NAD83 / New York Long Island (ftUS) (EPSG 2263).

Now add a raster.
Double click on the
<i class="ms ms-raster"></i>
`elevation_2017` to add this digital elevation model.
This raster will not render in the map display
with the default symbology settings.
You will need to specify a color ramp
and load values from the raster.
A color ramp for a digital elevation model
is called hypsometric tinting.
Double click on
<i class="ms ms-raster"></i> `elevation_2017`
to open its layer properties menu.
In the symbology tab in the band rendering section,
first click `load color map from band`
to create a sequence of breakpoints
for a continuous color ramp,
then set the render type to `Singleband psuedocolor`,
and select a color ramp such as `viridis`
from the dropdown menu.
To select GRASS's elevation color ramp instead,
choose `create new color ramp`
from the color ramp dropdown,
select the `catalog: cpt-city` type,
then under QGIS select grass color ramps,
and pick `elevation`.
See the [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/)
topography collection for other great color ramps
such as `wiki-schwarzwald-cont` for
digital elevation models.
Save the color ramp to your favorites.
In the resampling section
set zoomed in to bilinear or cubic.
Since a digital elevation model
represents a continuous gradient of data
you should use bilinear or cubic interpolation
for resampling instead of nearest neighbor
which is more appropriate for discrete data.

| Digital Elevation Model (DEM) |
|:---:|
| ![Digital elevation model](/images/governors-island/elevation.jpg) |

To blend a hillshade with the elevation color ramp,
first make a copy of the layer `elevation_2017`.
To do this right click on `elevation_2017`
and select `duplicate layer`.
Turn on the new layer, move it above the original layer,
and change its symbology.
Set the render type to `hillshade`
and the blending mode to soft light.
Adjust the settings.
For example try setting the z-factor to 2.
Try adjusting the azimuth
to cast the shade from a different angle.
Hit apply to visualize the changes.
Optionally rename the layer to `shaded_elevation_2017`.

| Digital Elevation Model (DEM) with Hillshading |
|:---:|
| ![Digital surface model with hillshading](/images/governors-island/elevation-with-map-elements.jpg) |

To add contour lines as a layer style,
first make another copy of the layer `elevation_2017`.
Turn on the new layer, move it above the original layer,
and change its symbology.
Set the render type to `contours`
and then adjust the settings.
Try setting the contour interval to 3 feet.
To reduce noise try setting input downscaling to 6 feet.
Try different blending modes
such as screen with 60% percent brightness.

---

# GRASS Tools

What are GRASS Tools?

We will use GRASS Tools
to set the computational region
and then compute a hillshade.

In the browser expand the location
<i class="ms ms-grass-gis"></i> `nyspf_governors_island`.
Right click on the location
and select `new mapset`.
Name the mapset `terrain_analysis`.
Right click on the new mapset and select `Open Mapset`
to activate GRASS Tools.
GRASS Tools will open in a panel on the right.

The best practice for working with GRASS GIS
is to use the `PERMANENT` mapset for reference data
and use other mapsets for new data that you create.
This helps to preserve the original source data
and keep your project organized.
Whichever mapset you open,
you will still have access
to the maps in the `PERMANENT` mapset.

First set the computational region.
Under GRASS modules, expand region settings,
and double click `g.region.zoom`
to shrink the region until it meets non-NULL raster cells.
In the `g.region.zoom` options tab
set the raster to `elevation_2017@PERMANENT`.
Run and then close this module.

Then compute a hillshade.
Under GRASS modules expand raster,
then spatial analysis, and then terrain analysis.
Double click the module `r.relief`
to create a shaded relief map.
In the options tab for `r.relief`
set the input raster to `elevation_2017@PERMANENT`,
the output to `relief_2017`,
and the z-factor to 2 or 3.
Run the module, click view output to add it
to your layer manager and map display,
and then close the module.
Open the layer properties for `relief_2017`.
In the symbology settings,
set the render type to `singleband gray` and apply.
To blend the hillshade with the digital elevation model,
set the blending mode to `soft light`.
Make sure the layer `elevation_2017` is turned on
and is below layer `relief_2017`.

| Shaded Relief |
|:---:|
| ![Shaded Relief](/images/governors-island/hillshade.jpg) |
