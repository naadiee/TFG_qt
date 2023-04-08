import yfinance as yf
from ta.momentum import RSIIndicator, StochasticOscillator, StochRSIIndicator
from ta.trend import MACD
TSLAyf = yf.Ticker("TSLA")
precio = TSLAyf.history(period="3y")["Close"]

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
    margen_porcentanje = (margen / 100)  # porcentaje de marge para tomar una vela como valida
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
    indicator = StochasticOscillator(high=df["High"], low=df["Low"], close=df["Close"], window=14,
                                                 smooth_window=3, fillna=False)

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