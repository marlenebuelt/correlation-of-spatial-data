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
data3 = data2

for key, value in subperiods_dict.items():
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