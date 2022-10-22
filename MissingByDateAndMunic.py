import pandas as pd
import SubperiodsDates as spd
import SubperiodsPaths as spp

#restructures data to easily see missing values

all_subp = spp.getAllSubP_afterdrop2()

final = pd.DataFrame(columns=['munic'])
final2= pd.DataFrame(columns=['Name'])
resultcsvlist = spp.setMissingByDateAndMunicAll()

for i in range(len(all_subp)):
    df = all_subp[i]
    result = pd.DataFrame()
    final = df.loc[:,['fdate']]
    municList = df['munic'].drop_duplicates().dropna().tolist()
    for j in range(len(municList)):
        df_munic = df[df['munic']==municList[j]]
        result = df_munic.loc[:,['fdate']]
        result[municList[j]] = df_munic.loc[:,['ETHANOLrp']]
        final= pd.merge(final, result, on='fdate', how='left')
    final.to_csv(resultcsvlist[i])
    print(final)