from forms.login.form_login import FormLogin
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mi_app = FormLogin()
    mi_app.show()
    sys.exit(app.exec_())



