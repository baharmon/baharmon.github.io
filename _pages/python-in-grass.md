---
title: Python scripting in GRASS GIS
subtitle:
description: An introduction to Python scripting in GRASS GIS.
featured_image: /images/
---

![](/images/)

**Contents**
* TOC
{:toc}

---

## Geospatial Programming in GRASS

This tutorial is an introduction to geospatial programming
in <i class="ms ms-grass"></i> GRASS GIS with Python.
For this tutorial install
<i class="ms ms-grass"></i> [GRASS GIS](https://grass.osgeo.org/)
and download the [sample dataset](...).
Optionally install a text editor like [Atom](https://atom.io/).
With the
[GRASS Python Scripting Library](https://grass.osgeo.org/grass78/manuals/libpython/)
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
| ![Screenshot of GRASS Interactive Python Shell](/images/) |

| GRASS scripting with a text editor |
|:---:|
| ![Screenshot GRASS scripting with text editor](/images/) |


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
Set your file path to input data.
```
r.in.gdal input=elevation.tif output=elevation
```

Open the Interactive Python Shell in the Layer Manager.
In the bottom left corner of the Interactive Python Shell
open the Simple Editor.
To run the same command in the Simple Editor using Python,
first add the Python shebang,
then import the <i class="ms ms-grass"></i>
[GRASS Python Scripting Library](https://grass.osgeo.org/grass78/manuals/libpython/)
with `import grass.script as gscript`{:.python},
and use the `run_command()` function from the `grass.script` package
to run a GRASS module.
```python
#!/usr/bin/env python3

import grass.script as gscript

gscript.run_command('r.in.gdal',
  input='',
  ouput='',
  overwrite=True)
```
---

## Importing Maps

Use a for loop to import all of the maps in a directory.


---

## Processing Maps

---

## Rendering Maps

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import grass.script as gscript

# set environment
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']
res=1

# set region
gscript.run_command('g.region', raster='landcover_2014')

# write map to image file
gscript.run_command('d.mon',
    start="cairo",
    width=1600,
    height=1600,
    output=os.path.join(gisdbase, location, 'landcover-2014.png'),
    overwrite=overwrite)
gscript.run_command('d.rast',
    map='landcover_2014')
gscript.run_command('d.text',
    text='Landcover',
    font='Lato-Bold',
    size=24,
    color='white',
    at=(2,95),
    flags='s')
gscript.run_command('d.legend',
    raster='landcover_2014',
    font='Lato-Regular',
    fontsize=18,
    color='white',
    at=(70, 94, 2, 5),
    flags='c')
gscript.run_command('d.northarrow',
    style='fancy_compass',
    font='Lato-Regular',
    color='white',
    text_color='white',
    at=(92.5,5))
gscript.run_command('d.barscale',
    length='500',
    units='feet',
    segment=2,
    color='white',
    bgcolor='none',
    text_position='left',
    fontsize=18,
    at=(75,5.8))
gscript.run_command('d.mon', stop="cairo")
```

| Landcover Map Rendered with Python |
|:---:|
| ![Landcover Map](/images/governors-island/landcover-2014.png) |
