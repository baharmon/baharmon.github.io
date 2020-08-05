---
title: Cartography in QGIS
subtitle:
description: Cartography in QGIS
featured_image: /images/natural-earth/natural-earth-europe.jpg
---

![The QGIS Interface](/images/natural-earth/natural-earth-europe.jpg)

**Contents**
* TOC
{:toc}

---

# Download Data

Graticules
https://www.naturalearthdata.com/downloads/50m-physical-vectors/50m-graticules/

---

# Azimuth Orthographic Projection

First set a predefined azimuth orthographic projection.
In the project menu, select properties.
In the properties dialog, select the CRS tab
and search for the `The_World_From_Space` projection.
Copy the well known text (WKT)
definition for this projection.
You will use it to make a custom projection
in the next step.

To set a custom azimuth orthographic projection
centered on your study area,
go to the settings menu
and select custom projection.
Use the plus button to create a new CRS,
name it `Custom_World_From_Space`,
set the format to WKT,
paste the WKT definition for the
`The_World_From_Space`,
and then edit it.
Adjust the latitude and longitude
of natural origin.
Remove `ID["ESRI",102038]` at the end of the definition,
but be sure to leave the final bracket
closing the definition.
Here is an example:
```
PROJCRS["Custom_World_From_Space",
    BASEGEOGCRS["GCS_Sphere_ARC_INFO",
        DATUM["D_Sphere_ARC_INFO",
            ELLIPSOID["Sphere_ARC_INFO",6370997,0,
                LENGTHUNIT["metre",1]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["Degree",0.0174532925199433]]],
    CONVERSION["The_World_From_Space",
        METHOD["Orthographic",
            ID["EPSG",9840]],
        PARAMETER["Latitude of natural origin",42.5333333333,
            ANGLEUNIT["Degree",0.0174532925199433],
            ID["EPSG",8801]],
        PARAMETER["Longitude of natural origin",0.0000000000,
            ANGLEUNIT["Degree",0.0174532925199433],
            ID["EPSG",8802]],
        PARAMETER["False easting",0,
            LENGTHUNIT["metre",1],
            ID["EPSG",8806]],
        PARAMETER["False northing",0,
            LENGTHUNIT["metre",1]]],
    CS[Cartesian,2],
        AXIS["(E)",east,
            ORDER[1],
            LENGTHUNIT["metre",1]],
        AXIS["(N)",north,
            ORDER[2],
            LENGTHUNIT["metre",1]],
    USAGE[
        SCOPE["unknown"],
        AREA["World"],
        BBOX[-90,-180,90,180]]]
```
Back in project properties in the CRS tab,
search for your new `Custom_World_From_Space` projection
and set it as the CRS.
Then in the custom CRS dialog,
try adjusting the Longitude of natural origin value
to rotate the globe until it centers on your study area.

Alternatively set the format to proj string
and enter the following parameters:
```
+proj=ortho +lat_0=42.5333333333 +lon_0=-0.53333333339999 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs
```
Adjust the latitude and longitude.


| Azimuth Orthographic Projection |
|:---:|
| ![Azimuth Orthographic Projection](/images/natural-earth/globe-wth-rivers.jpg) |


---

# Themes
...

---

# Extract a Continent

Extract by attribute
Input layer
ne_50m_admin_0_countries
Selection attribute: NAME
Value: Europe
Matching features:
ogr:dbname='D:/gisdata/natural_earth/natural_earth.gpkg' table="europe" (geom)

---

# Print Layout

Maps with different themes

Custom CRS
For the inset map of the globe
set your custom coordinate reference system (CRS).
In the item properties panel
set the CRS to `Custom_World_From_Space`.

For the main map,
set a coordinate reference system such as
`world_robinson`
in the item properties panel.

Scale bar
style numeric

<i class="ms ms-map"></i>
<i class="ms ms-globe"></i>

| Rivers of Europe |
|:---:|
| ![Rivers of Europe](/images/natural-earth/rivers-of-europe.jpg) |

| Natural Earth Map of Europe |
|:---:|
| ![Natural Earth Map of Europe](/images/natural-earth/natural-earth-europe.jpg) |
