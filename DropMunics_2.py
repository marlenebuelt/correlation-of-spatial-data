import pandas as pd
import SubperiodsPaths as spp
import SubperiodsDates as spd
#this categorization will delete any municipality that has more than four weeks missing in row
#Returns the new files in seperate csv-files

df_list = spp.getAllSubP_beforedrop()
subp_dict = spd.SubperiodsDatesDict()
result_csv_list = spp.setAllSubP_afterdrop2()
maxmissingweeks = 4

for i in range(len(df_list)): 
    df = df_list[i]
    municList = df['munic'].drop_duplicates().dropna().tolist()
    df_munic = pd.DataFrame()
    droplist = []
    result = pd.DataFrame()
    for j in range(len(municList)):
        df_munic = df[df['munic']==municList[j]]
        df_munic['Group']=df_munic.ETHANOLrp.notnull().astype(int).cumsum()
        df_munic=df_munic[df_munic.ETHANOLrp.isnull()]
        df_munic=df_munic[df_munic.Group.isin(df_munic.Group.value_counts()[df_munic.Group.value_counts()>maxmissingweeks].index)]
        df_munic['count']=df_munic.groupby('Group')['Group'].transform('size')
        result = result.append(df_munic, ignore_index=True)
    droplist = result['munic'].drop_duplicates()
    df = df[df.munic.isin(droplist)==False]
    df.to_csv(result_csv_list[i])