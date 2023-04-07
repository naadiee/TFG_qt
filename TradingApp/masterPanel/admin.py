from db.db_dao import DB_DAO
from PySide2 import QtWidgets
from stockFunctions import data


class Admin():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina Admin
        self.mainWindow.admin_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_admin))

        self.mainWindow.comboBox_addIndex_admin.currentIndexChanged.connect(self.selectStockIndex)
        #aceptarAddIndex_admin_bt_tab
        self.mainWindow.delete_admin_bt.clicked.connect(self.deleteUser)
        self.mainWindow.aactualizar_admin_bt.clicked.connect(self.mostrarUsuarios)
        self.mainWindow.aceptarAddIndex_admin_bt_tab.clicked.connect(self.saveData)


    def selectStockIndex(self):
        indexSeleccion = self.mainWindow.comboBox_addIndex_admin.currentIndex()
        seleeccion = self.mainWindow.comboBox_addIndex_admin.itemText(indexSeleccion)

        return [indexSeleccion, seleeccion]

    def downloadData(self, asset, timeFrame):
        priceData2years = data.get2yearDataSplit(asset, timeFrame)
        #priceData2years30 = data.getDatosMesIntervalo(asset, '60min', 'year1month1')

        return priceData2years

    def saveData(self):
        index, asset = self.selectStockIndex()
        registroActivos = [0, 0, 0, 0, 0, 0, 0]
        # TODO
        if index > 0: # else: muestra mensaje de error "No se ha seleccionado nada"

            if self.mainWindow.unoMin_box.isChecked():
                historicalData_1min = self.downloadData(asset, '1min')
                historicalData_1min[0].to_csv('data/' + asset + '_1min_year1.csv', index=False)
                historicalData_1min[1].to_csv('data/' + asset + '_1min_year2.csv', index=False)
                registroActivos[0] = 1

            if self.mainWindow.cincoMin_box.isChecked():
                historicalData_5min = self.downloadData(asset, '5min')
                historicalData_5min[0].to_csv('data/' + asset + '_5min_year1.csv', index=False)
                historicalData_5min[1].to_csv('data/' + asset + '_5min_year2.csv', index=False)
                registroActivos[1] = 1

            if self.mainWindow.quinceMin_box.isChecked():
                historicalData_15min = self.downloadData(asset, '15min')
                historicalData_15min[0].to_csv('data/' + asset + '_15min_year1.csv', index=False)
                historicalData_15min[1].to_csv('data/' + asset + '_15min_year2.csv', index=False)
                registroActivos[2] = 1
            if self.mainWindow.treintaMin_box.isChecked():
                historicalData_30min = self.downloadData(asset, '30min')
                historicalData_30min[0].to_csv('data/' + asset + '_30min_year1.csv', index=False)
                historicalData_30min[1].to_csv('data/' + asset + '_30min_year2.csv', index=False)
                registroActivos[3] = 1

            if self.mainWindow.cuarentacincoMin_box.isChecked():
                historicalData_45min = self.downloadData(asset, '45min')
                historicalData_45min[0].to_csv('data/' + asset + '_45min_year1.csv', index=False)
                historicalData_45min[1].to_csv('data/' + asset + '_45min_year2.csv', index=False)
                registroActivos[4] = 1

            if self.mainWindow.sesentaMin_box.isChecked():
                historicalData_60min = self.downloadData(asset, '60min')
                historicalData_60min[0].to_csv('data/' + asset + '_60min_year1.csv', index=False)
                historicalData_60min[1].to_csv('data/' + asset + '_60min_year2.csv', index=False)
                registroActivos[5] = 1

            if self.mainWindow.daily_box.isChecked():
                historicalData_daily = data.getDaily(asset)
                historicalData_daily[0] = historicalData_daily[0].rename(columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close'})  # cambiar los nombres de las columnas
                historicalData_daily[0].to_csv('data/' + asset + '_daily.csv')
                registroActivos[6] = 1

            self.dao.registrarActivo(asset, registroActivos)
            self.unCheckSaveFrame()
            print("Hecho.....")

        else:
            print("No ha hecho ninguna seleccion")

    def unCheckSaveFrame(self):

        self.mainWindow.unoMin_box.setChecked(False)
        self.mainWindow.cincoMin_box.setChecked(False)
        self.mainWindow.quinceMin_box.setChecked(False)
        self.mainWindow.treintaMin_box.setChecked(False)
        self.mainWindow.cuarentacincoMin_box.setChecked(False)
        self.mainWindow.sesentaMin_box.setChecked(False)
        self.mainWindow.daily_box.setChecked(False)


    # unoMin_box cincoMin_box quinceMin_box treintaMin_box
    # cuarentacincoMin_box sesentaMin_box  daily_box
    def mostrarUsuarios(self):
        datos = self.dao.mostrarUsuarios()
        totalusers = len(datos)
        self.mainWindow.tableWidget.setRowCount(totalusers)
        filaTabla = 0

        for columna in datos:
            self.mainWindow.tableWidget.setItem(filaTabla, 0, QtWidgets.QTableWidgetItem(columna[0]))
            filaTabla += 1

    def deleteUser(self):

        self.fila_seleccionada = self.mainWindow.tableWidget.currentRow()

        if self.fila_seleccionada != -1:
            nombre_usr = self.mainWindow.tableWidget.item(self.fila_seleccionada, 0).text()
            self.mainWindow.tableWidget.removeRow(self.fila_seleccionada)
            self.dao.deleteUser(nombre_usr)

