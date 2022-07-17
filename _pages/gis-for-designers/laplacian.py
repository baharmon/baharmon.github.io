#!/usr/bin/env python

"""
SCRIPT: laplacian.py
AUTHOR: Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Derive ridges and valleys from divergence in GRASS GIS
COPYRIGHT: GNU GPL (C) 2021 Brendan Harmon
"""

# import libraries
import grass.script as grass

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

    # set local variables
    elevation = 'elevation'
    laplacian = 'laplacian'
    ridges = 'ridges'
    valleys = 'valleys'
    threshold = 0.02

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

    # compute divergence
    compute_laplacian(elevation, laplacian)

    # derive ridges
    operator = '>='
    morphometric_features(ridges, laplacian, operator, threshold)

    # derive valleys
    operator = '<='
    threshold = -threshold
    morphometric_features(valleys, laplacian, operator, threshold)

    # extract vector ridges
    feature_extraction(ridges)

    # extract vector valleys
    feature_extraction(valleys)

    # render maps
    render_feature(ridges, valleys)

def compute_laplacian(elevation, laplacian):
    """calculate the divergence of the elevation gradient"""

    # calculate partial derivatives
    grass.run_command(
        'r.slope.aspect',
        elevation=elevation,
        dxx='dxx',
        dyy='dyy',
        overwrite=overwrite
        )

    # calculate laplacian
    grass.mapcalc(f"{laplacian} = dxx + dyy", overwrite=overwrite)

    # remove temporary maps
    grass.run_command(
        'g.remove',
        type='raster',
        name=['dxx','dyy'],
        flags='f',
        overwrite=overwrite
        )

def morphometric_features(feature, laplacian, operator, threshold):
    """derive morphometric features from the divergence"""

    # classify ridges from divergence
    grass.mapcalc(
        f"{feature} = if({laplacian} {operator} {threshold}, 1, null())",
        overwrite=overwrite
        )

def feature_extraction(feature):
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
        thres=50,
        overwrite=overwrite
        )

    # generalize
    grass.run_command(
        'v.generalize',
        input='cleaned',
        type='area',
        output='generalized',
        method='reumann',
        threshold=2,
        overwrite=overwrite
        )
    grass.run_command(
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
    grass.run_command(
        'g.remove',
        type='vector',
        name=['cleaned','generalized'],
        flags='f'
        )

def render_feature(ridges, valleys):
    """render morphometric maps"""

    # set image size
    extents = grass.parse_command(
        'g.region',
        flags='eg'
        )
    width = extents['ew_extent']
    height = extents['ns_extent']

    # write vector map to image file
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
            'laplacian_features.png'
            ),
        overwrite=overwrite
        )

    # display vector maps
    grass.run_command(
        'd.vect',
        map=ridges,
        color='none',
        fill_color=[0,0,0]
        )
    grass.run_command(
        'd.vect',
        map=valleys,
        color='none',
        fill_color=[125,125,125]
        )

    # add legend
    grass.run_command(
        'd.legend.vect',
        at=[4,20,2,4],
        font='segoeui',
        fontsize='18'
        )

    # close image file
    grass.run_command(
        'd.mon',
        stop="cairo"
        )


if __name__ == "__main__":
    main()
