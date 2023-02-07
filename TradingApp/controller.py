from PySide2 import QtCore
from PySide2.QtWidgets import *


class Controller():

    def __init__(self, panel):
        #self.dao = DB_DAO()

        self.panel = panel


       # self.panel.aceptar_bt_pg.clicked.connect(self.cambiarNombreUsuario)


    def getNuevoUser(self):
        return self.panel.usuarioNuevo_tb.text().strip()

