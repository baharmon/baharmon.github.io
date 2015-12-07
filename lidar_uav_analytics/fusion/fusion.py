# -*- coding: utf-8 -*-

"""
@brief: script for fusing low and high resolution digital elevation models and simulating water flow
This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.
@author: Brendan Harmon (brendanharmon@gmail.com)
"""

import os
import grass.script as gscript

def main():
    
    # temporary region
    gscript.use_temp_region()
    
    # set graphics driver
    driver = "cairo"
    
    # set rendering directory
    render = os.path.normpath("C:/Users/Brendan/Documents/grassdata/rendering/fusion")
    
    # set maps
    highres_dem = "uav_dsm@fusion"
    lowres_dem = "lidar_dem@fusion"
    
    # set parameters
    overwrite = True
    tension = 20
    smooth = 1
    npmin = 80
    dmin = 0.3
    
    # assign variables
    highres_sample = "highres_sample"
    lowres_sample = "lowres_sample"
    cover = "cover"
    fused_points="fused_points"
    fusion = "fusion"
    dx = "dx"
    dy = "dy"
    
    # set parameters for resampling
    info = gscript.raster_info(highres_dem)
    highres_npoints = int(info.cols) * int(info.rows) / 10
    info = gscript.raster_info(lowres_dem)
    lowres_npoints = int(info.cols) * int(info.rows) / 10
    
    # randomly sample high resolution dem
    gscript.run_command('g.region', raster=highres_dem)
    gscript.run_command('r.random', input=highres_dem, npoints=highres_npoints, vector=highres_sample, flags='d', overwrite=overwrite)
    
    # set cover map
    gscript.run_command('g.region', raster=lowres_dem)
    gscript.run_command('r.mapcalc', expression="{cover} = if(isnull({highres_dem}),{lowres_dem},null())".format(cover=cover, lowres_dem=lowres_dem, highres_dem=highres_dem), overwrite=overwrite)
    
    # randomly sample low resolution dem
    gscript.run_command('g.region', raster=lowres_dem)
    gscript.run_command('r.random', input=lowres_dem, npoints=lowres_npoints, cover=cover, vector=lowres_sample, flags='d', overwrite=overwrite)
    
    # patch
    gscript.run_command('v.patch', input=(highres_sample,lowres_sample), output=fused_points ,flags='b', overwrite=overwrite)
    
    # interpolation with partial derivatives
    gscript.run_command('v.surf.rst', input=fused_points, elevation=fusion, slope=dx, aspect=dy, tension=tension, smooth=smooth, npmin=npmin, dmin=dmin, flags='d', overwrite=overwrite)
    gscript.run_command('r.colors', map=fusion, color="elevation")
    
    # render elevation
    gscript.run_command('g.region', raster=lowres_dem)
    info = gscript.parse_command('r.info', map=fusion, flags='g')
    relief = "relief"
    gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,fusion+".png"), overwrite=overwrite)
    gscript.run_command('r.relief', input=fusion, output=relief, zscale=1, overwrite=overwrite)
    gscript.run_command('r.colors', map=fusion, color="elevation")
    gscript.run_command('d.shade', shade=relief, color=fusion, brighten=25)
    gscript.run_command('d.legend', raster=fusion, at=(5,50,5,7))
    gscript.run_command('d.mon', stop=driver)
    
    # remove temporary maps
    gscript.run_command('g.remove', type='vector', name=['highres_sample', 'lowres_sample', 'fused_points'], flags='f')
    gscript.run_command('g.remove', type='raster', name='cover', flags='f') 
    

if __name__ == "__main__":
    main()



        