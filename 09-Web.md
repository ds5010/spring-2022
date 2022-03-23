
# 09-Web

* Review the vaccines project
* Data for the broadband project
* Web technologies & Python 

## Vaccines

* Progress update with the vaccines v2
* Issues that I saw:
  * https://github.com/ds5010/vaccines/issues/74 -- Test data
  * https://github.com/ds5010/vaccines/issues/75 -- FIPS and the leading zero problem
  * https://github.com/ds5010/vaccines/issues/67 -- Roadmap
* Misc
  * Make tests doesn't work
  * FIPS and the leading zero
  * Data isn't there
    * It's not clear how folks are updating the repo
  * .DS_Store files are there (but shouldn't be)
  * Use ".gitignore"
    * Consider an independent set of "install instructions"
    * Definitely use ".gitignore" for things like ".DS_Store"

## Vaccines v2 TODO

* Create a .gitignore file to deal with data source and misc files (e.g., .DS_Store)
* Clean up "make test" Makefile
* Integrate Bridget's visualization
  * It's working in Bridget's branch -- doesn't require changes to other data sources
  * Check to see if the code could be more concise
* gh-pages site -- add the new visuals
* Update the gh-pages story
* Lessons learned (for next time)
  * More effort on the roadmap
  * Don't be afraid to open issues 

## Web apps

* In R: 
  * [Shiny](https://shiny.rstudio.com/)
* In Python:
  * Interactive plotting packages
    * [Bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/server.html)
    * [Plotly](https://plotly.com/javascript/) and [Plotly.js](https://github.com/plotly/plotly.js)
    * [GeoPandas](https://geopandas.org/en/stable/)
  * Web apps
    * [Dash](https://plotly.com/dash/)
    * [Voila](https://github.com/voila-dashboards/voila)
      * [Documentation](https://voila.readthedocs.io/en/stable/)
      ```
      conda install -c conda-forge voila
      conda install -c conda-forge bqplot
      ```
      * Note: You can usually find the install syntax by Googling: conda package-name
      * [Usage instructions](https://voila.readthedocs.io/en/stable/using.html)
      ```
      git clone https://github.com/voila-dashboards/voila
      cd voila
      voila notebooks/bqplot.ipynb
      ```
  * Packaging software for deployment
      * https://www.docker.com/resources/what-container/
* Markdown:
  * gh-pages converts markdown to HTML, including styling with [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * [vaccines](ds5010.github.io/vaccines)
* HTML, CSS, JavaScript
  * Run you own [http server](https://docs.python.org/3/library/http.server.html) for local development
  ```
  python -m http.server
  ```
  * If you set up an application in github, then you can deploy it in the cloud with various services
  * heroku.com has been doing this for a while
  * If you don't require a "back end" and you do everything with web technologies (HTML, CSS, JavaScript), use gh-pages
  * For example: https://pbogden.github.io

## Broadband

Start digging into the data

* DOT's FTP site (from Colby): https://file.ac/IhnSFOnW5LU/
* EDA of that data
* Think about a class project and website
* You can't use geopandas on a website without a back end (Python is not a web technology)
