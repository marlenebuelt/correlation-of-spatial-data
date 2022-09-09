from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:1000,['munic','fdate', 'ETHANOLrp', 'GASOLINErp']]
data2.set_index('munic')


#total NaNs
print(data2['ETHANOLrp'].isna().sum())
print(data2['GASOLINErp'].isna().sum())
print(data2.loc[2, 'munic'])

result = [['munic', 'count']]
for i in range(len(data2['munic'])):
    munic = data2.loc[i, 'munic']
    price = data2.loc[i, 'ETHANOLrp']
    if i-1 != i:
        counter = 0
        if price == 'nan':
            counter= counter + 1
        result.append(pd.Series([munic, counter]))

print(result)
#plt.scatter(data2['fdate'], data2['munic'])
#plt.show()