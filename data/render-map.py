#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AUTHOR:    Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE:   Rendering 2D maps
COPYRIGHT: (C) 2020 Brendan Harmon
LICENSE:   This program is free software under the GNU General Public
           License (>=v2).
"""

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
    output=os.path.join(gisdbase, location, 'landcover_2014.png'),
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
