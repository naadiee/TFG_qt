from db.db_dao import DB_DAO
from stockFunctions import data
from stockFunctions import analisisTecnico
from stockFunctions.trading import Trading
from datetime import datetime
import numpy as np
import pandas as pd
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
class TradingPanel():

    def __init__(self, panel, userName):
        self.dao = DB_DAO()
        self.mainWindow = panel
        self.userName = userName
        self.trading = Trading(self.userName)

        # Pagina Trading mostramos la pagina
        self.mainWindow.trading_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_trading))

        # cambiamos dentro de la pagina a la vista de solicitud de datos al otro stackedWidget
        self.mainWindow.ventanas_trading.setCurrentWidget(
            self.mainWindow.page_solicitarDatos)

        # al apretar el boton por un lado cambiamos a una nueva pagina ademas de pasar los datos
        self.mainWindow.aceptarDatos_trading_bt.clicked.connect(self.accion)

        # ahora cambiamos al stackedWidget de ventanas_trading nos movemos ahi
        self.mainWindow.back_resultadosTrading_bt.clicked.connect(
            lambda: self.mainWindow.ventanas_trading.setCurrentWidget(
                self.mainWindow.page_solicitarDatos))
        # para que se seleccione la opcion del combobox, aquilla que se quede marcada
        self.mainWindow.comboBox_selectIndix_trading.currentIndexChanged.connect(self.selectAsset)

        self.mainWindow.comboBox_selectTimeFrame.currentIndexChanged.connect(self.selectTimeFrame)

        # spinBox saldo y dias de exposicion
        self.mainWindow.spinBox_tiempoExposicion.editingFinished.connect(self.getSbxTiempoExposicion)
        self.mainWindow.spinBox_cantidadPosicion_trading.editingFinished.connect(self.getSbxCantidadPosicion)


    def getSbxTiempoExposicion(self):
        tiempo = int(self.mainWindow.spinBox_tiempoExposicion.value())
        return tiempo

    def getSbxCantidadPosicion(self):
        cantidad = int(self.mainWindow.spinBox_cantidadPosicion_trading.value())
        return cantidad

    def selectAsset(self):
        indexSeleccion = self.mainWindow.comboBox_selectIndix_trading.currentIndex()
        seleeccion = self.mainWindow.comboBox_selectIndix_trading.itemText(indexSeleccion)

        return [indexSeleccion, seleeccion]

    def selectTimeFrame(self):
        indexSeleccion = self.mainWindow.comboBox_selectTimeFrame.currentIndex()
        seleeccion = self.mainWindow.comboBox_selectTimeFrame.itemText(indexSeleccion)

        return [indexSeleccion, seleeccion]

    def getFecha(self):
        date = self.mainWindow.dateEdit_fechaInicio_trading.date()
        fecha = datetime(date.year(), date.month(), date.day())
        #return [date.day(), date.month(), date.year()]
        return fecha

    def getAsset(self):
        datos = self.selectAsset()
        #print(datos[1])
        return datos[1]

    def getTimeFrame(self):
        datos = self.selectTimeFrame()
        #print(datos[1])
        return datos[1]


    def getAssetDataIntraday(self, timeFrame):
        index, asset = self.selectAsset()

        if index > 0:
            try:
                datos = data.readAssetData(asset, timeFrame)
                return datos
            except:
                print("no se ha enontrado el fichero")


    def getAssetDataDaily(self):
        index, asset = self.selectAsset()

        if index > 0:
            try:
                datos = data.readDailyData(asset)
                return datos
            except:
                print("no se ha enontrado el fichero")

    def accion(self):
        self.mainWindow.ventanas_trading.setCurrentWidget(self.mainWindow.page_resultados)
        asset = self.getAsset()
        timeFrame = self.getTimeFrame()
        fecha = self.getFecha()
        year = fecha.year
        month = fecha.month
        cantidad = self.getSbxCantidadPosicion()

        df = self.getAssetDataIntraday(timeFrame)
        df_technicalData = analisisTecnico.getDatosTecnicos(df)
        df_month = analisisTecnico.getMonthCandlestick(df, year, month)
        entradas = analisisTecnico.posiblesEntradas(df_technicalData)
        lista_datos = self.trading.tradingResults(df_month,entradas, year, month, asset, cantidad)
        self.mainWindow.tableWidget_3.setRowCount(len(lista_datos))
        filaTabla = 0

        for tupla in lista_datos:

            self.mainWindow.tableWidget_3.setItem(filaTabla, 0, QtWidgets.QTableWidgetItem(str(tupla[0])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 1, QtWidgets.QTableWidgetItem(str(tupla[1])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 2, QtWidgets.QTableWidgetItem(str(tupla[2])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 3, QtWidgets.QTableWidgetItem(str(tupla[3])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 4, QtWidgets.QTableWidgetItem(str(tupla[4])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 5, QtWidgets.QTableWidgetItem(str(tupla[5])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 6, QtWidgets.QTableWidgetItem(str(tupla[6])))
            self.mainWindow.tableWidget_3.setItem(filaTabla, 7, QtWidgets.QTableWidgetItem(tupla[7]))
            filaTabla += 1

    def getResults(self):
        #obtenemos los datos la analisisTecnico.py pero antes se leen en data.py
        pass

    def mostrarResultados(self):
        # los mostramos en la pagina mostrar data
        pass

