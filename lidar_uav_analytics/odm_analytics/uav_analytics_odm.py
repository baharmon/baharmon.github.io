# -*- coding: utf-8 -*-

"""
@brief: UAV point cloud interpolation and analysis
This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.
@author: Brendan Harmon (brendanharmon@gmail.com)
"""

import os
import grass.script as gscript

# temporary region
gscript.use_temp_region()

# set graphics driver
driver = "cairo"

# set odm directory
odm_directory = os.path.normpath("C:/Users/Brendan/odm/data/reconstruction-with-image-size-2400-results")

# file
file = "pointcloud_georef.las"
fullpath_filename = os.path.join(odm_directory,file)

# set rendering directory
render = os.path.normpath("C:/Users/Brendan/Documents/grassdata/rendering/odm_analytics")

# set region
gscript.run_command('g.region', res=0.3)
        
# binning         
binning = "overview_odm"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=binning, overwrite=True)
gscript.run_command('r.colors', map=binning, color="elevation")
# render
info = gscript.parse_command('r.info', map=binning, flags='g')
relief = "relief_odm"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,binning+".png"), overwrite=True)
gscript.run_command('r.relief', input=binning, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=binning, color="elevation")
gscript.run_command('d.shade', shade=relief, color=binning, brighten=25)
gscript.run_command('d.legend', raster=binning)
gscript.run_command('d.mon', stop=driver)

# set region
gscript.run_command('g.region', n=219540, s=219440, e=637220, w=637120, res=0.3)
        
# binning         
binning = "binning_odm"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=binning, overwrite=True)
gscript.run_command('r.colors', map=binning, color="elevation")
# render
info = gscript.parse_command('r.info', map=binning, flags='g')
relief = "relief_odm"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,binning+".png"), overwrite=True)
gscript.run_command('r.relief', input=binning, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=binning, color="elevation")
gscript.run_command('d.shade', shade=relief, color=binning, brighten=25)
gscript.run_command('d.legend', raster=binning)
gscript.run_command('d.mon', stop=driver)

# set region
gscript.run_command('g.region', n=219540, s=219440, e=637220, w=637120, res=0.3)

# interpolation        
points = "points_odm"
gscript.run_command('v.in.lidar', input=fullpath_filename, output=points, flags='trb', overwrite=True)
elevation = "elevation_odm"
slope = "slope_odm"
aspect = "aspect_odm"
gscript.run_command('v.surf.rst', input=points, elevation=elevation, slope=slope, aspect=aspect, tension=40, smooth=1, dmin=0.3, overwrite=True)
gscript.run_command('r.colors', map=elevation, color="elevation")
# render elevation
info = gscript.parse_command('r.info', map=elevation, flags='g')
relief = "relief_odm"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,elevation+".png"), overwrite=True)
gscript.run_command('r.relief', input=elevation, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=elevation, color="elevation")
gscript.run_command('d.shade', shade=relief, color=elevation, brighten=25)
gscript.run_command('d.legend', raster=elevation)
gscript.run_command('d.mon', stop=driver)
# render slope
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,slope+".png"), overwrite=True)
gscript.run_command('d.shade', shade=relief, color=slope, brighten=25)
gscript.run_command('d.legend', raster=slope)
gscript.run_command('d.mon', stop=driver)
# render aspect
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,aspect+".png"), overwrite=True)
gscript.run_command('d.shade', shade=relief, color=aspect, brighten=25)
gscript.run_command('d.legend', raster=aspect)
gscript.run_command('d.mon', stop=driver)

# water flow
depth = "depth_odm"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,depth+".png"), overwrite=True)
gscript.run_command('r.slope.aspect', elevation=elevation, dx='dx', dy='dy', overwrite=True)
gscript.run_command('r.sim.water', elevation=elevation, dx='dx', dy='dy', rain_value=155, depth=depth, man_value=0.3, nwalkers=10000, niterations=10, overwrite=True)
gscript.run_command('g.remove', flags='f', type='raster', name=['dx', 'dy'])
gscript.run_command('d.shade', shade=relief, color=depth, brighten=25)
gscript.run_command('d.legend', raster=depth)
gscript.run_command('d.mon', stop=driver)

# skyview
skyview = "skyview_odm"
gscript.parse_command('r.skyview', input=elevation, output=skyview, overwrite=True)
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,skyview+".png"), overwrite=True)
gscript.run_command('d.rast', map=skyview)
gscript.run_command('d.mon', stop=driver)

# pca
pca = "pca_odm"
gscript.parse_command('r.shaded.pca', input=elevation, output=pca, zscale=100.0, overwrite=True)
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,pca+".png"), overwrite=True)
gscript.run_command('d.rast', map=pca)
gscript.run_command('d.mon', stop=driver)
