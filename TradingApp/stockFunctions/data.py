from alpha_vantage.timeseries import TimeSeries
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


def getDatosMesIntervalo(activo, intervalo, periodo):
    ts = TimeSeries(key=ALPHA_VANTAGE_KEY, output_format='csv')

    # download the csv interval = 60min
    totalData = ts.get_intraday_extended(symbol=activo, interval=intervalo, slice=periodo)

    # csv --> dataframe
    df = pd.DataFrame(list(totalData[0]))

    # setup of column and index
    header_row = 0
    df.columns = df.iloc[header_row]
    df = df.drop(header_row)
    # df.set_index('time', inplace=True)
    df.reset_index(drop=True, inplace=True)

    # show output
    # print(df)
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
    data, meta_data = ts_daily.get_daily_adjusted(symbol=activo, outputsize='full')

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
    year1 = pd.read_csv('data/' + assetName + '_' + timeFrame + '_year1.csv', index_col=False)
    year2 = pd.read_csv('data/' + assetName + '_' + timeFrame + '_year2.csv', index_col=False)

    fullData = fullIntradayData2([year1, year2])
    fullData = fullData.reindex(index=fullData.index[::-1])
    fullData = cambiarIndexName(fullData, 'date')
    fullData = upperNames(fullData)
    fullData.index = pd.to_datetime(fullData.index)


    return fullData


def fullIntradayData2(twoYearArr):
    nuevo_df = pd.DataFrame()
    nuevo_df = pd.concat([twoYearArr[0], twoYearArr[1]], axis=0)
    nuevo_df.reset_index(drop=True, inplace=True)
    nuevo_df = nuevo_df.set_index('time')  # respecto a la otra funcion se diferencia el nombre de los indices

    return nuevo_df


def readDailyData(asset):
    daily = pd.read_csv('data/' + asset + '_daily.csv', index_col=False)
    daily = daily.drop(['4. close', '7. dividend amount', '8. split coefficient'], axis=1)  # eliminar columnas que no sirven
    daily = daily.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '5. adjusted close': 'Close', '6. volume': 'Volume'})
    daily = daily.set_index('date')  # cambiamos el indice a date
    daily_aux = daily.reindex(index=daily.index[::-1])  # invertir dataframe pasar de [1-300] a [300-1] primero datos antiguos últimos los nuevos

    return daily_aux


def upperNames(df):
    df = df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    return df


def cambiarIndexName(df, newIndexName):
    if df.index.name != newIndexName:
        df = df.rename_axis('date')  # 2

    return df
