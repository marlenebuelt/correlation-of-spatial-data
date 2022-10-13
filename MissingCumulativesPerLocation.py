import pandas as pd
import matplotlib.pyplot as plt
import SubperiodsPaths as spp

#inspired by: https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas
#convert dates and drop anything after january 1st, 2020
data = spp.getOriginalFile()

municList = data['munic'].drop_duplicates().dropna().tolist()

df = pd.DataFrame()
result2= pd.DataFrame()

#missing cumulatives in ethanol --> count column shows number of weeks
for i in range(len(municList)):
    df = data[data['munic']==municList[i]]
    df['Group']=df.ETHANOLrp.notnull().astype(int).cumsum()
    df=df[df.ETHANOLrp.isnull()]
    df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>4].index)]
    df['count']=df.groupby('Group')['Group'].transform('size')
    df = df.drop_duplicates(['Group'], keep='first')
    result2 = result2.append(df, ignore_index=True)
result2 = result2[['munic', 'fdate', 'count']]
result2.to_csv(spp.maxCumulativesPerLocationEthanol())

#missing cumulatives in gasoline --> count column shows number of weeks
result3= pd.DataFrame()
for i in range(len(municList)):
    df = data[data['munic']==municList[i]]
    df['Group']=df.GASOLINErp.notnull().astype(int).cumsum()
    df=df[df.GASOLINErp.isnull()]
    df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>4].index)]
    df['count']=df.groupby('Group')['Group'].transform('size')
    df = df.drop_duplicates(['Group'],keep='first')
    result3 = result3.append(df, ignore_index=True)
result3 = result3[['munic', 'fdate', 'count']]
result3.to_csv(spp.maxCumulativesPerLocationGasoline())