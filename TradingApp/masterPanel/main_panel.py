from PySide2.QtWidgets import *
from forms.login.form_login_view import FormLoginView
from db.db_dao import DB_DAO
from masterPanel.main_panel_view import MainPanelView
from forms.registrar.form_registation import FormRegister

from PySide2 import QtCore
from PySide2 import QtGui,QtWidgets
from PySide2.QtCore import QPropertyAnimation

class MainPanel(MainPanelView, QMainWindow):
    def __init__(self):
        #self.dao = DB_DAO()
        super().__init__()
        self.mainWindow = MainPanelView()
        self.mainWindow.setupUi(self)
        self.setWindowTitle("TradingApp")

        # Acceso a paginas:

        # Pagina Inicio
        self.mainWindow.inicio_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_inicio))
        #Pagina Trading
        self.mainWindow.trading_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_trading))
        # Pagina Historial
        self.mainWindow.historial_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_historial))
        # Pagina Información
        self.mainWindow.info_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_info)) # IMPORTANTE: info_bt y page_ayuda mismo nombre hay confusion
        # Pagina perfil
        self.mainWindow.perfil_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_perfil))

        # Pagina Admin
        self.mainWindow.admin_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_admin))

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

