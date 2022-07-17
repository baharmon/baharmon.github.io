---
title: Acquiring Global Data for GRASS GIS
subtitle:
description: A guide to importing global data into GRASS GIS.
featured_image:
---

![Swiss Shaded Relief](/images/importing-global-data/swiss-shaded-relief.png)

---

## Data Sources

See my list of [geospatial data sources](geospatial-data-sources).

---

## Importing the NASA Digital Elevation Model

In this section, we will download part of a
global digital elevation model
from NASA Earthdata. <i class="ms ms-grass-gis"></i> GRASS GIS has an addon module
[r.in.nasadem](https://grass.osgeo.org/grass-stable/manuals/addons/r.in.nasadem.html)
that automates the import of the NASADEM digital elevation model.
[NASADEM](https://lpdaac.usgs.gov/products/nasadem_hgtv001/)
is a digital elevation model
at 1 arcsecond or approximately 30 meter resolution
derived from the Shuttle Radar Topography Mission (SRTM)
and other sources including the
the ASTER Global Digital Elevation Model and
and the ALOS Global Digital Surface Model.
Register with the NASA [Earthdata](https://urs.earthdata.nasa.gov/users/new) portal and save your username and password.

Since NASADEM uses
<i class="ms ms-sphere"></i> World Geodetic System 1984 (WGS84)
as its coordinate reference system,
it must be imported into GRASS in a WGS84 location.
While you could create a new WGS84 location
using EPSG code 4326,
we will use Natural Earth Dataset for GRASS GIS.
Download the [Natural Earth Dataset for GRASS GIS](https://zenodo.org/record/3762852/files/natural-earth-dataset.zip?download=1).
This dataset is a GRASS GIS location in WGS84
with global background maps from the
[Natural Earth](https://www.naturalearthdata.com/) collection.
Extract the zip archive and move the `natural-earth-dataset`
to your GRASS GIS database directory named `grassdata`.

Start <i class="ms ms-grass-gis"></i> GRASS GIS.
Set the GRASS GIS database directory to `grassdata`,
set the location to the `natural-earth-dataset`,
and select the mapset called `tutorial`.
First install the `r.in.nasadem` addon module
with [g.extension](https://grass.osgeo.org/grass-stable/manuals/g.extension.html).
If it does not exist, create it now.
Before running `r.in.nasadem`
you must first set a computational region
with [g.region](https://grass.osgeo.org/grass-stable/manuals/g.region.html)
defining the area for downloading and importing raster tiles.

In this tutorial we will set the region
to the boundary of Switzerland.
Add the raster map `natural_earth`
and the vector map `countries` to the map display.
Extract Switzerland from the `countries` vector map using the module
[v.extract](https://grass.osgeo.org/grass-stable/manuals/v.extract.html).
Set the region to the new vector map `switzerland` and
set the resolution to 1 arcsecond.
Or optionally zoom into a smaller region within the country
and from the `various zoom options` button in the map display
select `set computational region extent from display`.
Run the addon module
[r.in.nasadem](https://grass.osgeo.org/grass-stable/manuals/addons/r.in.nasadem.html)
with your username and password for Earthdata.
For Switzerland `r.in.nasadem` will automatically
download, import, and patch 8 raster tiles to generate
a 1 arcsecond digital elevation model for the country.
After importing the NASADEM raster,
set a mask using the vector map for Switzerland
with [r.mask](https://grass.osgeo.org/grass-stable/manuals/r.mask.html)
and use map algebra to crop the elevation raster
with [r.mapcalc](https://grass.osgeo.org/grass-stable/manuals/r.mapcalc.html).
Then set the color table to `elevation`
using [r.colors](https://grass.osgeo.org/grass-stable/manuals/r.colors.html)
and optionally set histogram equalization with the `-e` flag.
```
g.extension extension=r.in.nasadem
d.rast map=natural_earth
d.vect map=countries fill_color=none
v.extract input=countries where="ADMIN = 'Switzerland'" output=switzerland
g.region vector=switzerland res=0:00:01
r.in.nasadem output=swiss_elevation username=your_username password=your_password
r.mask vector=switzerland
r.mapcalc "swiss_elevation = swiss_elevation" --overwrite
r.colors -e map=swiss_elevation color=elevation
```

| Swiss Topography |
|:---:|
| ![Swiss Topography](/images/importing-global-data/swiss-elevation.png) |

To better visualize the topography,
compute a shaded relief map with the module
[r.relief](https://grass.osgeo.org/grass-stable/manuals/r.relief.html).
Then overlay the relief map with the elevation map
using the module
[r.shade](https://grass.osgeo.org/grass-stable/manuals/r.shade.html)
to create a colorized shaded relief map.
Add a legend for the elevation map using the module
[d.legend](https://grass.osgeo.org/grass-stable/manuals/d.legend.html).
```
r.relief input=swiss_elevation output=swiss_relief
r.shade shade=swiss_relief color=swiss_elevation output=swiss_shaded_relief brighten=30
d.legend raster=swiss_elevation
```
Compare the map with hypsometric tinting with shaded relief
from Natural Earth with the shaded relief map derived from NASADEM.
Use the module
[r.info](https://grass.osgeo.org/grass-stable/manuals/r.info.html)
to compare the resolution of both maps.
The resolution of the natural earth map is `0:01:12`,
while the resolution of NASADEM is `0:00:01`
in degrees-minutes-seconds.

| Swiss Shaded Relief |
|:---:|
| ![Swiss Shaded Relief](/images/importing-global-data/swiss-shaded-relief.png) |

Other sources of elevation data for Switzerland include:
* the 25 m resolution
[EU-DEM](https://www.eea.europa.eu/data-and-maps/data/copernicus-land-monitoring-service-eu-dem)
available for download from
[Copernicus](https://land.copernicus.eu/imagery-in-situ/eu-dem/eu-dem-v1.1)
* data from the Swiss Federal Office of Topography
at [swisstopo](https://www.swisstopo.admin.ch/).
