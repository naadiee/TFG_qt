from ta.momentum import RSIIndicator, StochasticOscillator, StochRSIIndicator
from ta.trend import MACD

import numpy as np
import pandas as pd
from datetime import datetime

def maximos_minimosLocales(precio, ventana):
    extremos_relativos_min = []
    extremos_relativos_max = []
    for i in range(ventana, len(precio) - ventana):
        max_precio = max(precio[(i - ventana): (i + ventana)])
        if precio[i] == max_precio:
            extremos_relativos_max.append(max_precio)

        min_precio = min(precio[(i - ventana): (i + ventana)])

        if precio[i] == min_precio:
            extremos_relativos_min.append(min_precio)

    return extremos_relativos_max + extremos_relativos_max


def precio_valido(precio1, precio2, margen):
    margen_aux = 1 - (min([precio1, precio2]) / max([precio1, precio2]))

    return margen_aux < margen


def index_notin(indexi, indexj, indexArray):
    if indexi not in indexArray and indexj not in indexArray:
        return True
    else:
        False


def soportes_resistencias(precios, ventana, margen):
    extremos_relativos = maximos_minimosLocales(precios, ventana)
    margen_porcentanje = (margen / 100)  # porcentaje de marge para tomar una vela como válida
    soportes_resistencias = []
    index_vistos = []
    print(margen_porcentanje)

    for i in range(len(extremos_relativos)):
        for j in range(len(extremos_relativos)):
            if precio_valido(extremos_relativos[i], extremos_relativos[j], margen_porcentanje):
                if i != j and index_notin(i, j, index_vistos):
                    soportes_resistencias.append(extremos_relativos[i])
                    index_vistos.append(i)
                    index_vistos.append(j)

    return list(dict.fromkeys(soportes_resistencias))


def numVecesResistenciaTocada(precios, resistencias, margen):
    dic_resistencias = dict.fromkeys(resistencias, 0)

    for key, value in dic_resistencias.items():
        for j in range(len(precios)):
            if precio_valido(key, precios[j], margen):
                dic_resistencias[key] += 1

    return dic_resistencias


def getRSI(dfClose):
    indicator = RSIIndicator(close=dfClose["Close"], window=14, fillna=False)
    return indicator.rsi()


def getStoch(df):
    indicator = StochasticOscillator(high=df["High"], low=df["Low"], close=df["Close"], window=14, smooth_window=3, fillna=False)

    return [indicator.stoch(), indicator.stoch_signal()]


def getStochRSI(dfClose):
    indicator = StochRSIIndicator(close=dfClose["Close"], window=14, smooth1=3, smooth2=3, fillna=False)

    return [indicator.stochrsi(), indicator.stochrsi_d(), indicator.stochrsi_k()]


def getMACD(dfClose):
    indicator = MACD(close=dfClose["Close"], window_slow=26, window_fast=12, window_sign=9, fillna=False)

    return [indicator.macd(), indicator.macd_diff(), indicator.macd_signal()]


def buscarVelasSegunFecha(df, fechaObjetivo):
    year = fechaObjetivo.year
    month = fechaObjetivo.month
    day = fechaObjetivo.day
    condicion = (df.index.year == year) & (df.index.month == month) & (df.index.day == day)
    result = df.loc[condicion]

    return result


def existeResistencia_soporte(dic, num):
    if num in dic:
        return dic[num]

    return 0

    # si existe una resistencia o soporte devuelve un numero positivo distinto de 0, en caso contrario devulve un cero


def removeWeakSupotResistance(dic_sr):
    nuevo_dic = dic_sr.copy()  # hacemos una copia del original para que la funcion no modifique el original, ya que da error porque cambia el tamaño al iterar "RuntimeError"
    for clave, valor in dic_sr.items():
        if valor < 3:
            del nuevo_dic[clave]

    return nuevo_dic
# quitamos aquellos maximos o minimos locales los cuales hayan sido tocados menos de 3 veces

def getDatosTecnicos(df):
    rsi = True
    stoch = True
    macd = True

    df_aux = df.copy()
    if rsi:
        rsi_df = getRSI(df)
        df_aux["rsi"] = rsi_df

    if stoch:
        stoch_df = getStoch(df)
        df_aux["stoch"] = stoch_df[0]
        df_aux["stoch_signal"] = stoch_df[1]

    if macd:
        macd_df = getMACD(df)
        df_aux["macd"] = macd_df[0]
        df_aux["macd_signal"] = macd_df[1]

    return df_aux


def rsi_sobreventa(row):  # buy signal
    return row['rsi'][0] < 30


def rsi_sobrecompra(row):  # sell signal
    return row['rsi'][0] > 70


def rsi_neutral(buy_signal, sell_signal):
    return buy_signal and sell_signal


def rsi_calculo(row):
    if row['rsi'] < 30:
        return 1
    elif row['rsi'] > 70:
        return -1
    else:
        return 0

def stoch_sobreventa(row):
    return row['stoch'][0] < 20

def stoch_sobrecompra(row):
    return row['stoch'][0] > 80

def stoch_cruce_compra(row):
    return row['stoch'][0] > row['stoch_signal'][0]

def stoch_cruce_venta(row):
    return row['stoch'][0] < row['stoch_signal'][0]

# row['stoch'][0] para acceder al dato ya que el tipo de datos que devuleve es numpy.float64

def stoch_calculo(row):
    if row['stoch'] < 20:
        return 1
    elif row['stoch'] > 80:
        return -1
    else:
        return 0

def stoch_cruce_calculo(row):
    if row['stoch'][0] > row['stoch_signal'][0]:
        return 1
    elif row['stoch'][0] < row['stoch_signal'][0]:
        return -1

def macd_calculo(row):
    if row['macd'][0] > row['macd_signal'][0]:
        return 1 # buy signal
    elif row['macd'][0] < row['macd_signal'][0]:
        return -1 #sell signal
    else:
        return 0 # neutral


def posiblesEntradas(df):
    df_nuevo = pd.DataFrame(
        columns=['Open', 'High', 'Low', 'Close', 'Volume', 'rsi', 'stoch', 'stoch_signal', 'macd', 'macd_signal'])

    for index, row in df.iterrows():

        if rsi_calculo(row) == 1:
            if stoch_calculo(row) == 1:
                df_nuevo.loc[index] = row

    return df_nuevo

def posiblesSalidasTecnicos(df):
    df_nuevo = pd.DataFrame(
        columns=['Open', 'High', 'Low', 'Close', 'Volume', 'rsi', 'stoch', 'stoch_signal', 'macd', 'macd_signal'])

    for index, row in df.iterrows():

        if rsi_calculo(row) == -1:
            if stoch_calculo(row) == -1:
                df_nuevo.loc[index] = row

    return df_nuevo

def salidaPorcentaje(df, porcentaje, precio_medio):
    df_nuevo = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    valor_multiplicativo = (porcentaje / 100) + 1
    precio_objetivo = valor_multiplicativo * precio_medio

    for index, row in df.iterrows():
        if precio_objetivo >= row['Low'] and precio_objetivo <= row['High']:  # El precio de salida esta dentro del rango de precio de la vela, es decir, se ha llegao en algun momento
            df_nuevo.loc[index] = row

    return df_nuevo


def comprasDias(df_dia, porcentaje):
    valorMult = 1 - (porcentaje / 100)
    numCompras = 0
    precioMedio = 0
    ultimaCompra = 0
    ultimaCompraTime = df_dia.index[0]

    for index, row in df_dia.iterrows():
        if numCompras == 0:
            precioMedio = precioMedio + row['Close']
            ultimaCompra = row['Close']
            numCompras = numCompras + 1
            # Registrar en base de datos para historia
            # print("NumCompras:",numCompras)
            print(index)
            print(row['Close'])
            print("-----------------------")
            precioNuevoAux = ultimaCompra * valorMult
        elif numCompras > 0 and numCompras < 4:
            if (precioNuevoAux > row['Close']):
                precioMedio = precioMedio + row['Close']
                ultimaCompra = row['Close']
                numCompras = numCompras + 1
                precioNuevoAux = ultimaCompra * valorMult
                ultimaCompraTime = index
                print(index)
                # Registrar en base de datos para historia
                # print("NumCompras:",numCompras)
                print(row['Close'])
                print("-----------------------")
        else:
            break

    return [precioMedio / numCompras, numCompras, ultimaCompraTime]


def ventaDia(df, dollarAmount, numVecesPromedio, precioCompra, lastBuyTime):
    year = lastBuyTime.year
    month = lastBuyTime.month
    day = lastBuyTime.day
    hour = lastBuyTime.hour
    minute = lastBuyTime.minute
    venta = False
    # aux = porcentaje * 1.02
    nuevoPrecioCompra = precioCompra * 1.02

    remain_df = getSalidasAvailable(df, year, month, day, hour)

    for index, row in remain_df.iterrows():

        if lastBuyTime != index:
            if nuevoPrecioCompra >= row['Low'] and nuevoPrecioCompra <= row['High']:
                venta = True
                # Registrar la venta en la base de datos
                break

    return venta


def getMonthCandlestick(df, year, month):
    condicion = (df.index.year == year) & (df.index.month == month)
    result = df.loc[condicion]

    return result


def getSalidasAvailable(df, year, month, day, hour):
    condicion = (df.index.year == year) & (df.index.month == month) & (df.index.day == day) & (df.index.hour >= hour)

    result = df.loc[condicion]

    return result


