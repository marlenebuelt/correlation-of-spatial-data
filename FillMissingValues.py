import pandas as pd
import math
import SubperiodsPaths as spp

getAllSubPeriods = spp.getAllSubPeriods()
finaldf = pd.DataFrame()
setfinalslist = spp.setfinalslist()

for i in range(len(getAllSubPeriods)):
    df = getAllSubPeriods[i]
    finaldf = pd.DataFrame()
    municList = df['munic'].drop_duplicates().dropna().tolist()
    for j in range(len(municList)): #slices the large dataframe into munics to avoid incorrect values when the first value in a row is missing
        municdf = df[df['munic']==municList[j]]
        count = 0
        for k in range(len(municdf)):
            erp = municdf.iloc[k, 3]
            try:
                if math.isnan(erp) and municdf.iloc[k-1, 3].notnull:
                    fillna = municdf.iloc[k-1, 3]
                    municdf = municdf.replace(to_replace = [df.iloc[k, 3]], value = fillna)
            except:
                fillna = 0
                municdf = municdf.replace(to_replace = [df.iloc[k, 3]], value = fillna)
        finaldf = finaldf.append(municdf, ignore_index=True)
    finaldf.to_csv(setfinalslist[i])