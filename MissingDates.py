from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:,['fdate', 'ETHANOLrp', 'GASOLINErp']]
dateList = data2['fdate'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['fdate', 'ETHANOLrp_NaN', 'GASOLINErp_NaN'])

for i in range(len(dateList)):
    date_df = data2[data2['fdate']==dateList[i]]
    count = date_df['ETHANOLrp'].isna().sum()
    row = pd.Series({'fdate': dateList[i], 'ETHANOLrp_NaN': date_df['ETHANOLrp'].isna().sum(), 'GASOLINErp_NaN':date_df['GASOLINErp'].isna().sum()})
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
print(result)
result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/missingByDate.csv')