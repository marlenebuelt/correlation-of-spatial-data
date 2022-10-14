import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import SubperiodsPaths as spp
import SubperiodsDates as spd
#this categorization will delete any municipality that has more than four weeks missing in row
#Returns the munics we'll drop in seperate csv-files
#WIP
df_list = spp.getAllSubP_beforedrop()
subp_dict = spd.SubperiodsDatesDict()
print(df_list)
result = pd.DataFrame()
result_csv_list = spp.setAllSubP_afterdrop2()
print(len(result_csv_list))

count = 0
for df in df_list: 
    result_period = pd.DataFrame()
    municList = df['munic'].drop_duplicates().dropna().tolist()
    df_subperiod = pd.DataFrame()
    maxmissingweeks = 4
    for i in range(len(municList)):
        current_munic_df = df[df['munic']==municList[i]]
        current_munic_df['Group']=current_munic_df.ETHANOLrp.notnull().astype(int).cumsum()
        current_munic_df=current_munic_df[current_munic_df.ETHANOLrp.isnull()]
        #current_munic_df=current_munic_df[current_munic_df.Group.isin(current_munic_df.Group.value_counts()[current_munic_df.Group.value_counts()<maxmissingweeks].index)]
        current_munic_df=current_munic_df[current_munic_df.Group.isin(current_munic_df.Group.value_counts())]
        current_munic_df['count']=current_munic_df.groupby('Group')['Group'].transform('size')
        #current_munic_df = current_munic_df.drop_duplicates(['Group'], keep='first')
        result = result.append(current_munic_df, ignore_index=True)
    result.to_csv(result_csv_list[count])
    count = count + 1
    print(result)


"""result2 = pd.DataFrame()
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
#df_all = df_all.drop_duplicates("""