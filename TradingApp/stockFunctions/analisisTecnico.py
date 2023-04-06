import yfinance as yf

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