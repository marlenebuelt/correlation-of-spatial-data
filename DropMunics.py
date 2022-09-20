import pandas as pd

#import data - result2 --> missing cumulatives from ethanol (see missing prices by location)
df = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result2.csv')

df = df.loc[:2000,['munic','count']]
df = df[df['count']>100]
print(df)

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv').dropna()
#merge with large file to get long and lat data
df_merged = pd.merge(df,data,on='munic', how='inner')
df_merged = df_merged.loc[:, ['munic', 'count', 'longitude', 'latitude']].drop_duplicates().dropna()
df_merged['munic'] = df_merged['munic'].dropna()
df_merged = df_merged.dropna(subset=['munic'])
df_merged = df_merged.drop_duplicates(subset=['munic'])
print(df_merged)

df_merged.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/df_merged.csv')