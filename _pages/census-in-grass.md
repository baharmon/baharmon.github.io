---
title: Census Data in GRASS GIS
subtitle: Census Data in GRASS GIS
description: A guide to importing and mapping census data in GRASS GIS.
featured_image: /images/nyc/population-normal-choropleth-inferno.png
---

![Population choropleth](/images/nyc/population-normal-choropleth-inferno.png)

**Contents**
* TOC
{:toc}

---

## Census Data

Every 10 years the US Census Bureau conducts a census
collecting demographic information from US residents
and publishes aggregated statistics.
In addition to the
[decennial census](https://www.census.gov/programs-surveys/decennial-census/2020-census.html),
the US Census Bureau also conducts the
[American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs/)
collecting more detailed information
from a sample of the population every month.
To protect people's privacy
only aggregated statistical data is published.
Census data is aggregated for geographic regions at scales ranging from
the nation to states to counties to tracts to block groups to blocks.
Use data from the American Community Survey
to map the estimated population of each census tract
in New York City.

---

## Download Census Data

To find and download tabular data from the US Census Bureau go to
[data.census.gov](https://data.census.gov/).
Search for the survey
`ACS Demographic and Housing Estimates`
or table `DP05`.
Select the table `DP05`.
Select the product `2018: ACS 5-Year Estimates Data Profiles`.
Only the 5-year estimates have census tract and block group level data.
Click customize table.
Set `Geos` to select a geographic region and level of detail.
Select `Tract`, within `New York` state,
all census tracts within `New York`
Then Download the table as a `csv` for 2018.

```
Survey: ACS DEMOGRAPHIC AND HOUSING ESTIMATES
Survey: ACS
Table ID: DP05
Product: 2018: ACS 5-Year Estimates Data Profiles
Geo:
Geography: Tract
Tract: New York
Within: all census tracts within New York
Download as csv
```
Edit the `.csv` table in a spreadsheet program
such as Excel or [LibreOffice Calc](https://www.libreoffice.org/).
Delete the second row that describes each column,
then use find and replace to remove
the prefix `1400000US` from the first column with GEO_IDs.
Since deleting all unneeded columns will dramatically improve performance,
delete all columns except for GEO_ID, NAME,
and `DP05_0033E` with total population estimates.
Save the table as [population.csv](/data/population.csv).

To be mapped the tabular demographic data from the census
needs to be joined to geospatial data for the appropriate geographic regions,
in this case the census tracts for New York.
The Topologically Integrated Geographic Encoding and Referencing (Tiger/Line)
database contains spatial data for
roads, rail, buildings, hydrography, and geographic regions in the US
including census tracts and block groups.
Find and download the TIGER/Line shapefile for the census tracts in New York
at https://www.census.gov/cgi-bin/geo/shapefiles/index.php.
Set the year to 2018, layer type to census tracts, and state to New York.
Download and extract `tl_2018_36_tract.zip`.
The tables with demographic data and the census tract shapefiles
share geographic entity codes (GEOIDs) that can be used to join them.

To limit the study to New York City,
download and extract
[borough boundaries](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm)
from [NYC Open Data](https://opendata.cityofnewyork.us/).
---

## Importing Census Data

This tutorial uses the
[Governor's Island Dataset for GRASS GIS](https://zenodo.org/record/3940780/files/nyspf_govenors_island.zip?download=1).
Download, extract, and move this geospatial dataset
for Governor's Island in New York City
to your `grassdata` directory.
Start <i class="ms ms-grass-gis"></i> GRASS GIS,
set the GRASS GIS database directory to `grassdata` directory,
set the location to `nyspf_govenors_island`,
and create a new mapset called `census`.
Alternatively you can create a new GRASS location
for New York Long Island State Plane Feet
either using the EPSG code 2263
or based on the georeferenced file `nybb.shp`
from the borough boundaries.

First import and reproject the census tract boundaries for the state of New York
with [v.import]().

clip to borough boundaries
https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm


Joining may take a very long time
if you do not first delete unnecessary rows and columns.

```
v.import input=D:\nyc\census\tl_2018_36_tract\tl_2018_36_tract.shp layer=tl_2018_36_tract output=nyc_census_tracts

v.in.ogr input=D:\nyc\census\nybb_20c\nybb.shp output=boroughs

v.clip input=nyc_census_tracts clip=boroughs output=census_tracts

db.in.ogr input=D:\nyc\census\ACSDP5Y2018.DP05_2020-11-12T121457\population.csv output=population

v.db.join map=census_tracts column=GEOID other_table=population other_column=GEO_ID

v.db.addcolumn map=census_tracts columns="population INT"

v.db.update map=census_tracts column=population query_column=DP05_0033E where="DP05_0033E >= 0"

v.colors map=census_tracts@demo use=attr column=population color=viridis

```

---

## Choropleth Map
Choropleth

[d.vect.thematic](https://grass.osgeo.org/grass78/manuals/d.vect.thematic.html)


```
d.vect.thematic -l --overwrite map=census_tracts column=population algorithm=equ nclasses=9 colors=68:1:84,71:44:122,59:81:139,44:113:142,33:144:141,39:173:129,92:200:99,170:220:50,253:231:37 boundary_color=none legend_title=Population

d.legend.vect at=2,98 font=Lato-Regular fontsize=14 sub_font=Lato-Bold sub_fontsize=16

d.vect.chart map=census_tracts chart_type=bar columns=population size_column=population size=1 scale=0.04
```
Try quantile instead of normal distribution with `algorithm=qua`

| Population Choropleth |
|:---:|
| ![Population choropleth](/images/nyc/population-normal-choropleth.png) |

Inferno
```
d.vect.thematic -l --overwrite map=census_tracts column=population algorithm=equ nclasses=9 colors=0:0:4,31:12:72,85:15:109,136:34:106,168:54:85,227:89:51,249:149:10,249:201:50,252:255:164 boundary_color=none legend_title=Population
```

| Population Choropleth |
|:---:|
| ![Population choropleth](/images/nyc/population-normal-choropleth-inferno.png) |





Export PDF with
```
d.legend.vect at=1,98 font=Lato-Light fontsize=48 sub_font=Lato-Medium output=D:\grassdata\nyspf_govenors_island\population_legend.csv --overwrite

d.legend.vect at=1,98 font=Lato-Light fontsize=48 sub_font=Lato-Medium input=D:\grassdata\nyspf_govenors_island\population_legend.csv --overwrite
```

Save and then print workspace
```
m.printws --overwrite input=D:\grassdata\nyspf_govenors_island\population.gxw dpi=300 output=D:\grassdata\nyspf_govenors_island\population_choropleth page=Flexi
```

[Population choropleth](/images/nyc/population-choropleth.pdf)





---

## Hexagonal Binning Map

Set the computational region to the map of census tracts


Hexagonal binned (hexbin) map

Create a hexagonal grid with v.mk.grid

[v.mkgrid](https://grass.osgeo.org/grass78/manuals/v.mkgrid.html)

[v.select](https://grass.osgeo.org/grass78/manuals/v.select.html)

[v.rast.stats](https://grass.osgeo.org/grass78/manuals/v.rast.stats.html)

```
g.region vector=census_tracts res=100
v.to.rast input=census_tracts output=population use=attr attribute_column=population
v.mkgrid -h map=grid box=1000,1000
v.select ainput=grid binput=boroughs output=hexagons operator=intersects
v.rast.stats -c map=hexagons raster=population column_prefix=population
d.vect.thematic -l --overwrite map=hexagons column=population_maximum algorithm=equ nclasses=9 colors=68:1:84,71:44:122,59:81:139,44:113:142,33:144:141,39:173:129,92:200:99,170:220:50,253:231:37 boundary_color=none legend_title=Population
d.legend.vect at=2,98 font=Lato-Regular fontsize=14 sub_font=Lato-Bold sub_fontsize=16
```

| Hexagonal Binning of Population |
|:---:|
| ![Hexagonal Binning of Population](/images/nyc/population-hexbin.png) |

Export PDF with
```
d.legend.vect at=1,98 font=Lato-Light fontsize=48 sub_font=Lato-Medium output=D:\grassdata\nyspf_govenors_island\population_legend.csv --overwrite

d.legend.vect at=1,98 font=Lato-Light fontsize=48 sub_font=Lato-Medium input=D:\grassdata\nyspf_govenors_island\population_legend.csv --overwrite
```

Save and then print workspace
```
m.printws --overwrite input=D:\grassdata\nyspf_govenors_island\population.gxw dpi=300 output=D:\grassdata\nyspf_govenors_island\population_hexbin page=Flexi
```
[Hexagonal Binning of Population](/images/nyc/population-hexbin.pdf)
