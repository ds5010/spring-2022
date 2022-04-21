
# todo

TODO list for the broadband project, now that we have data...

* Add UI element to select type -- DONE
* Clean up the README -- DONE
* Add a gh-pages site via settings -- main branch, ./docs directory -- DONE
* Create a bootstrap framework for the web page -- DONE
  * Note: started with the vaccines project -- that HTML should be cleaned up
  * Added bootstrap's javascript for a responsive navbar
  * Note: difference between .container and .container-fluid for navbar
  * Note: you can use relative paths for images
  * Note: make sure to close tags
    * Debugging HTML and CSS is a pain!!
    * Indenting is important -- you can break things without throwing an error
  * Added some HTML comments to help distinguish bootstrap rows & cols
  * Note: there is no "p-10" (found one in the acknowledgements)
  * Ref: [bootstrap examples](https://www.w3schools.com/bootstrap/bootstrap_examples.asp) -- w3schools
* Add "the story"
  * Replace "blah, blah, blah..."
  * Replace vaccines images with the "story" figures
  * Organization -- is the organization of the page correct?
* Initial condition
  * How should we start the page?
  * What prompting do we need so that a user knows the map is interactive?
* Other detail
  * Eligible is spelled wrong
  * Note URL construction -- If it isn't broken, don't fix it
* Performance
  * Cumberland county tier-4 is really big
  * tier-4 is big in all the southern counties 
* Colors -- need to implement colormaps (where we have them) to layers
* Labels for type -- need human-understandable labels (e.g., what does "may_unserved_density" mean?)
* Styling of "elegible"
  * what are we doing with it?
  * this layer is unlike the others -- it's a processed result
  * leave it out?
* Other...
  * Move the current content in "README.md" somewhere else -- README.md should focus on reproducibility and updating
  * Document data processing for reproducibility
  * Clean up source code -- put it in ./src
  * Clean up the index.html vaccines project
  * Better color-contrast for the lines (deaths/100k) on Bridget's chart (vaccines project)
  * Axis label on rhs of Bridget's chart should be "per 100k" instead of "per 1e5"
