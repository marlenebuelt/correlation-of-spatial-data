import pandas as pd
import GlobalVars as gv

#TO DO: Check Values
#looks at seperate csv-files of dropped periods and returns values

#data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
#data2 = data.loc[:10000,['munic','fdate', 'ETHANOLrp']]
#data2['fdate'] = pd.to_datetime(data2['fdate'])

data_subp1 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod1.csv')
data_subp2 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod2.csv')
data_subp3 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod3.csv')
data_subp4 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod4.csv')
data_subp5 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/data_subperiods/subperiod5.csv')

all_subp = [data_subp1, data_subp2, data_subp3, data_subp4, data_subp5]
subp_list = gv.SubperiodsNames
print(subp_list)

for df in all_subp:
    df = df.loc[:5000]
    df['fdate'] = pd.to_datetime(df['fdate'])
    totalobs = (df['ETHANOLrp'].count())

final = pd.DataFrame(columns=['munic'])
"""
#returns nothing new
for df in all_subp:
    municList = df['munic'].drop_duplicates().dropna().tolist()
    result = pd.DataFrame(columns=['munic'])
    for i in range(len(municList)):
        munic_df = df[df['munic']== municList[i]].isna().sum()
        row = pd.Series({'munic': municList[i], 'key': munic_df.loc['ETHANOLrp']})
        result = pd.concat([result, row.to_frame().T], ignore_index=True)
    final = pd.merge(final, result, on='munic', how='outer')
#final.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')
print(final)
"""
#Missing # of obs, missing % of obs, max length missing ---> DOUBLE CHECK VALUES
list = ['Missing # of obs', 'Missing % of obs', 'max length']

#missing # of obs
final2= pd.DataFrame(columns=['Name'])
for i in range(len(all_subp)):
    df = all_subp[i]
    print(df)
    result = pd.DataFrame(columns=['Name'])
    row = pd.Series({'Name': list[0], subp_list[i]: df['ETHANOLrp'].isna().sum()})
    print(subp_list[i])
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
    print(result) 
    final2 = pd.merge(final2, result, on=['Name'], how='outer')
print(final2)

#missing % of obs
final3= pd.DataFrame(columns=['Name'])
for i in range(len(all_subp)):
    df = all_subp[i]
    print(df)
    result2 = pd.DataFrame(columns=['Name'])
    #Missing # of obs
    missing_number = df['ETHANOLrp'].isna().sum()
    print(missing_number)
    #Missing % of obs
    totalobs = (df['munic'].count()) #looking at the munic column to avoid issues with nan-values
    print(totalobs)
    missing_percent = (missing_number/totalobs)
    print(missing_percent)
    row = pd.Series({'Name': list[1], subp_list[i]: missing_percent})
    result2 = pd.concat([result2, row.to_frame().T], ignore_index=True)
    print(result2)
    final3 = pd.merge(final3, result2, on='Name', how='outer')
print(final3)

#maxlength
df = pd.DataFrame()
result3= pd.DataFrame()
maxmissingweeks = 4
final4= pd.DataFrame(columns=['Name'])
for i in range(len(all_subp)):
    df = all_subp[i]
    print(df)
    result4 = pd.DataFrame(columns=['Name'])
    #Missing cumulatives of obs
    missing_number = df['ETHANOLrp'].isna().sum()
    df['Group']=df.ETHANOLrp.notnull().astype(int).cumsum()
    df=df[df.ETHANOLrp.isnull()]
    df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>maxmissingweeks].index)]
    df['count']=df.groupby('Group')['Group'].transform('size')
    df = df.drop_duplicates(['Group'], keep='first')
    max = df['count'].max()
    #result4 = result4.append(df, ignore_index=True)
    row = pd.Series({'Name': list[2], subp_list[i]: max})
    result4 = pd.concat([result4, row.to_frame().T], ignore_index=True)  
    final4 = pd.merge(final4, result4, on='Name', how='outer')
print(final4)