---
title: Rendering a Photorealistic Tree
subtitle:
description:
featured_image: https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree.png
usemathjax: true
---

![Rendered tree](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree.png)

**Contents**
* TOC
{:toc}

---

## Rendered Tree

In this tutorial you will learn how to work with
libraries of procedurally generated 3D plants in Grasshopper
and render them with
[Thea for Rhino](https://www.thearender.com/products/thea-for-rhino/).
You can use this workflow to replace the
[parametric tree](parametric-tree)
with a tree from a 3D library
for all of the planting exercises in this course.
Xfrog is software for procedurally generating 3D plants
based on processes such as branching, spiraling, and gravity.
It has been used to generate large libraries with thousands of plants.
This tutorial uses a [European Aspen](http://xfrog.com/product/EU52.html)
from the [XfrogPlants Europe 3](http://xfrog.com/product/X-44.html) library
and a [Ryegrass](http://xfrog.com/product/AG12.html)
from the [XfrogPlants Agriculture](http://xfrog.com/product/X-55.html)
library.
Download the Grasshopper definition
[<i class="fas fa-project-diagram"></i>](https://github.com/baharmon/generative-design/raw/main/grasshopper/rendered-tree.gh)
for this tutorial.

* **Software:** [Rhino](https://www.rhino3d.com/),
[Grasshopper](https://www.rhino3d.com/6/new/grasshopper/),
and
[Thea for Rhino](https://www.thearender.com/products/thea-for-rhino/)
* **Plugins:** [Elefront](https://www.food4rhino.com/app/elefront)
* **Library:** [Xfrog Plants](http://xfrog.com/category/libraries.html),
free [Xfrog Samples](http://xfrog.com/category/samples.html),
or free [Thea Libraries](https://www.thearender.com/resources/libraries/)
* **Definition:** [<i class="fas fa-project-diagram"></i>](https://github.com/baharmon/generative-design/raw/main/grasshopper/rendered-tree.gh)
* **Videos:** [<i class="fab fa-youtube"></i>](https://youtu.be/MPoksbmbFt8)
* **Reading:** Deussen, Oliver, and Bernd Lintermann. 2010. Digital Design of Nature: Computer Generated Plants and Organics. Springer.


---

## Blocks

In Rhino models from Thea libraries (*.lib.thea*) are imported as blocks.
[Blocks](https://docs.mcneel.com/rhino/6/help/en-us/commands/block.htm)
are a way to efficiently work with repeating geometry,
while keeping file sizes small.
A single block definition describes all instances of the block in the file.
So when a 3D tree is imported as a block and copied multiple times,
the geometry is only defined once.
Use the extended geometry parameter from the plugin
[Elefront](https://www.food4rhino.com/app/elefront)
to work with blocks -- such as 3D trees -- in Grasshopper.

First in Rhino install a Thea library with 3D plants,
then import a model of a 3D tree from the library.
The model will be imported as a block.
Place the block at `0,0,0` -- the origin of your scene.
If necessary move the block on the z-axis
so that the roots are just below the World XY plane.
```
TheaInstallLibrary
TheaImportModel
```

In Grasshopper add an extended geometry parameter
from [Elefront](https://www.food4rhino.com/app/elefront)
to your canvas.
Right click, select `set one extended geometry`,
and pick the block in Rhino.
Now you can work with the block in Grasshopper.
Before you can render the results,
you will need to bake them.

![Grasshopper program for setting blocks](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-0.png)

---

## Ground

Model a small circular region of ground for your tree and grass.
First generate a
[circle](http://grasshopperdocs.com/components/grasshoppercurve/circle.html),
then create
[boundary surface](http://grasshopperdocs.com/components/grasshoppersurface/boundarySurfaces.html)
from the circle, and
[extrude](https://grasshopperdocs.com/components/grasshoppersurface/extrude.html)
the surface to form a solid.

![Grasshopper program for creating a circular region of ground](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-3.png)

Bake the solid to a new layer named `ground` in Rhino
using the
[bake objects](https://grasshopperdocs.com/components/elefront/bakeObjects.html)
component from [Elefront](https://www.food4rhino.com/app/elefront).
Define the new `ground` layer for the baked object
by connecting a panel to
[Define Layer](https://grasshopperdocs.com/components/elefront/defineLayer.html)
and
[Define Object Attributes](https://grasshopperdocs.com/components/elefront/defineObjectAttributes.html).
Click `Activate` to bake the geometry to the new layer
and then add a Thea material.


![Grasshopper program for baking the ground to a new layer](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-4.png)

---

## Populate Trees

Randomly place a tree in the circular region.
First create a random point on the boundary surface with the
[populate geometry](http://grasshopperdocs.com/components/grasshoppervector/populateGeometry.html)
component.
Try changing the seed to get a different point.
Then [move](http://grasshopperdocs.com/components/grasshoppertransform/move.html)
the block with the tree to the random point.
Define the motion vector with
[vector2pt](https://grasshopperdocs.com/components/grasshoppervector/vector2Pt.html)
with the origin `0,0,0` as the base point
and the random point as the tip point.

![Grasshopper program for randomly placing a tree](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-5.png)

Bake the resulting block to a new layer named `tree`
with
[bake objects](https://grasshopperdocs.com/components/elefront/bakeObjects.html).

![Grasshopper program for baking a tree to a new layer](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-6.png)

---

## Populate Grass

Randomly place a tree in the circular region.
First create hundreds of random points on the boundary surface with
[populate geometry](http://grasshopperdocs.com/components/grasshoppervector/populateGeometry.html).
Then [move](http://grasshopperdocs.com/components/grasshoppertransform/move.html)
the block with grass to the random points.

![Grasshopper program for randomly populating the scene with grass](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-7.png)

Randomly [rotate](https://grasshopperdocs.com/components/grasshoppertransform/rotate.html)
and [scale](http://grasshopperdocs.com/components/grasshoppertransform/scale.html)
the blocks.

![Grasshopper program for transforming grass](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-8.png)

Bake the resulting list of blocks to a new layer named `grass` with
[bake objects](https://grasshopperdocs.com/components/elefront/bakeObjects.html).

![Grasshopper program for baking grass to a new layer](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree-program-9.png)

## Rendering

Photorealistically render the scene with Thea for Rhino.
In the Thea panel of the sidebar
turn on soft shadow and uniform illumination in the environment tab
and sync the resolution with the current Rhino viewport in the camera tab.
Add lighting such as the
[sun](http://docs.mcneel.com/rhino/6/help/en-us/commands/sun.htm)
to the scene.
Add a material from the Thea Content Browser to the ground.
Then open Thea Darkroom, set production mode, and start rendering.
When the rendering finishes,
adjust the settings
and then hit `save image` to export a `.png`.

![A rendered scene of a tree and grass](https://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/rendered-tree/rendered-tree.png)
