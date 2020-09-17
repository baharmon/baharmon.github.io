#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRIPT: process-drone-data.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: process time series of drone data
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
raster_list = gscript.list_grouped('rast', pattern='surface_*')[mapset]

for raster in raster_list:
    # set region
    gscript.run_command('g.region',
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
