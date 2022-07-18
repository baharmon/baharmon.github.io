---
title: 3D Printing a City
subtitle: A tutorial on 3D printing a city with GRASS GIS  and RhinoTerrain
---

![Manhattan](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/nyc/manhattan-2.png)

**Contents**
* TOC
{:toc}

---


---

## Tiling

In <i class="ms ms-grass-gis"></i> GRASS GIS
```
v.mkgrid -h --overwrite map=grid box=1600,1600
```



In the `RhinoTerrain` menu
select `Import / Export` and then `Import elevation raster file`.

Choose Target Coordinate System
Use input data coordinate system

Import the elevation raster as a point cloud.

`hh_NYC_025.tif`


---

## Python Scripting

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTHOR:    Brendan Harmon <brendan.harmon@gmail.com>

PURPOSE:   Extract raster tiles in GRASS GIS

COPYRIGHT: (C) 2020 Brendan Harmon

LICENSE:   This program is free software under the GNU General Public
           License (>=v2).
"""

import os
import sys
import atexit
import grass.script as gscript
from grass.exceptions import CalledModuleError

# temporary region
gscript.use_temp_region()

# set environment
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']

# set parameters
grid='hex'
raster='surface_2012'
rows=5
columns=5

def main():
    """Extract tiles of raster data from vector grid"""

    make_grid()
    info = extract_tiles()
    export_tiles(info)
    atexit.register(cleanup)
    sys.exit(0)

def make_grid():
    """Generate vector grid"""

    # Make vector grid
    gscript.run_command('v.mkgrid',
    map=grid,
    grid=[rows,columns],
    flags='h',
    overwrite=overwrite)

def extract_tiles():
    """Extract tiles of raster data from vector grid"""

    # determine number of areas in vector grid
    info = gscript.parse_command('v.info',
        map=grid,
        flags='t')
    # extract each grid cell from vector grid
    for i in xrange(1, int(info['areas'])+1):
        gscript.run_command('v.extract',
            input=grid,
            cats=i,
            output=grid+'_'+str(i),
            overwrite=overwrite)
        # set mask to cell
        gscript.run_command('r.mask',
            vector=grid+'_'+str(i),
            overwrite=overwrite)
        #  write raster tile
        gscript.run_command('r.mapcalc',
            expression='{output} = {raster}'.format(output=grid+'_'+str(i),
                raster=raster),
            overwrite=overwrite)
        # remove mask
        gscript.run_command('r.mask',
            flags='r')
    return info

def export_tiles(info):
    """Export tiles of raster data extracted from grid"""

    # export raster tiles as geotiff
    for i in xrange(1, int(info['areas'])+1):
        gscript.run_command('r.out.gdal',
            input=grid+'_'+str(i),
            output=os.path.join(gisdbase, location, grid+'_'+str(i)+'.tif'),
            overwrite=overwrite)

def cleanup():
    try:
        # remove mask
        gscript.run_command('r.mask',
            flags='r')
    except CalledModuleError:
        pass

if __name__ == "__main__":
    atexit.register(cleanup)
    sys.exit(main())

```


---

## 3D Printing


Units m
Paste
RtMeshTerrainBase Absolute -50
SaveAs
Export

3D printer settings
--------------------
scale x to 145mm
scale factor approx: 0.052
z rotation for form2: -15
