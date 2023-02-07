from masterPanel.main_panel_view import MainPanelView
from PySide2 import QtCore
from PySide2.QtWidgets import *


class Controller(MainPanelView, QMainWindow):

    def __init__(self):
        #self.dao = DB_DAO()
        super().__init__()
        self.panel = MainPanelView()
        self.panel.setupUi(self)

        self.panel.aceptar_bt_pg.clicked.connect(self.cambiarNombreUsuario)


    def getNuevoUser(self):
        return self.panel.usuarioNuevo_tb.text().strip()

