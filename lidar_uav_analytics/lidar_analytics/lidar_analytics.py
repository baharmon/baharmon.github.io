# -*- coding: utf-8 -*-

"""
@brief: Lidar point cloud interpolation and analysis
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

# set lidar directory
lidar_directory = os.path.normpath("C:/Users/Brendan/Documents/grassdata/")

# file
file = "mid_pines_spm_2013.las"
fullpath_filename = os.path.join(lidar_directory,file)

# set rendering directory
render = os.path.normpath("C:/Users/Brendan/Documents/grassdata/rendering/lidar_analytics")

"""binning"""
# set region
gscript.run_command('g.region', n=220218, s=218694, e=637795, w=636271, res=1, flags='a')

# binning multiple return density    
density = "density"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=density, method='n', overwrite=True)
gscript.run_command('r.colors', map=density, color="bcyr")
# render
info = gscript.parse_command('r.info', map=density, flags='g')
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,density+".png"), overwrite=True)
gscript.run_command('d.rast', map=density)
gscript.run_command('d.legend', raster=density, at=(5,50,5,7), flags='fsd')
gscript.run_command('d.mon', stop=driver)

# binning ground density        
density_ground = "density_ground"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=density_ground, class_filter=2, method='n', overwrite=True)
gscript.run_command('r.colors', map=density_ground, color="bcyr")
# render
info = gscript.parse_command('r.info', map=density_ground, flags='g')
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,density_ground+".png"), overwrite=True)
gscript.run_command('d.rast', map=density_ground)
gscript.run_command('d.legend', raster=density_ground, at=(5,50,5,7), flags='fsd')
gscript.run_command('d.mon', stop=driver)

# binning ground      
ground = "ground"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=ground, class_filter=2, method='mean', resolution=3, overwrite=True)
gscript.run_command('r.colors', map=ground, color="elevation")
# render
info = gscript.parse_command('r.info', map=ground, flags='g')
relief = "relief"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,ground+".png"), overwrite=True)
gscript.run_command('r.relief', input=ground, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=ground, color="elevation")
gscript.run_command('d.shade', shade=relief, color=ground, brighten=25)
gscript.run_command('d.legend', raster=ground, at=(5,50,5,7), flags='fsd')
gscript.run_command('d.mon', stop=driver)

# binning dsm    
binning_dsm = "binning_dsm"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=binning_dsm, class_filter=(1,2), method='max', resolution=3, overwrite=True)
gscript.run_command('r.colors', map=binning_dsm, color="elevation")
# render
info = gscript.parse_command('r.info', map=binning_dsm, flags='g')
relief = "relief"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,binning_dsm+".png"), overwrite=True)
gscript.run_command('r.relief', input=binning_dsm, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=binning_dsm, color="elevation")
gscript.run_command('d.shade', shade=relief, color=binning_dsm, brighten=25)
gscript.run_command('d.legend', raster=binning_dsm, at=(5,50,5,7), flags='fsd')
gscript.run_command('d.mon', stop=driver)

# binning last return   
last_return = "last_return"
gscript.run_command('r.in.lidar', input=fullpath_filename, output=last_return, class_filter=(1,2),  return_filter='last', method='mean', resolution=3, overwrite=True)
gscript.run_command('r.colors', map=last_return, color="elevation")
# render
info = gscript.parse_command('r.info', map=last_return, flags='g')
relief = "relief"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,last_return+".png"), overwrite=True)
gscript.run_command('r.relief', input=last_return, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=last_return, color="elevation")
gscript.run_command('d.shade', shade=relief, color=last_return, brighten=25)
gscript.run_command('d.legend', raster=last_return, at=(5,50,5,7), flags='fsd')
gscript.run_command('d.mon', stop=driver)

# classes
classes="classes"
gscript.run_command('r.mapcalc', expression="{classes} = if( ! isnull({last_return}), 2, if( !isnull({ground}), 1, if( !isnull({binning_dsm}),3, null())))".format(classes=classes, last_return=last_return, ground=ground, binning_dsm=binning_dsm), overwrite=True)
#render
info = gscript.parse_command('r.info', map=classes, flags='g')
relief = "relief"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,classes+".png"), overwrite=True)
gscript.run_command('r.relief', input=binning_dsm, output=relief, zscale=1, overwrite=True)
# color rules
rules = "lidar_classes.txt"
rules_path = os.path.join(lidar_directory,rules)
gscript.run_command('r.colors', map=classes, rules=rules_path)
gscript.run_command('d.shade', shade=relief, color=classes, brighten=25)
gscript.run_command('d.legend', raster=classes, at=(5,50,5,7), flags='fsd')
gscript.run_command('d.mon', stop=driver)


"""DEM interpolation"""
# set region
gscript.run_command('g.region', n=220218, s=218694, e=637795, w=636271, res=1)

# interpolation for ground points      
ground_points = "ground_points"
gscript.run_command('v.in.lidar', input=fullpath_filename, output=ground_points, class_filter=2, flags='trb', overwrite=True)
elevation = "dem"
slope = "dem_slope"
aspect = "dem_aspect"
gscript.run_command('v.surf.rst', input=ground_points, elevation=elevation, slope=slope, aspect=aspect, tension=20, smooth=1, npmin=80, dmin=0.3, overwrite=True)
gscript.run_command('r.colors', map=elevation, color="elevation")
# render elevation
info = gscript.parse_command('r.info', map=elevation, flags='g')
relief = "dem_relief"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,elevation+".png"), overwrite=True)
gscript.run_command('r.relief', input=elevation, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=elevation, color="elevation")
gscript.run_command('d.shade', shade=relief, color=elevation, brighten=25)
gscript.run_command('d.legend', raster=elevation, at=(5,50,5,7))
gscript.run_command('d.mon', stop=driver)
# render slope
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,slope+".png"), overwrite=True)
gscript.run_command('d.shade', shade=relief, color=slope, brighten=25)
gscript.run_command('d.legend', raster=slope, at=(5,50,5,7))
gscript.run_command('d.mon', stop=driver)
# render aspect
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,aspect+".png"), overwrite=True)
gscript.run_command('d.shade', shade=relief, color=aspect, brighten=25)
gscript.run_command('d.legend', raster=aspect, at=(5,50,5,7))
gscript.run_command('d.mon', stop=driver)

# water flow
#depth = "dem_depth"
#gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,depth+".png"), overwrite=True)
#gscript.run_command('r.slope.aspect', elevation=elevation, dx='dx', dy='dy', overwrite=True)
#gscript.run_command('r.sim.water', elevation=elevation, dx='dx', dy='dy', rain_value=155, depth=depth, man_value=0.3, nwalkers=10000, niterations=10, overwrite=True)
#gscript.run_command('g.remove', flags='f', type='raster', name=['dx', 'dy'])
#gscript.run_command('d.shade', shade=relief, color=depth, brighten=25)
#gscript.run_command('d.legend', raster=depth, at=(5,50,5,7))
#gscript.run_command('d.mon', stop=driver)

# skyview
skyview = "dem_skyview"
gscript.parse_command('r.skyview', input=elevation, output=skyview, overwrite=True)
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,skyview+".png"), overwrite=True)
gscript.run_command('d.rast', map=skyview)
gscript.run_command('d.mon', stop=driver)

# pca
pca = "dem_pca"
gscript.parse_command('r.shaded.pca', input=elevation, output=pca, zscale=100.0, overwrite=True)
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,pca+".png"), overwrite=True)
gscript.run_command('d.rast', map=pca)
gscript.run_command('d.mon', stop=driver)

# outliers
gscript.run_command('v.outlier', input=ground_points, output="dummy", outlier="dummy", flags='e')


"""DSM interpolation"""
# set region
gscript.run_command('g.region', n=220218, s=218694, e=637795, w=636271, res=0.3)

# interpolation for ground points      
dsm_points = "dsm_points"
gscript.run_command('v.in.lidar', input=fullpath_filename, output=dsm_points, class_filter=(1,2), return_filter="first", flags='trb', overwrite=True)
elevation = "dsm"
slope = "dsm_slope"
aspect = "dsm_aspect"
gscript.run_command('v.surf.rst', input=dsm_points, elevation=elevation, slope=slope, aspect=aspect, tension=20, smooth=1, npmin=80, dmin=0.3, overwrite=True)
gscript.run_command('r.colors', map=elevation, color="elevation")
# render elevation
info = gscript.parse_command('r.info', map=elevation, flags='g')
relief = "dsm_relief"
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,elevation+".png"), overwrite=True)
gscript.run_command('r.relief', input=elevation, output=relief, zscale=1, overwrite=True)
gscript.run_command('r.colors', map=elevation, color="elevation")
gscript.run_command('d.shade', shade=relief, color=elevation, brighten=25)
gscript.run_command('d.legend', raster=elevation, at=(5,50,5,7))
gscript.run_command('d.mon', stop=driver)
# render slope
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,slope+".png"), overwrite=True)
gscript.run_command('d.shade', shade=relief, color=slope, brighten=25)
gscript.run_command('d.legend', raster=slope, at=(5,50,5,7))
gscript.run_command('d.mon', stop=driver)
# render aspect
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,aspect+".png"), overwrite=True)
gscript.run_command('d.shade', shade=relief, color=aspect, brighten=25)
gscript.run_command('d.legend', raster=aspect, at=(5,50,5,7))
gscript.run_command('d.mon', stop=driver)

# water flow
#depth = "dsm_depth"
#gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,depth+".png"), overwrite=True)
#gscript.run_command('r.slope.aspect', elevation=elevation, dx='dx', dy='dy', overwrite=True)
#gscript.run_command('r.sim.water', elevation=elevation, dx='dx', dy='dy', rain_value=155, depth=depth, man_value=0.3, nwalkers=10000, niterations=10, overwrite=True)
#gscript.run_command('g.remove', flags='f', type='raster', name=['dx', 'dy'])
#gscript.run_command('d.shade', shade=relief, color=depth, brighten=25)
#gscript.run_command('d.legend', raster=depth, at=(5,50,5,7))
#gscript.run_command('d.mon', stop=driver)

# skyview
skyview = "dsm_skyview"
gscript.parse_command('r.skyview', input=elevation, output=skyview, overwrite=True)
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,skyview+".png"), overwrite=True)
gscript.run_command('d.rast', map=skyview)
gscript.run_command('d.mon', stop=driver)

# pca
pca = "dsm_pca"
gscript.parse_command('r.shaded.pca', input=elevation, output=pca, zscale=100.0, overwrite=True)
gscript.run_command('d.mon', start=driver, width=info.cols, height=info.rows, output=os.path.join(render,pca+".png"), overwrite=True)
gscript.run_command('d.rast', map=pca)
gscript.run_command('d.mon', stop=driver)