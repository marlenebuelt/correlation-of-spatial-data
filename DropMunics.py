import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import GlobalVars as gv
#TO DO: Plot, replace all NA-Values
#doublecheck values

#Returns the munics we'll drop in seperate csv-files
df = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
dropfile = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/dropfile_new.csv', sep=';')
dropfile = dropfile.loc[:,['munic', 'Subperiod 1', 'Subperiod 2', 'Subperiod 3', 'Subperiod 5']]
df['fdate'] = pd.to_datetime(df['fdate'])
df = df.loc[:5000, ['munic', 'fdate', 'ETHANOLrp']]
print(dropfile)

#subperiod 4
df2 = df
df2 = df2.loc[(df2['fdate']>gv.subperiod4_start())]
df2 = df2.loc[(df2['fdate']<gv.subperiod4_end())]

municList = df2['munic'].drop_duplicates().dropna().tolist()
print(municList)
maxmissingweeks = 4
df_subperiod4 = pd.DataFrame()
result = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod4 = df2[df2['munic']==municList[i]]
    df_subperiod4['Group']=df_subperiod4.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod4=df_subperiod4[df_subperiod4.ETHANOLrp.isnull()]
    df_subperiod4=df_subperiod4[df_subperiod4.Group.isin(df_subperiod4.Group.value_counts()[df_subperiod4.Group.value_counts()<=maxmissingweeks].index)]
    df_subperiod4['count']=df_subperiod4.groupby('Group')['Group'].transform('size')
    df_subperiod4 = df_subperiod4.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod4, ignore_index=True)
print(result)
resultlist = result['munic'].drop_duplicates().dropna().tolist() # list of munics we don't drop

result2 = pd.DataFrame()
for i in range(len(resultlist)):
    df2 = df[df['munic']==resultlist[i]]
    item = df[df['munic']==resultlist[i]]
    result2 = result2.append(item, ignore_index=True)
result2 = result2.loc[:, ['munic']]
result2 = result2.drop_duplicates()
result2['Subperiod 4'] = 1

#Dropped munics
result = pd.DataFrame()
df3 = df
df3 = df3.loc[(df3['fdate']>gv.subperiod4_start())]
df3 = df3.loc[(df3['fdate']<gv.subperiod4_end())]
df_subperiod4_drop = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod4_drop = df3[df3['munic']==municList[i]]
    df_subperiod4_drop['Group']=df_subperiod4_drop.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod4_drop=df_subperiod4_drop[df_subperiod4_drop.ETHANOLrp.isnull()]
    df_subperiod4_drop=df_subperiod4_drop[df_subperiod4_drop.Group.isin(df_subperiod4_drop.Group.value_counts()[df_subperiod4_drop.Group.value_counts()>=maxmissingweeks].index)]
    df_subperiod4_drop['count']=df_subperiod4_drop.groupby('Group')['Group'].transform('size')
    df_subperiod4_drop = df_subperiod4_drop.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod4_drop, ignore_index=True)
droplist = result['munic'].drop_duplicates().dropna().tolist()
print(droplist) # list of munics we don't drop

result3 = pd.DataFrame()
for i in range(len(droplist)):
    item = df3[df3['munic']==droplist[i]]
    result3 = result3.append(item, ignore_index=True)
result3 = result3.loc[:, ['munic']]
result3 = result3.drop_duplicates()
result3['Subperiod 4'] = 0
result3.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4_2.csv')

result2 = pd.merge(df3, result2, on='munic', how='outer')
result2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')

print(result2)

#subperiod 1
df1 = df.loc[~(df['fdate'] <= gv.subperiod1_start())]
df1 = df.loc[~(df['fdate'] >= gv.subperiod1_end())]

df_subperiod1 = dropfile.loc[:, ['munic', 'Subperiod 1']]
#df_subperiod1 = df_subperiod1[df_subperiod1['Subperiod 1']==1]
df_subperiod1 = pd.merge(df1, df_subperiod1, how='left', on=['munic'])

df_subperiod1.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod1.csv')
print(df_subperiod1)

#subperiod 2
df2 = df.loc[~(df['fdate'] <= gv.subperiod2_start())]
df2 = df.loc[~(df['fdate'] >= gv.subperiod2_end())]
df_subperiod2 = dropfile.loc[:, ['munic', 'Subperiod 2']]
df_subperiod2 = df_subperiod2[df_subperiod2['Subperiod 2']==1]
df_subperiod2 = pd.merge(df2, df_subperiod2, how='left')
df_subperiod2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod2.csv')
print(df_subperiod2)

#subperiod 3
df3 = df.loc[~(df['fdate'] <= gv.subperiod3_start())]
df3 = df.loc[~(df['fdate'] >= gv.subperiod3_end())]

df_subperiod3 = dropfile.loc[:, ['munic', 'Subperiod 3']]
df_subperiod3 = df_subperiod3[df_subperiod3['Subperiod 3']==1]
df_subperiod3 = pd.merge(df3, df_subperiod2, how='inner')
df_subperiod3.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod3.csv')
print(df_subperiod3)

#subperiod 5 --> full period
df = df.loc[~(df['fdate'] <= gv.subperiod5_start())]
df = df.loc[~(df['fdate'] >= gv.subperiod5_end())]

df_subperiod5 = dropfile.loc[:, ['munic', 'Subperiod 5']]
df_subperiod5 = df_subperiod5[df_subperiod5['Subperiod 5']==1]
df_subperiod5 = pd.merge(df, df_subperiod5, how='inner')
df_subperiod5.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod5.csv')
print(df_subperiod5)

dropfile = pd.merge(dropfile, result2, on = 'munic', how = 'outer')
print(dropfile)
df_all = pd.DataFrame()
df_all = pd.merge(df2, dropfile[['munic', 'Subperiod 1', 'Subperiod 2', 'Subperiod 3', 'Subperiod 4', 'Subperiod 5']], on='munic', how='left')
#df_all = df_all.drop_duplicates()