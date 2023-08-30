from db.db_dao import DB_DAO
from werkzeug.security import generate_password_hash


class Perfil:

    def __init__(self, panel, user):
        self.dao = DB_DAO()
        self.mainWindow = panel
        self.user_id = user

        # Pagina perfil
        self.mainWindow.perfil_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_perfil))
        # Aceptar cambiar nombre
        # Cambiar nombres de botones un poco mierda
        self.mainWindow.aceptarUser_perfil_bt.clicked.connect(self.cambiarNombreUsuario)
        self.mainWindow.cambioPass_perfil_bt.clicked.connect(self.cambiarpassword)
        self.mainWindow.aceptarPassworDelete_perfil_bt.clicked.connect(self.eliminarCuenta)
        self.mainWindow.aceptarCuenta_perfil_bt.clicked.connect(self.modificarDatosCuenta)
        # ComboBox seleccion de nivel
        self.mainWindow.comboBox_selecLevel_perfil.currentIndexChanged.connect(self.seleccionarNivelUsuario)
        # SpinBox saldo get value when stop pushing
        self.mainWindow.spinBox_selectSaldo_perfil.editingFinished.connect(self.getSbxSaldo)

    def cambiarNombreUsuario(self):

        nuevo_user = self.mainWindow.usuarioNuevo_tab.text()
        confirm_pass = self.mainWindow.passwordConfirm_tab.text()

        if not self.dao.existeUsuario(nuevo_user):
            if self.dao.correct_password(confirm_pass, self.user_id):
                self.dao.cambiarNombre(nuevo_user, self.user_id)
                self.user_id = nuevo_user
                print("Nombre de usuario cambiado")
                self.mainWindow.usuarioNuevo_tab.clear()
                self.mainWindow.passwordConfirm_tab.clear()
            else:
                print("contraseña incorrecta")
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
                self.mainWindow.oldPasword_perfil_tab.clear()
                self.mainWindow.newPassword_perfil_tab.clear()
                self.mainWindow.newPasswordConfirm_perfil_tab.clear()
            else:
                print("Contraseña incorrecta")
        else:
            print("Nueva contraseña no coincide con confirmación")

    def eliminarCuenta(self):

        confirm_pass = self.mainWindow.passwordConfirmDelete_tab.text()

        if self.dao.correct_password(confirm_pass, self.user_id):
            if self.mainWindow.delete_box.isChecked():  # cambiar nombre del combobox
                self.dao.deleteUser(self.user_id)
                print("Se ha eliminado la cuenta con éxito")
                self.mainWindow.passwordConfirmDelete_tab.clear()
            else:
                print("No se ha marcado la casilla")
        else:
            print("Contraseña incorrecta")

    def getSbxSaldo(self):
        saldo = int(self.mainWindow.spinBox_selectSaldo_perfil.value())
        return saldo

    def modificarSaldo(self):
        saldo = self.getSbxSaldo()
        if saldo > 0:
            self.dao.setSaldo(saldo, self.user_id)
            self.mainWindow.spinBox_selectSaldo_perfil.clearFocus()
            self.mainWindow.spinBox_selectSaldo_perfil.setValue(0)

    def modificarNivel(self):
        cbx = self.seleccionarNivelUsuario()
        index = cbx[0]
        # nivel = cbx[1]

        if index > 0:
            self.dao.setExperiencia(index, self.user_id)
            self.mainWindow.comboBox_selecLevel_perfil.setCurrentIndex(0)

    def seleccionarNivelUsuario(self):
        indexSeleccion = self.mainWindow.comboBox_selecLevel_perfil.currentIndex()
        seleeccion = self.mainWindow.comboBox_selecLevel_perfil.itemText(indexSeleccion)

        return [indexSeleccion, seleeccion]

    def modificarDatosCuenta(self):
        self.modificarNivel()
        self.modificarSaldo()
