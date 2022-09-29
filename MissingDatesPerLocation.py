import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import GlobalVars

#convert dates and drop anything after january 1st, 2020
#this file will be used for creating new files for the different scenarios
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:10000,['munic','fdate', 'ETHANOLrp']]
data2['fdate'] = pd.to_datetime(data2['fdate'])
totalobs = (data2['ETHANOLrp'].count())

municList = data2['munic'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['munic', 'ETHANOLrp'])

#Subperiod 1
#missing totals for Ethanol and Gasoline
#munic_df = data2.loc[[data2['fdate']>GlobalVars.subperiod1_start()]:[data2['fdate']<GlobalVars.subperiod1_end()], :]
munic_df = data2.loc[data2['fdate']>GlobalVars.subperiod1_start()]
munic_df = data2.loc[data2['fdate']<GlobalVars.subperiod1_end()]
print(munic_df)
for i in range(len(municList)):
    munic_df = data2[data2['munic']== municList[i]].isna().sum()
    row = pd.Series({'munic': municList[i], 'ETHANOLrp': munic_df.loc['ETHANOLrp']})
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
#result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')
print(result)
