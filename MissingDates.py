from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data[['fdate', 'ETHANOLrp', 'GASOLINErp']]
print(data2.info())

#total NaNs
print(data2['ETHANOLrp'].isna().sum())
print(data2['GASOLINErp'].isna().sum())

plt.plot(data)
#per date
"""for i in range(len(data2['ETHANOLrp'])):
    #element = data2['ETHANOLrp'[i]].values
    counter = 0
    element = data2.iloc[i, 1]
    check = np.isnan(element)

result = pd.DataFrame(columns=['Date','NumberOfNaN'])
    
for i in range(len(data2['ETHANOLrp'])):
    element = data2.iloc[i, 1]
    date = data2.iloc[i,0]
    check = np.isnan(element)
    if check == True:
        result.append({'Date':date, 'NumberOfNaN':1}, ignore_index = True)

print(result)
"""