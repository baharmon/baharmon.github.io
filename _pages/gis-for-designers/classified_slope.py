#!/usr/bin/env python

"""
SCRIPT: classified_slope.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Compute classified slope map in GRASS GIS
COPYRIGHT: GNU GPL (C) 2021 Brendan Harmon
"""

# import libraries
import os
import atexit
import grass.script as gscript
from grass.exceptions import CalledModuleError

# settings
gscript.use_temp_region()
env = gscript.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']

reclass = """\
0 thru 5 = 1
5 thru 10 = 2
10 thru 90 = 3
"""

categories = """\
1|Gentle
2|Moderate
3|Steep
"""

# set region
gscript.run_command(
    'g.region',
    n=189782,
    s=188996,
    e=978180,
    w=977573,
    res=1,
    save='ridges',
    overwrite=overwrite
    )

# smooth terrain
gscript.run_command(
    'r.neighbors',
    input='elevation_2017',
    output='elevation',
    size=15,
    flags='c',
    overwrite=overwrite
    )

# compute slope
gscript.run_command(
    'r.slope.aspect',
    elevation='elevation',
    slope='slope',
    format='degrees',
    flags='e',
    overwrite=overwrite
    )

# reclassify slope
gscript.write_command(
    'r.reclass',
    input='slope',
    output='slope_classes',
    rules='-',
    stdin=reclass,
    overwrite=overwrite
    )

# set slope categories
gscript.write_command(
    'r.category',
    map='slope_classes',
    separator='pipe',
    rules='-',
    stdin=categories,
    overwrite=overwrite
    )

# set color table
gscript.run_command(
    'r.colors',
    map='slope_classes',
    color='viridis',
    overwrite=overwrite
    )

# compute shaded relief
gscript.run_command(
    'r.relief',
    input='elevation',
    output='relief',
    zscale='2',
    units='survey',
    overwrite=overwrite
    )

# set image size
extents = gscript.parse_command(
    'g.region',
    flags='eg'
    )
width = extents['ew_extent']
height = extents['ns_extent']

# start writing image file
gscript.run_command(
    'd.mon',
    start="cairo",
    width=width,
    height=height,
    resolution=2,
    bgcolor='none',
    output=os.path.join(
        gisdbase,
        location,
        'classified_slope.png'
        ),
    overwrite=overwrite
    )

# overlay slope with shaded relief
gscript.run_command(
    'd.shade',
    shade='relief',
    color='slope_classes',
    brighten=75,
    overwrite=overwrite
    )

# add legend
gscript.run_command(
    'd.legend',
    raster='slope_classes',
    at=[4,20,2,4],
    font='segoeui',
    fontsize='18',
    flags='c'
    )

# close image file
gscript.run_command(
    'd.mon',
    stop="cairo"
    )
