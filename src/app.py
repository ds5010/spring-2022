# GeoPandas demo using broadband GeoJSON -- works on the desktop
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pbogden/broadband/master/zipfiles/density-of-unserved-may-be-layer-UKtUhvoEC95KBH6HsnWIU.zip"

gdf = gpd.read_file(url);

gdf.plot()
plt.show();
