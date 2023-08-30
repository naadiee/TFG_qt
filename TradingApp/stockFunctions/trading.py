from db.db_dao import DB_DAO
from stockFunctions import data
from stockFunctions import analisisTecnico

class Trading():

    def __init__(self, userName):
        self.userName = userName
        self.dao = DB_DAO()


    def ventaDia(self, df, dollarAmount, numVecesPromedio, precioCompra, lastBuyTime):
        year = lastBuyTime.year
        month = lastBuyTime.month
        day = lastBuyTime.day
        hour = lastBuyTime.hour
        minute = lastBuyTime.minute
        venta = False
        # aux = porcentaje * 1.02
        nuevoPrecioCompra = precioCompra * 1.02

        remain_df = analisisTecnico.getSalidasAvailable(df, year, month, day, hour)

        for index, row in remain_df.iterrows():

            if lastBuyTime != index:
                if nuevoPrecioCompra >= row['Low'] and nuevoPrecioCompra <= row['High']:
                    venta = True
                    #self.dao.registrarOperacion(self.userName, "venta", "TSLA", 100, index)
                    break

        return venta

    def comprasDias(self, df_dia, porcentaje, activo, cantidad):
        valorMult = 1 - (porcentaje / 100)
        numCompras = 0
        precioMedio = 0
        ultimaCompra = 0
        ultimaCompraTime = df_dia.index[0]

        for index, row in df_dia.iterrows():
            fechaAux = str(index.year) + "-" + str(index.month) + "-" + str(index.day)
            if numCompras == 0:
                precioMedio = precioMedio + row['Close']
                ultimaCompra = row['Close']
                numCompras = numCompras + 1
                # Registrar en base de datos para historia
                self.dao.registrarOperacion(self.userName, "compra", activo, float(row['Close']), cantidad, fechaAux)
                # print("NumCompras:",numCompras)
                print(index)
                print(type(row['Close']))
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
                    #fechaAux = str(index.year) + "-" + str(index.month) + "-" + str(index.day)
                    # Registrar en base de datos para historia
                    self.dao.registrarOperacion(self.userName, "compra", activo, float(row['Close']), cantidad, fechaAux)
                    # print("NumCompras:",numCompras)
                    print(type(row['Close']))
                    print(row['Close'])
                    print("-----------------------")
            else:
                break

        return [precioMedio / numCompras, numCompras, ultimaCompraTime]

    def tradingResults(self, df, year, month, activo, cantidad):
        month_df = analisisTecnico.getMonthCandlestick(df, year, month)

        while (month_df.shape[0] > 0):  # comprobamos que el df tiene filas
            day_df = analisisTecnico.buscarVelasSegunFecha(month_df, month_df.index[0])
            # Llamamos a funcion que busque operaciones de entrada y dentro las apunte en la base de datos y las de salida
            # llamada a la funcion de operacion
            precio = self.comprasDias(day_df, 1, activo, cantidad)
            # print(month_df.index[0])
            self.ventaDia(day_df, 10000, precio[1], precio[0], precio[2])
            print("Precio: ", precio)
            indices_a_eliminar = day_df.index
            month_df = month_df.drop(indices_a_eliminar)
            print("*********************************")

