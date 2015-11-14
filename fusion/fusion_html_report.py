#!/usr/bin/env python

import grass.script as gscript
from collections import defaultdict
import os


# set global variables

# set background image
background_image = "fusion.png"

# CSS style template 
style_template = """
/* global and body settings */

body {
    background-color: #EEEEEE;
    font-family: "Open Sans", "Helvetica Neue", Ubuntu, Arial, sans-serif;
    font-size: 90%;
    color: black;
}

/* site top image */

#header-image {
    height: 200px;
    background-image: url(background_image); 
    background-size: 100%;
    background-repeat: no-repeat;
}

#header-image p {
    position: absolute;
    top:100px;
    left:25px;
    font-size: 200%;
    /*font-weight: bold;*/
    font-size: 40px;
    color: white;
    text-shadow: 0 0 10px black;
    /*color: #444;*/
    /*text-shadow: 0 0 2px white;*/
}

/* links */

a {
    color: #909090; 
    text-decoration: none;
}
    a:hover {
    color: #444;
    text-decoration: underline;
}

/* headings */

h1, h2, h3, h4, h5, h6 {
    font-weight: bold;
    color: #444;
    clear: both;
    border-bottom: 2px solid #F3F3F3;
    padding-bottom: 0.1em;
}

/* links inside the headings - the standard settings */
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    font-weight: bold;
    color: green;
}

/* main menu navigation */

nav {
    margin: 0;
    padding: 0;
    overflow: auto;
    border: 0px solid #dcddde;
    background-color: #ffffff;
    border-radius: 0px;
    /*box-shadow: 0 0 8px #eee;*/
    background-color: #444;
    font-size: 1.3em;
}

nav ul {
    margin:0;
    padding:0;
    padding: 0px;
    display: block;
    list-style-type:none;
}

nav li {
    margin: 0;
    padding: 0;
    text-decoration: none;
    float: left;
    border-right: 2px solid #F3F3F3;
    /*border-left: 1px solid #DDDDDD;*/
    padding-left: 15px;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-right: 15px;
}

.nav a {
text-decoration:none;
color: #F3F3F3;
}

nav li:hover {
    background: #666;
    color: #FFF;
}

/* footer */

footer {
    position: relative;
    clear: both;
    margin: 0;
    margin-top: 15px;
    padding: 0px;
    font-size: 80%;
    color: #888;
    background-color: #EEE
}

/* footer navigation */

footer nav ul {
    margin: 0;
    padding: 0;
    background-color: #ffffff;
    overflow: auto;
    list-style-type: none;
}

footer nav li {
    height: 1.5em;
    float: left;
    margin-right: 0px;
    border-right: 1px solid #aaa;
    padding: 0 20px;
}

footer nav li:last-child {
    border-right: none;
}

footer nav li:hover {
    background: #FFF;
    color: #888;
}
/* only for bullet list next to wrapped figure
ul {
    list-style-position: inside;
}
*/

/* list with images and headings */

.image-list {
    margin: 0;
    padding: 0;
    list-style-type: none;
}

.image-list li {
    padding: 5px;
    overflow: auto;
}

.image-list li img {
    width: 100px;
    float: left;
    margin: 0 15px 0 0;
    background: white;
}

.image-list li p {
    margin: 0px;
}

.image-list li h4 {
    margin: 5px;
    clear: none;
}

/* list with images and text under them */


/* must be without ul to work */
.logo-list {
    list-style-type: none;
    overflow: auto;
    margin: 0px;
    padding: 0px;
}

.logo-list li {
    float: left;
    text-align: center;
    width: 150px;
    padding: 20px;
}

.logo-list li img {
    height: 100px;
}

.logo-list p {
    margin: 0px;
    padding: 0px;
}

/* bigger padding for dd */

dd {
    padding: 4px;
}

/* show more from the long list button */

.more-button {
    margin-left: 90px;
    /*text-transform:uppercase;*/
    font-size:110%;
    color: rgb(128, 128, 128) !important
}

.center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 90%;
}

.wrap {
    float: left;
}

figure .video {
    width: 100%;
    height: 345px;
    background-color: #ffffff;
}

figure .image {
    width: 100%;
}

figure {
    text-align: center;
    display: table;
    max-width: 50%; /* demo; set some amount (px or %) if you can */
    margin: 10px auto; /* not needed unless you want centered */
}

iframe {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

b {
	color:#444;
}

img.displayed {
    display: block;
    margin-left: auto;
    margin-right: auto }
"""

# CSS layout template 
layout_template = """
html, body {
    height: 100%;
}

body {
    margin: 0;
    padding: 0;
}


#container
{
    position: relative;
    margin: 0 auto;
    padding-left: 10px;
    padding-right: 10px;
    width: 760px;
    background-color: white;
    height:auto !important;
    min-height:100%;
    border-style:solid;
    border-bottom-width:1px;
    border-top-width:1px;
    border-left-width:10px;
    border-right-width:10px;
    border-color: #DDDDDD;
}


#header-image {
    width: auto;
    background-position: center top;
    vertical-align: bottom;
}
"""



# HTML template for the header of a report
start_template = """
<html>
<head>
<title>{title}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link href="layout.css" rel="stylesheet" type="text/css" media="screen">
<link href="style.css" rel="stylesheet" type="text/css" media="screen">
</head>
<div id="outercontainer">
<div id="container">
<body>
<header>
<div id="header-image"><p>{title}</p></div>
<!--
<nav>
<ul class="nav">
<li><a href="index.html">About</a></li>
<li><a href="research.html">Research</a></li>
<li><a href="publications.html">Publications</a></li>
<li><a href="teaching.html">Teaching</a></li>
</ul>
</nav
-->
</header> 
<main>
"""

# HTML template for adding a raster to a report
raster_template = """
<h2>{raster_title}</h2>
<h3>Statistics</h3>
<table>
<tr><td>Min</td><td>{min}</td>
<tr><td>Max</td><td>{max}</td>
<tr><td>Mean</td><td>{mean}</td>
<tr><td>Variance</td><td>{var}</td>
</table>
<h3>Map</h3>
<p style="text-align:center;">
<img src="{name}.png">
</p>
"""

# HTML template for ending a report
end_template = """
</main>
</body>
</html>
"""

def main():

    # set rendering directory
    directory = os.path.normpath("C:/Users/Brendan/Documents/grassdata/rendering/fusion")
    
    # files
    html_file = "report.html"
    style = "style.css"
    layout = "layout.css"
    fullpath_html = os.path.join(directory,html_file)
    fullpath_style = os.path.join(directory,style)
    fullpath_layout = os.path.join(directory,layout)

    # initialize a dictionary for each category of raster
    cats = defaultdict(list)

    # loop through the elevation, slope, aspect, pca, depth, stddev, variance, and coeff maps
    categories = ["fusion"]
    for category in categories:
        
        # variables
        pattern = category+"*"

        # get list of rasters
        rasters = gscript.list_strings('raster', pattern=pattern)
    
        # iterate through the list of rasters
        for raster in rasters:

            # add values to dictionary
            cats[category].append(raster)

    # template variables
    title = "lidar-uav fusion"

    # write to a css file using the style template
    with open(fullpath_style, 'w') as output:
        output.write(style_template.replace("background_image",background_image))
        
    # write to a css file using the layout template
    with open(fullpath_layout, 'w') as output:
        output.write(layout_template)

    # write to an html file using templates
    with open(fullpath_html, 'w') as output:

            output.write(start_template.format(title=title))
        
            for category in categories:
                for raster in cats[category]:
                    
                    # compute univariate statistics                    
                    stat = gscript.parse_command('r.univar', map=raster, flags='g')
                    
                    # partition raster name
                    name, separator, mapset = raster.partition('@')

                    # write html
                    output.write(raster_template.format(
                        raster_title=raster, name=name, min=stat['min'], max=stat['max'], mean=stat['mean'], var=stat['variance']))
                        
            output.write(end_template)

if __name__ == "__main__":
    main()