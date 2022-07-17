---
title: Python scripting in GRASS GIS
subtitle:
description: An introduction to Python scripting in GRASS GIS.
featured_image: /images/
---

![GRASS Interactive Python Shell](/images/python/python-editor.png)

**Contents**
* TOC
{:toc}

---

## Geospatial Programming in GRASS

This tutorial is an introduction to geospatial programming
in <i class="ms ms-grass"></i> GRASS GIS with Python.
In this tutorial you will learn how to automatically
import, process, render maps of
a time series of digital surface models
from aerial surveys of the LSU Hilltop Arboretum.
For this tutorial install
<i class="ms ms-grass"></i> [GRASS GIS](https://grass.osgeo.org/)
and download [hilltop_drone_data.zip](https://drive.google.com/file/d/1zYPDHpXxWDG3zj2zeGum0MOsPUiEk67I/view?usp=sharing),
extract it, and move it your
<i class="ms ms-database"></i> GRASS  database directory.
Optionally install a text editor like [Atom](https://atom.io/).
With the
[GRASS Python Scripting Library](https://grass.osgeo.org/grass-stable/manuals/libpython/)
you can:
* Automate the import and export of geospatial data
* Automate geospatial computations
* Automate map production
* Develop new add-on modules

There are two ways to run Python scripts in <i class="ms ms-grass"></i> GRASS.
In the Interactive Python Shell in the Layer Manager
you can open a simple editor where you can write and run scripts.
Or you can write your scripts in a text editor
and then launch the script from the GRASS file menu.

| GRASS Interactive Python Shell |
|:---:|
| ![GRASS Interactive Python Shell](/images/python/python-editor.png) |

| GRASS scripting with a text editor |
|:---:|
| ![GRASS scripting with text editor](/images/python/grass-scripting.png) |


Start <i class="ms ms-grass-gis"></i> GRASS
and open the Python tab in the Layer Manager.
This an Interactive Python Shell.
Try some Python here.

```python
print("Hello World!")
```

---

## GRASS Commands in Python

Open the Console in the Layer Manager
and run a GRASS command.
Import a raster map with the module
[r.in.gdal](https://grass.osgeo.org/grass-stable/manuals/r.in.gdal.html).
Set your input data file path to one of the rasters
in the `hilltop_drone_data` directory.
Use the full file path.
```
r.in.gdal input=surface_2020_03_19.tif output=surface_2020_03_19
```

Open the Interactive Python Shell in the Layer Manager.
In the bottom left corner of the Interactive Python Shell
open the Simple Editor.
To run the same command in the Simple Editor using Python,
first add the Python shebang,
then import the <i class="ms ms-grass"></i>
[GRASS Python Scripting Library](https://grass.osgeo.org/grass-stable/manuals/libpython/)
with `import grass.script as gscript`{:.python},
and use the `run_command()` function from the `grass.script` package
to run a GRASS module.
Use the full file path for the input map in the example below.

```python
#!/usr/bin/env python3

import grass.script as gscript

gscript.run_command(
    'r.in.gdal',
    input='surface_2020_03_19.tif',
    ouput='surface_2020_03_19',
    overwrite=True)
```

---

## Importing Maps

Write a script that uses a for loop
to import all of the maps in a directory.
Start <i class="ms ms-grass"></i> GRASS and
create a new location called `laspm_hilltop`
with EPSG code 6478 for `NAD83(2011) / Louisiana South Meters`.

In the script first import
the `os` library and the `grass.script` library.
Then set the GRASS environment settings.
Assign the <i class="ms ms-database"></i> GRASS database directory
to the variable `gisdbase`.
The use the `os.path.join` method to set the filepath
to `hilltop_drone_data` directory
inside of the <i class="ms ms-database"></i> GRASS database directory.
Use a for loop to iterate through all of the files in that directory.
For each file, use an if statement to test if it is a geotiff.
If it is then import it with the module
[r.in.gdal](https://grass.osgeo.org/grass-stable/manuals/r.in.gdal.html).

```python
#!/usr/bin/env python3

import os
import grass.script as gscript

# settings
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']

# set path
data = os.path.join(
    gisdbase,
    "hilltop_drone_data")

# set region
gscript.run_command('g.region', res=0.1)

# iterate through files in directory
for file in os.listdir(data):
    filename = os.path.splitext(file)[0]
    # iterate through geotiffs
    if file.endswith('.tif'):
        # check if raster is already in mapset
        gscript.run_command('r.in.gdal',
            input=os.path.join(data, file),
            output=filename,
            overwrite=overwrite)
    else:
        pass
```


---

## Processing Maps

To automatically process maps in <i class="ms ms-grass"></i> GRASS,
create a list of maps with the module
[g.list](https://grass.osgeo.org/grass-stable/manuals/g.list.html)
then use a for loop to iterate through the list of maps,
running modules to process each map.
This example iterates through the digital surface models
that you just imported from `hilltop_drone_data`
to generate shaded relief maps for each.

```python
#!/usr/bin/env python3

import os
import grass.script as gscript

# settings
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']

# list rasters in mapset
raster_list = gscript.list_grouped('rast',
    pattern='surface_*')[mapset]

for raster in raster_list:
    # set region
    gscript.run_command(
        'g.region',
        raster=raster,
        res=0.1)
    # set color tables
    gscript.run_command(
        'r.colors',
        map=raster,
        color='viridis',
        flags='e')
    # compute hillshade
    gscript.run_command(
        'r.relief',
        input=raster,
        output='relief'+raster[-11:],
        zscale=3,
        overwrite=overwrite)
    # compute shaded relief
    gscript.run_command(
        'r.shade',
        shade='relief'+raster[-11:],
        color=raster,
        output='shaded_relief'+raster[-11:],
        brighten=30,
        overwrite=overwrite)
```

---

## Rendering Maps

To automatically render maps from <i class="ms ms-grass"></i> GRASS,
create a list of maps with the module
[g.list](https://grass.osgeo.org/grass-stable/manuals/g.list.html),
iterate through the list with a for loop,
start a graphics display monitor with
[d.mon](https://grass.osgeo.org/grass-stable/manuals/d.mon.html)
using the Cairo driver,
add a map with [d.rast](https://grass.osgeo.org/grass-stable/manuals/d.rast.html),
and stop the monitor.
The maps in the graphics monitors will written directly to files
in the current GRASS location.


```python
#!/usr/bin/env python3

import os
import grass.script as gscript

# settings
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']

# list rasters in mapset
raster_list = gscript.list_grouped('rast',
    pattern='shaded_relief_*')[mapset]

for raster in raster_list:
    # set region
    gscript.run_command(
        'g.region',
        raster=raster,
        res=0.1)
    # write map to image file
    gscript.run_command(
        'd.mon',
        start="cairo",
        width=1000,
        height=1000,
        output=os.path.join(
            gisdbase,
            location,
            raster+'.png'),
        overwrite=overwrite)
    gscript.run_command(
        'd.rast',
        map=raster)
    gscript.run_command(
        'd.mon',
        stop="cairo")

```

| March 19, 2020 |
|:---:|
| ![Shaded Relief](/images/python/shaded_relief_2020_03_19.png) |

| April 25, 2020 |
|:---:|
| ![Shaded Relief](/images/python/shaded_relief_2020_04_25.png) |

| June 1, 2020 |
|:---:|
| ![Shaded Relief](/images/python/shaded_relief_2020_06_01.png) |

| June 30, 2020 |
|:---:|
| ![Shaded Relief](/images/python/shaded_relief_2020_06_30.png) |

| August 3, 2020 |
|:---:|
| ![Shaded Relief](/images/python/shaded_relief_2020_08_03.png) |

| August 29, 2020 |
|:---:|
| ![Shaded Relief](/images/python/shaded_relief_2020_08_29.png) |
