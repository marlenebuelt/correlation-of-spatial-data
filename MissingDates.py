import pandas as pd
import SubperiodsDates as spd
import SubperiodsPaths as spp
# looks at the dates in detail
df = spp.getOriginalFile()

dateList = df['fdate'].drop_duplicates().dropna().tolist()
result = pd.DataFrame(columns=['fdate'])
subp_dict = spd.SubperiodsDict
subpall = spp.missingValsAll()
counter = 0

for key in subp_dict: 
    result_period = pd.DataFrame()
    startenddatelist = subp_dict[key]
    startdate = startenddatelist[0]
    enddate = startenddatelist[1]
    for i in range(len(dateList)):
        date_df = df[(df['fdate']==dateList[i]) & (df['fdate']>startdate) & (df['fdate']<enddate)]
        row = pd.Series({'fdate': dateList[i], key: date_df['ETHANOLrp'].isna().sum()})
        result_period = pd.concat([result_period, row.to_frame().T], ignore_index=True)
    print(result_period)
    result_period.to_csv(subpall[counter])
    counter = counter + 1
