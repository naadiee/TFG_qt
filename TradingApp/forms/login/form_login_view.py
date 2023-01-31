# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TradingApp2FOxDaQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormLoginView(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 633)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(77, 125, 238);\n"
"\n"
"border-radius:10px;\n"
"border:1px solid #00007f;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 30, 161, 141))
        self.label.setStyleSheet(u"border:Noe")
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setPixmap(QPixmap(u"img/logo2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 180, 181, 61))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 75 24pt \"Arial\";\n"
"border:Noe")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 300, 181, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 75 24pt \"Arial\";\n"
"border:Now")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(280, 350, 231, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(107, 107, 107, 217))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush2 = QBrush(QColor(107, 107, 107, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush3 = QBrush(QColor(255, 255, 255, 63))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.password.setPalette(palette)
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.password.setFont(font1)
        self.password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)
        self.login_bt = QPushButton(self.frame)
        self.login_bt.setObjectName(u"login_bt")
        self.login_bt.setGeometry(QRect(290, 430, 101, 41))
        palette1 = QPalette()
        brush5 = QBrush(QColor(33, 142, 36, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.login_bt.setPalette(palette1)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.login_bt.setFont(font2)
        self.login_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000\n"
"}\n"
"")
        self.salir_bt = QPushButton(self.frame)
        self.salir_bt.setObjectName(u"salir_bt")
        self.salir_bt.setGeometry(QRect(350, 550, 101, 41))
        palette2 = QPalette()
        brush6 = QBrush(QColor(200, 1, 17, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.salir_bt.setPalette(palette2)
        self.salir_bt.setFont(font2)
        self.salir_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgb(200, 1, 17);\n"
"	font: 75 14pt \"Arial\";\n"
"border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		\n"
"	\n"
"	background-color: rgb(132, 1, 11);\n"
"	font: 75 14pt \"Arial\";\n"
"border: 2px solid #000000\n"
"}\n"
"")
        self.usuario = QLineEdit(self.frame)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(280, 250, 231, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.usuario.setPalette(palette3)
        self.usuario.setFont(font1)
        self.usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.usuario.setAlignment(Qt.AlignCenter)
        self.usuario_incorrecto = QLabel(self.frame)
        self.usuario_incorrecto.setObjectName(u"usuario_incorrecto")
        self.usuario_incorrecto.setGeometry(QRect(290, 286, 221, 20))
        palette4 = QPalette()
        brush7 = QBrush(QColor(237, 0, 17, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        brush8 = QBrush(QColor(77, 125, 238, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.usuario_incorrecto.setPalette(palette4)
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.usuario_incorrecto.setFont(font3)
        self.usuario_incorrecto.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.usuario_incorrecto.setAlignment(Qt.AlignCenter)
        self.contrasena_incorrecta = QLabel(self.frame)
        self.contrasena_incorrecta.setObjectName(u"contrasena_incorrecta")
        self.contrasena_incorrecta.setGeometry(QRect(280, 390, 221, 20))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.contrasena_incorrecta.setPalette(palette5)
        self.contrasena_incorrecta.setFont(font3)
        self.contrasena_incorrecta.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta.setAlignment(Qt.AlignCenter)
        self.registra_bt = QPushButton(self.frame)
        self.registra_bt.setObjectName(u"registra_bt")
        self.registra_bt.setGeometry(QRect(410, 430, 101, 41))
        palette6 = QPalette()
        brush9 = QBrush(QColor(11, 69, 16, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        self.registra_bt.setPalette(palette6)
        self.registra_bt.setFont(font2)
        self.registra_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgb(11, 69, 16);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		\n"
"	background-color: rgb(12, 81, 9);\n"
"	font: 75 14pt \"Arial\";\n"
"border: 2px solid #000000\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.salir_bt.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su contrase\u00f1a", None))
        self.login_bt.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.salir_bt.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su usuario o correo", None))
        self.usuario_incorrecto.setText("")
        self.contrasena_incorrecta.setText("")
        self.registra_bt.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
    # retranslateUi

