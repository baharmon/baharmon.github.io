---
title: CNC Milling Terrain Models
subtitle: CNC milling terrain models with RhinoCAM
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/cnc/
usemathjax: true
---

![](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/cnc/)

**Contents**
* TOC
{:toc}

---

## CNC Milling Terrain Models

---

## Digital Elevation Model

```
g.region n=189850 s=189100 e=978550 w=976850 save=landforms
r.info map=elevation_2017
r.mapcalc expression="elevation = if(isnull(elevation_2017),-4,elevation_2017)"
r.out.xyz input=elevation output=elevation.xyz separator=comma
```

---

## Terrain Mesh
Start Rhino in the Feet Large Template
Bake from Grasshopper
Set the Units to Inches

750x1700

```
Scale
0,0,0
.01
```

---

## Machine Setup

Part Box Stock
Align: Set World C.S.


---
