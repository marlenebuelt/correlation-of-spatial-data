from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:2000,['munic','fdate', 'ETHANOLrp', 'GASOLINErp']]
print(data2)
#total NaNs
print(data2['ETHANOLrp'].isna().sum())
print(data2['GASOLINErp'].isna().sum())

result = pd.DataFrame({'munic':[], 'count':[]})
municList = data2['munic'].drop_duplicates().dropna().tolist()
print(municList)

for i in range(len(municList)):
    munic = municList[i]
    for j in range(len(data2['munic']==munic)): #irgendwie am munic festhalten
        counter = 0
        price = data2['ETHANOLrp'].loc[j]
        if pd.isna(price): # == 'nan': #wenn wert nicht wie oben, dann neu zählen --> besser neuer loop?
            counter += 1
            print(counter)
            #result.append({'munic': municList[i], 'counter': counter}, ignore_index=True)
            helperdf = pd.DataFrame([[munic, counter]], columns = ['munic', 'count'])
            #print(helperdf)
            result.append(helperdf)
print(result)
