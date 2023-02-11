# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowHUVVDZ.ui'
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
"font: 14pt \"Arial\";\n"
"border-radius:10px;")
        self.tabWidget_perfil.setTabPosition(QTabWidget.North)
        self.tabWidget_perfil.setTabShape(QTabWidget.Rounded)
        self.usuario_tab = QWidget()
        self.usuario_tab.setObjectName(u"usuario_tab")
        self.aceptarUser_perfil_bt = QPushButton(self.usuario_tab)
        self.aceptarUser_perfil_bt.setObjectName(u"aceptarUser_perfil_bt")
        self.aceptarUser_perfil_bt.setGeometry(QRect(490, 360, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarUser_perfil_bt.sizePolicy().hasHeightForWidth())
        self.aceptarUser_perfil_bt.setSizePolicy(sizePolicy)
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
        self.aceptarUser_perfil_bt.setPalette(palette1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.aceptarUser_perfil_bt.setFont(font1)
        self.aceptarUser_perfil_bt.setLayoutDirection(Qt.LeftToRight)
        self.aceptarUser_perfil_bt.setStyleSheet(u"QPushButton{\n"
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
        self.passwordConfirm_tab.setGeometry(QRect(490, 160, 231, 31))
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
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
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
        self.label_9.setGeometry(QRect(270, 160, 181, 31))
        self.label_9.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.contrasena_incorrecta_usr_tab = QLabel(self.usuario_tab)
        self.contrasena_incorrecta_usr_tab.setObjectName(u"contrasena_incorrecta_usr_tab")
        self.contrasena_incorrecta_usr_tab.setGeometry(QRect(500, 200, 221, 20))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush10 = QBrush(QColor(255, 255, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.contrasena_incorrecta_usr_tab.setPalette(palette4)
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.contrasena_incorrecta_usr_tab.setFont(font3)
        self.contrasena_incorrecta_usr_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta_usr_tab.setAlignment(Qt.AlignCenter)
        self.existe_usuario_tab = QLabel(self.usuario_tab)
        self.existe_usuario_tab.setObjectName(u"existe_usuario_tab")
        self.existe_usuario_tab.setGeometry(QRect(490, 130, 221, 20))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush14 = QBrush(QColor(0, 0, 0, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush15 = QBrush(QColor(0, 0, 0, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush16 = QBrush(QColor(0, 0, 0, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.existe_usuario_tab.setPalette(palette5)
        self.existe_usuario_tab.setFont(font3)
        self.existe_usuario_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.existe_usuario_tab.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.usuario_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 20, 341, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(26)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.tabWidget_perfil.addTab(self.usuario_tab, "")
        self.password_tab = QWidget()
        self.password_tab.setObjectName(u"password_tab")
        self.oldPasword_perfil_tab = QLineEdit(self.password_tab)
        self.oldPasword_perfil_tab.setObjectName(u"oldPasword_perfil_tab")
        self.oldPasword_perfil_tab.setGeometry(QRect(490, 90, 231, 31))
        sizePolicy1.setHeightForWidth(self.oldPasword_perfil_tab.sizePolicy().hasHeightForWidth())
        self.oldPasword_perfil_tab.setSizePolicy(sizePolicy1)
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
        self.oldPasword_perfil_tab.setPalette(palette6)
        self.oldPasword_perfil_tab.setFont(font2)
        self.oldPasword_perfil_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.oldPasword_perfil_tab.setEchoMode(QLineEdit.Password)
        self.oldPasword_perfil_tab.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.password_tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(270, 90, 201, 31))
        self.label_13.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.newPassword_perfil_tab = QLineEdit(self.password_tab)
        self.newPassword_perfil_tab.setObjectName(u"newPassword_perfil_tab")
        self.newPassword_perfil_tab.setGeometry(QRect(490, 160, 231, 31))
        sizePolicy1.setHeightForWidth(self.newPassword_perfil_tab.sizePolicy().hasHeightForWidth())
        self.newPassword_perfil_tab.setSizePolicy(sizePolicy1)
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.newPassword_perfil_tab.setPalette(palette7)
        self.newPassword_perfil_tab.setFont(font2)
        self.newPassword_perfil_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPassword_perfil_tab.setEchoMode(QLineEdit.Password)
        self.newPassword_perfil_tab.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.password_tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(270, 160, 201, 31))
        self.label_14.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.newPasswordConfirm_perfil_tab = QLineEdit(self.password_tab)
        self.newPasswordConfirm_perfil_tab.setObjectName(u"newPasswordConfirm_perfil_tab")
        self.newPasswordConfirm_perfil_tab.setGeometry(QRect(490, 230, 231, 31))
        sizePolicy1.setHeightForWidth(self.newPasswordConfirm_perfil_tab.sizePolicy().hasHeightForWidth())
        self.newPasswordConfirm_perfil_tab.setSizePolicy(sizePolicy1)
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
        self.newPasswordConfirm_perfil_tab.setPalette(palette8)
        self.newPasswordConfirm_perfil_tab.setFont(font2)
        self.newPasswordConfirm_perfil_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPasswordConfirm_perfil_tab.setEchoMode(QLineEdit.Password)
        self.newPasswordConfirm_perfil_tab.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.password_tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 230, 201, 31))
        self.label_15.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 16pt \"Arial\";")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.cambioPass_perfil_bt = QPushButton(self.password_tab)
        self.cambioPass_perfil_bt.setObjectName(u"cambioPass_perfil_bt")
        self.cambioPass_perfil_bt.setGeometry(QRect(490, 370, 101, 41))
        sizePolicy.setHeightForWidth(self.cambioPass_perfil_bt.sizePolicy().hasHeightForWidth())
        self.cambioPass_perfil_bt.setSizePolicy(sizePolicy)
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush17 = QBrush(QColor(0, 0, 0, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush18 = QBrush(QColor(0, 0, 0, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush19 = QBrush(QColor(0, 0, 0, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.cambioPass_perfil_bt.setPalette(palette9)
        self.cambioPass_perfil_bt.setFont(font1)
        self.cambioPass_perfil_bt.setStyleSheet(u"QPushButton{\n"
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
        self.contrasena_incorrecta_pass_tab = QLabel(self.password_tab)
        self.contrasena_incorrecta_pass_tab.setObjectName(u"contrasena_incorrecta_pass_tab")
        self.contrasena_incorrecta_pass_tab.setGeometry(QRect(490, 130, 221, 20))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush20 = QBrush(QColor(0, 0, 0, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush21 = QBrush(QColor(0, 0, 0, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush21)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush22 = QBrush(QColor(0, 0, 0, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.contrasena_incorrecta_pass_tab.setPalette(palette10)
        self.contrasena_incorrecta_pass_tab.setFont(font3)
        self.contrasena_incorrecta_pass_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta_pass_tab.setAlignment(Qt.AlignCenter)
        self.passDiferente_incorrecto_perfil_tab = QLabel(self.password_tab)
        self.passDiferente_incorrecto_perfil_tab.setObjectName(u"passDiferente_incorrecto_perfil_tab")
        self.passDiferente_incorrecto_perfil_tab.setGeometry(QRect(500, 270, 221, 20))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush23 = QBrush(QColor(0, 0, 0, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush24 = QBrush(QColor(0, 0, 0, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush25 = QBrush(QColor(0, 0, 0, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        self.passDiferente_incorrecto_perfil_tab.setPalette(palette11)
        self.passDiferente_incorrecto_perfil_tab.setFont(font3)
        self.passDiferente_incorrecto_perfil_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.passDiferente_incorrecto_perfil_tab.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.password_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 20, 391, 31))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tabWidget_perfil.addTab(self.password_tab, "")
        self.delete_tab = QWidget()
        self.delete_tab.setObjectName(u"delete_tab")
        self.delete_box = QCheckBox(self.delete_tab)
        self.delete_box.setObjectName(u"delete_box")
        self.delete_box.setGeometry(QRect(320, 80, 111, 21))
        self.passwordConfirmDelete_tab = QLineEdit(self.delete_tab)
        self.passwordConfirmDelete_tab.setObjectName(u"passwordConfirmDelete_tab")
        self.passwordConfirmDelete_tab.setGeometry(QRect(470, 150, 231, 31))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.passwordConfirmDelete_tab.setPalette(palette12)
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
        self.aceptarPassworDelete_perfil_bt = QPushButton(self.delete_tab)
        self.aceptarPassworDelete_perfil_bt.setObjectName(u"aceptarPassworDelete_perfil_bt")
        self.aceptarPassworDelete_perfil_bt.setGeometry(QRect(490, 370, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarPassworDelete_perfil_bt.sizePolicy().hasHeightForWidth())
        self.aceptarPassworDelete_perfil_bt.setSizePolicy(sizePolicy)
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush26 = QBrush(QColor(0, 0, 0, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush26)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush27 = QBrush(QColor(0, 0, 0, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush28 = QBrush(QColor(0, 0, 0, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.aceptarPassworDelete_perfil_bt.setPalette(palette13)
        self.aceptarPassworDelete_perfil_bt.setFont(font1)
        self.aceptarPassworDelete_perfil_bt.setStyleSheet(u"QPushButton{\n"
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
        self.contrasena_incorrecta_delete_tab = QLabel(self.delete_tab)
        self.contrasena_incorrecta_delete_tab.setObjectName(u"contrasena_incorrecta_delete_tab")
        self.contrasena_incorrecta_delete_tab.setGeometry(QRect(480, 190, 221, 20))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush29 = QBrush(QColor(0, 0, 0, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush29)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush30 = QBrush(QColor(0, 0, 0, 128))
        brush30.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush30)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush31 = QBrush(QColor(0, 0, 0, 128))
        brush31.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        self.contrasena_incorrecta_delete_tab.setPalette(palette14)
        self.contrasena_incorrecta_delete_tab.setFont(font3)
        self.contrasena_incorrecta_delete_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta_delete_tab.setAlignment(Qt.AlignCenter)
        self.noCheck_delete_tab = QLabel(self.delete_tab)
        self.noCheck_delete_tab.setObjectName(u"noCheck_delete_tab")
        self.noCheck_delete_tab.setGeometry(QRect(450, 80, 221, 20))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush32 = QBrush(QColor(0, 0, 0, 128))
        brush32.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush32)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush33 = QBrush(QColor(0, 0, 0, 128))
        brush33.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush33)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush34 = QBrush(QColor(0, 0, 0, 128))
        brush34.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush34)
#endif
        self.noCheck_delete_tab.setPalette(palette15)
        self.noCheck_delete_tab.setFont(font3)
        self.noCheck_delete_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.noCheck_delete_tab.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.delete_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 20, 341, 31))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.tabWidget_perfil.addTab(self.delete_tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_perfil)

        self.stackedWidget.addWidget(self.page_perfil)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.tabWidget = QTabWidget(self.page_admin)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, 9, 921, 603))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgba(0, 0, 0, 240);\n"
"border-radius:10px;")
        self.add_index_admin_tab = QWidget()
        self.add_index_admin_tab.setObjectName(u"add_index_admin_tab")
        self.comboBox_addIndex_admin = QComboBox(self.add_index_admin_tab)
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.addItem("")
        self.comboBox_addIndex_admin.setObjectName(u"comboBox_addIndex_admin")
        self.comboBox_addIndex_admin.setGeometry(QRect(340, 80, 221, 41))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(17)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.comboBox_addIndex_admin.setFont(font5)
        self.comboBox_addIndex_admin.setStyleSheet(u"selection-background-color: rgb(72, 125, 255);\n"
"font: 17pt \"Arial\";\n"
"color: rgba(0, 0, 0, 240);")
        self.comboBox_addIndex_admin.setEditable(False)
        self.comboBox_addIndex_admin.setInsertPolicy(QComboBox.InsertAtTop)
        self.aceptarAddIndex_admin_bt_tab = QPushButton(self.add_index_admin_tab)
        self.aceptarAddIndex_admin_bt_tab.setObjectName(u"aceptarAddIndex_admin_bt_tab")
        self.aceptarAddIndex_admin_bt_tab.setGeometry(QRect(370, 370, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarAddIndex_admin_bt_tab.sizePolicy().hasHeightForWidth())
        self.aceptarAddIndex_admin_bt_tab.setSizePolicy(sizePolicy)
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush35 = QBrush(QColor(0, 0, 0, 128))
        brush35.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush35)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush36 = QBrush(QColor(0, 0, 0, 128))
        brush36.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush36)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush37 = QBrush(QColor(0, 0, 0, 128))
        brush37.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush37)
#endif
        self.aceptarAddIndex_admin_bt_tab.setPalette(palette16)
        self.aceptarAddIndex_admin_bt_tab.setFont(font1)
        self.aceptarAddIndex_admin_bt_tab.setStyleSheet(u"QPushButton{\n"
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
        self.label_7 = QLabel(self.add_index_admin_tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 20, 341, 31))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.add_index_admin_tab, "")
        self.usr_ajustes_admin_tab = QWidget()
        self.usr_ajustes_admin_tab.setObjectName(u"usr_ajustes_admin_tab")
        self.tableWidget = QTableWidget(self.usr_ajustes_admin_tab)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 30, 351, 231))
        self.aactualizar_admin_bt = QPushButton(self.usr_ajustes_admin_tab)
        self.aactualizar_admin_bt.setObjectName(u"aactualizar_admin_bt")
        self.aactualizar_admin_bt.setGeometry(QRect(510, 40, 101, 41))
        sizePolicy.setHeightForWidth(self.aactualizar_admin_bt.sizePolicy().hasHeightForWidth())
        self.aactualizar_admin_bt.setSizePolicy(sizePolicy)
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush38 = QBrush(QColor(0, 0, 0, 128))
        brush38.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush38)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush39 = QBrush(QColor(0, 0, 0, 128))
        brush39.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush39)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush40 = QBrush(QColor(0, 0, 0, 128))
        brush40.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush40)
#endif
        self.aactualizar_admin_bt.setPalette(palette17)
        self.aactualizar_admin_bt.setFont(font1)
        self.aactualizar_admin_bt.setLayoutDirection(Qt.LeftToRight)
        self.aactualizar_admin_bt.setStyleSheet(u"QPushButton{\n"
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
        self.delete_admin_bt = QPushButton(self.usr_ajustes_admin_tab)
        self.delete_admin_bt.setObjectName(u"delete_admin_bt")
        self.delete_admin_bt.setGeometry(QRect(510, 100, 101, 41))
        sizePolicy.setHeightForWidth(self.delete_admin_bt.sizePolicy().hasHeightForWidth())
        self.delete_admin_bt.setSizePolicy(sizePolicy)
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush41 = QBrush(QColor(212, 0, 15, 255))
        brush41.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush41)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush41)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush41)
        brush42 = QBrush(QColor(0, 0, 0, 128))
        brush42.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush42)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush41)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush41)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush41)
        brush43 = QBrush(QColor(0, 0, 0, 128))
        brush43.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush43)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush41)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush41)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush41)
        brush44 = QBrush(QColor(0, 0, 0, 128))
        brush44.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush44)
#endif
        self.delete_admin_bt.setPalette(palette18)
        self.delete_admin_bt.setFont(font1)
        self.delete_admin_bt.setLayoutDirection(Qt.LeftToRight)
        self.delete_admin_bt.setStyleSheet(u"QPushButton{\n"
"		\n"
"	background-color: rgb(212, 0, 15);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"		\n"
"	background-color: rgb(153, 0, 11);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000\n"
"}\n"
"")
        self.tabWidget.addTab(self.usr_ajustes_admin_tab, "")
        self.stackedWidget.addWidget(self.page_admin)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_perfil.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.comboBox_addIndex_admin.setCurrentIndex(0)


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
        self.aceptarUser_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.passwordConfirm_tab.setPlaceholderText("")
        self.usuarioNuevo_tab.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nuevo nombre de usuario", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.contrasena_incorrecta_usr_tab.setText("")
        self.existe_usuario_tab.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cambiar nombre de usuario", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.usuario_tab), QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.oldPasword_perfil_tab.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a antigua", None))
        self.newPassword_perfil_tab.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a nueva", None))
        self.newPasswordConfirm_perfil_tab.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Confirmar contrase\u00f1a ", None))
        self.cambioPass_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.contrasena_incorrecta_pass_tab.setText("")
        self.passDiferente_incorrecto_perfil_tab.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a de usuario", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.password_tab), QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.delete_box.setText(QCoreApplication.translate("MainWindow", u"Eliminar perfil", None))
        self.passwordConfirmDelete_tab.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.aceptarPassworDelete_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.contrasena_incorrecta_delete_tab.setText("")
        self.noCheck_delete_tab.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Eliminar cuenta ", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.delete_tab), QCoreApplication.translate("MainWindow", u"Eliminar perfil", None))
        self.comboBox_addIndex_admin.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un indice", None))
        self.comboBox_addIndex_admin.setItemText(1, QCoreApplication.translate("MainWindow", u"TSLA (Tesla)", None))
        self.comboBox_addIndex_admin.setItemText(2, QCoreApplication.translate("MainWindow", u"COIN (Coinbase)", None))
        self.comboBox_addIndex_admin.setItemText(3, QCoreApplication.translate("MainWindow", u"NFLX (Netflix)", None))
        self.comboBox_addIndex_admin.setItemText(4, QCoreApplication.translate("MainWindow", u"META (Meta Plataforms)", None))
        self.comboBox_addIndex_admin.setItemText(5, QCoreApplication.translate("MainWindow", u"NIO (Nio Inc)", None))
        self.comboBox_addIndex_admin.setItemText(6, QCoreApplication.translate("MainWindow", u"NVDA (NVDIA Corp)", None))
        self.comboBox_addIndex_admin.setItemText(7, QCoreApplication.translate("MainWindow", u"NKE (Nike)", None))
        self.comboBox_addIndex_admin.setItemText(8, QCoreApplication.translate("MainWindow", u"AMZN (Amazon)", None))
        self.comboBox_addIndex_admin.setItemText(9, QCoreApplication.translate("MainWindow", u"BA (Boeing)", None))

        self.aceptarAddIndex_admin_bt_tab.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir \u00edndice", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_index_admin_tab), QCoreApplication.translate("MainWindow", u"Agregar indice", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.aactualizar_admin_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.delete_admin_bt.setText(QCoreApplication.translate("MainWindow", u"Elimnar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usr_ajustes_admin_tab), QCoreApplication.translate("MainWindow", u"Usuarios", None))
    # retranslateUi

