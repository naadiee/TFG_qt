from db.db_dao import DB_DAO
from PySide2 import QtWidgets


class Historial:

    def __init__(self, panel, usrName):
        self.dao = DB_DAO()
        self.mainWindow = panel
        self.usrName = usrName

        # Pagina Historial
        self.mainWindow.historial_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_historial))

        self.mostrarHistorial()



    def mostrarHistorial(self):
        datos = self.dao.getHistorial(self.usrName)
        totalHistorial = len(datos)
        self.mainWindow.tableWidget_2.setRowCount(totalHistorial)
        filaTabla = 0

        for fila in datos:
            columnaTabla = 0
            print(fila[2])
            print(fila[3])
            print(type(fila[4]))
            print(type(fila[5]))
            print(fila[6])
            print("----")
            precio = str(fila[4])
            cantidad = str(fila[5])
            fecha = fila[6].strftime('%d-%m-%Y')
            print(fecha)
            self.mainWindow.tableWidget_2.setItem(filaTabla, 0, QtWidgets.QTableWidgetItem(fila[2]))
            self.mainWindow.tableWidget_2.setItem(filaTabla, 1, QtWidgets.QTableWidgetItem(fila[3]))
            self.mainWindow.tableWidget_2.setItem(filaTabla, 2, QtWidgets.QTableWidgetItem(precio))
            self.mainWindow.tableWidget_2.setItem(filaTabla, 3, QtWidgets.QTableWidgetItem(cantidad))
            self.mainWindow.tableWidget_2.setItem(filaTabla, 4, QtWidgets.QTableWidgetItem(fecha))
            filaTabla += 1
       # for columna in datos:
        #    self.mainWindow.tableWidget_2.setItem(filaTabla, 0, QtWidgets.QTableWidgetItem(columna[0]))
         #

