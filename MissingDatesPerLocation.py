import pandas as pd
import SubperiodsDates as spd
import SubperiodsPaths as spp

#looks at seperate csv-files of dropped periods and returns values

all_subp = spp.getAllSubPeriods()
subp_list = spd.SubperiodsNames
print(subp_list)

final = pd.DataFrame(columns=['munic'])

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

results_merged = pd.DataFrame(columns=['Name'])
results_merged = results_merged.append(final2)
results_merged = results_merged.append(final3)
results_merged = results_merged.append(final4)
print(results_merged)