import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import GlobalVars as gv
#TO DO: Plot, replace all NA-Values

#import data - result2 --> missing cumulatives from ethanol (see MissinCumulativesPerLocation.py)
df = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
dropfile = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/dropfile.csv', sep=';')
df['fdate'] = pd.to_datetime(df['fdate'])

#subperiod 1
df1 = df.loc[~(df['fdate'] <= gv.subperiod1_start())]
df1 = df.loc[~(df['fdate'] >= gv.subperiod1_end())]

df_subperiod1 = dropfile.loc[:, ['munic', 'Subperiod 1 (Jan 1, 2011 - August 12, 2015)']]
df_subperiod1 = df_subperiod1[df_subperiod1['Subperiod 1 (Jan 1, 2011 - August 12, 2015)']==1]
df_subperiod1 = pd.merge(df1, df_subperiod1, how='inner')
df_subperiod1.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod1.csv')
#next step: plot
df_subperiod1.plot(x='munic', y='fdate')
plt.show()

#subperiod 2
df = df.loc[~(df['fdate'] <= gv.subperiod2_start())]
df = df.loc[~(df['fdate'] >= gv.subperiod2_end())]

df_subperiod2 = dropfile.loc[:, ['munic', 'Subperiod 2 (January 1, 2016 - August 5, 2017)']]
df_subperiod2 = df_subperiod2[df_subperiod2['Subperiod 2 (January 1, 2016 - August 5, 2017)']==1]
df_subperiod2 = pd.merge(df, df_subperiod2, how='inner')
df_subperiod2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod2.csv')

#subperiod 3
df3 = df.loc[~(df['fdate'] <= gv.subperiod3_start())]
df3 = df.loc[~(df['fdate'] >= gv.subperiod3_end())]

df_subperiod3 = dropfile.loc[:, ['munic', '(August 13, 2017 - December 31, 2019)']]
df_subperiod3 = df_subperiod3[df_subperiod3['(August 13, 2017 - December 31, 2019)']==1]
df_subperiod3 = pd.merge(df3, df_subperiod2, how='inner')
df_subperiod3.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod3.csv')

#subperiod 4 --> Jan 1, 2016 - dec 31, 2019
df = df.loc[~(df['fdate'] <= gv.subperiod4_start())]
df = df.loc[~(df['fdate'] >= gv.subperiod4_start())]

municList = df['munic'].drop_duplicates().dropna().tolist()
maxmissingweeks = 4
df_subperiod4 = pd.DataFrame()
result = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod4 = df[df['munic']==municList[i]]
    df_subperiod4['Group']=df_subperiod4.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod4=df_subperiod4[df_subperiod4.ETHANOLrp.isnull()]
    df_subperiod4=df_subperiod4[df_subperiod4.Group.isin(df_subperiod4.Group.value_counts()[df_subperiod4.Group.value_counts()<=maxmissingweeks].index)]
    df_subperiod4['count']=df_subperiod4.groupby('Group')['Group'].transform('size')

    #returns result all munics with less than 4 weeks in a row missing, next step: store in seperate df and merge with large df
    df_subperiod4 = df_subperiod4.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod4, ignore_index=True)
resultlist = result['munic'].drop_duplicates().dropna().tolist()
print(resultlist) # list of munics we don't drop

result2 = pd.DataFrame()
for i in range(len(resultlist)):
    df2 = df[df['munic']==resultlist[i]]
    item = df[df['munic']==resultlist[i]]
    print(type(item))
    result2 = result2.append(item, ignore_index=True) 
print(result2)
result2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')

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

#subperiod 5 --> full period
df = df.loc[~(df['fdate'] <= gv.subperiod5_start())]
df = df.loc[~(df['fdate'] >= gv.subperiod5_end())]

df_subperiod5 = dropfile.loc[:, ['munic', 'Full ']]
df_subperiod5 = df_subperiod5[df_subperiod5['Full ']==1]
df_subperiod5 = pd.merge(df, df_subperiod5, how='inner')
df_subperiod5.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod5.csv')
