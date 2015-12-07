# -*- coding: utf-8 -*-

"""
@brief: script for fusing low and high resolution digital elevation models and simulating water flow
This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.
@author: Brendan Harmon (brendanharmon@gmail.com)
"""

import grass.script as gscript

def main():
    
    # temporary region
    gscript.use_temp_region()
        
    # set parameters
    overwrite = True
    rain_value = 50.
    man_value = 0.05
    niterations = 25
    nwalkers = 40000
    mapset = "fusion"

    # assign variables
    elevation = "fusion"
    depth="depth"
    dx = "dx"
    dy = "dy"

    # set temporal parameters
    temporaltype='relative'
    strds='depth_timeseries'
    title="depth_timeseries"
    description="timeseries of depth maps"
    
    # assign temporal variables
    datatype='strds'
    increment=str(niterations)+" minutes"
    raster='raster'
  
    # water flow
    gscript.run_command('g.region', raster=elevation, res=1)
    gscript.run_command('r.sim.water', elevation=elevation, dx=dx, dy=dy, rain_value=rain_value, depth=depth, man_value=man_value, nwalkers=nwalkers, niterations=niterations, flags ="t", overwrite=overwrite)

    # create a raster space time dataset
    gscript.run_command('t.create', type=datatype, temporaltype=temporaltype, output=strds, title=title, description=description, overwrite=overwrite)
    
    # list rasters
    timeseries = gscript.list_grouped('rast', pattern="depth.*")[mapset]

    # register the rasters
    gscript.run_command('t.register', type=raster, input=strds, maps=timeseries, increment=increment, overwrite=overwrite)

    # g.gui.animation strds=depth_timeseries

if __name__ == "__main__":
    main()



        