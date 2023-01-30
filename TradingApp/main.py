from forms.login.form_login import FormLogin
from PyQt5 import QtCore, QtGui, QtWidgets
from db.db_dao import DB_DAO

dao = DB_DAO()

dao.registrarUsuario(["pedro", "1234"])


