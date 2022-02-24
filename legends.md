
# Legends

* [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb) by Jake VanderPlas -- github
  * [4.00 -- Introduction to matplotlib](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html)
    * [Two interfaces for the price of one](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html#Two-Interfaces-for-the-Price-of-One)
    * Presents two different ways to create a simple figure with multiple sets of axes...
    * MATLAB-style interface
      * `plt.figure()`
      * `plt.subplot(2,2,1)`
      * `plt.plot(x, np.sin(x))`
    * Object-oriented interface uses Figure and Axes objects with their associated methods
      * `fig, ax = plt.subplots(2)`
    * [Aside: Matplotlib gotchas](https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html#Aside:-Matplotlib-Gotchas)

## Matplotlib scatterplots & legends 

* [matplotlib.pyplot.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html) API reference
  * [matplotlib artist](https://matplotlib.org/stable/api/artist_api.html) API reference with inheritance diagram
* [matplotlib custom legends](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html) gallery demo
  * this shows several levels of customization
  * simplest uses defaults, more complex uses the API
* [Scatterplot with a legend](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html) 
  * First example uses user-specified labels
    * legend elements are based on 3 values for "label" created in the for loop
    * 3rd dimension: dot sizes are continuous, but the legend doesn't show sizes
* [Scatterplot with automatically generated (guessed) labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#automated-legend-creation) 
    * The second example has a legend based on size
    * The third example uses user-specified legend elements and parameters
      * Uses [\*args and \*\*kwargs idiom](https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters) -- stackoverflow
    * Also uses lambda function (sends a function as an argument)

## Vaccines demo

Reproduce the scatterplot from before -- this code snippet works in Colab
```
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/ds5010/spring-2022/main/data/merge.csv"
df = pd.read_csv(url, converters={'FIPS' : str})

df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

xlabel = 'Series_Complete_18PlusPop_Pct'
ylabel = 'Deaths_Per_1e5'

x = df[xlabel]
y = df[ylabel]
area = df['Census2019_18PlusPop'] / 1e4

fig, ax = plt.subplots()
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(0,100)
ax.set_ylim(0,500)
fig.set_size_inches(8,8)

scatter = ax.scatter(x, y, s=area, alpha=0.5)

# produce a legend with a cross section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
ax.legend(handles, labels, loc="upper right", title="Population Sizes (x10k)", labelspacing=2, borderpad=1);
```

## Customizing matplotlib legends

* [04-06 Customizing Legends](https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html)
  * Check cell #9
* Following snippet (modified slightly from the book) runs in Colab
  * Note warning if you uncomment the `plt.axis(aspect='equal')` line
```
import pandas as pd
# import numpy as np

base = "https://github.com/jakevdp/PythonDataScienceHandbook/raw/master/notebooks/"
cities = pd.read_csv(base + 'data/california_cities.csv')

# Extract the data we're interested in
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
# plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# Here we create a legend:
# we'll plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area,
                label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')

plt.title('California Cities: Area and Population');
```

# Seaborn scatterplots

* [4.14 -- Visualization with seaborn](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.14-Visualization-With-Seaborn.ipynb)
* [seaborn.scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) API reference
* [Controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html) -- seaborn tutorial
  * This customizes seaborn with matplotlib
* Following example demonstrates scatterplot with vaccines data
  * Following code snippet works in Colab
  * It could use some help (scales, limits, colors, etc.), but the demo works
```
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/ds5010/spring-2022/main/data/merge.csv"
df = pd.read_csv(url, converters={'FIPS' : str})

df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

xlabel = 'Series_Complete_18PlusPop_Pct'
ylabel = 'Deaths_Per_1e5'
area = df['Census2019_18PlusPop'] / 1e4

fig, ax = plt.subplots(figsize=(10,10))
sns.scatterplot(
    data=df, x=xlabel, y=ylabel, hue=area, size=area,
    sizes=(10, 200), legend="brief", ax=ax
);
```
