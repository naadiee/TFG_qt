from PySide2.QtWidgets import *
from forms.login.form_login_view import FormLoginView
from db.db_dao import DB_DAO
from masterPanel.main_panel_view import MainWindow
from forms.registrar.form_registation import FormRegister

from PySide2 import QtCore
from PySide2 import QtGui,QtWidgets
from PySide2.QtCore import QPropertyAnimation

class MainPanel(MainWindow, QMainWindow):
    def __init__(self):
        #self.dao = DB_DAO()
        super().__init__()
        self.mainWindow = MainWindow()
        self.mainWindow.setupUi(self)
        self.mainWindow.munu_bt.clicked.connect(self.mostrarMenu)



    def mostrarMenu(self):
        if True:
            ancho = self.mainWindow.frame_izq.width()
            ampliar = 0
            ocultar = 0
            if ancho == 0:
                ampliar = 200
            else:
                ampliar = ocultar
            self.animacion = QPropertyAnimation(self.mainWindow.frame_izq, b'minimumWidth')
            self.animacion.setDuration(250)
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(ampliar)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

