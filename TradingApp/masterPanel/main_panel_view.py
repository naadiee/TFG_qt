# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowHKiTVD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainPanelView(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 662)
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
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
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
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.inicio_bt = QPushButton(self.frame_izq)
        self.inicio_bt.setObjectName(u"inicio_bt")
        self.inicio_bt.setMinimumSize(QSize(50, 50))
        self.inicio_bt.setMaximumSize(QSize(16777215, 50))
        icon3 = QIcon()
        icon3.addFile(u"img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inicio_bt.setIcon(icon3)
        self.inicio_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.inicio_bt)

        self.trading_bt = QPushButton(self.frame_izq)
        self.trading_bt.setObjectName(u"trading_bt")
        self.trading_bt.setMinimumSize(QSize(50, 50))
        self.trading_bt.setMaximumSize(QSize(16777215, 50))
        icon4 = QIcon()
        icon4.addFile(u"img/trading.png", QSize(), QIcon.Normal, QIcon.Off)
        self.trading_bt.setIcon(icon4)
        self.trading_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.trading_bt)

        self.historial_bt = QPushButton(self.frame_izq)
        self.historial_bt.setObjectName(u"historial_bt")
        self.historial_bt.setMinimumSize(QSize(50, 50))
        self.historial_bt.setMaximumSize(QSize(16777215, 50))
        icon5 = QIcon()
        icon5.addFile(u"img/historial2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historial_bt.setIcon(icon5)
        self.historial_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.historial_bt)

        self.info_bt = QPushButton(self.frame_izq)
        self.info_bt.setObjectName(u"info_bt")
        self.info_bt.setMinimumSize(QSize(50, 50))
        self.info_bt.setMaximumSize(QSize(16777215, 50))
        icon6 = QIcon()
        icon6.addFile(u"img/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_bt.setIcon(icon6)
        self.info_bt.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.info_bt)

        self.perfil_bt = QPushButton(self.frame_izq)
        self.perfil_bt.setObjectName(u"perfil_bt")
        self.perfil_bt.setMinimumSize(QSize(50, 50))
        self.perfil_bt.setMaximumSize(QSize(16777215, 50))
        self.perfil_bt.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u"img/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfil_bt.setIcon(icon7)
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
        self.frame_contenedor.setMinimumSize(QSize(771, 621))
        self.frame_contenedor.setMaximumSize(QSize(921, 621))
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
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.inicio_label = QLabel(self.page_inicio)
        self.inicio_label.setObjectName(u"inicio_label")
        self.inicio_label.setGeometry(QRect(180, 0, 711, 611))
        self.inicio_label.setStyleSheet(u"border:Noe")
        self.inicio_label.setFrameShadow(QFrame.Plain)
        self.inicio_label.setPixmap(QPixmap(u"img/inico.png"))
        self.inicio_label.setScaledContents(True)
        self.inicio_label.setAlignment(Qt.AlignCenter)
        self.inicio_label.setIndent(0)
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_trading = QWidget()
        self.page_trading.setObjectName(u"page_trading")
        self.trading_bt_pg = QPushButton(self.page_trading)
        self.trading_bt_pg.setObjectName(u"trading_bt_pg")
        self.trading_bt_pg.setGeometry(QRect(190, 120, 641, 26))
        self.trading_bt_pg.setStyleSheet(u"background-color: rgb(27, 18, 255);")
        self.stackedWidget.addWidget(self.page_trading)
        self.page_historial = QWidget()
        self.page_historial.setObjectName(u"page_historial")
        self.historial_bt_pg = QPushButton(self.page_historial)
        self.historial_bt_pg.setObjectName(u"historial_bt_pg")
        self.historial_bt_pg.setGeometry(QRect(260, 120, 571, 26))
        self.historial_bt_pg.setStyleSheet(u"background-color: rgb(69, 255, 74);\n"
"color: rgba(0, 0, 0, 240);")
        self.stackedWidget.addWidget(self.page_historial)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.horizontalLayout_3 = QHBoxLayout(self.page_info)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.page_info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(237, 0, 17);")
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(237, 0, 17);")
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_info)
        self.page_perfil = QWidget()
        self.page_perfil.setObjectName(u"page_perfil")
        self.perfil_bt_pg = QPushButton(self.page_perfil)
        self.perfil_bt_pg.setObjectName(u"perfil_bt_pg")
        self.perfil_bt_pg.setGeometry(QRect(290, 220, 561, 26))
        self.perfil_bt_pg.setStyleSheet(u"background-color: rgb(172, 97, 36);")
        self.stackedWidget.addWidget(self.page_perfil)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.admin_bt_pg = QPushButton(self.page_admin)
        self.admin_bt_pg.setObjectName(u"admin_bt_pg")
        self.admin_bt_pg.setGeometry(QRect(280, 210, 571, 26))
        self.admin_bt_pg.setStyleSheet(u"background-color: rgb(69, 255, 74);\n"
"color: rgba(0, 0, 0, 240);")
        self.stackedWidget.addWidget(self.page_admin)

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
        self.inicio_bt.setText(QCoreApplication.translate("MainWindow", u"   Inicio  ", None))
        self.trading_bt.setText(QCoreApplication.translate("MainWindow", u"   Trading", None))
        self.historial_bt.setText(QCoreApplication.translate("MainWindow", u"   Hisorial", None))
        self.info_bt.setText(QCoreApplication.translate("MainWindow", u"   Ayuda  ", None))
        self.perfil_bt.setText(QCoreApplication.translate("MainWindow", u"  Perfil    ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TradingApp", None))
        self.inicio_label.setText("")
        self.trading_bt_pg.setText(QCoreApplication.translate("MainWindow", u"trading", None))
        self.historial_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"## Casa\n"
"### Subt\u00edtulo\n"
"Este es un ejemplo de texto que da entrada a una lista gen\u00e9rica de elementos:\n"
"- Elemento 1\n"
"- Elemento 2\n"
"- Elemento 3\n"
"Este es un ejemplo de texto que da entrada a una lista numerada:\n"
"1. Elemento 1\n"
"2. Elemento 2\n"
"3. Elemento 3\n"
"Al texto en Markdown puedes a\u00f1adirle formato como **negrita** o *cursiva* de una manera muy sencilla.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"## Casa\n"
"### Subt\u00edtulo\n"
"Este es un ejemplo de texto que da entrada a una lista gen\u00e9rica de elementos:\n"
"- Elemento 1\n"
"- Elemento 2\n"
"- Elemento 3\n"
"Este es un ejemplo de texto que da entrada a una lista numerada:\n"
"1. Elemento 1\n"
"2. Elemento 2\n"
"3. Elemento 3\n"
"Al texto en Markdown puedes a\u00f1adirle formato como **negrita** o *cursiva* de una manera muy sencilla.", None))
        self.perfil_bt_pg.setText(QCoreApplication.translate("MainWindow", u"perfil", None))
        self.admin_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
    # retranslateUi

