import pandas as pd
import GlobalVars as gv

#TO DO: analysis stuff
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:10000,['munic','fdate', 'ETHANOLrp']]
data2['fdate'] = pd.to_datetime(data2['fdate'])

totalobs = (data2['ETHANOLrp'].count())

municList = data2['munic'].drop_duplicates().dropna().tolist()
final = pd.DataFrame(columns=['munic'])
subperiods_dict =gv.SubperiodsDict
dates_helper = ['startdate', 'enddate']
data3 = pd.DataFrame()

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
            for i in range(len(municList)):
                munic_df = data3[data3['munic']== municList[i]].isna().sum()
                row = pd.Series({'munic': municList[i], key: munic_df.loc['ETHANOLrp']})
                result = pd.concat([result, row.to_frame().T], ignore_index=True)
    final = pd.merge(final, result, on='munic', how='outer')
final.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')
print(final)"""

#Missing # of obs, missing % of obs, max length missing
dateList = data2['fdate'].drop_duplicates().dropna().tolist()
list = ['Missing # of obs', 'Missing % of obs', 'max length']

final2= pd.DataFrame(columns=['Name'])


for key, value in subperiods_dict.items():
    i = 0
    data3 = data2
    result = pd.DataFrame(columns=['Name'])
    for i in range(len(dates_helper)):
        if dates_helper[i] == 'startdate':
            startdate = value[i]
        if dates_helper[i] == 'enddate':
            enddate = value[i]
            data3 = data3.loc[(data3['fdate']>startdate)]
            data3 = data3.loc[(data3['fdate']<enddate)]
            row = pd.Series({'Name': list[0], key: data3['ETHANOLrp'].isna().sum()})
            result = pd.concat([result, row.to_frame().T], ignore_index=True)
            i = i +1
    final2 = pd.merge(final2, result, on=['Name'], how='outer')
print(final2)

#hierweiter
"""final3= pd.DataFrame(columns=['Name'])
result2 = pd.DataFrame(columns=['Name'])
for key, value in subperiods_dict.items():
    i = 0
    data3 = data2
    print('start')
    for i in range(len(dates_helper)):
        if dates_helper[i] == 'startdate':
            startdate = value[i]
        if dates_helper[i] == 'enddate':
            enddate = value[i]
            data3 = data3.loc[(data3['fdate']>startdate)]
            data3 = data3.loc[(data3['fdate']<enddate)]
            #Missing # of obs
            missing_number = data3['ETHANOLrp'].isna().sum()
            i = i +1
            #Missing % of obs
            totalobs = (data3['ETHANOLrp'].count())
            missing_percent = missing_number/totalobs
            print(missing_percent)
            row = pd.Series({'Name': list[1], key: missing_percent})
            result2 = pd.concat([result2, row.to_frame().T], ignore_index=True)
            print(result2)
    final3 = pd.merge(final3, result2, on='Name', how='outer')
print(final3)
"""