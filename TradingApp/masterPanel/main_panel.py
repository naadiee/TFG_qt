from PySide2.QtWidgets import *
from masterPanel.main_panel_view import MainPanelView
from masterPanel.perfil import Perfil
from masterPanel.admin import Admin
from masterPanel.informacion import Informacion
from masterPanel.trading import Trading
from masterPanel.historial import Historial
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation


class MainPanel(MainPanelView, QMainWindow):
    def __init__(self):
        #self.dao = DB_DAO()
        super().__init__()
        self.mainWindow = MainPanelView()
        self.mainWindow.setupUi(self)
        self.setWindowTitle("TradingApp")
        self.perfil = Perfil(self.mainWindow)
        self.admin = Admin(self.mainWindow)
        self.info = Informacion(self.mainWindow)
        self.trading = Trading(self.mainWindow)
        self.historial = Historial(self.mainWindow)

        # Pagina Inicio
        self.mainWindow.inicio_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_inicio))

        # Menu dinamico -> mostrar o ocultar
        self.mainWindow.munu_bt.clicked.connect(self.mostrarMenu)





    def mostrarMenu(self):
        if True:
            ancho = self.mainWindow.frame_izq.width()
            ampliar = 0
            ocultar = 0
            if ancho == 0:
                ampliar = 150
            else:
                ampliar = ocultar
            self.animacion = QPropertyAnimation(self.mainWindow.frame_izq, b'minimumWidth')
            self.animacion.setDuration(250)
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(ampliar)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

