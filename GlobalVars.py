import keyword
from optparse import Values
from tracemalloc import start
import pandas as pd

def subperiod1_start():
    global startdate
    startdate = pd.to_datetime('2011-1-1')
    return startdate

def subperiod1_end():
    global enddate
    enddate = pd.to_datetime('2015-8-12')
    return enddate

def subperiod2_start():
    global startdate
    startdate = pd.to_datetime('2016-1-1')
    return startdate

def subperiod2_end():
    global enddate
    enddate = pd.to_datetime('2017-8-5')
    return enddate

def subperiod3_start():
    global startdate
    startdate = pd.to_datetime('2017-8-13')
    return startdate

def subperiod3_end():
    global enddate
    enddate = pd.to_datetime('2019-12-31')
    return enddate

def subperiod4_start():
    global startdate
    startdate = pd.to_datetime('2017-8-13')
    return startdate

def subperiod4_end():
    global enddate
    enddate = pd.to_datetime('2019-12-31')
    return enddate

def subperiod5_start():
    global startdate
    startdate = pd.to_datetime('2011-1-1')
    return startdate

def subperiod5_end():
    global enddate
    enddate = pd.to_datetime('2019-12-31')
    return enddate

#iterate over this dict? --> might delete it, cant access it
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
print(SubperiodsList())

def SubperiodsNames():
    global SubperiodsNames
    SubperiodsNames = ['Subperiod1', 'Subperiod2', 'Subperiod3', 'Subperiod4', 'Subperiod5']
    return SubperiodsNames
print(SubperiodsNames())