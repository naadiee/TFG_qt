from PySide2.QtWidgets import *
from db.db_dao import DB_DAO
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash



class Perfil():

    def __init__(self, panel, user):
        self.dao = DB_DAO()
        self.mainWindow = panel
        self.user_id = user

        # Pagina perfil
        self.mainWindow.perfil_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_perfil))
        # Aceptar cambiar nombre
        #Cambiar nombres de botones un poco mierda
        self.mainWindow.aceptarUser_perfil_bt.clicked.connect(self.cambiarNombreUsuario)
        self.mainWindow.cambioPass_perfil_bt.clicked.connect(self.cambiarpassword)
        self.mainWindow.aceptarPassworDelete_perfil_bt.clicked.connect(self.eliminarCuenta)

    def cambiarNombreUsuario(self):

        nuevo_user = self.mainWindow.usuarioNuevo_tab.text()
        confirm_pass = self.mainWindow.passwordConfirm_tab.text()

        if not self.dao.existeUsuario(nuevo_user):
            if self.dao.correct_password(confirm_pass, self.user_id):
                self.dao.cambiarNombre(nuevo_user, self.user_id)
                self.user_id = nuevo_user
                print("Nombre de usuario cambiado")
            else:
                print("contraseña incorecta")
        else:
            print("UserName en uso, elija otro")

    def cambiarpassword(self):

        old_pass = self.mainWindow.oldPasword_perfil_tab.text()
        new_pass = self.mainWindow.newPassword_perfil_tab.text()
        new_pass_confirm = self.mainWindow.newPasswordConfirm_perfil_tab.text()

        if new_pass == new_pass_confirm:
            if self.dao.correct_password(old_pass, self.user_id):
                encrypted_pass = generate_password_hash(new_pass, 'sha256')
                self.dao.cambiarPasword(encrypted_pass, self.user_id)
                print("contraseña cambiada correctamente")
            else:
                print("Contraseña incorecta")
        else:
            print("Nueva contraseña no coincide con confirmacion")

    def eliminarCuenta(self):

        confirm_pass = self.mainWindow.passwordConfirmDelete_tab.text()

        if self.dao.correct_password(confirm_pass, self.user_id):
            if self.mainWindow.checkBox.isChecked(): # cambiar nombre del combobox
                self.dao.deleteUser(self.user_id)
                print("Se ha eliminado la cuenta con exito")
            else:
                print("No se ha marcado la casilla")
        else:
            print("Contraseña incorrecta")

