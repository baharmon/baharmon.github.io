#!/usr/bin/env python3

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

# list rasters
raster_list  = gscript.list_grouped('rast', pattern='shaded_*')[mapset]

for raster in raster_list:
    gscript.run_command('d.mon',
        start="cairo",
        width=1000,
        height=1000,
        output=os.path.join(gisdbase, location, raster+'.png'),
        overwrite=overwrite)
    gscript.run_command('d.rast', map=raster)
    gscript.run_command('d.mon', stop="cairo")
