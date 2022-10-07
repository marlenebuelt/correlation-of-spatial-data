import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import GlobalVars as gv
#TO DO: Plot, replace all NA-Values
#merge funktioniert nicht, hier morgen weiter --> dropfile und datensatz zusammenbringen, ersten commit angucken
#import data - result2 --> missing cumulatives from ethanol (see MissinCumulativesPerLocation.py)
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
dropfile = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/dropfile.csv', sep=';')

data2 = data.loc[:10000,['munic','fdate', 'ETHANOLrp']]
data2['fdate'] = pd.to_datetime(data2['fdate'])
subperiods_dict =gv.SubperiodsDict
dates_helper = ['startdate', 'enddate']
data3 = pd.DataFrame()

#subperiod 4 - determine which munics we drop
data3 = data2
data3 = data3.loc[(data3['fdate']>gv.subperiod4_start())]
data3 = data3.loc[(data3['fdate']<gv.subperiod4_end())]
#data3.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')

municList = data3['munic'].drop_duplicates().dropna().tolist()
maxmissingweeks = 4 #if the max number of missing weeks needs to be changed, change this variable
df_subperiod4 = pd.DataFrame()
result = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod4 = data3.loc[data3['munic']==municList[i]]
    df_subperiod4['Group']=df_subperiod4.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod4=df_subperiod4.loc[df_subperiod4.ETHANOLrp.isnull()]
    #print(df_subperiod4)
    df_subperiod4=df_subperiod4.loc[df_subperiod4.Group.isin(df_subperiod4.Group.value_counts()[df_subperiod4.Group.value_counts()<=maxmissingweeks].index)]
    df_subperiod4['count']=df_subperiod4.groupby('Group')['Group'].transform('size')
    #returns result all munics with less than 4 weeks in a row missing
    df_subperiod4 = df_subperiod4.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod4, ignore_index=True)
resultlist = result['munic'].drop_duplicates().dropna().tolist() # list of munics we don't drop

result2 = pd.DataFrame()
for i in range(len(resultlist)):
    item = data3[data3['munic']==resultlist[i]]
    item['Subperiod 4'] = 1
    item = item.loc[:, ['munic', 'Subperiod 4']].drop_duplicates().dropna()
    result2 = result2.append(item, ignore_index=True)
print(result2)
#dropfile.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')

#Double Check: which ones did we drop
result = pd.DataFrame()
for i in range(len(municList)):
    df_subperiod4 = data2[data2['munic']==municList[i]]
    df_subperiod4['Group']=df_subperiod4.ETHANOLrp.notnull().astype(int).cumsum()
    df_subperiod4=df_subperiod4[df_subperiod4.ETHANOLrp.isnull()]
    df_subperiod4=df_subperiod4[df_subperiod4.Group.isin(df_subperiod4.Group.value_counts()[df_subperiod4.Group.value_counts()>=maxmissingweeks].index)]
    df_subperiod4['count']=df_subperiod4.groupby('Group')['Group'].transform('size')
    df_subperiod4 = df_subperiod4.drop_duplicates(['Group'], keep='first')
    result = result.append(df_subperiod4, ignore_index=True)
droplist = result['munic'].drop_duplicates().dropna().tolist()
print('droplist')
print(droplist) # list of munics we don't drop
print('resultlist')
print(resultlist)
result3 = pd.DataFrame()
for i in range(len(droplist)):
    item = data3[data3['munic']==droplist[i]]
    item['Subperiod 4'] = 0
    item = item.loc[:, ['munic', 'Subperiod 4']].drop_duplicates().dropna()
    result3 = result3.append(item, ignore_index=True)
print(result3)

#set up subperiods and merge with large file
"""for key, value in subperiods_dict.items():
    result = pd.DataFrame(columns=['munic'])
    data3 = data2
    for i in range(len(dates_helper)):
        if dates_helper[i] == 'startdate':
            startdate = value[i]
        if dates_helper[i] == 'enddate':
            enddate = value[i]
            data3 = data3.loc[(data3['fdate']>startdate)]
            data3 = data3.loc[(data3['fdate']<enddate)]
            #merge large datafile and dropfile
            data3 = pd.merge(data2, dropfile, on='munic', how = 'outer')
            #data3 = data3.loc[:, ['munic', 'fdate', 'ETHANOLrp',key]]
    #final = pd.merge(final, result, on='munic', how='outer')
#final.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')
    print(data3)

df['fdate'] = pd.to_datetime(df['fdate'])
print(df)
#subperiod 1
df1 = df.loc[~(df['fdate'] <= gv.subperiod1_start())]
df1 = df.loc[~(df['fdate'] >= gv.subperiod1_end())]

df_subperiod1 = df.loc[:, ['munic', 'Subperiod 1 (Jan 1, 2011 - August 12, 2015)', 'ETHANOLrp']]
df_subperiod1 = df_subperiod1[df_subperiod1['Subperiod 1 (Jan 1, 2011 - August 12, 2015)']==1]
df_subperiod1 = pd.merge(df1, df_subperiod1, how='inner')
df_subperiod1.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod1.csv')
print(df_subperiod1)


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
 

#subperiod 5 --> full period
df = df.loc[~(df['fdate'] <= gv.subperiod5_start())]
df = df.loc[~(df['fdate'] >= gv.subperiod5_end())]

df_subperiod5 = dropfile.loc[:, ['munic', 'Full ']]
df_subperiod5 = df_subperiod5[df_subperiod5['Full ']==1]
df_subperiod5 = pd.merge(df, df_subperiod5, how='inner')
df_subperiod5.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod5.csv')
"""