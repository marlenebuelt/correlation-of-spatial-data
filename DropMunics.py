import pandas as pd

#import data - result2 --> missing cumulatives from ethanol (see MissinCumulativesPerLocation.py)
df = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
dropfile = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/dropfile.csv', sep=';')

#subperiod 1
startdate = pd.to_datetime('2011-1-1')
enddate = pd.to_datetime('2015-8-12')
df['fdate'] = pd.to_datetime(df['fdate'])
df1 = df.loc[~(df['fdate'] <= startdate)]
df1 = df.loc[~(df['fdate'] >= enddate)]

df_subperiod1 = dropfile.loc[:, ['munic', 'Subperiod 1 (Jan 1, 2011 - August 12, 2015)']]
df_subperiod1 = df_subperiod1[df_subperiod1['Subperiod 1 (Jan 1, 2011 - August 12, 2015)']==1]
df_subperiod1 = pd.merge(df1, df_subperiod1, how='inner')
df_subperiod1.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod1.csv')

#subperiod 2
startdate = pd.to_datetime('2016-1-1')
enddate = pd.to_datetime('2017-8-5')
df['fdate'] = pd.to_datetime(df['fdate'])
df = df.loc[~(df['fdate'] <= startdate)]
df = df.loc[~(df['fdate'] >= enddate)]

df_subperiod2 = dropfile.loc[:, ['munic', 'Subperiod 2 (January 1, 2016 - August 5, 2017)']]
df_subperiod2 = df_subperiod2[df_subperiod2['Subperiod 2 (January 1, 2016 - August 5, 2017)']==1]
df_subperiod2 = pd.merge(df, df_subperiod2, how='inner')
df_subperiod2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod2.csv')

#subperiod 3
startdate = pd.to_datetime('2017-8-13')
enddate = pd.to_datetime('2019-12-31')
df['fdate'] = pd.to_datetime(df['fdate'])
df3 = df.loc[~(df['fdate'] <= startdate)]
df3 = df.loc[~(df['fdate'] >= enddate)]

df_subperiod3 = dropfile.loc[:, ['munic', '(August 13, 2017 - December 31, 2019)']]
df_subperiod3 = df_subperiod3[df_subperiod3['(August 13, 2017 - December 31, 2019)']==1]
df_subperiod3 = pd.merge(df3, df_subperiod2, how='inner')
df_subperiod3.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod3.csv')

#subperiod 4
startdate = pd.to_datetime('2011-1-1')
enddate = pd.to_datetime('2019-12-31')
df['fdate'] = pd.to_datetime(df['fdate'])
df = df.loc[~(df['fdate'] <= startdate)]
df = df.loc[~(df['fdate'] >= enddate)]

df_subperiod4 = dropfile.loc[:, ['munic', 'Full ']]
df_subperiod4 = df_subperiod4[df_subperiod4['Full ']==1]
df_subperiod4 = pd.merge(df, df_subperiod4, how='inner')
df_subperiod4.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')

#subperiod 5 --> Jan 1, 2016 - dec 31, 2019 --> drop wenn mehr als 4 na
startdate = pd.to_datetime('2016-1-1')
enddate = pd.to_datetime('2019-12-31')
df['fdate'] = pd.to_datetime(df['fdate'])
df = df.loc[~(df['fdate'] <= startdate)]
df = df.loc[~(df['fdate'] >= enddate)]

municList = df['munic'].drop_duplicates().dropna().tolist()
maxmissingweeks = 4
df_subperiod5 = pd.DataFrame()
#print(type(df_subperiod5))
result = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod5 = df[df['munic']==municList[i]]
    df_subperiod5['Group']=df_subperiod5.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod5=df_subperiod5[df_subperiod5.ETHANOLrp.isnull()]
    df_subperiod5=df_subperiod5[df_subperiod5.Group.isin(df_subperiod5.Group.value_counts()[df_subperiod5.Group.value_counts()<=maxmissingweeks].index)]
    df_subperiod5['count']=df_subperiod5.groupby('Group')['Group'].transform('size')

    #returns result all munics with less than 4 weeks in a row missing, next step: store in seperate df and merge with large df
    df_subperiod5 = df_subperiod5.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod5, ignore_index=True)
resultlist = result['munic'].drop_duplicates().dropna().tolist()
print(resultlist) # list of munics I don't drop

result2 = pd.DataFrame()
for i in range(len(resultlist)):
    df2 = df[df['munic']==resultlist[i]]
    item = df[df['munic']==resultlist[i]]
    print(type(item))
    result2 = result2.append(item, ignore_index=True) 
print(result2)
result2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod5.csv')

#Double Check: which ones did we drop
result = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod5 = df[df['munic']==municList[i]]
    df_subperiod5['Group']=df_subperiod5.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod5=df_subperiod5[df_subperiod5.ETHANOLrp.isnull()]
    df_subperiod5=df_subperiod5[df_subperiod5.Group.isin(df_subperiod5.Group.value_counts()[df_subperiod5.Group.value_counts()>=maxmissingweeks].index)]
    df_subperiod5['count']=df_subperiod5.groupby('Group')['Group'].transform('size')
    df_subperiod5 = df_subperiod5.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod5, ignore_index=True)
droplist = result['munic'].drop_duplicates().dropna().tolist()
print(droplist) # list of munics we don't drop

"""data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv').dropna()

#merge with large file to get long and lat data
df_merged = pd.merge(df,data,on='munic', how='inner')
df_merged = df_merged.loc[:, ['munic', 'count', 'longitude', 'latitude']].drop_duplicates().dropna()
df_merged['munic'] = df_merged['munic'].dropna()
df_merged = df_merged.dropna(subset=['munic'])
df_merged = df_merged.drop_duplicates(subset=['munic'])
df_merged.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/df_merged.csv')"""