
# 08-Earthquakes

## Quiz

* unittest and classes

## Project

* Update on discussions with Andrew Butcher
* We have a story and some data
* Now we can figure out what to do with them

## Collaborative assignment (Due 22 Mar)

* Create the gh-pages version
* Add this result [bridget_dev_final](https://github.com/ds5010/vaccines/tree/bridget_dev_final)
  * Make as few changes to the dataflow as possible
  * Implement a DRY strategy
  * Add unittests...?
  * Improve modularity...?
* Improve visualization of time
  * For example: [Bar Chart Race, Explained](https://observablehq.com/@d3/bar-chart-race-explained)

## Earthquakes

* [earthquakes](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
* [json](https://docs.python.org/3/library/json.html)
* [requests](https://docs.python-requests.org/en/latest/)
* **STOPPED HERE**
* [matplotlib basemap](https://matplotlib.org/basemap/index.html)
* notebook: [earthquakes.ipynb](./notebooks/earthquakes.ipynb)

## Scope

* First question in the quiz refers to "local", "global" and "nonlocal" keywords
  * The example is here: https://docs.python.org/3/tutorial/classes.html#private-variables
    * A question came up in class regarding use of the "nonlocal" keyword
    * In response to the question -- try commenting the line `spam = "test spam"`
    * After commenting that line, the line `nonlocal spam` throws "SyntaxError: no binding for nonlocal 'spam' found"
  * https://peps.python.org/pep-3104
    * the proposal addresses a shortcoming in ability to access names in outer scope
    * describes the historical issue that gave rise to the "nonlocal" keyword
    * includes comparison with other languages (JavaScript, Perl, Ruby, C, C#, etc.)
    * https://www.destroyallsoftware.com/talks/wat -- Wat talk

## GeoPandas

* notebook: [geopandas.ipynb](./notebooks/geopandas.ipynb)

## Unit testing

* [unittest.md](./unittest.md)
* [my_vaccines](https://github.com/pbogden/my_vaccines)
* TODO: Scope out roles and responsibilities for the collaborative assignment (above)
