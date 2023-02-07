from PySide2.QtWidgets import *
from db.db_dao import DB_DAO

from controller import Controller


class Perfil():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina perfil
        self.mainWindow.perfil_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_perfil))
        # Aceptar cambiar nombre
        self.mainWindow.aceptarUser_bt_pg.clicked.connect(self.cambiarNombreUsuario)

    def cambiarNombreUsuario(self):

        nuevo_user = self.mainWindow.usuarioNuevo_tab.text().strip()
        old_pass = self.mainWindow.passwordConfirm_tab.text().strip()

        print(nuevo_user)
        print(old_pass)