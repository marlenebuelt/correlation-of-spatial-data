import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/20220906Data2011_2020.csv')

data2 = data.loc[:2000,['munic','fdate', 'ETHANOLrp', 'GASOLINErp']]
print(data2['ETHANOLrp'].isna().sum())
print(data2['GASOLINErp'].isna().sum())
municList = data2['munic'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['munic', 'ETHANOLrp_NaN', 'GASOLINErp_NaN'])

for i in range(len(municList)):
    munic_df = data2[data2['munic']== municList[i]].isna().sum()
    print(munic_df)
    row = pd.Series({'munic': municList[i], 'ETHANOLrp_NaN': munic_df.loc['ETHANOLrp'], 'GASOLINErp_NaN':munic_df.loc['GASOLINErp']})
    result = pd.concat([result, row.to_frame().T], ignore_index=True)
print(result)
result.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/result.csv')