# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowMqOKWP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color: rgb(77, 125, 238);\n"
"border:Noe")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.munu_bt = QPushButton(self.frame_superior)
        self.munu_bt.setObjectName(u"munu_bt")
        self.munu_bt.setMinimumSize(QSize(150, 35))
        self.munu_bt.setMaximumSize(QSize(16777215, 35))
        palette = QPalette()
        brush = QBrush(QColor(77, 125, 238, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush2 = QBrush(QColor(0, 0, 0, 240))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.munu_bt.setPalette(palette)
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.munu_bt.setFont(font)
        self.munu_bt.setStyleSheet(u"QPushButton{\n"
"	border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(52, 78, 155);\n"
"	border-radius:5px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"img/menuu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.munu_bt.setIcon(icon)
        self.munu_bt.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.munu_bt)

        self.horizontalSpacer = QSpacerItem(594, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.admin_bt = QPushButton(self.frame_superior)
        self.admin_bt.setObjectName(u"admin_bt")
        self.admin_bt.setMaximumSize(QSize(16777215, 35))
        self.admin_bt.setStyleSheet(u"QPushButton{\n"
"	border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(52, 78, 155);\n"
"	\n"
"	\n"
"	border-radius:5px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"img/administrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.admin_bt.setIcon(icon1)
        self.admin_bt.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.admin_bt)

        self.salir_bt = QPushButton(self.frame_superior)
        self.salir_bt.setObjectName(u"salir_bt")
        self.salir_bt.setMaximumSize(QSize(16777215, 35))
        self.salir_bt.setStyleSheet(u"QPushButton{\n"
"	border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(52, 78, 155);\n"
"	border-radius:5px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"img/salir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salir_bt.setIcon(icon2)
        self.salir_bt.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.salir_bt)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"border:Noe")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_izq = QFrame(self.frame_inferior)
        self.frame_izq.setObjectName(u"frame_izq")
        self.frame_izq.setMinimumSize(QSize(0, 0))
        self.frame_izq.setMaximumSize(QSize(0, 16777215))
        self.frame_izq.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(77, 125, 238);\n"
"	border:Noe\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	\n"
"	font: 75 14pt \"Arial\";\n"
"	\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(52, 78, 155);\n"
"	font: 75 14pt \"Arial\";\n"
"	\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.frame_izq.setFrameShape(QFrame.StyledPanel)
        self.frame_izq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_izq)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.trading_bt = QPushButton(self.frame_izq)
        self.trading_bt.setObjectName(u"trading_bt")
        self.trading_bt.setMinimumSize(QSize(50, 50))
        self.trading_bt.setMaximumSize(QSize(16777215, 50))
        icon3 = QIcon()
        icon3.addFile(u"img/trading.png", QSize(), QIcon.Normal, QIcon.Off)
        self.trading_bt.setIcon(icon3)
        self.trading_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.trading_bt)

        self.historial_bt = QPushButton(self.frame_izq)
        self.historial_bt.setObjectName(u"historial_bt")
        self.historial_bt.setMinimumSize(QSize(50, 50))
        self.historial_bt.setMaximumSize(QSize(16777215, 50))
        icon4 = QIcon()
        icon4.addFile(u"img/historial2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historial_bt.setIcon(icon4)
        self.historial_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.historial_bt)

        self.info_bt = QPushButton(self.frame_izq)
        self.info_bt.setObjectName(u"info_bt")
        self.info_bt.setMinimumSize(QSize(50, 50))
        self.info_bt.setMaximumSize(QSize(16777215, 50))
        icon5 = QIcon()
        icon5.addFile(u"img/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_bt.setIcon(icon5)
        self.info_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.info_bt)

        self.perfil_bt = QPushButton(self.frame_izq)
        self.perfil_bt.setObjectName(u"perfil_bt")
        self.perfil_bt.setMinimumSize(QSize(50, 50))
        self.perfil_bt.setMaximumSize(QSize(16777215, 50))
        self.perfil_bt.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u"img/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfil_bt.setIcon(icon6)
        self.perfil_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.perfil_bt)

        self.verticalSpacer = QSpacerItem(20, 344, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_izq)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_izq)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:Noe")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:Noe")
        self.page_trading = QWidget()
        self.page_trading.setObjectName(u"page_trading")
        self.pushButton = QPushButton(self.page_trading)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 190, 641, 26))
        self.pushButton.setStyleSheet(u"background-color: rgb(27, 18, 255);")
        self.stackedWidget.addWidget(self.page_trading)
        self.page_historial = QWidget()
        self.page_historial.setObjectName(u"page_historial")
        self.pushButton_2 = QPushButton(self.page_historial)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 240, 571, 26))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(69, 255, 74);\n"
"color: rgba(0, 0, 0, 240);")
        self.stackedWidget.addWidget(self.page_historial)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.pushButton_3 = QPushButton(self.page_info)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 220, 431, 26))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(167, 14, 61);\n"
"color: rgba(0, 0, 0, 240);")
        self.stackedWidget.addWidget(self.page_info)
        self.page_perfil = QWidget()
        self.page_perfil.setObjectName(u"page_perfil")
        self.pushButton_4 = QPushButton(self.page_perfil)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 220, 561, 26))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(172, 97, 36);")
        self.stackedWidget.addWidget(self.page_perfil)
        self.page_veinte = QWidget()
        self.page_veinte.setObjectName(u"page_veinte")
        self.stackedWidget.addWidget(self.page_veinte)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.munu_bt.setText("")
        self.admin_bt.setText("")
        self.salir_bt.setText("")
        self.trading_bt.setText(QCoreApplication.translate("MainWindow", u"   Trading", None))
        self.historial_bt.setText(QCoreApplication.translate("MainWindow", u"   Hisorial", None))
        self.info_bt.setText(QCoreApplication.translate("MainWindow", u"   Ayuda  ", None))
        self.perfil_bt.setText(QCoreApplication.translate("MainWindow", u"  Perfil    ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TradingApp", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"trading", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"perfil", None))
    # retranslateUi

