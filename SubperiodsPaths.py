from asyncore import file_dispatcher
import pandas as pd

#get files (not the way getters and setters actually work, but the paths are capsuled here)
def getOriginalFile():
    global original_file
    original_file = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/20220906Data2011_2020.csv')
    original_file = original_file.loc[:10000,['fdate', 'munic', 'ETHANOLrp','GASOLINErp']]
    original_file['fdate'] = pd.to_datetime(original_file['fdate'])
    original_file = original_file.loc[~(original_file['fdate'] >= '2019-12-31')]
    return original_file

#data after dropping municipalities #1 (see excel file with 1/0 for drop or keep)
def getSubP1Path_drop1():
    global dataSubP1
    dataSubP1 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod1.csv')
    return dataSubP1

def getSubP2Path_drop1():
    global dataSubP2
    dataSubP2 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod2.csv')
    return dataSubP2

def getSubP3Path_drop1():
    global dataSubP3
    dataSubP3 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod3.csv')
    return dataSubP3

def getSubP4Path_drop1():
    global dataSubP4
    dataSubP4 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod4.csv')
    return dataSubP4

def getSubP5Path_drop1():
    global dataSubP5
    dataSubP5 = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_data/subperiod5.csv')
    return dataSubP5

#reads all subPeriods, returns a list of adapted data --> change length of frame here
def getAllSubP_drop1():
    global getAllSubP_drop1
    getAllSubP_drop1 = [getSubP1Path_drop1(), getSubP2Path_drop1(), getSubP3Path_drop1(), getSubP4Path_drop1(), getSubP5Path_drop1()]
    for i in range(len(getAllSubP_drop1)):
        df = getAllSubP_drop1[i]
        df = df.loc[:10000,['munic','fdate', 'ETHANOLrp']]
        df['fdate'] = pd.to_datetime(df['fdate'])
    return getAllSubP_drop1


#missing values per location
def missingValsSubp1():
    global missingVals1
    missingVals1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod1_missingvalues.csv'
    return missingVals1

def missingValsSubp2():
    global missingVals2
    missingVals2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod2_missingvalues.csv'
    return missingVals2

def missingValsSubp3():
    global missingVals3
    missingVals3 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod3_missingvalues.csv'
    return missingVals3

def missingValsSubp4():
    global missingVals4
    missingVals4 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod4_missingvalues.csv'
    return missingVals4

def missingValsSubp5():
    global missingVals5
    missingVals5 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod1_missingvalues.csv'
    return missingVals5

def missingValsAll():
    global missingvals
    missingvals = [missingValsSubp1(),missingValsSubp2(),missingValsSubp3(),missingValsSubp4(),missingValsSubp5()]
    return missingvals

#files with NAN-values filled
def setSubP1Final():
    global dataSubP1Final
    dataSubP1Final = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod1_final.csv'
    return dataSubP1Final

def setSubP2Final():
    global dataSubP2Final
    dataSubP2Final ='/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod2_final.csv'
    return dataSubP2Final

def setSubP3Final():
    global dataSubP3Final
    dataSubP3Final = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod3_final.csv'
    return dataSubP3Final

def setSubP4Final():
    global dataSubP4Final
    dataSubP4Final = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod4_final.csv'
    return dataSubP4Final

def setSubP5Final():
    global dataSubP5Final
    dataSubP5Final = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_final/subperiod5_final.csv'
    return dataSubP5Final

def setfinalslist():
    global getfinalslist
    getfinalslist = [setSubP1Final(), setSubP2Final(), setSubP3Final(), setSubP4Final(), setSubP5Final()]
    return getfinalslist

def maxCumulativesPerLocationEthanol():
    global missingEthanol
    missingEthanol = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/Missing_Ethanol.csv'
    return missingEthanol

def maxCumulativesPerLocationGasoline():
    global missingGasoline
    missingGasoline = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/Missing_Gasoline.csv'
    return missingGasoline

def missingByDate():
    global missingDates
    missingDates = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/missingByDate.csv'
    return missingDates