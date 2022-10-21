import pandas as pd
import SubperiodsPaths as spp
import SubperiodsDates as spd
import numpy as np

#Returns the munics we'll drop in seperate csv-files
#not doublechecked yet

df_list = spp.getAllSubP_beforedrop()
dropfile = spp.getDropFile()
dropfile= dropfile.astype({'Subperiod 4': np.float})
#print(dropfile)
subperiodnames = spd.SubperiodsNames
resultcsv = spp.setAllSubP_afterdrop1()

#subperiod 1
for i in range(len(df_list)):
    df = df_list[i]
    subp = subperiodnames[i]
    dropdf_subp = dropfile.loc[:,['munic', subp]]
    dropdf_subp = dropdf_subp[dropdf_subp[subp]==0]
    droplist = dropdf_subp['munic'].to_list()
    df = df[df.munic.isin(droplist)==False]
    print(df)
    df.to_csv(resultcsv[i])
#df_subperiod1 = pd.merge(df1, df_subperiod1, how='left', on=['munic'])

#df_subperiod1.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod1.csv')
#print(df_subperiod1)

"""#subperiod 4
df2 = df
df2 = df2.loc[(df2['fdate']>spp.subperiod4_start())]
df2 = df2.loc[(df2['fdate']<spp.subperiod4_end())]

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

result2 = pd.merge(df3, result2, on='munic', how='outer')
result2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')

print(result2)

"""