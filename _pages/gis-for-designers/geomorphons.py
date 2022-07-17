#!/usr/bin/env python

"""
SCRIPT: geomorphons.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Derive ridges and valleys from geomorphons in GRASS GIS
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

# classify morphometric features from geomorphons
gscript.run_command(
    'r.geomorphon',
    elevation='elevation',
    forms='landforms',
    search=36,
    skip=6,
    flat=12,
    overwrite=overwrite
    )

# extract ridges and valleys
gscript.mapcalc(f"ridges = if(landforms == 2 || landforms == 3, 1, null())",
    overwrite=overwrite
    )
gscript.mapcalc(f"valleys = if(landforms == 9 || landforms == 10, 1, null())",
    overwrite=overwrite
    )

landforms=['ridges', 'valleys']
for feature in landforms:

    # extract
    gscript.run_command(
        'r.to.vect',
        input=feature,
        output=feature,
        type='area',
        flags='s',
        overwrite=overwrite
        )

    # clean
    gscript.run_command(
        'v.clean',
        input=feature,
        output='cleaned',
        type='point,line,area',
        tool='rmarea',
        thres=10,
        overwrite=overwrite
        )

    # generalize
    gscript.run_command(
        'v.generalize',
        input='cleaned',
        type='area',
        output='generalized',
        method='reumann',
        threshold=2,
        overwrite=overwrite
        )
    gscript.run_command(
        'v.generalize',
        input='generalized',
        type='area',
        output=feature,
        method='snakes',
        threshold=2,
        alpha=1,
        beta=1,
        overwrite=overwrite
        )

    # remove temporary maps
    gscript.run_command(
        'g.remove',
        type='vector',
        name=['cleaned','generalized'],
        flags='f',
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
        'geomorphon_features.png'
        ),
    overwrite=overwrite
    )

# display vector maps
gscript.run_command(
    'd.vect',
    map='ridges',
    color='none',
    fill_color=[0,0,0]
    )
gscript.run_command(
    'd.vect',
    map='valleys',
    color='none',
    fill_color=[125,125,125]
    )

# add legend
gscript.run_command(
    'd.legend.vect',
    at=[4,20,2,4],
    font='segoeui',
    fontsize='18'
    )

# close image file
gscript.run_command(
    'd.mon',
    stop="cairo"
    )
