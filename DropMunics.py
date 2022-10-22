import pandas as pd
import SubperiodsPaths as spp
import SubperiodsDates as spd
import numpy as np

#Returns the munics we'll drop in seperate csv-files, decision based on dropfile

df_list = spp.getAllSubP_beforedrop()
dropfile = spp.getDropFile()
dropfile= dropfile.astype({'Subperiod 4': np.float})
subperiodnames = spd.SubperiodsNames
resultcsv = spp.setAllSubP_afterdrop1()

for i in range(len(df_list)):
    df = df_list[i]
    subp = subperiodnames[i]
    dropdf_subp = dropfile.loc[:,['munic', subp]]
    dropdf_subp = dropdf_subp[dropdf_subp[subp]==0]
    droplist = dropdf_subp['munic'].to_list()
    df = df[df.munic.isin(droplist)==False]
    print(df)
    df.to_csv(resultcsv[i])