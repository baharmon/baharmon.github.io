---
title: 'Landscape Evolution'
subtitle: 'A short term landscape evolution using a path sampling method to solve water and sediment flow continuity equations and model mass flows over complex topographies.'
date: 2019-05-15 00:00:00
description: ...
featured_image: 'https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-2.png'
---

<div class="gallery" data-columns="2">
    <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-1.png" alt="Elevation in 2012">
    <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-2.png" alt="Elevation simulated by SIMWE after a 50 mm/hr rainfall event lasting 120 min">
</div>

Digital elevation models
a) before and b) after
a simulated 2 hour storm with 50 mm/hr of rainfall.

---

## r.sim.terrain

Team: Brendan Harmon, Helena Mitasova, Vacalv Petras, & Anna Petrasova

---

<i class="fab fa-github"></i>
[Code](https://github.com/baharmon/landscape_evolution)

<i class="fab fa-github"></i> [Manual Pages](https://grass.osgeo.org/grass76/manuals/addons/r.sim.terrain.html)

<i class="fab fa-github"></i>
[Sample Dataset](https://github.com/baharmon/landscape_evolution_dataset)

<i class="ai ai-osf"></i> [Open Science Framework Repository](https://osf.io/tf6yb/)

---

A short-term landscape evolution model that simulates topographic change for both steady state and dynamic flow regimes across a range of spatial scales. This free and open source, GIS-based landscape evolution model uses empirical models (RUSLE3D & USPED) for soil erosion at watershed to regional scales and a physics-based model (SIMWE) for shallow overland water flow and soil erosion at subwatershed scales to compute short-term topographic change. This either steady state or dynamic model simulates how overland sediment mass flows reshape topography for a range of hydrologic soil erosion regimes based on topographic, land cover, soil, and rainfall parameters. As demonstrated by a case study for Patterson Branch subwatershed on the Fort Bragg military installation in North Carolina, r.sim.terrain can realistically simulate the development of fine-scale morphological features including ephemeral gullies, rills, and hillslopes. Applications include land management, erosion control, landscape planning, and landscape restoration. It has been implemented as the add-on module [r.sim.terrain](https://grass.osgeo.org/grass76/manuals/addons/r.sim.terrain.html) for [GRASS GIS](https://grass.osgeo.org/).

---

<div class="gallery" data-columns="2">
    <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-depth.png" alt="Water depth simulated by SIMWE after a 50 mm/hr rainfall event lasting 120 min">
    <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-erosion.png" alt="Erosion and deposition simulated by SIMWE after a 50 mm/hr rainfall event lasting 120 min">
    <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-net-difference.png" alt="Net difference in elevation simulated by SIMWE after a 50 mm/hr rainfall event lasting 120 min">
    <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/landscape-evolution-landforms.png" alt="Landforms simulated by SIMWE after a 50 mm/hr rainfall event lasting 120 min">
</div>

a) water depth,
b) erosion and deposition,
c) net difference in elevation,
and d) landforms
for a simulated 2 hour storm with 50 mm/hr of rainfall.


---

### Publications

Harmon, Brendan A, Helena Mitasova, Anna Petrasova, and Vaclav Petras. 2019. “r.sim.terrain: a dynamic landscape evolution model.” Geoscientific Model Development Discussions 2019: 1–23. [https://doi.org/10.5194/gmd-2019-18](https://doi.org/10.5194/gmd-2019-18).
