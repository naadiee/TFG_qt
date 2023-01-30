from forms.login.form_login import FormLogin
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("TradingApp")
    mi_app = FormLogin()
    app.setWindowIcon(QIcon('img/icono.ico'))
    mi_app.show()
    sys.exit(app.exec_())



