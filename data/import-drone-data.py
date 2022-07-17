#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRIPT: import-drone-data.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: import time series of drone data
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

# set path
data = os.path.join(gisdbase,"hilltop_drone_data")

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
