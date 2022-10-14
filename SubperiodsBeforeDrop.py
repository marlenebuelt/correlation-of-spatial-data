import pandas as pd
import SubperiodsPaths as spp
import SubperiodsDates as spd

#Returns the munics we'll drop in seperate csv-files
df = spp.getOriginalFile()
subp_dict = spd.SubperiodsDatesDict()
setAllSubP_beforedrop = spp.setAllSubP_beforedrop()

i = 0
for key in subp_dict: 
    result_period = pd.DataFrame()
    startenddatelist = subp_dict[key]
    startdate = startenddatelist[0]
    enddate = startenddatelist[1]
    df_subperiod = pd.DataFrame()
    df_subperiod = df[(df['fdate']>startdate) & (df['fdate']<enddate)]
    df_subperiod.to_csv(setAllSubP_beforedrop[i])
    i = i + 1
    print(df_subperiod)