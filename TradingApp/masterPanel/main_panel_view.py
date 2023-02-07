# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowUbZZuN.ui'
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
        MainWindow.resize(921, 661)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.munu_bt.setLayoutDirection(Qt.LeftToRight)
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

        self.horizontalLayout_2.addWidget(self.munu_bt, 0, Qt.AlignVCenter)

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
        sizePolicy.setHeightForWidth(self.frame_inferior.sizePolicy().hasHeightForWidth())
        self.frame_inferior.setSizePolicy(sizePolicy)
        self.frame_inferior.setStyleSheet(u"border:Noe")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_izq = QFrame(self.frame_inferior)
        self.frame_izq.setObjectName(u"frame_izq")
        sizePolicy.setHeightForWidth(self.frame_izq.sizePolicy().hasHeightForWidth())
        self.frame_izq.setSizePolicy(sizePolicy)
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
        self.frame_contenedor.setMinimumSize(QSize(921, 621))
        self.frame_contenedor.setMaximumSize(QSize(16777215, 16777215))
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
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.trading_bt_pg.sizePolicy().hasHeightForWidth())
        self.trading_bt_pg.setSizePolicy(sizePolicy)
        self.trading_bt_pg.setStyleSheet(u"background-color: rgb(27, 18, 255);")
        self.stackedWidget.addWidget(self.page_trading)
        self.page_historial = QWidget()
        self.page_historial.setObjectName(u"page_historial")
        self.historial_bt_pg = QPushButton(self.page_historial)
        self.historial_bt_pg.setObjectName(u"historial_bt_pg")
        self.historial_bt_pg.setGeometry(QRect(260, 120, 571, 26))
        sizePolicy.setHeightForWidth(self.historial_bt_pg.sizePolicy().hasHeightForWidth())
        self.historial_bt_pg.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.page_perfil.sizePolicy().hasHeightForWidth())
        self.page_perfil.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.page_perfil)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget_perfil = QTabWidget(self.page_perfil)
        self.tabWidget_perfil.setObjectName(u"tabWidget_perfil")
        sizePolicy.setHeightForWidth(self.tabWidget_perfil.sizePolicy().hasHeightForWidth())
        self.tabWidget_perfil.setSizePolicy(sizePolicy)
        self.tabWidget_perfil.setMinimumSize(QSize(921, 0))
        self.tabWidget_perfil.setMaximumSize(QSize(1677721, 16777215))
        self.tabWidget_perfil.setStyleSheet(u"color: rgba(0, 0, 0, 240);\n"
"border-radius:10px;")
        self.tabWidget_perfil.setTabPosition(QTabWidget.North)
        self.tabWidget_perfil.setTabShape(QTabWidget.Rounded)
        self.usuario_tab = QWidget()
        self.usuario_tab.setObjectName(u"usuario_tab")
        self.aceptarUser_bt_pg = QPushButton(self.usuario_tab)
        self.aceptarUser_bt_pg.setObjectName(u"aceptarUser_bt_pg")
        self.aceptarUser_bt_pg.setGeometry(QRect(450, 370, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarUser_bt_pg.sizePolicy().hasHeightForWidth())
        self.aceptarUser_bt_pg.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(33, 142, 36, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.aceptarUser_bt_pg.setPalette(palette1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.aceptarUser_bt_pg.setFont(font1)
        self.aceptarUser_bt_pg.setLayoutDirection(Qt.LeftToRight)
        self.aceptarUser_bt_pg.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(27, 86, 21);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000\n"
"}\n"
"")
        self.passwordConfirm_tab = QLineEdit(self.usuario_tab)
        self.passwordConfirm_tab.setObjectName(u"passwordConfirm_tab")
        self.passwordConfirm_tab.setGeometry(QRect(490, 150, 231, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush7 = QBrush(QColor(180, 180, 180, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(107, 107, 107, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.passwordConfirm_tab.setPalette(palette2)
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.passwordConfirm_tab.setFont(font2)
        self.passwordConfirm_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.passwordConfirm_tab.setEchoMode(QLineEdit.Password)
        self.passwordConfirm_tab.setAlignment(Qt.AlignCenter)
        self.usuarioNuevo_tab = QLineEdit(self.usuario_tab)
        self.usuarioNuevo_tab.setObjectName(u"usuarioNuevo_tab")
        self.usuarioNuevo_tab.setGeometry(QRect(490, 90, 231, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.usuarioNuevo_tab.sizePolicy().hasHeightForWidth())
        self.usuarioNuevo_tab.setSizePolicy(sizePolicy1)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.usuarioNuevo_tab.setPalette(palette3)
        self.usuarioNuevo_tab.setFont(font2)
        self.usuarioNuevo_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.usuarioNuevo_tab.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.usuario_tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 90, 201, 31))
        self.label_8.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.usuario_tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(270, 150, 181, 31))
        self.label_9.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.tabWidget_perfil.addTab(self.usuario_tab, "")
        self.password_tab = QWidget()
        self.password_tab.setObjectName(u"password_tab")
        self.oldPasword_tab = QLineEdit(self.password_tab)
        self.oldPasword_tab.setObjectName(u"oldPasword_tab")
        self.oldPasword_tab.setGeometry(QRect(490, 90, 231, 31))
        sizePolicy1.setHeightForWidth(self.oldPasword_tab.sizePolicy().hasHeightForWidth())
        self.oldPasword_tab.setSizePolicy(sizePolicy1)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.oldPasword_tab.setPalette(palette4)
        self.oldPasword_tab.setFont(font2)
        self.oldPasword_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.oldPasword_tab.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.password_tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(270, 90, 201, 31))
        self.label_13.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.newPassword_tab = QLineEdit(self.password_tab)
        self.newPassword_tab.setObjectName(u"newPassword_tab")
        self.newPassword_tab.setGeometry(QRect(490, 150, 231, 31))
        sizePolicy1.setHeightForWidth(self.newPassword_tab.sizePolicy().hasHeightForWidth())
        self.newPassword_tab.setSizePolicy(sizePolicy1)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.newPassword_tab.setPalette(palette5)
        self.newPassword_tab.setFont(font2)
        self.newPassword_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPassword_tab.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.password_tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(270, 150, 201, 31))
        self.label_14.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.newPasswordConfirm_tab = QLineEdit(self.password_tab)
        self.newPasswordConfirm_tab.setObjectName(u"newPasswordConfirm_tab")
        self.newPasswordConfirm_tab.setGeometry(QRect(490, 210, 231, 31))
        sizePolicy1.setHeightForWidth(self.newPasswordConfirm_tab.sizePolicy().hasHeightForWidth())
        self.newPasswordConfirm_tab.setSizePolicy(sizePolicy1)
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.newPasswordConfirm_tab.setPalette(palette6)
        self.newPasswordConfirm_tab.setFont(font2)
        self.newPasswordConfirm_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPasswordConfirm_tab.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.password_tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 210, 201, 31))
        self.label_15.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.aceptarUser_bt_pg_2 = QPushButton(self.password_tab)
        self.aceptarUser_bt_pg_2.setObjectName(u"aceptarUser_bt_pg_2")
        self.aceptarUser_bt_pg_2.setGeometry(QRect(450, 370, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarUser_bt_pg_2.sizePolicy().hasHeightForWidth())
        self.aceptarUser_bt_pg_2.setSizePolicy(sizePolicy)
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.aceptarUser_bt_pg_2.setPalette(palette7)
        self.aceptarUser_bt_pg_2.setFont(font1)
        self.aceptarUser_bt_pg_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(27, 86, 21);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000\n"
"}\n"
"")
        self.tabWidget_perfil.addTab(self.password_tab, "")
        self.delete_tab = QWidget()
        self.delete_tab.setObjectName(u"delete_tab")
        self.checkBox = QCheckBox(self.delete_tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(320, 80, 111, 21))
        self.passwordConfirmDelete_tab = QLineEdit(self.delete_tab)
        self.passwordConfirmDelete_tab.setObjectName(u"passwordConfirmDelete_tab")
        self.passwordConfirmDelete_tab.setGeometry(QRect(470, 150, 231, 31))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.passwordConfirmDelete_tab.setPalette(palette8)
        self.passwordConfirmDelete_tab.setFont(font2)
        self.passwordConfirmDelete_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.passwordConfirmDelete_tab.setEchoMode(QLineEdit.Password)
        self.passwordConfirmDelete_tab.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.delete_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(270, 150, 181, 31))
        self.label_10.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.aceptarPassworDelete_bt_pg = QPushButton(self.delete_tab)
        self.aceptarPassworDelete_bt_pg.setObjectName(u"aceptarPassworDelete_bt_pg")
        self.aceptarPassworDelete_bt_pg.setGeometry(QRect(450, 370, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarPassworDelete_bt_pg.sizePolicy().hasHeightForWidth())
        self.aceptarPassworDelete_bt_pg.setSizePolicy(sizePolicy)
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush14 = QBrush(QColor(0, 0, 0, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush15 = QBrush(QColor(0, 0, 0, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.aceptarPassworDelete_bt_pg.setPalette(palette9)
        self.aceptarPassworDelete_bt_pg.setFont(font1)
        self.aceptarPassworDelete_bt_pg.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(27, 86, 21);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000\n"
"}\n"
"")
        self.tabWidget_perfil.addTab(self.delete_tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_perfil)

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

        self.tabWidget_perfil.setCurrentIndex(0)


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
        self.aceptarUser_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.passwordConfirm_tab.setPlaceholderText("")
        self.usuarioNuevo_tab.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nuevo nombre de usuario", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.usuario_tab), QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.oldPasword_tab.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a antigua", None))
        self.newPassword_tab.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a nueva", None))
        self.newPasswordConfirm_tab.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Confirmar contrase\u00f1a ", None))
        self.aceptarUser_bt_pg_2.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.password_tab), QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Eliminar perfil", None))
        self.passwordConfirmDelete_tab.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.aceptarPassworDelete_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.delete_tab), QCoreApplication.translate("MainWindow", u"Eliminar perfil", None))
        self.admin_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
    # retranslateUi

