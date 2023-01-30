# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_registrarcjvReL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FormRegisterView(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(789, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(114, 205, 113);\n"
"border-radius:20px;\n"
"border:1px solid #00007f;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 40, 161, 141))
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
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 75 21pt \"Arial\";\n"
"border:Noe")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.usuario_rgs = QLineEdit(self.frame)
        self.usuario_rgs.setObjectName(u"usuario_rgs")
        self.usuario_rgs.setGeometry(QRect(280, 230, 231, 31))
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
        self.usuario_rgs.setPalette(palette)
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.usuario_rgs.setFont(font1)
        self.usuario_rgs.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.usuario_rgs.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 270, 181, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 75 21pt \"Arial\";\n"
"border:Now")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.password_rgs = QLineEdit(self.frame)
        self.password_rgs.setObjectName(u"password_rgs")
        self.password_rgs.setGeometry(QRect(280, 330, 231, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.password_rgs.setPalette(palette1)
        self.password_rgs.setFont(font1)
        self.password_rgs.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.password_rgs.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 380, 241, 51))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 75 21pt \"Arial\";\n"
"border:Now")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.passwordConfir_rgs = QLineEdit(self.frame)
        self.passwordConfir_rgs.setObjectName(u"passwordConfir_rgs")
        self.passwordConfir_rgs.setGeometry(QRect(280, 440, 231, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.passwordConfir_rgs.setPalette(palette2)
        self.passwordConfir_rgs.setFont(font1)
        self.passwordConfir_rgs.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.passwordConfir_rgs.setAlignment(Qt.AlignCenter)
        self.registrar_bt = QPushButton(self.frame)
        self.registrar_bt.setObjectName(u"registrar_bt")
        self.registrar_bt.setGeometry(QRect(330, 510, 131, 41))
        palette3 = QPalette()
        brush5 = QBrush(QColor(33, 142, 36, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.registrar_bt.setPalette(palette3)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.registrar_bt.setFont(font2)
        self.registrar_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(33, 142, 36);\n"
"	\n"
"	font: 75 14pt \"Arial\";\n"
"border: 2px solid #ffffff\n"
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
        self.passDiferente_incorrecto = QLabel(self.frame)
        self.passDiferente_incorrecto.setObjectName(u"passDiferente_incorrecto")
        self.passDiferente_incorrecto.setGeometry(QRect(290, 480, 221, 20))
        palette4 = QPalette()
        brush6 = QBrush(QColor(237, 0, 17, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(114, 205, 113, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.passDiferente_incorrecto.setPalette(palette4)
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.passDiferente_incorrecto.setFont(font3)
        self.passDiferente_incorrecto.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.passDiferente_incorrecto.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.usuario_rgs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su usuario o correo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.password_rgs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Repita su contrase\u00f1a", None))
        self.passwordConfir_rgs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmaci\u00f3n", None))
        self.registrar_bt.setText(QCoreApplication.translate("MainWindow", u"registrar", None))
        self.passDiferente_incorrecto.setText("")
    # retranslateUi

