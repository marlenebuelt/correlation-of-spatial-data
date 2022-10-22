import pandas as pd
import SubperiodsDates as spd
import SubperiodsPaths as spp
# #looks at dataframes of dropped periods in detail
# NOT CHECKED YET

subpall = spp.missingValsAll()
counter = 0

all_subp = spp.getAllSubP_afterdrop1()
subp_list = spd.SubperiodsNames

for i in range(len(all_subp)):
    subp = subp_list[i]
    current_subp = all_subp[i]
    result_period = pd.DataFrame()
    dateList = current_subp['fdate'].drop_duplicates().dropna().tolist()
    for j in range(len(dateList)):
        date_df = current_subp[(current_subp['fdate']==dateList[j])]
        row = pd.Series({'fdate': dateList[j], subp: date_df['ETHANOLrp'].isna().sum()})
        result_period = pd.concat([result_period, row.to_frame().T], ignore_index=True)
    result_period.to_csv(subpall[counter])
    counter = counter + 1
    print(result_period)