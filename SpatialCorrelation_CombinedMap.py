from cmath import nan
import numbers
import pandas as pd
import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from shapely.geometry import Point
#credit to: https://stackoverflow.com/questions/38882233/geopandas-matplotlib-plot-custom-colors

#overall file:
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
df = data.loc[:10000,['munic','ETHANOLrp','longitude', 'latitude']].dropna()
df['munic'] = df['munic'].drop_duplicates()

#munics we want to drop:
df_drop = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/df_merged.csv')

#merge the two files and add a column to determine which ones we drop
df_all = pd.merge(df, df_drop, how = 'outer')

#Plot all municipalities
munic_map = gpd.read_file('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/BR_Municipios_2020/BR_Municipios_2020.shp')

crs = {'init':'EPSG:4326'}
geometry = [Point(xy) for xy in zip(df_all['longitude'], df_all['latitude'])]
geo_df = gpd.GeoDataFrame(df_all, crs = crs, geometry = geometry )

#df_all.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/munic_map.csv')
print(geo_df)

#geht nicht, weil bisher nichts übergeben wird
cmap = LinearSegmentedColormap.from_list('mycmap', [(nan, 'grey'), (numbers, 'blue')])
cdict = LinearSegmentedColormap
geo_df.plot(column='count', cmap=cmap)

fig, ax = plt.subplots(figsize = (10,10))
munic_map.to_crs(epsg=4326).plot(ax=ax, color='pink')
geo_df.plot(ax=ax, alpha = .1 )

geo_df.plot(ax=ax, alpha = .1 )

ax.set_title('Municipalities_all')
plt.savefig('Municipalities_all')
plt.show()