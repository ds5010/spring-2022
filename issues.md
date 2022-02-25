
# Issues

Key ingredients: the story and the data

## TODO

* Get the story straight
* Get the data workflow straightened out and documented -- from acquisition to visualization
* Update the roadmap and assign roles and responsibilities

## The story

* Vaccine effectiveness...?
  * Is this our story? If so, define it?  If not, then what?
  * We are investigating relationship between deaths and vaccination-status at the county-level
  * Are we investigating vaccine effectiveness? 
  * [CDC research](https://www.cdc.gov/vaccines/covid-19/effectiveness-research/protocols.html)
  * [Vaccine effectiveness](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/effectiveness/index.html)
  * [COVID-19 Deaths by Vaccination Status](https://covid.cdc.gov/covid-data-tracker/#rates-by-vaccine-status)
    * Bridget's analysis shares aspects of this approach.
    * She discussed potential flaws in the interpretation.
* Scatterplot of merged data
  * Whatever it is, it's a compelling visualization that raises a lot of questions
* Time evolution
  * Even more compelling
  * How should we present it?
* Animation of scatterplots
  * [imageio](https://github.com/imageio/imageio) -- github
  * This seems like an actively maintained and well-documented project
  * [Documentation](https://imageio.readthedocs.io/en/stable/) -- readthedocs.io
  * [animated gi2 f](https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python) -- stackoverflow
* Time series?
  * Bridget's analysis is compelling and simple, regardless of caveats (stimulates creation of more questions)
  * Should be simple and/or reference an authoritative source.
* Choropleth maps
* Anything else?

## The data

* CDC data
  * % vaccinated & population for a specific date and all counties
  * GOOD: both vaccination and population are available from this one source
  * BAD: the date is hard-wired into the code
* JHU data
  * Deaths -- total deaths per 100K for a range of dates
  * BAD: Varying date parameters is a challenge (hard wired)
  * Duplication of code (copying and pasting to make only a small change)
* Merge data by county
  * FIPS is critical
  * Pandas Dataframe makes it particularly easy
* Anything else?

## Roadmap

* Update ROADMAP.md
1. CDC data (vaccinations, population, FIPS, etc.) for specified date(s)
  * Format of the output/return value
  * Should it be a function or a script?
  * What needs to be specified on the command line vs hard-wired?
  * What other details?
2. JHU data 
  * Format of the output/return value
  * Should it be a function or a script?
  * What needs to be specified on the command line vs hard-wired?
  * What other details?
3. README content
  * Overview -- what's our story?  Vaccine effectiveness?  If so, what is it?  If not, then what? (see below)
  * Reproducibility
  * Attribution/references! -- authoritative references, not blog/stackoverflow posts
  * Primary results, explanation, caveats.
  * Keep it concise -- you have a sophisticated audience and you don't want to risk a TL;DR
  * What else?
4. Merging
  * How should it be done -- separate script?
5. Scatterplot
  * Reproduce the one from class, at a minimum
6. Time sequence
  * What is it and how to create it
7. Animation
  * Create an animated GIF?
  * Use [imageio](https://imageio.readthedocs.io/en/stable/) -- readthedocs
  * [imagio](https://github.com/imageio/imageio) -- github
  * [stackoverflow](https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python) post by a software developer who recommends imageio
    * be careful in general, but this is a common package
    * `import imageio` should be possible with the baseline anaconda distribution
8. Clean up the repository
  * remove unused files (e.g., SCHEDULE.md, data copied from JHU)
* Assign responsibilities
  * If they can be clearly defined, put them in the ROADMAP
  * If discussion needs to occur, put them in "issues"
  * If someone is going to...
    * raise an issue, then they'll need to monitor it
    * modify "main", then they need to be sure there are no conflicts or changes to data people might be using
  * Tag the current branch -- in case folks are using the code
  * Show how to use tags and tag a stable version of the main branch
