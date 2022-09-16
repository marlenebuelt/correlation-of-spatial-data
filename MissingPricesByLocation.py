from operator import index
from stringprep import in_table_a1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:2000,['munic','fdate', 'ETHANOLrp', 'GASOLINErp']]

municList = data2['munic'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['munic', 'ETHANOLrp_NaN', 'GASOLINErp_NaN'])

"""for i in range(len(municList)):
    munic_df = data2[data2['munic']== municList[i]].isna().sum()
    row = pd.Series({'munic': municList[i], 'ETHANOLrp_NaN': munic_df.loc['ETHANOLrp'], 'GASOLINErp_NaN':munic_df.loc['GASOLINErp']})
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
print(result)
result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')
"""
df = pd.DataFrame()
#extract and possibly drop: hier weiter: zählen, wie viele hintereinander 0 --> dann automatisch ausfüllen
for i in range(len(municList)):
    df = data2[data2['munic']== municList[i]]
    #munic_df['consecutive'] = munic_df.loc[i, 'ETHANOLrp'].groupby((munic_df.loc[i, 'ETHANOLrp'] != munic_df.loc[i,'ETHANOLrp'].shift()).cumsum()).transform('size') * munic_df.loc[i,'ETHANOLrp']
    #counter = 0
    df['Group']=df.ETHANOLrp.notnull().astype(int).cumsum()
    df=df[df.ETHANOLrp.isnull()]
    df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>3].index)]
    df['count']=df.groupby('Group')['Group'].transform('size')
    df.drop_duplicates(['Group'],keep='first')

    print(df)

    """if np.isnan(munic_df['ETHANOLrp'].iloc[i]) == np.isnan(munic_df['ETHANOLrp'].iloc[i-1]):
        print("x")
        munic_df['consecutive'] = counter +1
    else:
        print("y")
        munic_df['consecutive'] = 0
    print(munic_df)
    print(max(munic_df['consecutive']))

    #row = pd.Series({'munic': municList[i], 'Cumulative_NaN': cumNaN})
    #resultNaN = pd.concat([resultNaN, row.to_frame().T], ignore_index=True)
"""
"""
Steps:
- filter how many are nan consecutively
- if 4 or less, fill automatically
- add column: assign value for full period, first period or drop
- if more than a specific number is missing, drop municipality

"""