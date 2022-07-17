---
title: Random Paving
subtitle: Generating random paving patterns in Grasshopper
featured_image: /images/random-paving/
usemathjax: true
---

![Paving pattern from noise](/images/random-paving/random-paving-5.png)

**Contents**
* TOC
{:toc}

---

## Random Paving Patterns

Download the Grasshopper definition
[<i class="fas fa-project-diagram"></i>](https://github.com/baharmon/generative-design/raw/main/grasshopper/random-paving.gh)
for this tutorial.


**Readings**
* Patricio Gonzalez Vivo & Jen Lowe, 2015. [Random](https://thebookofshaders.com/10/), The Book of Shaders.
* Patricio Gonzalez Vivo & Jen Lowe, 2015. [Noise](https://thebookofshaders.com/11/), The Book of Shaders.
* Stefan Gustavson, 2005. [Simplex Noise Demystified](http://staffwww.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf).

---

## Regular Paving

![Grasshopper program for regular paving](/images/random-paving/random-paving-program-1.png)

![Regular paving pattern](/images/random-paving/random-paving-1.png)

---

## Random Paving

![Grasshopper program for random paving](/images/random-paving/random-paving-program-2.png)

![Grasshopper program for baking to a new layer](/images/random-paving/random-paving-program-bake.png)

![Random paving pattern](/images/random-paving/random-paving-2.png)

---

## Random Gradient of Paving

![Grasshopper program for random gradient of paving](/images/random-paving/random-paving-program-3.png)

![Paving pattern with random gradient](/images/random-paving/random-paving-3.png)

---

## Paving from Noise

Noise is variation from an ideal signal.
It is used in computer graphics
to generate textures that appear pseudo-random,
yet have a consistent scale of detail.
Noise is often used to represent
organic surfaces like topography,
natural textures like marble,
and natural phenomena like clouds.
Perlin noise is created by interpolating between points
in a grid with pseudo-random gradients.
Use the Perlin or Simplex noise component
from the [4D Noise](https://www.food4rhino.com/app/4d-noise) addon
to assign a color gradient to a grid of pavers.
Create a [rectangular](http://grasshopperdocs.com/components/grasshoppervector/rectangular.html)
grid, flatten the resulting tree of cells,
and find the center of each cell with the
[polygon center](https://grasshopperdocs.com/components/grasshoppercurve/polygonCenter.html)
component.
Input the center of the cells as the values for Perlin Noise
and then add time and scale parameters.
Use [remap numbers](https://grasshopperdocs.com/components/grasshoppermaths/remapNumbers.html)
to rescale the noise values for a color gradient.
Set the source domain to the
[bounds](https://grasshopperdocs.com/components/grasshoppermaths/bounds.html)
of the noise
and set the target domain from 0 to 1.
Alternatively, deconstruct the domain of the noise
with [deconstruct domain](http://grasshopperdocs.com/components/grasshoppermaths/deconstructDomain.html)
to set the lower and upper limits of the color gradient.
Experiment with noise's time and scale parameters
to generate new patterns.

![Grasshopper program for paving from noise](/images/random-paving/random-paving-program-4.png)

![Paving pattern from noise](/images/random-paving/random-paving-4.png)

---

## Hexagonal Paving from Noise

Generate a hexagonal paving pattern from noise by
replacing the
[rectangular](http://grasshopperdocs.com/components/grasshoppervector/rectangular.html)
component with a
[hexagonal](https://grasshopperdocs.com/components/grasshoppervector/hexagonal.html)
component.
Use the center points of the hexagonal cells
as the input values for the noise.

![Grasshopper program for hexagonal paving from noise](/images/random-paving/random-paving-program-5.png)

![Hexagonal paving pattern from noise](/images/random-paving/random-paving-5.png)

---

## Pathway from Noise
Create a pathway from noise
by using a culling pattern to hide pavers
with a noise value greater than a given threshold.
Filter the list of pavers with
[cull pattern](https://grasshopperdocs.com/components/grasshoppersets/cullPattern.html)
and set the culling pattern to
[larger than](https://grasshopperdocs.com/components/grasshoppermaths/largerThan.html)
a threshold.
Adjust the parameters of the Perlin noise component
to form a connected pathway.

![Grasshopper program for pathway from noise](/images/random-paving/random-paving-program-6.png)

![Pathway from noise](/images/random-paving/random-paving-6.png)
