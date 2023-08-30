from PySide2.QtWidgets import *
from forms.login.form_login_view import FormLoginView
from db.db_dao import DB_DAO
from forms.registrar.form_registation import FormRegister
from masterPanel.main_panel import MainPanel
from werkzeug.security import check_password_hash


class FormLogin(FormLoginView, QMainWindow):

    def __init__(self):
        self.dao = DB_DAO()
        super().__init__()
        self.ui = FormLoginView()  # asignamos a la variable ui nuestra ventana
        self.ui.setupUi(self)  # la establecemos
        self.setWindowTitle("Login")
        self.ventana = FormRegister()

        #  Acciones de los botones Inicio, sesión y registrar
        self.ui.login_bt.clicked.connect(self.verificar)
        self.ui.registra_bt.clicked.connect(self.ventanaRegistrar)

    def verificar(self):
        self.ui.contrasena_incorrecta.setText('')
        self.ui.usuario_incorrecto.setText('')
        user_entry = self.ui.usuario.text()
        passw_entry = self.ui.password.text()

        if self.correctUser(user_entry) and self.correctPassword(passw_entry, user_entry):
            self.panel = MainPanel(user_entry)
            self.hide()
            self.panel.show()
        else:
            self.ui.contrasena_incorrecta.setText('Contraseña incorrecta')
            self.ui.usuario_incorrecto.setText('Usuario incorrecto')

    def correctUser(self, usuario):
        estado = True

        if not self.dao.existeUsuario(usuario):
            estado = False
        return estado

    def correctPassword(self, password, userName):
        same = False
        encrypted = self.dao.get_encryptedPassword(userName)

        if check_password_hash(encrypted, password):
            same = True

        return same

    def ventanaRegistrar(self):
        self.ventana.show()
