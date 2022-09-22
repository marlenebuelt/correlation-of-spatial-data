import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#convert dates and drop anything after january 1st, 2020
data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
enddate = pd.to_datetime('01jan2020')

data2 = data.loc[:10000,['munic','fdate', 'ETHANOLrp', 'GASOLINErp']]
data2['fdate'] = pd.to_datetime(data2['fdate'])
data2 = data2[~(data2['fdate'] > enddate)]

municList = data2['munic'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['munic', 'ETHANOLrp_NaN', 'GASOLINErp_NaN'])

#missing totals for Ethanol and Gasoline
for i in range(len(municList)):
    munic_df = data2[data2['munic']== municList[i]].isna().sum()
    row = pd.Series({'munic': municList[i], 'ETHANOLrp_NaN': munic_df.loc['ETHANOLrp'], 'GASOLINErp_NaN':munic_df.loc['GASOLINErp']})
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')