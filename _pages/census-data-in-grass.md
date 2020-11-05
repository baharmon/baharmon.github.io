---
title: Census Data in GRASS GIS
subtitle:
description: A guide to importing and mapping census data in GRASS GIS.
featured_image:
---

![](/images/)

**Contents**
* TOC
{:toc}

---

### Download Census Data

To find and download data from the US Census Bureau go to
[data.census.gov](https://data.census.gov/).
Search for "New York City, New York".

Customize table

Survey: ACS DEMOGRAPHIC AND HOUSING ESTIMATES
Survey: ACS
Table ID: DP05
Product: 2018: ACS 5-Year Estimates Data Profiles
Geo:
  Geography: Tract
  Tract: New York
  Within: all census tracts within New York
Download as csv


[New York City Profile](https://data.census.gov/cedsci/profile?g=1600000US3651000)

https://www.census.gov/programs-surveys/acs/

TIGER/Line shapefiles
https://www.census.gov/cgi-bin/geo/shapefiles/index.php
Year: 2018
Layer type: Census Tract
Submit
State: New York
tl_2018_36_tract.zip



---

### Importing Census Data


Create new location for nyspf using epsg code or boundary shp
or use nyspf_govenors_island

clip to borough boundaries
https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm
https://data.cityofnewyork.us/City-Government/Borough-Boundaries-Water-Areas-Included-/tv64-9x69


In Excel or LibreOffice Calc
first
Remove 2nd row
then
Remove
1400000US
from all GEO_IDs



```
v.import input=tl_2018_36_tract.shp layer=tl_2018_36_tract output=census_tracts

v.in.ogr input=nybb.shp output=boroughs


v.clip input=census_tracts clip=boroughs output=nyc_census_tracts

g.rename --overwrite vector=nyc_census_tracts@PERMANENT,census_tracts

db.in.ogr input=ACSDP5Y2018.DP05_data_with_overlays_2020-11-02T125050.csv output=population

v.db.join map=census_tracts column=GEOID other_table=population other_column=GEO_ID

v.db.addcolumn map=census_tracts columns="population INT"

v.db.update map=census_tracts column=population query_column=B00001_001E where="B00001_001E >= 0"

v.colors map=census_tracts use=attr color=viridis
```





Color by attribute:
population
income
number of ethnicities

### Choropleth Map
Choropleth
```
d.vect.thematic -l --overwrite map=census_tracts column=population algorithm=equ nclasses=3 colors=64:0:128:255,128:0:255:255,128:128:255:255 boundary_color=none legend_title=Population

d.legend.vect at=2,98 font=Lato-Regular fontsize=14 sub_font=Lato-Bold sub_fontsize=16

d.vect.chart map=census_tracts chart_type=bar columns=population size_column=population size=1 scale=0.04
```

---

### Hexagonal Bin Map

Hexagonal binned (hexbin) map

---

### Census Data on Race
https://data.census.gov/
Search: Race
Table: B02001
Product: 2018: ACS 5-Year Estimates Detailed Tables
https://data.census.gov/cedsci/table?q=race&tid=ACSDT5Y2018.B02001&hidePreview=false
Customize Table
Geos
Tract > New York > All Census Tracts within New York
Download Table

---

### Crime

from NYC Open Data
Export Original

Hate Crimes
https://data.cityofnewyork.us/Public-Safety/NYPD-Hate-Crimes/bqiq-cu78

Police Arrests
https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u

Police Precincts
https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz

### Public Use Microdata

PUMA from TIGER/Line
https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2018&layergroup=Public+Use+Microdata+Areas

Select Variables: RACENUM

Select Geographies: PUMA: New York State: all NYC Community Districts

https://data.census.gov/mdat/#/search?ds=ACSPUMS5Y2018&vv=*RACNUM&rv=ucgid&wt=PWGTP&g=7950000US3603701,3603702,3603703,3603704,3603705,3603706,3603707,3603708,3603709,3603710,3603801,3603802,3603803,3603804,3603805,3603806,3603807,3603808,3603809,3603810,3603901,3603902,3603903,3604001,3604002,3604003,3604004,3604005,3604006,3604007,3604008,3604009,3604010,3604011,3604012,3604013,3604014,3604015,3604016,3604017,3604018,3604101,3604102,3604103,3604104,3604105,3604106,3604107,3604108,3604109,3604110,3604111,3604112,3604113,3604114
