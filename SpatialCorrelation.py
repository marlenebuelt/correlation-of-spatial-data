import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import SubperiodsPaths as spp

#inspired by: https://builtin.com/data-science/exploratory-spatial-data-analysis-esda, 
# combining dataframes: https://towardsdatascience.com/exploratory-spatial-data-analysis-esda-spatial-autocorrelation-7592edcbef9a
#https://towardsdatascience.com/plotting-maps-with-geopandas-428c97295a73

#overall file: will be replaced with files for scenarios
all_df = spp.getAllSubP_drop1()

for df in all_df:
    map_brazil = gpd.read_file(spp.getMapBrazilPath())
    map_brazil.to_crs(epsg=4326).plot()

    crs = {'init':'EPSG:4326'}
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)

    fig, ax = plt.subplots(figsize = (10,10))
    map_brazil.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
    map_brazil.plot(ax=ax, color='purple')
    geo_df.plot(ax=ax)
    ax.set_title('Municipalities')

    fig, ax = plt.subplots(figsize = (10,10))
    map_brazil.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
    geo_df.plot(ax=ax, alpha = .1 )

    ax.set_title('Municipalities')
    plt.savefig('Municipalities')
    plt.show()

"""#step 2: munics we want to drop (list not final yet!)
geometry = [Point(xy) for xy in zip(df_drop['longitude'], df_drop['latitude'])]
geo_df2 = gpd.GeoDataFrame(df_drop, crs = crs, geometry = geometry)

fig, ax = plt.subplots(figsize = (10,10))
map_brazil.to_crs(epsg=4326).plot(ax=ax, color='red')
map_brazil.plot(ax=ax, color='black')
geo_df2.plot(ax=ax)
ax.set_title('Municipalities_drop')

fig, ax = plt.subplots(figsize = (10,10))
map_brazil.to_crs(epsg=4326).plot(ax=ax, color='pink')
geo_df2.plot(ax=ax, alpha = .1 )

ax.set_title('Municipalities_Drop')
plt.savefig('Municipalities_drop')
plt.show()"""