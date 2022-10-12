from asyncore import file_dispatcher
import pandas as pd

#get files (not the way getters and setters actually work, but the paths are capsuled here)
def getOriginalFile():
    global original_file
    original_file = pd.read_csv('/Users/marlenebultemann/Desktop/HTW/UM/correlation-of-spatial-data/resources/20220906Data2011_2020.csv')
    return original_file

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

#reads all subPeriods, returns a list of adapted data --> change length of frame here
def getAllSubPeriods():
    global getAllSubPeriods
    getAllSubPeriods = [getSubP1Path(), getSubP2Path(), getSubP3Path(), getSubP4Path(), getSubP5Path()]
    for i in range(len(getAllSubPeriods)):
        df = getAllSubPeriods[i]
        df = df.loc[:10000,['munic','fdate', 'ETHANOLrp']]
        df['fdate'] = pd.to_datetime(df['fdate'])
    return getAllSubPeriods

def getadaptedoriginalfile():
    global df_adapted
    df_adapted = getOriginalFile()
    df_adapted = df_adapted.loc[:10000,['fdate', 'ETHANOLrp']]
    df_adapted['fdate'] = pd.to_datetime(df_adapted['fdate'])
    df_adapted = df_adapted.loc[~(df_adapted['fdate'] >= '2019-12-31')]
    return df_adapted

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