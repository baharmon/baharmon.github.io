---
title: Acquiring Urban Data for GRASS GIS
subtitle:
description: A guide to acquiring urban data and importing it into GRASS GIS.
featured_image:
---

![Shaded relief map](/images/governors-island/surface.png)

**Contents**
* TOC
{:toc}

---

# Data Sources

In this tutorial we will use geospatial data from
[GIS.NY.GOV](http://gis.ny.gov/) and
New York City's [Open Data](https://data.cityofnewyork.us) portal.
See my list of [geospatial data sources](geospatial-data-sources)
for further sources of urban data.

---

# Download Data
Download a digital elevation model (DEM)
and digital surface model (DSM)
for Governor's Island, New York, NY, USA from
[GIS.NY.GOV](http://gis.ny.gov/elevation/NYC-topobathymetric-DEM.htm).
NYC commissioned a airborne lidar survey in 2017 and created
a 1 ft resolution bare earth DEM and a DSM from the lidar data.
The DEM represents the shape of the bare ground
with no trees, buildings, or other structures,
while the DSM represents the shape of the earth's surface
and everything on it.
Large rasters such as these are often divided
into tiles for easier downloading.
For Governor's Island download DEM and DSM tiles
[be_NYC_020.tif](ftp://ftp.gis.ny.gov/elevation/DEM/NYC_TopoBathymetric2017/be_NYC_020.tif) and
[hh_NYC_020.tif](ftp://ftp.gis.ny.gov/elevation/DEM/NYC_TopoBathymetric2017_DSM/hh_NYC_020.tif).
Extract both zip archives.
Download
[shoreline](https://data.cityofnewyork.us/Recreation/Shoreline/2qj2-cctx)
data from NYC Open Data.
Select `Export`, `Download`, and then `Shapefile`
to download `Shoreline.zip.`
Extract this archive containing
`NYC_2017_LiDAR_Low_Tide_Shoreline.shp`.

----

# Create New Location from Vector Data
Start GRASS GIS.
In the the startup screen, select `New` location.
In the `Define new GRASS Location` window,
first browse to set your GRASS GIS database directory
where the location will be created
and then set a name for the location.
Hit `Next` to continue.
Select `Read projection and datum terms from a georeferenced data file`.
Browse to select `NYC_2017_LiDAR_Low_Tide_Shoreline.shp`.
Hit `Next` and then `Finish` to continue.
Accept the `Import data` to import the data into the new location.
In the startup screen, select the new location
and the `PERMANENT` mapset and start the GRASS session.

Print information about the projection in the console with
[g.proj](https://grass.osgeo.org/grass78/manuals/g.proj.html)
with the `-p` flag.
The map projection should be
NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet
in U.S. Surveyor's Foot.
```
g.proj -p
```

---

# Process Vector Data
In the Map Display click the `Select vector feature` button.
Click on the shore of Governor's Island to select it.
In the `Select features` dialog, click `Create a new map`.
Rename the map to `shoreline` using
[g.rename](https://grass.osgeo.org/grass78/manuals/g.rename.html).
Alternatively query the vector map to find
the category for Governor's Island's shore
and then use
[v.extract](https://grass.osgeo.org/grass78/manuals/v.extract.html)
to extract it by category value.
```
v.extract input=NYC_2017_LiDAR_Low_Tide_Shoreline cats=184 output=shoreline
```
Or use an SQL query to select the category value.
```
v.extract input=NYC_2017_LiDAR_Low_Tide_Shoreline where="Cat = '184'" output=shoreline
```

---

# Import Raster Data
Set the computational region and mask
to the extracted shoreline for Governor's Island.
```
g.region vector=shoreline res=1
r.mask vector=shoreline
```

Then import the DEM and DSM with the module
[r.in.gdal](https://grass.osgeo.org/grass78/manuals/r.in.gdal.html)
with the `-r` flag to limit the import the region.
```
r.in.gdal -r input=be_NYC_020.tif output=elevation_2017
r.in.gdal -r input=hh_NYC_020.tif output=surface_2017
```
*Note:* When you want to import data
in a different projection into a location,
use [r.import](https://grass.osgeo.org/grass78/manuals/r.import.html)
to import with automatic reprojection.

Set a color table for each raster map using
[r.colors](https://grass.osgeo.org/grass78/manuals/r.colors.html).
Add a legend with
[d.legend](https://grass.osgeo.org/grass78/manuals/d.legend.html).
```
r.colors -e map=elevation_2017 color=viridis
r.colors -e map=surface_2017 color=viridis
```

| Digital elevation model| Digital surface model|
|:---:|:---:|
| ![Digital elevation model](/images/governors-island/elevation.png) | ![Digital surface model](/images/governors-island/surface.png) |
