import pandas as pd
import math
import SubperiodsPaths as spp

getAllSubPeriods = spp.getAllSubP_afterdrop1()
finaldf = pd.DataFrame()
setfinalslist = spp.setfinalslist()

for i in range(len(getAllSubPeriods)):
    df = getAllSubPeriods[i]
    finaldf = pd.DataFrame()
    municList = df['munic'].drop_duplicates().dropna().tolist()
    for j in range(len(municList)): #slices the large dataframe into munics to avoid incorrect values if the first value in a row is missing
        municdf = df[df['munic']==municList[j]]
        municdf = municdf.loc[:, ['munic', 'fdate', 'ETHANOLrp', 'longitude', 'latitude']]
        municdf = municdf.ffill(axis = 0)
        finaldf = finaldf.append(municdf, ignore_index=True)
    finaldf.to_csv(setfinalslist[i])
    print(finaldf)