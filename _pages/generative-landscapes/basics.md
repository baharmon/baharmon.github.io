---
title: An Introduction to Grasshopper
subtitle: Modeling points, lines, curves, and surfaces in Grasshopper
usemathjax: true
---

![Surface](/images/basics/basics-5.png)

**Contents**
* TOC
{:toc}

---

## Visual Programming with Grasshopper

Grasshopper is a visual programming interface
for the 3D modeling program
[Rhinoceros](https://www.rhino3d.com/).
Rhino uses non-uniform rational B-splines (NURBS)
to precisely, mathematically model geometry.
With visual programming,
you can algorithmically generate geometry
by composing diagrams that link data to functions.
An algorithmic approach enables designers
to create complex forms and
rapidly generate alternative designs.
Resources for learning more about Grasshopper include:
* [The Grasshopper Primer](https://modelab.gitbooks.io/grasshopper-primer/content/1-foundations/1-2/2_grasshopper-component-parts.html)
* [Grasshopper Basics with David Rutten](https://vimeo.com/channels/basicgh)
* [Grasshopper Docs](https://grasshopperdocs.com/)
* [TU Delft Grasshopper Tutorials](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper)

This tutorial is an introduction to modeling basic geometry -
such as points, line, polylines, curves, and surfaces - in Grasshopper.
Download the Grasshopper definition
[<i class="fas fa-project-diagram"></i>](https://github.com/baharmon/generative-design/raw/main/grasshopper/basics.gh) for this tutorial as a guide.
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

![Point from x, y, z coordinates](/images/basics/basics-program-1.png)

Points can also be defined by text panels with x, y, and z values.
Place a `Point` parameter
from the `Input` panel of the `Params` tab on the canvas.
Then place a `Panel` parameter from `Input` panel.  
Double click on the panel to edit it.
Type in x, y, and z values separated by commas.
Connect the `Panel` to the `Point` parameter.

![Point from text panel](/images/basics/basics-program-2.png)

The `Point` parameter can also be set
to a point drawn in Rhino.
Right click on the `Point` parameter
and select `set one point`.
Grasshopper will minimize
and the command line in Rhino will ask for a point location.
Either draw a point in one of the Rhino viewports
or type x, y, and z values separated by commas into the command line.

![Point from Rhino](/images/basics/basics-program-3.png)

![Point from x, y, and z coordinates](/images/basics/basics-1.png)

---

## Lines

In Grasshopper lines can be defined by start and end points
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

![Line from constructed points](/images/basics/basics-program-4.png)

![Line from points defined in panels](/images/basics/basics-program-5.png)

![Line from referenced points](/images/basics/basics-program-6.png)

To reference a line drawn in Rhino,
place a `Line` parameter.
Right click on the `Line` parameter and select `set one line`.
Grasshopper will minimize and the Rhino command line will ask for
the starting point and then ending point of the line.
Either draw the points in a Rhino viewport or
enter the coordinates in the command line.

![Line from Rhino](/images/basics/basics-program-7.png)

To draw a line from a starting point, length, and distance,
first place the
[Line SDL](https://grasshopperdocs.com/components/grasshoppercurve/lineSDL.html)
component.
Set a start point with `Point` parameter, `Panel`, or
`Construct Point` component.
Set a direction with a vector component such as
[Unit Z](https://grasshopperdocs.com/components/grasshoppervector/unitZ.html).
Set a length using a `Number Slider` or `Panel` parameter.

![Line from start, tangent, and length](/images/basics/basics-program-8.png)

To construct a line whose end point is relative to its start point,
first define a starting point
and then move it along a vector to the end position.
Start by placing a
[Line](https://grasshopperdocs.com/components/grasshoppercurve/line.html)
component.
Define its start point using a `Point` parameter, `Panel`, or
`Construct Point` component.
Then add a
[Move](https://grasshopperdocs.com/components/grasshoppertransform/move.html)
component to translate the point to a new position.
Connect the start point to the input `Geometry` parameter
for the `Move` component
and connect the output `Geometry` component
to the end point parameter for the `Line` component.
Then connect a vector to the `Motion` input parameter for the `Move` component.
For example add and connect a
[Unit X](https://grasshopperdocs.com/components/grasshoppervector/unitX.html)
vector to set the direction of movement along the x-axis.
Then connect a `Number Slider` parameter
to the input `Factor` for the
[Unit X](https://grasshopperdocs.com/components/grasshoppervector/unitX.html)
vector to set the length of movement.

![Line from translated end point](/images/basics/basics-program-9.png)


![Line from constructed points](/images/basics/basics-2.png)

---

## Polylines

Polylines are a sequence of lines connecting an ordered collection of points.
They can be closed to form polygons.
Place a
[Polyline](https://grasshopperdocs.com/components/grasshoppercurve/polyLine.html)
component and then connect multiple points to the `Vertices` input parameter.
Hold shift while dragging wires to add multiple inputs.
To close the polyline and form a polygon, set the `Closed` input parameter
to `True` either by adding a `Panel` or a `Boolean Toggle`.
Double click on the `Boolean Toggle` to change its state from true to false.

![Polyline](/images/basics/basics-program-10.png)

![Polygon](/images/basics/basics-3.png)

---

## Curves

Non-uniform rational basis spline (NURBS)
curves are interpolated through a set of control points.
To draw a curve place an
[Interpolate](https://grasshopperdocs.com/components/grasshoppercurve/interpolate.html)
component and connect its input `vertices` parameter to a set of points.
Points for a curve can be created from x, y, z coordinates with the
[Construct Point](https://grasshopperdocs.com/components/grasshoppervector/constructPoint.html)
component or a `Panel` parameter,
drawn in Rhino and referenced with a `Point` parameter,
or generated from a trigonometric function such as a sine wave.
`Point` parameters can easily to be edited using the gumball
to change the shape of the curve.

![Curve](/images/basics/basics-program-11.png)

To create a curve from a sine wave
first generate a range of values from for example 0 to 10 using the
[Range](http://grasshopperdocs.com/components/grasshoppersets/range.html)
component.
Connect the range to the x coordinate of a
[Construct Point](https://grasshopperdocs.com/components/grasshoppervector/constructPoint.html)
component.
Also connect the range to a
[Sine](https://grasshopperdocs.com/components/grasshoppermaths/sine.html)
component and then connect the output of the sine function
to the z coordinate of the `Construct Point` component.
Connect the point to the `Vertices` input parameter of an
[Interpolate](https://grasshopperdocs.com/components/grasshoppercurve/interpolate.html)
component.
Try changing the domain, frequency, and amplitude of the sine wave.

![Curve](/images/basics/basics-program-12.png)

![Curve](/images/basics/basics-program-13.png)

![Curve](/images/basics/basics-4.png)

---

## Surfaces

NURBS surfaces are interpolated through a 2-dimensional grid of control points.
Primitive surfaces can be generated with components such as
[Plane Surface](https://grasshopperdocs.com/components/grasshoppersurface/planeSurface.html),
[Box 2Pt](https://grasshopperdocs.com/components/grasshoppersurface/box2Pt.html), and
[Center Box](https://grasshopperdocs.com/components/grasshoppersurface/centerBox.html).
Freeform surfaces can be generated with components such as
[Boundary Surfaces](https://grasshopperdocs.com/components/grasshoppersurface/boundarySurfaces.html),
[Ruled Surface](https://grasshopperdocs.com/components/grasshoppersurface/ruledSurface.html),
and
[Loft](http://grasshopperdocs.com/components/grasshoppersurface/loft.html).


Create planar surfaces from planar curves with
[Boundary Surfaces](https://grasshopperdocs.com/components/grasshoppersurface/boundarySurfaces.html)
or as primitives with components like
[Plane Surface](https://grasshopperdocs.com/components/grasshoppersurface/planeSurface.html).

![Surface](/images/basics/basics-program-14.png)

![Surface](/images/basics/basics-program-15.png)

![Surface](/images/basics/basics-program-16.png)

![Surface](/images/basics/basics-program-17.png)

Create solids either by extruding surfaces with
[Extrude](https://grasshopperdocs.com/components/grasshoppersurface/extrude.html)
or as primitives such boxes or spheres.

![Surface](/images/basics/basics-program-18.png)

![Surface](/images/basics/basics-program-19.png)

![Surface](/images/basics/basics-program-20.png)

Freeform surfaces can be constructed from multiple curves
with components like
[Ruled Surface](https://grasshopperdocs.com/components/grasshoppersurface/ruledSurface.html),
and
[Loft](http://grasshopperdocs.com/components/grasshoppersurface/loft.html).

![Surface](/images/basics/basics-program-21.png)

![Surface](/images/basics/basics-program-22.png)

![Surface](/images/basics/basics-program-23.png)

![Surface](/images/basics/basics-5.png)

Learn how to transform this surface into furniture in the next tutorial:
[Modeling a Parametric Bench in Grasshopper](parametric-bench).
