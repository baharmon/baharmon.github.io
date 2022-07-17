---
title: Census Data in QGIS
subtitle:
description: A guide to importing and mapping census data in QGIS
featured_image: /images/nyc/population-normal-choropleth-inferno.png
---

![Population choropleth](/images/nyc/population-normal-choropleth-inferno.png)

**Contents**
* TOC
{:toc}

---

### Download Census Data

To find and download data from the US Census Bureau go to
[data.census.gov](https://data.census.gov/).

Search for the survey
`ACS Demographic and Housing Estimates`
or table `DP05`.
Select the table `DP05`.
Select the product `2018: ACS 5-Year Estimates Data Profiles`.
Only the 5-year estimates have census tract and block group level data.
Click customize table.
Set `Geos` to select a geographic region and level of detail.
Select `Tract`, within `New York`, all census tracts within `New York`
Then Download the table as a `csv` for 2018.

Survey: ACS DEMOGRAPHIC AND HOUSING ESTIMATES
Survey: ACS
Table ID: DP05
Product: 2018: ACS 5-Year Estimates Data Profiles
Geo:
  Geography: Tract
  Tract: New York
  Within: all census tracts within New York
Download as csv


https://www.census.gov/programs-surveys/acs/

TIGER/Line shapefiles
https://www.census.gov/cgi-bin/geo/shapefiles/index.php
Year: 2018
Layer type: Census Tract
Submit
State: New York
tl_2018_36_tract.zip

[population.csv](/data/population.csv)

---

### Importing Census Data

[QGIS Tutorial](https://www.qgistutorials.com/en/docs/3/performing_table_joins.html)

Add nypp

Layer > Add Delimited Text Layer
Opens Data Source Manager | Delimited Text
File name: D:\nyc\census\NYPD_Arrests_Data__Historic_.csv
File Format: CSV
Record and Field Options:
Check: First record has field names
Check: Detect field type
Point Coordinates:
X field: X_COORD_CD
Y field: Y_COORD_CD
Geometry CRS: Project CRS: EPSD 2263 - NAD83 / New York Long Island (ftUS)


Layer > Add Delimited Text Layer
Opens Data Source Manager | Delimited Text
File name: D:\nyc\census\NYPD_Hate_Crimes.csv
File Format: CSV
Record and Field Options:
Check: First record has field names
Check: Detect field type
Check: No Geometry

Processing Tools > Vector General > Join Attributes by Field Value
NYDP Hate Crimes

Input layer: nypp
Table field: Precinct
Input layer 2: NYPD_Hate_Crimes
Table Field 2: Complaint Precinct Code
Join type: one to many
