import keyword
from optparse import Values
from tracemalloc import start
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

#get files (not the way getters and setters actually work, but the data is capsuled here)
def getSubP1Path():
    global dataSubP1
    dataSubP1 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod1.csv')
    return dataSubP1

def getSubP2Path():
    global dataSubP2
    dataSubP2 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod2.csv')
    return dataSubP2

def getSubP3Path():
    global dataSubP3
    dataSubP3 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod3.csv')
    return dataSubP3

def getSubP4Path():
    global dataSubP4
    dataSubP4 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod4.csv')
    return dataSubP4

def getSubP5Path():
    global dataSubP5
    dataSubP5 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod5.csv')
    return dataSubP5

#reads all subPeriods, returns a list of adapted data
def getAllSubPeriods():
    global getAllSubPeriods
    getAllSubPeriods = [getSubP1Path(), getSubP2Path(), getSubP3Path(), getSubP4Path(), getSubP5Path()]
    for i in range(len(getAllSubPeriods)):
        df = getAllSubPeriods[i]
        df = df.loc[:10000,['munic','fdate', 'ETHANOLrp']]
        df['fdate'] = pd.to_datetime(df['fdate'])
    return getAllSubPeriods

#files with NAN-values filled
def setSubP1Final(df):
    global dataSubP1Final
    dataSubP1Final = df.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod1_final.csv')
    return dataSubP1Final

def setSubP2Final(df):
    global dataSubP2Final
    dataSubP2Final = df.to_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod2_final.csv')
    return dataSubP2Final

def setSubP3Final():
    global dataSubP3Final
    dataSubP3Final = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod3_final.csv')
    return dataSubP3Final

def setSubP4Final():
    global dataSubP4Final
    dataSubP4Final = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod4_final.csv')
    return dataSubP4Final

def setSubP5Final():
    global dataSubP5Final
    dataSubP5Final = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod5_final.csv')
    return dataSubP5Final

def setfinalslist():
    global getfinalslist
    getfinalslist = [setSubP1Final(), setSubP2Final(), setSubP3Final(), setSubP4Final(), setSubP5Final()]
    return getfinalslist