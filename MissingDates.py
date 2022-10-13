from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import SubperiodsDates as spd
import SubperiodsPaths as spp
#Problem: the result dataframe inserts zeros instead of NaN --> whenever that is fixed, insert total # of missing obs, total %, max length
df = spp.getadaptedoriginalfile()

dateList = df['fdate'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['fdate'])
result.set_index('fdate')

#foreach einbauen
for

#Subperiod 1
result1 = pd.DataFrame(columns=['fdate', 'Subperiod 1'])
for i in range(len(dateList)):
    date_df = df[(df['fdate']==dateList[i]) & (df['fdate']>spd.subperiod1_start()) & (df['fdate']<spd.subperiod1_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 1': date_df['ETHANOLrp'].isna().sum()})
    result1 = pd.concat([result1, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result1, on='fdate', how='outer')

#Subperiod 2
result2 = pd.DataFrame(columns=['fdate', 'Subperiod 2'])
for i in range(len(dateList)):
    date_df = df[(df['fdate']==dateList[i]) & (df['fdate']>spd.subperiod2_start()) & (df['fdate']<spd.subperiod2_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 2': date_df['ETHANOLrp'].isna().sum()})
    result2 = pd.concat([result2, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result2, on='fdate', how='outer')

#Subperiod 3
result3 = pd.DataFrame(columns=['fdate', 'Subperiod 3'])
for i in range(len(dateList)):
    date_df = df[(df['fdate']==dateList[i]) & (df['fdate']>spd.subperiod3_start()) & (df['fdate']<spd.subperiod3_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 3': date_df['ETHANOLrp'].isna().sum()})
    result3 = pd.concat([result3, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result3, on='fdate', how='outer')

#Subperiod 4
result4 = pd.DataFrame(columns=['fdate', 'Subperiod 4'])
for i in range(len(dateList)):
    date_df = df[(df['fdate']==dateList[i]) & (df['fdate']>spd.subperiod4_start()) & (df['fdate']<spd.subperiod4_end())]
    row = pd.Series({'fdate': dateList[i], 'Subperiod 4': date_df['ETHANOLrp'].isna().sum()})
    result4 = pd.concat([result4, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result4, on='fdate', how='outer')

#full Period
result_full = pd.DataFrame(columns=['fdate', 'Full Period'])
for i in range(len(dateList)):
    date_df = df[(df['fdate']==dateList[i]) & (df['fdate']>spd.subperiod5_start()) & (df['fdate']<spd.subperiod5_end())]
    row = pd.Series({'fdate': dateList[i], 'Full Period': date_df['ETHANOLrp'].isna().sum()})
    result_full = pd.concat([result_full, row.to_frame().T], ignore_index=True)
result = pd.merge(result, result_full, on='fdate', how='outer')

result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/missingByDate.csv')