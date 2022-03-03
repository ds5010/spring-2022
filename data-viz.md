## Data viz in Python

[Python data visualization 2018: Why so many libraries](https://www.anaconda.com/blog/python-data-visualization-2018-why-so-many-libraries)

### Data science in a browser

* Python
  * [Google Colab](https://colab.research.google.com/) -- Jupyter notebook on steroids, with a big-data back end and no configuration.
  * [Plotly.com](https://plotly.com/) -- "AI, ML, and Python analytics for business at 5% the cost of a full-stack approach."
    * Under the hood, data visualization uses web technologies.
* [R](https://ggplot2.tidyverse.org/) -- R Studio, R Shiny
  * [R Studio](https://shiny.rstudio.com/) is the R counterpart.
  * "Shiny apps are easy to write. No web development skills are required."
  * Under the hood, data visualization uses web technologies.
* JavaScript -- [Observable](https://observablehq.com/) -- by Mike Bostock (creator of D3)
  * This is it -- there's no hood to look under!

### Observable

* Exploratory data analysis
  * [Scatterplot matrix](https://observablehq.com/@d3/brushable-scatterplot-matrix?collection=@d3/d3-brush)
  * [Observable Plot](https://observablehq.com/@observablehq/plot)
  * [Dashboards](https://observablehq.com/@mbostock/dashboard)
  * [Mona Lisa Histogram](https://observablehq.com/@d3/mona-lisa-histogram)
* Teaching
  * [Sorting algorithms](https://observablehq.com/@tmcw/sorting-overview?collection=@tmcw/sorting-algorithms)
  * [Bridgeson's algorithm](https://observablehq.com/@mbostock/bridsons-algorithm)
  * [Shuffling algorithm](https://observablehq.com/@mbostock/visualizing-order)
  * [Linked Lists](https://observablehq.com/@mbostock/linked-lists?collection=@mbostock/data-structures)
  * [Golden ratio](https://observablehq.com/@mbostock/golden-mona-lisa)
* Geospatial analysis, modeling, collaboration, etc., etc.
  * [Streaming shapefiles](https://observablehq.com/@mbostock/streaming-shapefiles)
  * [Fluid physics](https://observablehq.com/@mbostock/liquidfun)
  * [Dynamical systems](https://observablehq.com/@mbostock/de-jong-attractor-ii?collection=@observablehq/webgl)
  * [Hello, Three.js!](https://observablehq.com/@mbostock/hello-three-js)
  * [Deck.gl](https://observablehq.com/@pessimistress/deck-gl-tutorial?collection=@pessimistress/deck-gl-tutorials)
  * [Scatter-gl](https://observablehq.com/d/386845a4a17cfb25?collection=@pbogden/3d) from [tensorflow.org](http://projector.tensorflow.org/)
* Data science, ML, AI, etc.
* Collaboration and innovation!
* "We’re building from the bottom up to retain expressiveness, creativity, and flexibility."
  * "We can reduce effort...Less work to prepare, and less to perform."
  * "Reducing effort is incredibly exciting because it doesn’t just save time, it changes who engages in a task, and when!"

### Numpy, Pandas, Seaborn

* [numpy](https://numpy.org/)
  * Check out the case studies: first image of a black hole, gravitational waves, cricket analytics, deep learning
  * Each case study discusses data "size" and includes a chart of software dependencies
  * This is cutting-edge data science (with really big data)
* [pandas](https://pandas.pydata.org/) 
  * A cross between Numpy, spreadsheets and RDBMS
  * [Introduction](https://pandas.pydata.org/about/index.html) -- began in 2008 at AQR Capital Management
  * [Wes McKiney and team](https://pandas.pydata.org/about/team.html)
* [seaborn](https://seaborn.pydata.org/index.html)
  * [Statistical data visualization](https://seaborn.pydata.org/index.html)

### Pandas

* [Python for Data Analysis, 3rd Ed](https://learning.oreilly.com/library/view/python-for-data/9781098104023)
  * "pandas blends array-computing ideas of NumPy with the data manipulation capabilities of spreadsheets and relational dideas atabases (such as SQL)."
    * What kind of data?
    * [this kind](https://learning.oreilly.com/library/view/python-for-data/9781098104023/ch01.html#intro_what_kind_of_data)
      * Tabular/spreadsheet and columns of similar type (string, numeric, date, or otherwise). 
      * Multidimensional arrays (matrices).
      * Multiple tables of data interrelated by key columns (what would be primary or foreign keys for a SQL user).
      * Evenly or unevenly spaced time series.
  * Two key structures: [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) & 
[Dataframe](https://pandas.pydata.org/docs/reference/frame.html)
* [In-memory database-style joining and merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging)

### Seaborn

* Seaborn overview
  * [Overview](https://seaborn.pydata.org/tutorial/function_overview.html)
  * Plot types (modules): “relational”, “distributional”, and “categorical” 
* [Data structures accepted by Seaborn](https://seaborn.pydata.org/tutorial/data_structure.html)
  * Long-form & wide form "tidy" datasets
* [Tutorial](https://seaborn.pydata.org/tutorial.html)
  * Nice overview of statistical data viz
* [figure-level vs axes-level functions](https://seaborn.pydata.org/tutorial/function_overview.html#figure-level-vs-axes-level-functions)
  * "Matplotlib offers good support for making figures with multiple axes; seaborn builds on top of this to directly link the structure of the plot to the structure of your dataset."
  * [Mutiplot grids](https://seaborn.pydata.org/tutorial/axis_grids.html) tutorial
    * [seaborn.displot](https://seaborn.pydata.org/generated/seaborn.displot.html) API reference
* FacetGrid is a seaborn class that enables "faceting"
  * "facet" (the verb): look simultaneously at the various dimensions ("facets" -- the noun) of your dataset
  * [seaborn.FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) API reference
  * [scatterplot with continuous hues & sizes](https://seaborn.pydata.org/examples/scatterplot_sizes.html) example
  * [FaceGrid.map_dataframe()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html) API reference
