import pandas_ta as ta
from finta import TA
from alpha_vantage.timeseries import TimeSeries
import numpy as np
import pandas as pd

ALPHA_VANTAGE_KEY = "TB29HAQCE0Z1EKTA"

def getFecha(time):
    aux = time.split()
    return aux[0]

def getTime(time):
    aux = time.split()
    return aux[1]

def getAnyo(date):
    date_aux = getFecha(date)
    return date_aux.split('-')[0]

def getMes(date):
    date_aux = getFecha(date)
    return date_aux.split('-')[1]

def getDia(date):
    date_aux = getFecha(date)
    return date_aux.split('-')[2]

def getHoras(hora):
    hora_aux = getTime(hora)
    return hora_aux.split(':')[0]

def getMinutos(hora):
    hora_aux = getTime(hora)
    return hora_aux.split(':')[1]

def getDatosMesIntervalo(activo , intervalo, periodo):
    ts = TimeSeries(key = ALPHA_VANTAGE_KEY, output_format = 'csv')

    #download the csv interval = 60min
    totalData = ts.get_intraday_extended(symbol = activo, interval = intervalo, slice = periodo)

    #csv --> dataframe
    df = pd.DataFrame(list(totalData[0]))

    #setup of column and index
    header_row=0
    df.columns = df.iloc[header_row]
    df = df.drop(header_row)
    #df.set_index('time', inplace=True)
    df.reset_index(drop=True, inplace=True)

    #show output
    #print(df)
    return df


def getDatosAnyo(activo, intervalo, anyo):
    mes = 1
    df = pd.DataFrame()
    df_aux = pd.DataFrame()

    for i in range(1, 13):
        slice_srt = "year" + str(anyo) + "month" + str(i)
        df_aux = getDatosMesIntervalo(activo, intervalo, slice_srt)
        df = pd.concat([df, df_aux], axis=0)

    # df.reset_index(drop=True, inplace=True)    FALTA
    return df

def getDaily(activo):
    ts_daily = TimeSeries(key=ALPHA_VANTAGE_KEY, output_format='pandas')
    data, meta_data = ts_daily.get_daily_adjusted(symbol= activo, outputsize='full')

    return [data, meta_data]


def completarMes(df_old, df_new):
    auxDate = df_old['time'][0]
    aux = df_new.query('time == @auxDate').index
    i = aux[0]

    df_aux = df_new.iloc[0: i]

    nuevo_df = pd.concat([df_aux, df_old], axis=0)
    nuevo_df.reset_index(drop=True, inplace=True)

    return nuevo_df


def get2yearDataSplit(activo, intervalo):
    datosAnyo1 = getDatosAnyo(activo, intervalo, 1)
    datosAnyo2 = getDatosAnyo(activo, intervalo, 2)
    datosAnyo1.reset_index(drop=True, inplace=True)
    datosAnyo2.reset_index(drop=True, inplace=True)

    return [datosAnyo1, datosAnyo2]


def fullIntradayData(twoYearArr):
    nuevo_df = pd.DataFrame()
    nuevo_df = pd.concat([twoYearArr[0], twoYearArr[1]], axis=0)
    nuevo_df.reset_index(drop=True, inplace=True)
    nuevo_df = nuevo_df.set_index('time')  #

    return nuevo_df


def descargarDatos(asset, timeFrame):
    twoYearData = get2yearDataSplit(asset, timeFrame)
    return twoYearData

def cambiar_tipos_de_columnas(df, columnas, tipos_de_datos):
    """
    Esta función cambia el tipo de datos de varias columnas en un DataFrame de Pandas.

    Args:
        df (pandas.DataFrame): El DataFrame original.
        columnas (list): Una lista con los nombres de las columnas a las que se les quiere cambiar el tipo de datos.
        tipos_de_datos (list): Una lista con los nuevos tipos de datos a los que se quiere convertir las columnas.

    Returns:
        pandas.DataFrame: El DataFrame con las columnas convertidas a los nuevos tipos de datos.
    """
    for columna, tipo_de_dato in zip(columnas, tipos_de_datos):
        df[columna] = df[columna].astype(tipo_de_dato)
    return df

def guardarDatos(asset, timeFrame):
    historicalData = descargarDatos(asset, timeFrame)
    historicalData[0].to_csv('data/' + asset + '_' + timeFrame + '_year1.csv', index=False)
    historicalData[1].to_csv('data/' + asset + '_' + timeFrame + '_year2.csv', index=False)
    print("datos guardados.... ")

# -----------------------------------------------------------------------------------------------------------------------------------
#                                                       LEER DATOS
# -----------------------------------------------------------------------------------------------------------------------------------

def readAssetData(assetName, timeFrame):
    year1 = pd.read_csv('datos/' + assetName + '_' + timeFrame + '_year1.csv', index_col=False)
    year2 = pd.read_csv('datos/' + assetName + '_' + timeFrame + '_year2.csv', index_col=False)

    fullData = fullIntradayData([year1, year2])
    fullData = fullData.reindex(index=fullData.index[::-1])

    return fullData

def upperNames(df):
    df = df.rename(columns = {'open':'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    return df


def cambiarIndexName(df, newIndexName):
    if df.index.name != newIndexName:
        df = df.rename_axis('date')  # 2

    return df

