#!/usr/bin/env python

"""
SCRIPT: geomorphometry.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Geomorphometric analysis of terrain
COPYRIGHT: GNU GPL (C) 2021 Brendan Harmon
"""

# import libraries
import os
import atexit
import grass.script as grass
from grass.exceptions import CalledModuleError

# settings
grass.use_temp_region()
env = grass.gisenv()
overwrite = True
env['GRASS_OVERWRITE'] = overwrite
env['GRASS_VERBOSE'] = False
env['GRASS_MESSAGE_FORMAT'] = 'standard'
gisdbase = env['GISDBASE']
location = env['LOCATION_NAME']
mapset = env['MAPSET']

def main():

    # set region
    grass.run_command(
        'g.region',
        n=189782,
        s=188996,
        e=978180,
        w=977573,
        res=1,
        save='ridges',
        overwrite=overwrite
        )

    morphometric_parameters()
    morphometric_features()
    rendering()

def morphometric_parameters():
    """compute morphometric parameters for digital elevation model"""

    # smooth terrain
    grass.run_command(
        'r.neighbors',
        input='elevation_2017',
        output='elevation',
        size=15,
        flags='c',
        overwrite=overwrite
        )

    # compute shaded relief
    grass.run_command(
        'r.relief',
        input='elevation',
        output='relief',
        zscale=2,
        units='survey',
        overwrite=overwrite
        )

    # compute skyview
    grass.run_command(
        'r.skyview',
        input='elevation',
        output='skyview',
        ndir=16,
        overwrite=overwrite
        )

    # compute morphometric parameters
    grass.run_command(
        'r.slope.aspect',
        elevation='elevation',
        slope='slope',
        aspect='aspect',
        pcurvature='pcurvature',
        tcurvature='tcurvature',
        dx='dx',
        dy='dy',
        dxx='dxx',
        dyy='dyy',
        dxy='dxy',
        format='degrees',
        overwrite=overwrite
        )

    # compute laplacian
    grass.mapcalc("laplacian = dxx + dyy", overwrite=overwrite)

    # set color tables
    grass.run_command(
        'r.colors',
        map=['dx', 'dy', 'dxx', 'dyy', 'dxy', 'laplacian'],
        color='viridis',
        flags='e')

def morphometric_features():
    """classify and extract morphometric features"""

    # classify ridges from divergence
    feature = 'laplacian_ridges'
    grass.mapcalc(f"{feature} = if(laplacian >= 0.025, 1, null())",
        overwrite=overwrite
        )
    feature_extraction(feature, 75, 2)

    # classify valleys from divergence
    feature = 'laplacian_valleys'
    grass.mapcalc(f"{feature} = if(laplacian <= -0.025, 1, null())",
        overwrite=overwrite
        )
    feature_extraction(feature, 75, 2)

    # classify morphometric features from convergence index
    feature = 'ci_ridges'
    try:
        grass.run_command(
            'g.extension',
            extension='r.convergence')
    except CalledModuleError:
        pass
    grass.run_command(
        'r.convergence',
        input='elevation',
        output='convergence',
        window=15,
        weights='standard',
        flags='c',
        overwrite=overwrite
        )
    grass.mapcalc(f"{feature} = if(convergence <= -15, 1, null())",
        overwrite=overwrite
        )
    feature_extraction(feature, 75, 2)

    # classify morphometric features from concavity and convexity
    feature = 'convex_ridges'
    grass.run_command(
        'r.param.scale',
        input='elevation',
        output='features',
        method='feature',
        size=15,
        overwrite=overwrite
        )
    grass.mapcalc(f"{feature} = if(features == 5, 1, null())",
        overwrite=overwrite
        )
    feature_extraction(feature, 75, 2)

    # classify morphometric features from geomorphons
    feature = 'geomorphon_ridges'
    grass.run_command(
        'r.geomorphon',
        elevation='elevation',
        forms='landforms',
        search=36,
        skip=6,
        flat=12,
        overwrite=overwrite
        )
    grass.mapcalc(f"{feature} = if(landforms == 3, 1, null())",
        overwrite=overwrite
        )
    feature_extraction(feature, 10, 2)

def feature_extraction(feature, clean, generalize):
    """extract morphometric features as vector maps"""

    # extract
    grass.run_command(
        'r.to.vect',
        input=feature,
        output=feature,
        type='area',
        flags='s',
        overwrite=overwrite
        )

    # clean
    grass.run_command(
        'v.clean',
        input=feature,
        output='cleaned',
        type='point,line,area',
        tool='rmarea',
        thres=clean,
        overwrite=overwrite
        )

    # generalize
    grass.run_command(
        'v.generalize',
        input='cleaned',
        type='area',
        output='generalized',
        method='reumann',
        threshold=generalize,
        overwrite=overwrite
        )
    grass.run_command(
        'v.generalize',
        input='generalized',
        type='area',
        output=feature,
        method='snakes',
        threshold=generalize,
        alpha=1,
        beta=1,
        overwrite=overwrite
        )

    # remove temporary maps
    grass.run_command(
        'g.remove',
        type='vector',
        name=['cleaned','generalized'],
        flags='f',
        overwrite=overwrite
        )

def rendering():
    """render morphometric maps"""

    # set image size
    extents = grass.parse_command(
        'g.region',
        flags='eg'
        )
    width = extents['ew_extent']
    height = extents['ns_extent']

    # list rasters in mapset
    raster_list = grass.list_grouped('rast', pattern='*')[mapset]

    # write rasters to image file
    for raster in raster_list:
        if raster != 'relief':
            grass.run_command(
                'd.mon',
                start="cairo",
                width=width,
                height=height,
                resolution=2,
                bgcolor='none',
                output=os.path.join(
                    gisdbase,
                    location,
                    raster+'.png'
                    ),
                overwrite=overwrite
                )
            if raster == 'aspect':
                grass.run_command(
                    'd.rast',
                    map=raster
                    )
            else:
                grass.run_command(
                    'd.shade',
                    shade='skyview',
                    color=raster,
                    brighten=36
                    )
                grass.run_command(
                    'd.legend',
                    raster=raster,
                    at=[4,30,2,4],
                    font='segoeui',
                    fontsize='18'
                    )
            grass.run_command(
                'd.mon',
                stop="cairo"
                )

    # list vector maps in mapset
    vector_list = grass.list_grouped('vect',pattern='*')[mapset]

    # write vector maps to image file
    for vector in vector_list:
        grass.run_command(
            'd.mon',
            start="cairo",
            width=width,
            height=height,
            resolution=2,
            bgcolor='none',
            output=os.path.join(
                gisdbase,
                location,
                vector+'.png'
                ),
            overwrite=overwrite
            )
        grass.run_command(
            'd.vect',
            map=vector,
            color='none',
            fill_color=[0,0,0]
            )
        grass.run_command(
            'd.mon',
            stop="cairo"
            )

if __name__ == "__main__":
    main()
