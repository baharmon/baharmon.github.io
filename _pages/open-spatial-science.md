---
title: Tools for Open Spatial Science
subtitle: A brief introduction to tools for open spatial science.
description: A brief introduction to tools for open spatial science.
featured_image: images/
---

## Principles of open science
* Reproducibility
* Replicability
* Transparency
* Reusability
* Accessibility
* Collaboration

---

## Types of open science
* Open data
* Open access
* Open education
* Open source
* Open methodology
* Open peer review

---

## Tools for open spatial science
* [Git](https://git-scm.com/) + [GitHub](https://github.com/) + [GitBook](https://www.gitbook.com/)
* [Markdown](https://daringfireball.net/projects/markdown/)
* [Jekyll](https://jekyllrb.com/) / [Hugo](http://gohugo.io/)
* [LaTeX](https://www.latex-project.org/)
* [Python](https://www.python.org/)
* [R](https://www.r-project.org/)
* [Leaflet](https://leafletjs.com/)
* [Jupyter Notebooks](https://jupyter.org/)
* [Docker](https://www.docker.com/)
* [Dataverse](https://dataverse.org/)
* [Zenodo](https://zenodo.org/)
* [Open Science Framework](https://osf.io/)
* [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about)

---

## Demo
In this demo, I will demonstrate how to
host, track, and publish spatial data online for the sake of
reproducibility, open data, open access, and open education.
I will show an example of a spatial dataset
for a research project on simulating landscape evolution
hosted on GitHub and tracked with Git for version control.
I will also show how to publish and track spatial data on
the [Open Science Framework](https://osf.io/)
and [Zenodo](https://zenodo.org/).

---

#### GRASS GIS
For a project on simulating landscape evolution
using [GRASS GIS](https://grass.osgeo.org/),
I created a sample dataset that can be downloaded
[here](https://github.com/baharmon/landscape_evolution_dataset/archive/master.zip).
I hosted this dataset on GitHub at
https://github.com/baharmon/landscape_evolution_dataset
for version control, easy sharing, and documentation.

----

#### GitHub
Upload your data to a GitHub repository
so that your can share your data online
and track changes with Git for version control.
To do this, first  create new repository on GitHub,
then clone the repository to your computer,
add your dataset and other files, commit your changes,
and push the changes to GitHub.
You can either do this with a GUI with
[GitHub Desktop](https://desktop.github.com/)
 or [GitKraken](https://www.gitkraken.com/)
or with Git and Bash in the command line.
If you are on Windows and want to use Git and Bash in the command line
then I recommend using
[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about).

Here are the commands for uploading
the landscape evolution dataset for the first time:
```bash
git clone git@github.com:baharmon/landscape_evolution_dataset.git
cd landscape_evolution_dataset
git add -A
git commit 'initial commit'
git push
```

---

#### Markdown
Add documentation to your spatial data repository on GitHub
by writing a ``README.md`` file in Markdown.
Markdown is a way to write plain text
that can be rendered in formats like HTML.
It is meant to be very easy to read and write.
The basic syntax includes:
```markdown
# heading level 1
## heading level 2
## heading level 3
*italics*
**bold**
* unordered list
1. ordered list
`code`
[link](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
![image](https://octodex.github.comhttps://media.githubusercontent.com/media/baharmon/baharmon.github.io/master/images/labtocat.png)
```

The readme for the landscape evolution dataset looks like this:

```markdown
# Landscape Evolution Dataset
A sample dataset for the landscape evolution model
[r.sim.terrain](https://github.com/baharmon/landscape_evolution).
This dataset includes the [GRASS GIS](grass.osgeo.org)
location **nc_spm_evolution**
in the North Carolina State Plane HARN Meters
coordinate system (EPSG code 3358).
It contains the mapset **PERMANENT**
with spatial data for Fort Bragg, NC.
The location also contains rainfall records,
rules for custom color tables, rules for recoding data,
and metadata.

## License
This dataset is licensed under the
[Open Database License](https://opendatacommons.org/licenses/odbl/)
by Brendan Harmon
```

---

#### Open Science Framework
Publish your research project on the
[<i class="ai ai-osf"></i> Open Science Framework](https://osf.io/)
and make a page for your spatial dataset.
You can either upload data directly to OSF
or connect to data on
GitHub, Google Drive, Box, Amazon, Mendeley, Dataverse, etc.
OSF will track changes in the Recent Activity section.
When you make your OSF repository public,
you can generate a DOI.
For my OSF repository for the
[<i class="ai ai-osf"></i> Landscape Evolution](https://osf.io/tf6yb/)
project I connected the GitHub repositories for the code and the dataset.

---

#### Zenodo

You can either upload data directly to [Zenodo](https://zenodo.org/)
or integrate it with GitHub.
When you publish a release for your GiHub project,
then it will be automatically uploaded to Zenodo
where a DOI will be generated.
Follow this [guide](https://guides.github.com/activities/citable-code/).
Here is the latest release of my
<i class="ai ai-doi"></i>
[Landscape Evolution Dataset](https://zenodo.org/badge/latestdoi/115289574)
on Zenodo.

---

## Examples

* Di Stefano and Mayer 2018, [An Automatic Procedure for the Quantitative Characterization of Submarine Bedforms](https://doi.org/10.3390/geosciences8010028) +
[<i class="fas fa-book-open"></i> Jupyter Notebook](https://nbviewer.jupyter.org/gist/epifanio/1ec46faa0ee6c1bcae21682f3c4d6c93) +
[<i class="ai ai-doi"></i> Zenodo](https://zenodo.org/record/1169423#.XoNjRIhKguU)
* Petras, Newcomb, & Mitasova 2017, [Generalized 3D fragmentation index derived from lidar point clouds](https://doi.org/10.1186/s40965-017-0021-8) + [<i class="fab fa-github"></i> Repository](https://github.com/wenzeslaus/forestfrag3d)
* [Geopandas Docs](https://geopandas.org/mapping.html) using Markdown, Jupyter Notebooks, and GitBooks

---

## Readings

* Kieran Healy, [The Plain Person’s Guide to Plain Text Social Science](https://kieranhealy.org/files/papers/plain-person-text.pdf)
* Rocchini & Neteler 2012, [Let the four freedoms paradigm apply to ecology](https://doi.org/10.1016/j.tree.2012.03.009)
* Vaclav Petras, [<i class="fab fa-github"></i> Open Science Course](https://ncsu-geoforall-lab.github.io/open-science-course/)
* [<i class="fab fa-github"></i> Open Science Training Handbook](https://book.fosteropenscience.eu/en/)

---

## License
<i class="fab fa-creative-commons"></i>
Open educational materials licensed
Creative Commons Attribution-ShareAlike 4.0
by Brendan Harmon.
