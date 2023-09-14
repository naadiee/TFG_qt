from db.db_dao import DB_DAO
from stockFunctions import data
from stockFunctions import analisisTecnico

class Trading():

    def __init__(self, userName):
        self.userName = userName
        self.dao = DB_DAO()


    def ventaDia(self, df, tradingPower, numVecesPromedio, precioCompra, lastBuyTime, activo):
        year = lastBuyTime.year
        month = lastBuyTime.month
        day = lastBuyTime.day
        hour = lastBuyTime.hour
        minute = lastBuyTime.minute
        venta = 0
        nuevoPrecioCompra = precioCompra * 1.015
        remain_df = analisisTecnico.buscarVelasSegunFecha(df, lastBuyTime)

        for index, row in remain_df.iterrows():

            if lastBuyTime != index and index.hour >= hour:
                if nuevoPrecioCompra >= row['Low'] and nuevoPrecioCompra <= row['High']:
                    venta = nuevoPrecioCompra
                    fechaAux = str(index.year) + "-" + str(index.month) + "-" + str(index.day)
                    cantidadCompra = tradingPower * (numVecesPromedio/4)
                    self.dao.registrarOperacion(self.userName, "venta", activo, float(venta), cantidadCompra, fechaAux)
                    break

        return venta

    def comprasDias(self, df_dia, porcentaje, activo, cantidad):
        valorMult = 1 - (porcentaje / 100)
        numCompras = 0
        precioMedio = 0
        precioNuevoAux = 0
        ultimaCompraTime = df_dia.index[0]
        datosCompras = () #tupla vacia
        precioCompraMedia = 0

        for index, row in df_dia.iterrows():
            fechaAux = str(index.year) + "-" + str(index.month) + "-" + str(index.day)
            if index.hour <= 16:
                if numCompras == 0:
                    precioMedio = precioMedio + row['Close']
                    ultimaCompra = row['Close']
                    numCompras = numCompras + 1
                    self.dao.registrarOperacion(self.userName, "compra", activo, float(row['Close']), cantidad, fechaAux)
                    datosCompras = datosCompras + (float(row['Close']),)
                    precioNuevoAux = ultimaCompra * valorMult
                elif numCompras > 0 and numCompras < 4:
                    if precioNuevoAux > row['Close']:
                        precioMedio = precioMedio + row['Close']
                        ultimaCompra = row['Close']
                        numCompras = numCompras + 1
                        precioNuevoAux = ultimaCompra * valorMult
                        ultimaCompraTime = index
                        self.dao.registrarOperacion(self.userName, "compra", activo, float(row['Close']), cantidad, fechaAux)
                        datosCompras = datosCompras + (float(row['Close']),)
                else:
                    break

                precioCompraMedia = precioMedio / numCompras

        return [precioCompraMedia, numCompras, ultimaCompraTime, datosCompras]

    def tradingResults(self, df_month,df, year, month, activo, cantidad):
        month_df = analisisTecnico.getMonthCandlestick(df, year, month)
        lista_mes = []

        while (month_df.shape[0] > 0):  # comprobamos que el df tiene filas
            day_df = analisisTecnico.buscarVelasSegunFecha(month_df, month_df.index[0])

            precio = self.comprasDias(day_df, 1, activo, cantidad)
            if precio[0] != 0:
                if precio[1] == 1:
                    precio[3] = precio[3] + (0,0,0,)
                if precio[1] == 2:
                    precio[3] = precio[3] + (0,0)
                if precio[1] == 3:
                    precio[3] = precio[3] + (0,)

                datos_trade = precio[3]
                venta_aux = self.ventaDia(df_month, cantidad, precio[1], precio[0], precio[2], activo)
                precioVenta = round(venta_aux, 3)
                precioCompra = round(precio[0], 3)
                fecha = precio[2].strftime('%d-%m-%Y')
                ganancias_aux = self.getGanancias(precioCompra, precioVenta, cantidad, precio[1])
                ganancias = round(ganancias_aux, 3)
                datos_trade = datos_trade + (precioVenta, precioCompra, ganancias, fecha,)
                lista_mes.append(datos_trade)
            indices_a_eliminar = day_df.index
            month_df = month_df.drop(indices_a_eliminar)

        return lista_mes

    def getGanancias(self, precioCompra, precioVenta, cantidad, vecesPromediado):

        ganancias = 0

        if precioVenta != 0:
            diferencia = precioVenta - precioCompra
            cantidadDisponible = cantidad * (vecesPromediado/4)
            cantidadComprada = cantidadDisponible/precioCompra
            ganancias = cantidadComprada * diferencia

        return ganancias