import pandas as pd

def subperiod1_start():
    global startdate1
    startdate1 = pd.to_datetime('2011-1-1')
    return startdate1

def subperiod1_end():
    global enddate1
    enddate1 = pd.to_datetime('2015-8-12')
    return enddate1

def subperiod2_start():
    global startdate2
    startdate2 = pd.to_datetime('2016-1-1')
    return startdate2

def subperiod2_end():
    global enddate2
    enddate2 = pd.to_datetime('2017-8-5')
    return enddate2

def subperiod3_start():
    global startdate3
    startdate3 = pd.to_datetime('2017-8-13')
    return startdate3

def subperiod3_end():
    global enddate3
    enddate3 = pd.to_datetime('2019-12-31')
    return enddate3

def subperiod4_start():
    global startdate4
    startdate4 = pd.to_datetime('2016-01-01')
    return startdate4

def subperiod4_end():
    global enddate4
    enddate4 = pd.to_datetime('2019-12-31')
    return enddate4

def subperiod5_start():
    global startdate5
    startdate5 = pd.to_datetime('2011-1-1')
    return startdate5

def subperiod5_end():
    global enddate5
    enddate5 = pd.to_datetime('2019-12-31')
    return enddate5

def SubperiodsDict():
    global SubperiodsDict
    SubperiodsDict = {'Subperiod 1': [subperiod1_start(), subperiod1_end()], 'Subperiod 2': [subperiod2_start(), subperiod2_end()], 
        'Subperiod 3': [subperiod3_start(), subperiod3_end()], 'Subperiod 4': [subperiod4_start(), 
        subperiod4_end()],'Subperiod 5': [subperiod5_start(), subperiod5_end()]}
    return SubperiodsDict
print(SubperiodsDict())
print(SubperiodsDict.values())

#lists
def SubperiodsList():
    global SubperiodsList
    SubperiodsList = [subperiod1_start(), subperiod1_end(), subperiod2_start(), subperiod2_end(), 
        subperiod3_start(), subperiod3_end(), subperiod4_start(), subperiod4_end(), subperiod5_start(), subperiod5_end()]
    return SubperiodsList


def SubperiodsNames():
    global SubperiodsNames
    SubperiodsNames = ['Subperiod 1', 'Subperiod 2', 'Subperiod 3', 'Subperiod 4', 'Subperiod 5']
    return SubperiodsNames
print(SubperiodsNames())

