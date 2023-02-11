from forms.registrar.form_registation_view import FormRegisterView
from werkzeug.security import generate_password_hash
from db.db_dao import DB_DAO
from PySide2.QtWidgets import *
import time


class FormRegister(FormRegisterView, QMainWindow):

    def __init__(self):
        self.dao = DB_DAO()
        super().__init__()
        self.ventana = FormRegisterView()
        self.ventana.setupUi(self)
        self.setWindowTitle("Registrar")
        self.ventana.registrar_bt.clicked.connect(self.register)
        self.ventana.back_bt.clicked.connect(self.back)


    def back(self):
        self.hide()

    def register(self):
        if self.isConfirmationPassword():
            userName_entry = self.ventana.usuario_rgs.text().strip()
            password_entry = self.ventana.password_rgs.text().strip()
            encrypted_password = self.encriptarPassword(password_entry)

            if not self.dao.existeUsuario(userName_entry):
                self.dao.registrarUsuario([userName_entry, encrypted_password])
                print("Se ha registrado el usuario")
                self.ventana.registroOK_label.setText('Se ha registrado con exito')
                self.ventana.usuario_rgs.clear()
                self.ventana.password_rgs.clear()
                self.ventana.passwordConfir_rgs.clear()

                self.hide()
        self.ventana.registroOK_label.setText(' ')

    def isConfirmationPassword(self):
        status: bool = True
        self.ventana.passDiferente_incorrecto.setText('')
        password_entry = self.ventana.password_rgs.text()
        passwordConfir_entry = self.ventana.passwordConfir_rgs.text()

        if (password_entry != passwordConfir_entry):
            status = False
            self.ventana.passDiferente_incorrecto.setText('Las contraseñas no coinciden')

        return status


    def encriptarPassword(self, password_text):
        encrypted_pass = generate_password_hash(password_text, 'sha256')
        return encrypted_pass