# What is GRASS GIS?

* Geographic Resource Analysis Support System (GRASS) GIS
* Free and open source
* Cross platform: Windows, Mac, and Linux

The Geographic Resource Analysis Support System (GRASS) is a free and open source geographic information systemms (GIS). This cross platform GIS runs on Windows, Mac, and Linux. GRASS GIS is released under the GNU General Public License with source code on GitHub at https://github.com/OSGeo/grass. Go to the [GRASS GIS Website](https://grass.osgeo.org/) to download it, find datasets, find tutorials, and read the documentation. GRASS GIS has more than 500 modules for working with geospatial data. The GRASS GIS tutorials in this [course](gis-for-designers) will cover terrain analysis,  geomorphometry, map algebra, hydrology, landscape ecology, solar analysis, lidar data analytics, urban modeling, and more.

---

# How to Install GRASS GIS

* Download from grass.osgeo.org

Download a GRASS GIS installer from https://grass.osgeo.org/download/. Choose a standalone installer for the lastest stable release for your operating system - Windows, Mac, or Linux.

---

# Download a Dataset

* Natural Earth Dataset

Download the [Natural Earth Dataset for GRASS GIS](https://zenodo.org/record/3762852/files/natural-earth-dataset.zip?download=1). This dataset is a GRASS GIS location in the World Geodetic System 1984 (WGS84) with global background maps from the [Natural Earth](https://www.naturalearthdata.com/) collection. Extract the zip archive and move the `natural-earth-dataset` to your GRASS GIS database directory named `grassdata`.


---

# Starting GRASS GIS

* Download sample datasets
* GRASS GIS Database Directory
* Locations and mapsets
* Demo of `nyspf_governors_island` mapsets

To start GRASS GIS, you need to set the GRASS GIS database directory, select a location, and then select a mapset. The GRASS GIS database directory will contain locations which in turn contain mapsets. A location is a set of directories containing mapsets with a given coordinate system. Every location has a `PERMANENT` mapset which contains reference data. Read the [GRASS GIS Quickstart](https://grass.osgeo.org/grass78/manuals/helptext.html) to learn more.

| GRASS GIS Startup Screen |
|:---:|
| ![GRASS GIS Startup Screen](/images/grass_start.png) |

| GRASS GIS Database Structure |
|:---:|
| ![GRASS GIS Database Structure](grass_database.png) |

A good way of working is to first import reference data for a given project to the `PERMANENT` mapset and then create a new mapset for processing and analyzing the reference data. Data in the `PERMANENT` mapset is always accessible from other mapsets. Working this way means that all your reference data will be safe and easily accessible in the `PERMANENT` mapset, while all new data will be created in the new mapset.

Note that you can create a new location with `New` button or download sample datasets as locations with the `Download` button. New locations can be created from [EPSG](https://epsg.org/) codes for coordinate systems, from geospatial data such as shapefiles and geotiffs, etc.

For this tutorial download, extract, and move the [Natural Earth Dataset for GRASS GIS](https://zenodo.org/record/3762852/files/natural-earth-dataset.zip?download=1) to a directory name `grassdata`. This will be your GRASS GIS database directory. In the GRASS GIS Startup Screen first set your GRASS GIS database directory by browsing to `grassdata`. Then select `natural-earth-dataset` as your Location. Select `PERMANENT` as your mapset. Then click `Start GRASS session`.

---

# Using GRASS GIS

* Layout of the user interface
* Add raster and vector maps
* Console
* Modules & menus
* Computational region
* Example of a command
* Workspace

---

# Displaying Maps

Once your GRASS session starts,
the layer manager will be one the left
and the map display will be on the right.
Use the `add raster map layer` button
or the hotkey `Ctrl+Shift+R`
to add the `natural_earth` raster
to the map display on the right.
This module is called `d.rast`
with `d` standing for display and `rast` for raster.

Then use the `add vector map layer` button
or the hotkey `Ctrl+Shift+V`
to add the `coastlines` vector
to the map display.
This module is called `d.vect`.

Maps can also be added using the command console.
At the bottom of the layer manager, select the console tab.
In the console, type `d.vect` and hit enter to open the add vector dialog. Or type the command in console:
```
d.vect map=countries fill_color=none
```
Use the console to add the `countries` vector map with no fill color.

Then use either `add vector map layer` dialog or the console
to add the `rivers` vector with blue linework.
```
d.vect map=rivers color=blue
```

---

# Running Modules

In this section of the tutorial,
you will create a new map with rivers for Brazil.
Because you will be creating new data from reference data,
you should first create a new mapset.
Create a new mapset called `tutorial` by selecting
`Settings > GRASS Working Environment > Create New Mapset`
from the menu at the top of the layer manager.
Or in the command console type:
```
g.mapset -c mapset=tutorial
```
The `-c` flag enables the creation of a new mapset.

Commands can be run from the menus at the top of the layer manager, or from the console or modules tabs at the bottom of the layer manager.  

First extract a map of Brazil from the map of countries. Either use the `select vector features` button to highlight Brazil and create a new map layer or run the module
[v.extract](https://grass.osgeo.org/grass78/manuals/v.extract.html)
in the console:
```
v.extract input=countries where="ADMIN = 'Brazil'" output=brazil
```

Zoom to Brazil by right clicking on the map layer and selecting `zoom to selected map`. Then use the module [v.select](https://grass.osgeo.org/grass78/manuals/v.select.html) to create a vector map of rivers in Brazil. Set the `a` input to `rivers` and the `b` input to `brazil`. Use the `within` operator to select only rivers within the country of Brazil.
```
v.select ainput=rivers binput=brazil output=brazilian_rivers operator=within
```

Set a color table for the Brazilian rivers based on their stream order, i.e. their relative size, using [v.colors](https://grass.osgeo.org/grass78/manuals/v.colors.html). Right click on the `brazilian_rivers` layer and select `set color table` or run the command `v.colors` in the console. Set source values to the attribute table, set the attribute column to `scalerank`, and the color table to `water`.
```
v.colors map=brazilian_rivers use=attr column=scalerank color=water
```

---

# Tutorials

* Vaclav Petras'
[<i class="fab fa-youtube"></i>](https://www.youtube.com/watch?reload=9&v=wT5SbZtZ12E) [Introduction to GRASS GIS](http://ncsu-geoforall-lab.github.io/grass-intro-workshop/) + [Video]()
* Paulo van Breugel's [ GRASS GIS, QGIS, and R Tutorials](https://ecodiv.earth/TutorialsNotes/)
