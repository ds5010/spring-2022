
# 04-Vaccines

Case study: Vaccine effectiveness (continued)

## Learning goals

* Data aquisition & pre-processing
* Documenting provenance
* Creating a well-organized project repo

## Debugging

* Some students don't know how to debug their code.
* It seems that VSCode encourages you to run entire scripts all at once (I'm not a VSCode user)
* You need the discipline of breaking things apart that you can analyze on their own
* Otherwise, you can spend way too much time trying to "fix" things that aren't relevant. 
* When I debug my code, I'll often run code line by line and check the result of each line. 
* ALSO: 
  * Sometimes it make sense to have someone else look at your code, or to just step away for a while.
  * Are your variables set correctly?  Today's date is not "02/9/2021", for example.
  * Have you cast your strings to numbers where appropriate?

## Mention...

* Pushing from the command line with [github personal access tokens](github_tokens.md)
* How to ask a question -- see stackoverflow link on [01-Intro.md](./01-Intro.md)
* Requirements and dependencies
  * For users: Make it clear how to install/run the code
    * You shouldn't insert commands that install software with pip or otherwise -- e.g., Makfile yikes experience!!
    * But you should mention the necessary dependencies (e.g., with import code, etc.)
  * For developers: see below
* For example: [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas
  * This book is about 5 years old, but much of the code won't run 
  * [Jupyter/Colab notebooks](https://github.com/jakevdp/PythonDataScienceHandbook) -- github.com

## Review...

* Goals -- county-level information
* [COVID-19 Incidents and Death Rates](https://www.cdc.gov/mmwr/volumes/71/wr/mm7104e2.htm) -- cdc.gov
  * [Covid Data Tracker](https://covid.cdc.gov/covid-data-tracker/#vaccinations_vacc-total-admin-rate-total) -- cdc.gov
    * Table 2 (about 2/3 of the way down the page) shows average cases & deaths
    * Top half of the table is cases, broken down by various factors (incidents/100K)
    * Bottom half of the table is deaths, broken down by various factors (incidents/100K)
    * 70 times higher chance of death for unvaccinated compared to boosted -- Oct-Nov 2021
* Next steps
  * Download and process CDC data -- [covid](../../topics/covid)
  * What story would you like to tell?  What question(s) would you like to answer?
    * [COVID-19 vaccinations by county](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh)
  * Decide on the data to use
    * Which fields?
    * Which dates?
    * What's a FIPS?

## Processing CDC data

* Review student assignments
* Review the contents of [vaccines](../../topics/covid/vaccines)

## Vaccine effectiveness

Continuing from Wednesday...

* We've seen county-level data on vaccination rate.
  * How can we investigate the relationship between COVID-related deaths and vaccination rate?
  * What data do we need and what questions will we be able to investigate?
  * Recall that we're interested in county-level information
    * Rationale/working hypothesis: variation by county can be used to investigate effectiveness
* New data source: [COVID Daily reports](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)
* Next steps: 
  * Goal: Visualize vaccine effectiveness
  * Create a single project repository for accessing, processing and visualizing the data.
  * Documenting everything.
  * Use a collaborative development model
  * Individuals will develop code on their own and contribute via pull requests
  * Everyone will comment on the requests
  * Discuss requests, features, bugs on github
  * Ask questions on piazza
* TODO: Collect some ideas
  * vaccination rate vs death rate
  * [Scatterplot](https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html)
  * [Choropleth](https://observablehq.com/@d3/choropleth)

## A well-organized repo

Case study: [Pandas on github](./pandas_on_github.md)

## Collaborative development

* Project repo
  * https://github.com/ds5010/vaccines
  * everyone should have access
  * Discuss pull requests on github
  * Discuss issues & feature requests on github
  * Use Piazza to ask for help on something that's not in the repo.
  * TODO: Decide on a collaborative development model
* [Pull requests](https://docs.github.com/en/pull-requests)
  * [Committing changes to your project](https://docs.github.com/en/pull-requests/committing-changes-to-your-project)
  * [Collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
    * [About collaborative development models](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models)
* [Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
  * [Contributing to projects (with forks)](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
  * [Create a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
