from PySide2.QtWidgets import *
from forms.login.form_login_view import FormLoginView
from db.db_dao import DB_DAO

from controller import Controller


class Perfil:

    def __init__(self):
        self.dao = DB_DAO()
        super().__init__()
        #self.panel = MainPanelView()
        self.controller = Controller()

    def cambiarNombreUsuario(self):

        print(self.controller.getNuevoUser())
