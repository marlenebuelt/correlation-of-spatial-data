import pandas as pd
import GlobalVars as gv
import math

getAllSubPeriods = gv.getAllSubPeriods()

for i in range(len(getAllSubPeriods)):
    df = getAllSubPeriods[i]
    municList = df['munic'].drop_duplicates().dropna().tolist()
    for j in range(len(municList)): #slices the large dataframe into munics to avoid incorrect values when the first value in a row is missing
        municdf = df.loc[:,['munic']==municList[j]]
        count = 0
        for k in range(len(municdf)):
            erp = municdf.iloc[k, 3]
            #index = 
            count = 0
            try:
                if math.isnan(erp):
                    fillna = municdf.iloc[k-1, 3]
                    municdf['ETHANOLrp'] = municdf['ETHANOLrp'].replace(to_replace = [municdf.iloc[k, 3]], value = fillna)
            except:
                fillna = 0
                df['ETHANOLrp'] = df['ETHANOLrp'].replace(to_replace = [municdf.iloc[k, 3]], value = fillna)
                count = count + 1
                print(count)
        print(municdf)