import pandas as pd
import SubperiodsPaths as spp

#NOT DOUBLECHECKED YET
#inspired by: https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas
all_subp = spp.getAllSubP_afterdrop1()

df = pd.DataFrame()
result= pd.DataFrame()
maxmissingweeks = 4

#missing cumulatives in ethanol --> count column shows number of weeks
for i in range(len(all_subp)):
    current_subp = all_subp[i]
    municList = current_subp['munic'].drop_duplicates().dropna().tolist()
    for j in range(len(municList)):
        df = current_subp[current_subp['munic']==municList[j]]
        df['Group']=df.ETHANOLrp.notnull().astype(int).cumsum()
        df=df[df.ETHANOLrp.isnull()]
        df=df[df.Group.isin(df.Group.value_counts()[df.Group.value_counts()>maxmissingweeks].index)]
        df['count']=df.groupby('Group')['Group'].transform('size')
        df = df.drop_duplicates(['Group'], keep='first')
        result = result.append(df, ignore_index=True)
    result = result[['munic', 'fdate', 'count']]
    result.to_csv(spp.maxCumulativesPerLocationEthanol())
print(result)