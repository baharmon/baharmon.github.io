---
title: Terrain Modeling
subtitle: A Gentle Introduction to Terrain Modeling with Grasshopper
description: A Gentle Introduction to Terrain Modeling with Grasshopper
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/grasshopper/
usemathjax: true
---

![Terrain modeling in Grasshopper](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topography.png)

**Contents**
* TOC
{:toc}

---

# Overview

This tutorial is a gentle introduction to terrain modeling with Grasshopper.
The tutorial begins with a brief guide to the basics of
[Rhino](https://www.rhino3d.com/)'s visual programming interface, Grasshopper.
Then it covers how to import, model, grade, and analyze terrain
using the [Docofossor](https://www.food4rhino.com/app/docofossor) plugin.
Materials for this tutorial include videos, a dataset, and an example:

**<i class="fab fa-youtube"></i> Videos:**
[Terrain Modeling](https://youtu.be/WTY78FIPegc) &
[Grading Terrain](https://youtu.be/Eih1g-tjFpc).

**<i class="ms ms-data-cube"></i> Dataset:**
[ governors-island-landform.xyz](https://github.com/baharmon/generative-design/raw/main/grasshopper/data/governors-island-landform.xyz)

**<i class="fas fa-project-diagram"></i> Visual Programs:**
[ fundamentals.gh](https://github.com/baharmon/generative-design/raw/main/grasshopper/fundamentals.gh) &
[ topographic-modeling.gh](https://github.com/baharmon/generative-design/raw/main/grasshopper/topographic-modeling.gh)

**<i class="ms ms-database"></i> Plugin:**
[ Docofossor](https://www.food4rhino.com/app/docofossor)

<!-- **Server** [ https://discord.gg/qFYwQxwSGT](https://discord.gg/qFYwQxwSGT) -->

---

# Fundamentals of Grasshopper

Grasshopper is a visual programming interface
for the 3D modeling program
[Rhinoceros](https://www.rhino3d.com/).
With visual programming,
you can algorithmically generate geometry
by composing diagrams that link data to functions.
An algorithmic approach enables designers
to create complex forms and
rapidly generate alternative designs.

This part of the tutorial covers how model basic geometry -
such as points, lines, meshes, and surfaces - in Grasshopper.
First start Rhino.
Type `grasshopper` in the Rhino's command line
to launch the visual programming interface.
The Grasshopper interface has a menu bar,
a toolbar with parameters and components,
and a canvas for composing diagrams.
Parameters are used to set and store data.
Components are functions for performing operations.
Drop parameters and  components on the canvas
and connect them together with wires
to create node based diagrams
that generate geometry in Rhino.
A visual programming diagram composed in Grasshopper
generates geometry in Rhino.
Grasshopper's visual programs are called *definitions*.
Download the example definition
[<i class="fas fa-project-diagram"></i> fundamentals.gh](https://github.com/baharmon/baharmon.github.io/blob/master/data/fundamentals.gh?raw=true)
as a guide for this section.

---

## Points

In Cartesian space a point
is defined by x, y, and z coordinates.
In Grasshopper points can either be
constructed from x, y, and z coordinates or
drawn in Rhino and referenced in Grasshopper.
One way to define a point is with the
[Construct Point](https://grasshopperdocs.com/components/grasshoppervector/constructPoint.html)
component.
Find the `Construct Point` component
in the `Points` panel of the `Vector` tab.
Drop this component on the canvas.
Then add input data for the x, y, and z parameters
using `Number Slider` parameters.
Find the `Number Slider` parameters
in the `Input` panel of the `Params` tab.
Or double click on the canvas to search for a component
and then type in either number slider or a value for the slider such as 10.
Connect wires from each of the output nodes
on the right side of the number sliders
to the respective input node on the left of the `Construct Point` component.
Drag the handle on each slider to a set x, y, and z values for the point.

<!-- ![Point from x, y, z coordinates](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-1.png) -->
<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-1.png" alt="Point from x, y, z coordinates" width="750"/>

Points can also be defined by text panels with x, y, and z values.
Place a `Point` parameter
from the `Input` panel of the `Params` tab on the canvas.
Then place a `Panel` parameter from `Input` panel.
Double click on the panel to edit it.
Type in x, y, and z values separated by commas.
Connect the `Panel` to the `Point` parameter.

<!-- ![Point from text panel](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-2.png) -->
<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-2.png" alt="Point from text panel" width="750"/>

The `Point` parameter can also be set
to a point drawn in Rhino.
Right click on the `Point` parameter
and select `set one point`.
Grasshopper will minimize
and the command line in Rhino will ask for a point location.
Either draw a point in one of the Rhino viewports
or type x, y, and z values separated by commas into the command line.

<!-- ![Point from Rhino](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-3.png) -->
<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-3.png" alt="Point from Rhino" width="750"/>

![Point from x, y, and z coordinates](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-1.png)

---

## Lines

In Grasshopper,
lines can be defined by start and end points
by a start point, direction, and length,
or by drawing a line in Rhino.
Start and end points can set by
constructing points from sliders,
by defining coordinate in panels,
or by drawing points in Rhino.
Place a
[Line](https://grasshopperdocs.com/components/grasshoppercurve/line.html)
component from the `Input` panel of the `Params` tab on the canvas.
Then connect the output for start and end points -
whether from `Number Slider`, `Point`, or `Panel` parameters -
to the respective input parameters on the `Line` component.

<!-- ![Line from constructed points](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-4.png) -->
<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-4.png" alt="Line from constructed points" width="750"/>

<!-- ![Line from points defined in panels](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-5.png) -->
<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-5.png" alt="Line from points defined in panels" width="750"/>

<!-- ![Line from referenced points](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-6.png) -->
<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-6.png" alt="Line from referenced points" width="750"/>

---

## Meshes

A mesh is a set of connected polygons composed of vertices, edges, and faces.
Meshes are often used to represent topography.
In Grasshopper, a mesh can be generated from a set of points
using the Delaunay triangulation algorithm.

<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-24.png" alt="Mesh from random points" width="750"/>

![Mesh from random points](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-6.png)

---

## Surfaces

Topography can also be represented as smooth, continuous surfaces
defined by boundaries, control points, and surface tension.

<img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-program-25.png" alt="Surface from random points" width="750"/>

![Surface from random points](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/basics/basics-7.png)

---

# Terrain Modeling

This part of the tutorial covers terrain modeling
with the [Docofossor](https://www.food4rhino.com/app/docofossor) plugin.
Download the example definition
[<i class="fas fa-project-diagram"></i> topographic-modeling.gh](https://github.com/baharmon/generative-design/raw/main/grasshopper/topographic-modeling.gh)
as a guide for this section.

---

## Data

[Docofossor](https://www.food4rhino.com/app/docofossor),
is a Grasshopper plugin for efficiently and iteratively modeling terrain
using signed distance functions.
In Docofossor terrain is represented as a grid of elevation values (Z).
Docofossor's signed distance field (df) data structure
has a header that defines the properties of the grid
and then a list of Z values.
This grid of values can be transformed using signed distance functions,
enabling an efficient, iterative process for terrain modeling in Grasshopper.
To visualize the terrain data in Grasshopper
the grid can be converted into either 3D points or a quadrilateral mesh.
To install this plugin on Windows
first download [Docofossor](https://www.food4rhino.com/app/docofossor),
right click on the zip archive to open properties and unblock it,
then extract the zip archive,
move the contents to your Grasshopper components library,
and restart Rhino and Grasshopper.

---

## Modeling

Download the gridded point cloud
[governors-island-landform.xyz](https://github.com/baharmon/generative-design/raw/main/grasshopper/data/governors-island-landform.xyz)
for the Hills of Governor's Island.
In Grasshopper add the file path for this dataset
to your canvas as a parameter.
In the `Params` tab under `Primitive` select and add a `File Path` parameter.
Right click on the parameter, choose `select an existing file`,
and set the path to the downloaded `.xyz` data.
In the `Docofossor` tab under `IO` add the
[dfImportXYZ](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfimportxyz)
component.
Set [dfImportXYZ](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfimportxyz)'s
input parameter `f` to the `File Path` parameter
to import the point cloud as a Docofossor grid (`df`).
Optionally add a skip parameter `n` to reduce the size of the point cloud.
In the `Docofossor` tab under `Grid` add the
[dfGridShift](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfgridshift)
component and set the grid as its input `df`
to shift the grid to from its geographic coordinates
to the XY origin of the local Cartesian coordinate system.
In the `Docofossor` tab under `Geometry` add the
[dfGridMesh](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfgridmesh)
component to generate a quadrilateral mesh from the shifted grid.

![Terrain modeling](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-program-1.png)
<!-- <img src="https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/terrain-modeling-program-1.png" alt="Terrain modeling" width="750"/> -->

![Terrain modeling in Grasshopper](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-1.png)

---

## Grading

In the `Docofossor` tab under `Operations Absolute` add the
[dfCutFillInPath](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfcutfillinpath)
component to cut and fill along a curve.
Connect the terrain data as the input Docofossor list (df),
a curve interpolated through points as the input curve,
and number sliders for the
input width, inner slope, outer slope, and maximum distance.
Convert the output Docofossor list (df)
to a mesh for visualization with the
[dfGridMesh](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfgridmesh)
component.

![Grading terrain](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-program-2.png)

![Grading in Grasshopper](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-2.png)

---

## Cut & Fill

Calculate the volume of cut and fill with the
[dfGridCompare](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md#-dfgridcompare)
component.
Connect the Docofossor list (df) before grading as the first input
and the Docofossor list (df) after grading as the second input.
Connect panels to the outputs to see the volume of cut, fill, and the balance
(i.e. the difference in the volume).

![Cut and fill calculations](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-program-3.png)

---

## Visualization

Since Docofossor expects points to be listed from
left to right and from bottom to top,
XYZ point clouds that are sorted differently -
such as [governors-island-landform.xyz](https://github.com/baharmon/generative-design/raw/main/grasshopper/data/governors-island-landform.xyz) -
will be mirrored vertically.
To fix this use the
[mirror](https://grasshopperdocs.com/components/grasshoppertransform/mirror.html)
component with the grid mesh as the input geometry
and an [XZ plane](https://grasshopperdocs.com/components/grasshoppervector/xZPlane.html)
with its origin set to the center of the mesh
as the input plane.
Find the center of the mesh using the
[area](https://grasshopperdocs.com/components/grasshoppersurface/area.html)
component.
Connect a custom preview with a color swatch
to the output mesh to better visualize the terrain.

![Visualize terrain](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-program-4.png)

---

## Contours

Generate contours from the mesh with the
[contour](http://grasshopperdocs.com/components/grasshopperintersect/contour.html)
component.
For the
[contour](http://grasshopperdocs.com/components/grasshopperintersect/contour.html)
component, connect the terrain mesh as the input shape,
the [unit z vector](https://grasshopperdocs.com/components/grasshoppervector/unitZ.html)
as the input direction,
and a number slider for the input distance.
Connect a custom preview with a color swatch
to the output mesh to better visualize the contours.

![Contours](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-program-5.png)

---

## Cutting Plane

Use a cutting plane to visualize flooding or sea level rise.
Create a surface and
[move](https://grasshopperdocs.com/components/grasshoppertransform/move.html)
it along the [z-axis](https://grasshopperdocs.com/components/grasshoppervector/unitZ.html) to visualize changes in sea level.

![Cutting plane](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-program-6.png)

![Terrain visualization in Grasshopper](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-3.png)

![Sea level rise visualization in Grasshopper](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/terrain-modeling/topographic-modeling-4.png)

---

# Resources

## Grasshopper
* [The Grasshopper Primer](https://modelab.gitbooks.io/grasshopper-primer/content/1-foundations/1-2/2_grasshopper-component-parts.html)
* [Grasshopper Docs](https://grasshopperdocs.com/)
* [Grasshopper Basics with David Rutten](https://vimeo.com/channels/basicgh)
* [TU Delft Grasshopper Tutorials](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper)

## Docofossor
* [Docofossor Documentation](https://github.com/dbt-ethz/docofossor/blob/master/DOCUMENTATION.md)
* [Computational Terrain Modeling with Distance Functions for Large Scale Landscape Design](https://gispoint.de/fileadmin/user_upload/paper_gis_open/DLA_2019/537663024.pdf)

## Data Sources
* [Geospatial Data Sources](geospatial-data-sources)
