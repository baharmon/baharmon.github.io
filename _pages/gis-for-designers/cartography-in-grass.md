---
title: Cartography in GRASS GIS
subtitle:
description: A guide to cartography in GRASS GIS.
featured_image: /images/governors-island/landcover-map.png
---

![Landcover Map](/images/governors-island/landcover-map.png)

**Contents**
* TOC
{:toc}

---

## Start GRASS

Download and extract the
[Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
This geospatial dataset contains the
GRASS GIS location `nyspf_governors_island` with
raster and vector data for
Governor's Island, New York City, USA.
Its coordinate reference system (CRS) is
NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet
in US Survey Feet.
Move the GRASS GIS location `nyspf_governors_island` to your
[GRASS GIS database](https://grass.osgeo.org/grass-stable/manuals/grass_database.html)
directory.
Start <i class="ms ms-grass-gis"></i> GRASS GIS,
set the GRASS GIS database directory to
[GRASS GIS database](https://grass.osgeo.org/grass-stable/manuals/grass_database.html)
directory,
select `nyspf_governors_island` as your location,
and open the `PERMANENT` mapset.
Optionally download and install the free, open source font
[Lato](https://www.latofonts.com/lato-free-fonts/).

---

## Render Map Display

Layout a <i class="ms ms-map"></i> map of landcover
with cartographic elements including a title and legend
in <i class="ms ms-grass-gis"></i> GRASS GIS.
First add the raster map `landcover_2014`
and resize your map display.
```
d.rast map=landcover_2014
```

Add cartographic elements to your map
using either the toolbar at the top of the map display window
or the command line.
Add a title and descriptive text
using the add text button in the add map elements menu
or by running the module
[d.text](https://grass.osgeo.org/grass-stable/manuals/d.text.html)
from the command console.
Optionally set the font, font color, and size.
Position the text manually or using the `at` parameter in the command.
```
d.text -s text="Landcover" color=white at=2,98 font=Lato-Bold size=24
d.text -s text="Governor's Island" color=white at=2,95 font=Lato-Regular size=18
d.text -s text="New York City, USA" color=white at=2,92.5 font=Lato-Light size=18
```

Add a legend
using the add legend button in the add map elements menu
or by running the module
[d.legend](https://grass.osgeo.org/grass-stable/manuals/d.text.html)
from the command console.
Set the raster to `landcover_2014` and
optionally set the font, font color, and size.
Position and resize the legend manually
or using the `at` parameter in the command.
```
d.legend -c raster=landcover_2014 at=70,89,2,5 color=white font=Lato-Regular fontsize=14
```

Add a scale bar and north arrow.
```
d.northarrow style=fancy_compass at=90.0,10.0 color=white text_color=white font=Lato-Regular
d.barscale at=72,5.8 length=500 units=feet segment=2 color=white bgcolor=none text_position=left fontsize=14
```

Render your <i class="ms ms-map"></i> map
as a `.png` using the `save display to file` button
in the map display window toolbar.
This will save an image file from the map display
at screen resolution.

| Landcover Map |
|:---:|
| ![Landcover Map](/images/governors-island/landcover-map.png) |


---

## Print Workspace

To print a higher resolution map as an image or pdf
use the addon module
[m.printws](https://grass.osgeo.org/grass-stable/manuals/addons/m.printws.html).
This addon module uses the settings saved in a workspace file to print a map.
First install the addon module with
[g.extension](https://grass.osgeo.org/grass-stable/manuals/g.extension.html).

Save the workspace.
In the `File` menu select `Workspace` and then `Save as`
to save the workspace as `landcover.gxw`.
Run [m.printws](https://grass.osgeo.org/grass-stable/manuals/addons/m.printws.html)
Note that you may need to run `m.printws --ui` with the `--ui` flag
to force the graphical user interface for the addon module to open.
In [m.printws](https://grass.osgeo.org/grass-stable/manuals/addons/m.printws.html)
set the workspace, the output file, the page type, and the format.
Use the flexi page type to fit the landcover raster.
Set the format to either `png` or `pdf`.
After running the module, check the map it generated.
The position of map elements may need to be adjusted.
Reposition the map elements in the GRASS map display,
save the workspace again, and re-run
[m.printws](https://grass.osgeo.org/grass-stable/manuals/addons/m.printws.html).

```
g.extension extension=m.printws
g.region raster=landcover_2014
d.rast map=landcover_2014
d.text -s text="Landcover" color=white at=2,95 font=Lato-Bold size=24
d.text -s text="Governor's Island" color=white at=2,92.5 font=Lato-Regular size=18
d.text -s text="New York City, USA" color=white at=2,90.5 font=Lato-Light size=18
d.legend -c raster=landcover_2014 at=70,89,2,5 color=white font=Lato-Regular fontsize=14
d.northarrow style=fancy_compass at=90.0,4.5 color=white text_color=white font=Lato-Regular
d.barscale at=72,5.8 length=500 units=feet segment=2 color=white bgcolor=none text_position=left fontsize=14
m.printws input=landcover.gxw output=landcover-150dpi.png page=Flexi format=png
```

| 150 DPI Landcover Map |
|:---:|
| ![Landcover Map at 150 DPI](/images/governors-island/landcover-150dpi.png) |

---

## Cartographic Composer

To render a high resolution <i class="ms ms-map"></i> map
as a `pdf` use the cartographic composer
[g.gui.psmap](https://grass.osgeo.org/grass-stable/manuals/g.gui.psmap.html).
First set your computational region
to the landcover <i class="ms ms-raster"></i> raster.
```
g.region raster=landcover_2014
```
In the file menu select cartographic composer.
A new window with the cartographic composer
will open.  In page setup
set the units to mm,
the page size format to custom,
the width and height to `1000`,
and all margins to `0`.
Click on the map frame button
and draw a frame over the entire canvas.
In the map frame settings
set fit frame to match current computational region.
Set the resolution to at least 300 dpi.
Uncheck draw border around the map frame.
Click the add raster map layer button
and set the raster to `landcover_2014`.

Add cartographic elements including
a title, legend, and scale bar to the map.
To add a title and text
click on the add map elements button
and select add text.
In the text settings dialog,
type `Landcover` as the text,
set the font to Helvetica,
the font size to `64`,
and the font color to white.
In the position tab
set the units to millimeters,
the x position to `10`,
the y position to `20`,
and the reference point to the top left corner.

To add a legend
click on the add map elements button
and select add legend.
In the raster legend settings
check show raster legend and then
set the source raster to current,
the type of legend to discrete,
set the units to millimeters,
the x position to `10`
and the y position to `50`.
Set the font to Helvetica,
the font size to `36`,
and the color to white.

To add a scale bar
click on the add map elements button
and select add scale bar.
In the scale bar settings
set the units to millimeters,
x position to `10`,
 y position to `950`,
length to `1000` feet,
height to `5` mm,
segments to `2`,
font size to `36`,
and check transparent background.


Click the generate pdf output button
to save the <i class="ms ms-map"></i> map.

| Cartographic Composer |
|:---:|
| ![GRASS Cartographic Composer](/images/governors-island/cartographic-composer.jpg) |

---

## Python

Maps can be automatically generated using
the <i class="ms ms-grass"></i>
[GRASS Python Scripting Library](https://grass.osgeo.org/grass-stable/manuals/libpython/).
This can be an efficient way
to produce a large number of maps quickly.
For a demo download the Python script
[render-map.py](https://github.com/baharmon/baharmon.github.io/blob/master/data/render-map.py?raw=true) and run it in GRASS.
In GRASS' file menu choose launch script
and browse to select `render-map.py`.
The image `landcover-2014.png` will be written to
your `nyspf_govenors_island` directory.
See the tutorial [Python in GRASS](python-in-grass)
for a more detailed guide to using Python in GRASS.

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
