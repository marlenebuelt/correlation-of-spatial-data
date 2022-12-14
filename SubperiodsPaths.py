from asyncore import file_dispatcher
import pandas as pd

#get files (not the way getters and setters actually work, but the paths are capsuled here)
def getOriginalFile():
    global original_file
    original_file = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/20220906Data2011_2020.csv')
    original_file = original_file.loc[:10000, ['munic', 'fdate', 'ETHANOLrp', 'longitude', 'latitude']]
    original_file['fdate'] = pd.to_datetime(original_file['fdate'])
    original_file = original_file.loc[~(original_file['fdate'] >= '2019-12-31')]
    return original_file

def getDropFile():
    global dropfile
    dropfile = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/dropfile_all_periods.csv', sep=';')
    return dropfile

#dates before drop, original df sliced into subperiods
def setSubP1Path_beforedrop():
    global dataSubP1_beforedrop
    dataSubP1_beforedrop = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_beforedrop/subperiod1_beforedrop.csv'
    return dataSubP1_beforedrop

def setSubP2Path_beforedrop():
    global dataSubP2_beforedrop
    dataSubP2_beforedrop = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_beforedrop/subperiod2_beforedrop.csv'
    return dataSubP2_beforedrop

def setSubP3Path_beforedrop():
    global dataSubP3_beforedrop
    dataSubP3_beforedrop = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_beforedrop/subperiod3_beforedrop.csv'
    return dataSubP3_beforedrop

def setSubP4Path_beforedrop():
    global dataSubP4_beforedrop
    dataSubP4_beforedrop = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_beforedrop/subperiod4_beforedrop.csv'
    return dataSubP4_beforedrop

def setSubP5Path_beforedrop():
    global dataSubP5_beforedrop
    dataSubP5_beforedrop = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_beforedrop/subperiod5_beforedrop.csv'
    return dataSubP5_beforedrop

def setAllSubP_beforedrop():
    global setAllSubP_beforedrop
    setAllSubP_beforedrop = [setSubP1Path_beforedrop(), setSubP2Path_beforedrop(), setSubP3Path_beforedrop(), setSubP4Path_beforedrop(), setSubP5Path_beforedrop()]
    return setAllSubP_beforedrop

def getSubP1Path_beforedrop():
    global subP1Path_beforedrop
    subP1Path_beforedrop = pd.read_csv(setSubP1Path_beforedrop())
    return subP1Path_beforedrop

def getSubP2Path_beforedrop():
    global subP2Path_beforedrop
    subP2Path_beforedrop = pd.read_csv(setSubP2Path_beforedrop())
    return subP2Path_beforedrop

def getSubP3Path_beforedrop():
    global subP3Path_beforedrop
    subP3Path_beforedrop = pd.read_csv(setSubP3Path_beforedrop())
    return subP3Path_beforedrop

def getSubP4Path_beforedrop():
    global subP4Path_beforedrop
    subP4Path_beforedrop = pd.read_csv(setSubP4Path_beforedrop())
    return subP4Path_beforedrop

def getSubP5Path_beforedrop():
    global subP5Path_beforedrop
    subP5Path_beforedrop = pd.read_csv(setSubP5Path_beforedrop())
    return subP5Path_beforedrop

def getAllSubP_beforedrop():
    global getAllSubP_beforedrop
    getAllSubP_beforedrop = [getSubP1Path_beforedrop(), getSubP2Path_beforedrop(), getSubP3Path_beforedrop(), getSubP4Path_beforedrop(), getSubP5Path_beforedrop()]
    return getAllSubP_beforedrop

#drop1
def setSubP1Path_afterdrop1():
    global dataSubP1_afterdrop1
    dataSubP1_afterdrop1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_1/subperiod1_afterdrop1.csv'
    return dataSubP1_afterdrop1

def setSubP2Path_afterdrop1():
    global dataSubP2_afterdrop1
    dataSubP2_afterdrop1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_1/subperiod2_afterdrop1.csv'
    return dataSubP2_afterdrop1

def setSubP3Path_afterdrop1():
    global dataSubP3_afterdrop1
    dataSubP3_afterdrop1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_1/subperiod3_afterdrop1.csv'
    return dataSubP3_afterdrop1

def setSubP4Path_afterdrop1():
    global dataSubP4_afterdrop1
    dataSubP4_afterdrop1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_1/subperiod4_afterdrop1.csv'
    return dataSubP4_afterdrop1

def setSubP5Path_afterdrop1():
    global dataSubP5_afterdrop1
    dataSubP5_afterdrop1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_1/subperiod5_afterdrop1.csv'
    return dataSubP5_afterdrop1

def setAllSubP_afterdrop1():
    global setAllSubP_afterdrop1
    setAllSubP_afterdrop1 = [setSubP1Path_afterdrop1(), setSubP2Path_afterdrop1(), setSubP3Path_afterdrop1(), setSubP4Path_afterdrop1(), setSubP5Path_afterdrop1()]
    return setAllSubP_afterdrop1

def getSubP1Path_afterdrop1():
    global subP1Path_afterdrop
    subP1Path_afterdrop = pd.read_csv(setSubP1Path_afterdrop1())
    return subP1Path_afterdrop

def getSubP2Path_afterdrop1():
    global subP2Path_afterdrop
    subP2Path_afterdrop = pd.read_csv(setSubP2Path_afterdrop1())
    return subP2Path_afterdrop

def getSubP3Path_afterdrop1():
    global subP3Path_afterdrop
    subP3Path_afterdrop = pd.read_csv(setSubP3Path_afterdrop1())
    return subP3Path_afterdrop

def getSubP4Path_afterdrop1():
    global subP4Path_afterdrop
    subP4Path_afterdrop = pd.read_csv(setSubP4Path_afterdrop1())
    return subP4Path_afterdrop

def getSubP5Path_afterdrop1():
    global subP5Path_afterdrop
    subP5Path_afterdrop = pd.read_csv(setSubP5Path_afterdrop1())
    return subP5Path_afterdrop

def getAllSubP_afterdrop1():
    global getAllSubP_afterdrop1
    getAllSubP_afterdrop1 = [getSubP1Path_afterdrop1(), getSubP2Path_afterdrop1(), getSubP3Path_afterdrop1(), getSubP4Path_afterdrop1(), getSubP5Path_afterdrop1()]
    return getAllSubP_afterdrop1

#drop2
def setSubP1Path_afterdrop2():
    global dataSubP1_afterdrop2
    dataSubP1_afterdrop2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_2/subperiod1_afterdrop2.csv'
    return dataSubP1_afterdrop2

def setSubP2Path_afterdrop2():
    global dataSubP2_afterdrop2
    dataSubP2_afterdrop2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_2/subperiod2_afterdrop2.csv'
    return dataSubP2_afterdrop2

def setSubP3Path_afterdrop2():
    global dataSubP3_afterdrop2
    dataSubP3_afterdrop2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_2/subperiod3_afterdrop2.csv'
    return dataSubP3_afterdrop2

def setSubP4Path_afterdrop2():
    global dataSubP4_afterdrop2
    dataSubP4_afterdrop2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_2/subperiod4_afterdrop2.csv'
    return dataSubP4_afterdrop2

def setSubP5Path_afterdrop2():
    global dataSubP5_afterdrop2
    dataSubP5_afterdrop2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_afterdrop_2/subperiod5_afterdrop2.csv'
    return dataSubP5_afterdrop2

def setAllSubP_afterdrop2():
    global setAllSubP_afterdrop2
    setAllSubP_afterdrop2 = [setSubP1Path_afterdrop2(), setSubP2Path_afterdrop2(), setSubP3Path_afterdrop2(), setSubP4Path_afterdrop2(), setSubP5Path_afterdrop2()]
    return setAllSubP_afterdrop2

def getSubP1Path_afterdrop2():
    global subP1Path_afterdrop
    subP1Path_afterdrop = pd.read_csv(setSubP1Path_afterdrop2())
    return subP1Path_afterdrop

def getSubP2Path_afterdrop2():
    global subP2Path_afterdrop
    subP2Path_afterdrop = pd.read_csv(setSubP2Path_afterdrop2())
    return subP2Path_afterdrop

def getSubP3Path_afterdrop2():
    global subP3Path_afterdrop
    subP3Path_afterdrop = pd.read_csv(setSubP3Path_afterdrop2())
    return subP3Path_afterdrop

def getSubP4Path_afterdrop2():
    global subP4Path_afterdrop
    subP4Path_afterdrop = pd.read_csv(setSubP4Path_afterdrop2())
    return subP4Path_afterdrop

def getSubP5Path_afterdrop2():
    global subP5Path_afterdrop
    subP5Path_afterdrop = pd.read_csv(setSubP5Path_afterdrop2())
    return subP5Path_afterdrop

def getAllSubP_afterdrop2():
    global getAllSubP_afterdrop2
    getAllSubP_afterdrop2 = [getSubP1Path_afterdrop2(), getSubP2Path_afterdrop2(), getSubP3Path_afterdrop2(), getSubP4Path_afterdrop2(), getSubP5Path_afterdrop2()]
    return getAllSubP_afterdrop2

# get subp after drop 2 (more than 4 in row missing)
def getSubP1Path_beforedrop():
    global subP1Path_beforedrop
    subP1Path_beforedrop = pd.read_csv(setSubP1Path_beforedrop())
    return subP1Path_beforedrop

def getSubP2Path_beforedrop():
    global subP2Path_beforedrop
    subP2Path_beforedrop = pd.read_csv(setSubP2Path_beforedrop())
    return subP2Path_beforedrop

def getSubP3Path_beforedrop():
    global subP3Path_beforedrop
    subP3Path_beforedrop = pd.read_csv(setSubP3Path_beforedrop())
    return subP3Path_beforedrop

def getSubP4Path_beforedrop():
    global subP4Path_beforedrop
    subP4Path_beforedrop = pd.read_csv(setSubP4Path_beforedrop())
    return subP4Path_beforedrop

def getSubP5Path_beforedrop():
    global subP5Path_beforedrop
    subP5Path_beforedrop = pd.read_csv(setSubP5Path_beforedrop())
    return subP5Path_beforedrop

def getAllSubP_beforedrop():
    global getAllSubP_beforedrop
    getAllSubP_beforedrop = [getSubP1Path_beforedrop(), getSubP2Path_beforedrop(), getSubP3Path_beforedrop(), getSubP4Path_beforedrop(), getSubP5Path_beforedrop()]
    return getAllSubP_beforedrop

#missing values per location
def setMissingValsSubp1():
    global missingVals1
    missingVals1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod1_missingvalues.csv'
    return missingVals1

def setMissingValsSubp2():
    global missingVals2
    missingVals2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod2_missingvalues.csv'
    return missingVals2

def setMissingValsSubp3():
    global missingVals3
    missingVals3 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod3_missingvalues.csv'
    return missingVals3

def setMissingValsSubp4():
    global missingVals4
    missingVals4 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod4_missingvalues.csv'
    return missingVals4

def setMissingValsSubp5():
    global missingVals5
    missingVals5 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/subperiods_missingvalues/subperiod5_missingvalues.csv'
    return missingVals5

def setMissingValsAll():
    global missingvals
    missingvals = [setMissingValsSubp1(),setMissingValsSubp2(),setMissingValsSubp3(),setMissingValsSubp4(),setMissingValsSubp5()]
    return missingvals

# Missing values by date and munic
def setMissingByDateAndMunicSubP1Path():
    global dataSubP1
    dataSubP1 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/MissingByDateAndMunic/MissingByDateAndMunicSubperiod1.csv'
    return dataSubP1

def setMissingByDateAndMunicSubP2Path():
    global dataSubP2
    dataSubP2 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/MissingByDateAndMunic/MissingByDateAndMunicSubperiod2.csv'
    return dataSubP2

def setMissingByDateAndMunicSubP3Path():
    global dataSubP3
    dataSubP3 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/MissingByDateAndMunic/MissingByDateAndMunicSubperiod3.csv'
    return dataSubP3

def setMissingByDateAndMunicSubP4Path():
    global dataSubP4
    dataSubP4 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/MissingByDateAndMunic/MissingByDateAndMunicSubperiod4.csv'
    return dataSubP4

def setMissingByDateAndMunicSubP5Path():
    global dataSubP5
    dataSubP5 = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/MissingByDateAndMunic/MissingByDateAndMunicSubperiod5.csv'
    return dataSubP5

def setMissingByDateAndMunicAll():
    global missingByDateAndMunic
    missingByDateAndMunic = [setMissingByDateAndMunicSubP1Path(),setMissingByDateAndMunicSubP2Path(),setMissingByDateAndMunicSubP3Path(),setMissingByDateAndMunicSubP4Path(),setMissingByDateAndMunicSubP5Path()]
    return missingByDateAndMunic

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

def missingByDate():
    global missingDates
    missingDates = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/missingByDate.csv'
    return missingDates

def getMapBrazilPath():
    global mapBrazil
    mapBrazil = '/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/BR_Municipios_2020/BR_Municipios_2020.shp'
    return mapBrazil