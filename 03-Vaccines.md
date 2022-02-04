
# 03-Vaccines

* 3 Feb is Job Fair -- nobody goes after 7pm -- plan on 6-7 optional, with 7-7:30 class.
  * http://rouxevents.northeastern.edu/roux-virtual-networking-winter22-employers
* Last week
  * Got as far as "need to float the strings" with the iris dataset.
  * Homework assignment: finish the exercises -- iris project and penguins project
  * Provided guidance on creating a good data-project repo in github (allisonhorst penguins template)

## Homework solution/discussion

* Review and discuss solutions
* https://github.com/ds5010/assignment02-solution
* Matplotlib references
  * [matplotlib scatterplot](https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html)
    * Example of scatterplot with data-dependent size and color
    * Note: Tick marks & axis limits are automatic but there are no axis labels, legends or any other annotation
  * [Basic usage](https://matplotlib.org/stable/tutorials/introductory/usage.html)
    * Shows how to use: `fig, ax = plt.subplots()  # Create a figure containing a single axes.`
    * Shows the anatomy of figure & axes objects
    * Once you have a handle to the axes, shows how to add labels, title and legend
  * [matplotlib.axes](https://matplotlib.org/stable/api/axes_api.html)
    * Detailed API reference

## Case study: Vaccine effectiveness

Learning goals

* Data aquisition
* Documentating provenance
* Well organized project repository

Discussion

* Discuss goals -- county-level information
  * Today's (2 Feb 2022) headline on the NY Times: "U.S. has far higher COVID death rate than other wealthy countries"
  * Relevant commentary from FiveThirtyEight: ["The COVID-19 Metrics Policymakers Should Be Watching After Omicron"](https://fivethirtyeight.com/features/the-covid-19-metrics-policymakers-should-be-watching-after-omicron/)
  * Q: Why are things so bad in the U.S.? Are the vaccines effective? 
  * Q: What are the socio-economic issues?
* [COVID-19 Incidents and Death Rates](https://www.cdc.gov/mmwr/volumes/71/wr/mm7104e2.htm) -- cdc.gov
  * [Covid Data Tracker](https://covid.cdc.gov/covid-data-tracker/#vaccinations_vacc-total-admin-rate-total) -- cdc.gov
    * Table 2 (about 2/3 of the way down the page) shows average cases & deaths
    * Top half of the table is cases, broken down by various factors (incidents/100K)
    * Bottom half of the table is deaths, broken down by various factors (incidents/100K)
    * 70 times higher chance of death for unvaccinated compared to boosted -- Oct-Nov 2021
  * Q: Next steps?
* Get started with CDC -- review the website
  * Download and process CDC data -- [covid](../../topics/covid)

## In-class exercises

* What story would you like to tell?  What question(s) would you like to answer?
* Decide on the data to use
  * What fields?
  * What dates?
* [COVID-19 vaccinations by county](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh)
* Issues/Questions:
  * What's FIPS?

