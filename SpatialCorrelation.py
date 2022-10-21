import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import SubperiodsPaths as spp
import SubperiodsDates as spd

#inspired by: https://builtin.com/data-science/exploratory-spatial-data-analysis-esda, 
#https://towardsdatascience.com/plotting-maps-with-geopandas-428c97295a73

all_df = spp.getAllSubP_afterdrop2()
subperiodnames = spd.SubperiodsNames

map_brazil = gpd.read_file(spp.getMapBrazilPath())
map_brazil.to_crs(epsg=4326)

crs = {'init':'EPSG:4326'}

"""for i in range(len(all_df)):
    df = all_df[i]
    
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)
    fig, ax = plt.subplots(figsize = (10,10))
    map_brazil.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
    map_brazil.plot(ax=ax)
    geo_df.plot(ax=ax)
    
    fig, ax = plt.subplots(figsize = (10,10))
    map_brazil.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
    geo_df.plot(ax=ax, alpha = .1 )
    
    ax.set_title('Municipalities' + subperiodnames[i])
    plt.savefig('Municipalities' + subperiodnames[i])
"""

#missing municipalities summer 2015 --> looks at the original dataframe on aug 29th, 2015
df1 = spp.getOriginalFile()
df1 = df1[df1['fdate']=='2015-08-29']
df1 = df1[df1['ETHANOLrp'].isna()]


geometry = [Point(xy) for xy in zip(df1['longitude'], df1['latitude'])]
geo_df = gpd.GeoDataFrame(df1, crs = crs, geometry = geometry)
fig, ax = plt.subplots(figsize = (10,10))
map_brazil.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
map_brazil.plot(ax=ax)
geo_df.plot(ax=ax)
    
fig, ax = plt.subplots(figsize = (10,10))
map_brazil.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
geo_df.plot(ax=ax, alpha = .1 )
    
ax.set_title('Municipalities missing in summer 2015')
plt.savefig('Municipalities missing in summer 2015')