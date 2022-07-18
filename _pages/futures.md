---
title: FUTURES
subtitle:
description: A brief introduction to the FUTURES land change model.
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/
---

FUTure Urban-Regional Environment Simulation (FUTURES) is a model for multilevel simulations of emerging urban-rural landscape structure. FUTURES produces regional projections of landscape patterns using coupled submodels that integrate nonstationary drivers of land change.

---

## Submodels
* Potential: site suitability
* Demand: per capita demand
* Patch Growing Algorithm (PGA): the spatial structure of conversion events

---

## Potential Submodel Variables

| Development Pressure | Predictors |
|---|---|
| Urban change | Protected areas |
|  | Roads |
|  | Water |
|  | Forest |
|  | City center |

## Demand Submodel Variables

| Demand |
|---|
| Population statistics |

---

## Research Questions
* Where is growth happening?
* How should we rethink development?

---

## Scenario Variables

| Incentives | Predictors | Weight |
|---|---|---|
| Normal | Wellbeing index | Digitized development zones |
| Sprawl | Landcover scenario | Digitized conservation zones |
| Infill | Flood zones |  |

---

## Scenario Evaluation

A matrix comparing hydrological and landcover change (LCC) scenarios.

*CC: Hydrological events with a climate change multiplier.*

| Hydrological Event | LCC Incentives | LCC Predictors |
|---|---|---|
| 25 yr storm | Normal |  |
| 50 yr storm | Normal |  |
| 100 yr storm | Normal |  |
| 500 yr storm | Normal |  |
| 25 yr storm x CC | Normal |  |
| 50 yr storm x CC | Normal |  |
| 100 yr storm x CC | Normal |  |
| 500 yr storm x CC | Normal |  |
| 25 yr storm | Normal | Social vulnerability |
| 50 yr storm | Normal | Social vulnerability |
| 100 yr storm | Normal | Social vulnerability |
| 500 yr storm | Normal | Social vulnerability |
| 25 yr storm | Infill |  |
| 50 yr storm | Infill |  |
| 100 yr storm | Infill |  |
| 500 yr storm | Infill |  |
| ... | ... | ... |

---

## Resources
* [NCSU Center for Geospatial Analytics: FUTURES Urban Growth Model](https://cnr.ncsu.edu/geospatial/research/futures/)
* [FUTURES Tutorial](https://grasswiki.osgeo.org/wiki/FUTURES_land-change_modeling_for_evaluating_innovative_conservation_scenarios)
