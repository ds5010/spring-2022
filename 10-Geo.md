
# 10-Geo

* Geospatial in Python builds on remarkably powerful open source libraries written in C and C++.
* Environments help to avoid potential install/dependency challenges when developing locally.
* Things tend to work pretty well in Colab for protyping.

## GeoPandas

* [Introduction](https://geopandas.org/en/stable/getting_started/introduction.html)
  * Getting started docs have some simple examples
* Dependencies
  * GEOS, GDAL, PROJ -- open source stack
  * C and C++ libraries "can sometimes be a challenge to install" -- UNDERSTATMENT!
* WARNING: Installation can be a challenge because of the C-library dependencies (GEOS, GDAL, PROJ)!!
  * GeoPandas works in Colab (see install instructions below)
  * However, desktop install may well be problematic. In my experience (on a Mac)...
    * `conda install geopandas` takes a long time...and it does **not** work.
    * GeoPandas works on the desktop (see install instructions below), except for [interactive mapping](https://geopandas.org/en/stable/docs/user_guide/interactive_mapping.html).
    * GeoPandas.explore(), which provides interactive mapping with Folium, does **not** work on the desktop.
    * However, [Folium](https://python-visualization.github.io/folium/) does work on its own!

## Folium

Folium is Leaflet for Python -- Leaflet is a popular open source JavaScript slipyy-map library.

* [Folium](https://python-visualization.github.io/folium/) -- github.io
* [Folium install](https://python-visualization.github.io/folium/installing.html)
* Note: `conda install folium` is **not** a recommended install option.
  * See below for desktop & Colab installs
* Note: [contributing](https://github.com/python-visualization/folium/blob/main/.github/CONTRIBUTING.md)
  * (Re)introducing the world of open source
  * Imposter syndrome
  * The "little voice inside your head"
* Interactive mapping on the desktop
  * [PyQt](https://riverbankcomputing.com/software/pyqt)
  * [Folium & Qt](https://stackoverflow.com/questions/58590199/how-to-show-folium-map-inside-a-pyqt5-gui)

## Colab install

Install with pip in Colab -- it's that easy. No need to deal with environments.

```
!pip install geopandas
```

* The `.explore()` method uses Leaflet, for which you'll need Folium
* [Folium](https://python-visualization.github.io/folium/) -- gh-pages
* Warning: [Colab needs the latest folium](https://github.com/geopandas/geopandas/issues/2187)
  * Google helps you find this!
  * Google the error message and add "geopandas"

```
# Be careful to use the "-U" option with folium
!pip install folium -U
!pip install mapclassify
```

## Desktop install

Introducing [Conda "environments"](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)

* The following is my experience on a Mac, your mileage may differ...
  * No guarantees for folks using Windoze
* Create a fresh environment (don't install in "base")
* Install from [conda-forge](https://conda-forge.org/docs/)
  ```
  conda create -name geo
  conda activate geo
  conda install --channel conda-forge geopandas
  conda install -c conda-forge pyqt
  ```
* Note: Folium is installed automatically via conda-forge
* Activate the environment: `conda activate geo`
  * Once you activate the environment to use geopandas from the command line.
  * However, getting Jupyter notebooks to recognize your environment can be a challenge! (I haven't gotten it to work.)
* Deactivate the environment: `conda deactivate geo`

## GeoPandas demo

In Python, you can import

```
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
```

Then read and visualize a zipped GeoJSON file with GeoPandas
```
url = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/density-of-unserved-may-be-layer-UKtUhvoEC95KBH6HsnWIU.zip"

gdf = gpd.read_file(url);
```

In Colab, the next line (if it's last) will render data (the geometry) from the first row:

```
gdf['geometry'][0]
```

Render the entire geopandas dataframe

```
gdf.plot()
```

Render the dataframe with a colormap and legend

```
# Use the "area" column to create a colormap
df.plot("area", legend=True)
```

## src

The 3 files in `./src` have the following demos:

* Choropleth map using Folium and Qt
  * `python -B src/choropleth.py`
* GeoPandas demo using broadband GeoJSON -- works on desktop
  * `python -B src/app.py`
* Folium Stamen demo
  * `python -B src/demo.py`

## docs

* The files in `./docs` have bootstrap demos
* Templates for gh-pages -- the vaccines and broadband projects
* One of them show how to embed a Leaflet app created with Folium
* [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML) has links to tutorials -- mozilla.org

## Broadband project

[braodband.md](broadband.md)
