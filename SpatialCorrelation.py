from distutils.log import info
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pysal.lib import weights
from esda.moran import Moran, Moran_Local
from splot.esda import moran_scatterplot, plot_moran, lisa_cluster
from shapely.geometry import Point, Polygon

#inspired by: https://builtin.com/data-science/exploratory-spatial-data-analysis-esda, 
# combining dataframes: https://towardsdatascience.com/exploratory-spatial-data-analysis-esda-spatial-autocorrelation-7592edcbef9a
#https://towardsdatascience.com/plotting-maps-with-geopandas-428c97295a73
#overall file:
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

df = data.loc[:5000,['munic','ETHANOLrp','longitude', 'latitude']].dropna()

#munics we want to drop:
df_drop = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/df_merged.csv')

#Step 1: All municipalities
munic_map = gpd.read_file('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/BR_Municipios_2020/BR_Municipios_2020.shp')
munic_map.to_crs(epsg=4326).plot()

crs = {'init':'EPSG:4326'}
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)

fig, ax = plt.subplots(figsize = (10,10))
munic_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
munic_map.plot(ax=ax, color='purple')
geo_df.plot(ax=ax)
ax.set_title('Municipalities')

fig, ax = plt.subplots(figsize = (10,10))
munic_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
geo_df.plot(ax=ax, alpha = .1 )

ax.set_title('Municipalities')
plt.savefig('Municipalities')
plt.show()

#step 2: munics we want to drop (list not final yet!)
geometry = [Point(xy) for xy in zip(df_drop['longitude'], df_drop['latitude'])]
geo_df2 = gpd.GeoDataFrame(df_drop, crs = crs, geometry = geometry)

fig, ax = plt.subplots(figsize = (10,10))
munic_map.to_crs(epsg=4326).plot(ax=ax, color='red')
munic_map.plot(ax=ax, color='black')
geo_df2.plot(ax=ax)
ax.set_title('Municipalities_drop')

fig, ax = plt.subplots(figsize = (10,10))
munic_map.to_crs(epsg=4326).plot(ax=ax, color='pink')
geo_df2.plot(ax=ax, alpha = .1 )

ax.set_title('Municipalities_Drop')
plt.savefig('Municipalities_drop')
plt.show()