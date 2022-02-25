
# 05-Collaborate

## Goals (Wednesday)

* Merge and visualize death & vaccine rates
* Practice debugging (data & code) with Pandas & Colab
* Review the collaborative development process

## Vaccine-effectiveness notebook

* Strategy
  * Break project into manageable/isolatable chunks
  * Prototype in Colab
  * Save working code to github
* [Vaccines.ipynb](./notebooks/Vaccines.ipynb)
  * Step 1: vaccine data (read/clean/sample)
  * Step 2: mortality data (read/clean/sample)
  * Step 3: Merge and plot datasets
    * scatterplot of deaths vs vaccination by county

## Deal with missing data

* "Catch" the analysis error and add a print statement to diagnose the problem
  * try/except blocks can be incredibly helpful
  * [8. Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html) tutorial -- python.org
  * We're debugging the data, as opposed to debugging the code
* FIPS = "UNK" is the missing data value in the CDC dataframe
  * You won't see any of these if you cleaned the CDC data beforehand
  * 89 bad values out of 3268 -- too few to worry about
* Missing data
  * [Working with missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html) -- pandas.pydata.org
  * [np.nan](https://numpy.org/doc/stable/user/misc.html) is a floating point number (WAT?) -- numpy.org
  * [pd.NA](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#experimental-na-scalar-to-denote-missing-values) is still experimental
  * [Handling missing data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html) -- jakevdp.github.io
    * None -- a Python object (that can't be stored as a floating point number)
    * NaN -- an IEEE floating point representation (Not a Number)
  * Why do I care?
    * None cannot be used in any arbitrary NumPy/Pandas array
      * only in arrays with data type 'object' (i.e., arrays of Python objects)
    * Pandas tries to make `None` and `NaN` interchangeable
      * [NaN and None in Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html#NaN-and-None-in-Pandas) -- jakevcp.github.io
