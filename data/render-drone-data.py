#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRIPT: render-drone-data.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: render time series of drone data
COPYRIGHT: GNU GPL (C) 2020 Brendan Harmon
"""

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
raster_list = gscript.list_grouped('rast', pattern='shaded_relief_*')[mapset]

for raster in raster_list:
    # write map to image file
    gscript.run_command('d.mon',
        start="cairo",
        width=800,
        height=800,
        output=os.path.join(gisdbase, location, raster+'.png'),
        overwrite=overwrite)
    gscript.run_command('d.rast',
        map=raster)
    gscript.run_command('d.mon', stop="cairo")
