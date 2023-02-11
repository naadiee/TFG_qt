from db.db_dao import DB_DAO
from PySide2 import QtWidgets


class Admin():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina Admin
        self.mainWindow.admin_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_admin))

        self.mainWindow.comboBox_addIndex_admin.currentIndexChanged.connect(self.seleccStockIndex)

        self.mainWindow.delete_admin_bt.clicked.connect(self.deleteUser)
        self.mainWindow.aactualizar_admin_bt.clicked.connect(self.mostrarUsuarios)



    def seleccStockIndex(self):
        indexSeleccion = self.mainWindow.comboBox_addIndex_admin.currentIndex()
        seleeccion = self.mainWindow.comboBox_addIndex_admin.itemText(indexSeleccion)

        print(seleeccion + " = ", indexSeleccion)

    def mostrarUsuarios(self):
        #no se porque peta al vovler a dar a actualizar
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


