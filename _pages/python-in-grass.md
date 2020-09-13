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

# Hello World

# Python in GRASS

Maps can be automatically generated using
the <i class="ms ms-grass"></i>
[GRASS Python Scripting Library](https://grass.osgeo.org/grass78/manuals/libpython/).
For more information see the [GRASS Wiki page](https://grasswiki.osgeo.org/wiki/GRASS_Python_Scripting_Library).
For a demo download the Python script
[render-maps.py](https://github.com/baharmon/baharmon.github.io/blob/master/data/render-maps.py?raw=true).
To run this script in GRASS
open the file menu, choose launch script,
and browse to select the script.
The `.png` image will automatically be written to
your `nyspf_govenors_island` directory.

# Dataset




# Importing Maps


In the Python script
import the
[GRASS Python Scripting Library](https://grass.osgeo.org/grass78/manuals/libpython/)
with `import grass.script as gscript`{:.python}.
Use the `run_command()` function from the `grass.script` package
to run GRASS modules.
```python
gscript.run_command()
```


```python
#!/usr/bin/env python
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
