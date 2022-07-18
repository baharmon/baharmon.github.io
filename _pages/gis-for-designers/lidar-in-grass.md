---
title: Lidar in GRASS GIS
subtitle: A tutorial on lidar in GRASS GIS.
description: A tutorial on lidar in GRASS GIS.
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/
usemathjax: true
---

![Lidar](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/)

**Contents**
* TOC
{:toc}



## Lidar

What is lidar?

Download tiles of lidar from:
https://orthos.dhses.ny.gov/
Zoom in on Governor's island
and then click the download icon.
From the Lidar results tab
download the following lidar tiles from 2017:

NYC_TopoBathymetric2017_LiDAR

* 975187.las
* 975190.las
* 977187.las
* 977190.las
* 980187.las
* 980190.las

USGS_NYC2014_LIDAR

* 18TWL820030.las
* 18TWL820045.las
* 18TWL835030.las
* 18TWL835045.las

## Point Data Abstraction Library

[Point Data Abstraction Library](https://pdal.io/)

Install Anaconda

Install PDAL

On Windows right click on the `Anaconda3` prompt
and run as Administrator
```
conda update conda
conda install -c conda-forge pdal
conda install -c conda-forge pdal python-pdal gdal
```

[r.in.pdal](https://grass.osgeo.org/grass-stable/manuals/addons/r.in.pdal.html)

```
g.extension extension=r.in.pdal
```


## Binning Lidar

Start GRASS GIS
in the `nyspf_govenors_island` location
in a new mapset called `lidar`.

```
r.in.pdal input=D:\nyc\lidar_2017\975187.las output=binned_2017
```





```
g.region n=189850 s=189100 e=978550 w=976850 save=landforms
r.mask vector=shoreline
```

Import all 2017 tiles

Then set region to landforms and reimport

| Binned Lidar |
|:---:|
| ![Binned Lidar](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/governors-island/binned-elevation.png) |

## Interpolating Lidar


## Volumetric Change

Later in digital fabrication chapter
3D print difference in 2014 and 2017?  
