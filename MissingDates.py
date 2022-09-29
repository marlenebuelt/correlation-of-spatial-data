from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import GlobalVars as gv
#Problem: the result dataframe inserts zeros instead of NaN --> whenever that is fixed, insert total # of missing obs, total %, max length
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:10000,['fdate', 'ETHANOLrp']]
data2['fdate'] = pd.to_datetime(data2['fdate'])
data2 = data2.loc[~(data2['fdate'] >= '2019-12-31')]
dateList = data2['fdate'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['fdate'])
result.set_index('fdate')

#Subperiod 1
result1 = pd.DataFrame(columns=['fdate', 'Subperiod 1'])
for i in range(len(dateList)):
    date_df = data2[(data2['fdate']==dateList[i]) & (data2['fdate']>gv.subperiod1_start()) & (data2['fdate']<gv.subperiod1_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 1': date_df['ETHANOLrp'].isna().sum()})
    result1 = pd.concat([result1, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result1, on='fdate', how='outer')

#Subperiod 2
result2 = pd.DataFrame(columns=['fdate', 'Subperiod 2'])
for i in range(len(dateList)):
    date_df = data2[(data2['fdate']==dateList[i]) & (data2['fdate']>gv.subperiod2_start()) & (data2['fdate']<gv.subperiod2_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 2': date_df['ETHANOLrp'].isna().sum()})
    result2 = pd.concat([result2, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result2, on='fdate', how='outer')

#Subperiod 3
result3 = pd.DataFrame(columns=['fdate', 'Subperiod 3'])
for i in range(len(dateList)):
    date_df = data2[(data2['fdate']==dateList[i]) & (data2['fdate']>gv.subperiod3_start()) & (data2['fdate']<gv.subperiod3_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 3': date_df['ETHANOLrp'].isna().sum()})
    result3 = pd.concat([result3, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result3, on='fdate', how='outer')

#Subperiod 4
result4 = pd.DataFrame(columns=['fdate', 'Subperiod 4'])
for i in range(len(dateList)):
    date_df = data2[(data2['fdate']==dateList[i]) & (data2['fdate']>gv.subperiod4_start()) & (data2['fdate']<gv.subperiod4_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 4': date_df['ETHANOLrp'].isna().sum()})
    result4 = pd.concat([result4, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result4, on='fdate', how='outer')

#full Period
result_full = pd.DataFrame(columns=['fdate', 'Full Period'])
for i in range(len(dateList)):
    date_df = data2[(data2['fdate']==dateList[i]) & (data2['fdate']>gv.subperiod5_start()) & (data2['fdate']<gv.subperiod5_end())]
    row = pd.Series({'fdate': dateList[i], 'Full Period': date_df['ETHANOLrp'].isna().sum()})
    result_full = pd.concat([result_full, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result_full, on='fdate', how='outer')

result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/missingByDate.csv')