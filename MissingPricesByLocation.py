from datetime import date, datetime
from operator import index
from stringprep import in_table_a1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#this might help as the problem is very similar: https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')
enddate = pd.to_datetime('01jan2020')
 
data2 = data.loc[:,['munic','fdate', 'ETHANOLrp', 'GASOLINErp']]
data2['fdate'] = pd.to_datetime(data2['fdate'])
data2 = data2[~(data2['fdate'] > enddate)]

municList = data2['munic'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['munic', 'ETHANOLrp_NaN', 'GASOLINErp_NaN'])

for i in range(len(municList)):
    munic_df = data2[data2['munic']== municList[i]].isna().sum()
    row = pd.Series({'munic': municList[i], 'ETHANOLrp_NaN': munic_df.loc['ETHANOLrp'], 'GASOLINErp_NaN':munic_df.loc['GASOLINErp']})
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')
df = pd.DataFrame()
result2= pd.DataFrame()

#missing in ethanol
for i in range(len(municList)):
    df = data2[data2['munic']==municList[i]]
    df['Group']=df.ETHANOLrp.notnull().astype(int).cumsum()
    df=df[df.ETHANOLrp.isnull()]
    df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>4].index)]
    df['count']=df.groupby('Group')['Group'].transform('size')
    df = df.drop_duplicates(['Group'], keep='first')
    result2 = result2.append(df, ignore_index=True)
result2.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result2.csv')
 
#missing in gasoline
result3= pd.DataFrame()
for i in range(len(municList)):
    df = data2[data2['munic']==municList[i]]
    df['Group']=df.GASOLINErp.notnull().astype(int).cumsum()
    df=df[df.GASOLINErp.isnull()]
    df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>4].index)]
    df['count']=df.groupby('Group')['Group'].transform('size')
    df = df.drop_duplicates(['Group'],keep='first')
    result3 = result3.append(df, ignore_index=True)
result3.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result3.csv')

"""Steps:
- filter how many are nan consecutively
- if 4 or less, fill automatically
- add column: assign value for full period, first period or drop - do manually?
- if more than a specific number is missing, drop municipality
"""