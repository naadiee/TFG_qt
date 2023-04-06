# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowaSOITY.ui'
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
        MainWindow.resize(925, 661)
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
        self.admin_bt.setEnabled(True)
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
        self.horizontalLayout_7 = QHBoxLayout(self.page_trading)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_4 = QFrame(self.page_trading)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(913, 610))
        self.frame_4.setMaximumSize(QSize(16777191, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.aceptarUser_perfil_bt_2 = QPushButton(self.frame_4)
        self.aceptarUser_perfil_bt_2.setObjectName(u"aceptarUser_perfil_bt_2")
        self.aceptarUser_perfil_bt_2.setGeometry(QRect(390, 230, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarUser_perfil_bt_2.sizePolicy().hasHeightForWidth())
        self.aceptarUser_perfil_bt_2.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush3 = QBrush(QColor(33, 142, 36, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.aceptarUser_perfil_bt_2.setPalette(palette1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.aceptarUser_perfil_bt_2.setFont(font1)
        self.aceptarUser_perfil_bt_2.setLayoutDirection(Qt.LeftToRight)
        self.aceptarUser_perfil_bt_2.setStyleSheet(u"QPushButton{\n"
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
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(210, 329, 311, 141))
        self.frame_5.setStyleSheet(u"background-color: rgb(63, 64, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 60, 81, 26))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.frame_4)

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
        self.label_2.setStyleSheet(u"color: rgba(0, 0, 0, 240);")
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgba(0, 0, 0, 240);")
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
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(False)
        self.tabWidget_perfil.setFont(font2)
        self.tabWidget_perfil.setStyleSheet(u"QTabBar::tab {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"	background: rgba(87, 129, 255, 159);\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 15ex;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"	background-color: rgb(72, 107, 211);\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"	\n"
"	border-color: 1px solid rgb(255, 255, 255);\n"
"\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:select"
                        "ed {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don't want overlapping margins */\n"
"}")
        self.tabWidget_perfil.setTabPosition(QTabWidget.North)
        self.tabWidget_perfil.setTabShape(QTabWidget.Rounded)
        self.usuario_tab = QWidget()
        self.usuario_tab.setObjectName(u"usuario_tab")
        self.horizontalLayout_16 = QHBoxLayout(self.usuario_tab)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 65)
        self.horizontalSpacer_15 = QSpacerItem(207, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.frame = QFrame(self.usuario_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(471, 481))
        self.frame.setMaximumSize(QSize(471, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tituloWidget = QWidget(self.frame)
        self.tituloWidget.setObjectName(u"tituloWidget")
        self.tituloWidget.setMinimumSize(QSize(461, 51))
        self.tituloWidget.setMaximumSize(QSize(461, 51))
        self.label_4 = QLabel(self.tituloWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 10, 341, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(26)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.tituloWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 43, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(461, 51))
        self.widget_2.setMaximumSize(QSize(461, 51))
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 10, 201, 31))
        self.label_8.setMinimumSize(QSize(201, 31))
        self.label_8.setMaximumSize(QSize(201, 31))
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.usuarioNuevo_tab = QLineEdit(self.widget_2)
        self.usuarioNuevo_tab.setObjectName(u"usuarioNuevo_tab")
        self.usuarioNuevo_tab.setGeometry(QRect(220, 10, 231, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.usuarioNuevo_tab.sizePolicy().hasHeightForWidth())
        self.usuarioNuevo_tab.setSizePolicy(sizePolicy1)
        self.usuarioNuevo_tab.setMinimumSize(QSize(231, 31))
        self.usuarioNuevo_tab.setMaximumSize(QSize(231, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush7 = QBrush(QColor(180, 180, 180, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(107, 107, 107, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.usuarioNuevo_tab.setPalette(palette2)
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.usuarioNuevo_tab.setFont(font4)
        self.usuarioNuevo_tab.setFocusPolicy(Qt.ClickFocus)
        self.usuarioNuevo_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.usuarioNuevo_tab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(461, 30))
        self.widget_6.setMaximumSize(QSize(461, 30))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_13 = QSpacerItem(213, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.existe_usuario_tab = QLabel(self.widget_6)
        self.existe_usuario_tab.setObjectName(u"existe_usuario_tab")
        self.existe_usuario_tab.setMinimumSize(QSize(221, 20))
        self.existe_usuario_tab.setMaximumSize(QSize(221, 20))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush10 = QBrush(QColor(255, 255, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.existe_usuario_tab.setPalette(palette3)
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(9)
        self.existe_usuario_tab.setFont(font5)
        self.existe_usuario_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.existe_usuario_tab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.existe_usuario_tab)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(461, 51))
        self.widget_5.setMaximumSize(QSize(461, 51))
        self.passwordConfirm_tab = QLineEdit(self.widget_5)
        self.passwordConfirm_tab.setObjectName(u"passwordConfirm_tab")
        self.passwordConfirm_tab.setGeometry(QRect(220, 10, 231, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.passwordConfirm_tab.setPalette(palette4)
        self.passwordConfirm_tab.setFont(font4)
        self.passwordConfirm_tab.setFocusPolicy(Qt.ClickFocus)
        self.passwordConfirm_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.passwordConfirm_tab.setEchoMode(QLineEdit.Password)
        self.passwordConfirm_tab.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 201, 31))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.frame)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(461, 35))
        self.widget_7.setMaximumSize(QSize(461, 30))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_14 = QSpacerItem(213, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.contrasena_incorrecta_usr_tab = QLabel(self.widget_7)
        self.contrasena_incorrecta_usr_tab.setObjectName(u"contrasena_incorrecta_usr_tab")
        self.contrasena_incorrecta_usr_tab.setMinimumSize(QSize(221, 20))
        self.contrasena_incorrecta_usr_tab.setMaximumSize(QSize(221, 20))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush14 = QBrush(QColor(0, 0, 0, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush15 = QBrush(QColor(0, 0, 0, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush16 = QBrush(QColor(0, 0, 0, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.contrasena_incorrecta_usr_tab.setPalette(palette5)
        self.contrasena_incorrecta_usr_tab.setFont(font5)
        self.contrasena_incorrecta_usr_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta_usr_tab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.contrasena_incorrecta_usr_tab)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.verticalSpacer_6 = QSpacerItem(20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(461, 51))
        self.widget.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, -1, -1, 9)
        self.horizontalSpacer_12 = QSpacerItem(333, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.aceptarUser_perfil_bt = QPushButton(self.widget)
        self.aceptarUser_perfil_bt.setObjectName(u"aceptarUser_perfil_bt")
        sizePolicy.setHeightForWidth(self.aceptarUser_perfil_bt.sizePolicy().hasHeightForWidth())
        self.aceptarUser_perfil_bt.setSizePolicy(sizePolicy)
        self.aceptarUser_perfil_bt.setMinimumSize(QSize(101, 41))
        self.aceptarUser_perfil_bt.setMaximumSize(QSize(101, 41))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush17 = QBrush(QColor(0, 0, 0, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush18 = QBrush(QColor(0, 0, 0, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush19 = QBrush(QColor(0, 0, 0, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.aceptarUser_perfil_bt.setPalette(palette6)
        self.aceptarUser_perfil_bt.setFont(font1)
        self.aceptarUser_perfil_bt.setLayoutDirection(Qt.LeftToRight)
        self.aceptarUser_perfil_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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

        self.horizontalLayout_13.addWidget(self.aceptarUser_perfil_bt)


        self.verticalLayout_5.addWidget(self.widget)


        self.horizontalLayout_16.addWidget(self.frame)

        self.horizontalSpacer_16 = QSpacerItem(207, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)

        self.tabWidget_perfil.addTab(self.usuario_tab, "")
        self.password_tab = QWidget()
        self.password_tab.setObjectName(u"password_tab")
        self.horizontalLayout_21 = QHBoxLayout(self.password_tab)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 65)
        self.horizontalSpacer_22 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_22)

        self.frame_6 = QFrame(self.password_tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(471, 481))
        self.frame_6.setMaximumSize(QSize(471, 481))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_10 = QWidget(self.frame_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(461, 51))
        self.widget_10.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_20 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(380, 31))
        self.label_5.setMaximumSize(QSize(380, 31))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_5)

        self.horizontalSpacer_21 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_21)


        self.verticalLayout_7.addWidget(self.widget_10)

        self.verticalSpacer_5 = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.widget_8 = QWidget(self.frame_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(461, 51))
        self.widget_8.setMaximumSize(QSize(461, 51))
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 10, 201, 31))
        self.label_13.setMinimumSize(QSize(201, 31))
        self.label_13.setMaximumSize(QSize(201, 31))
        self.label_13.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.oldPasword_perfil_tab = QLineEdit(self.widget_8)
        self.oldPasword_perfil_tab.setObjectName(u"oldPasword_perfil_tab")
        self.oldPasword_perfil_tab.setGeometry(QRect(220, 10, 231, 31))
        sizePolicy1.setHeightForWidth(self.oldPasword_perfil_tab.sizePolicy().hasHeightForWidth())
        self.oldPasword_perfil_tab.setSizePolicy(sizePolicy1)
        self.oldPasword_perfil_tab.setMinimumSize(QSize(231, 31))
        self.oldPasword_perfil_tab.setMaximumSize(QSize(231, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.oldPasword_perfil_tab.setPalette(palette7)
        self.oldPasword_perfil_tab.setFont(font4)
        self.oldPasword_perfil_tab.setFocusPolicy(Qt.ClickFocus)
        self.oldPasword_perfil_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.oldPasword_perfil_tab.setEchoMode(QLineEdit.Password)
        self.oldPasword_perfil_tab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.widget_8)

        self.widget_14 = QWidget(self.frame_6)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(461, 30))
        self.widget_14.setMaximumSize(QSize(461, 30))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_18 = QSpacerItem(213, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)

        self.contrasena_incorrecta_pass_tab = QLabel(self.widget_14)
        self.contrasena_incorrecta_pass_tab.setObjectName(u"contrasena_incorrecta_pass_tab")
        self.contrasena_incorrecta_pass_tab.setMinimumSize(QSize(221, 20))
        self.contrasena_incorrecta_pass_tab.setMaximumSize(QSize(221, 20))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush20 = QBrush(QColor(0, 0, 0, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush21 = QBrush(QColor(0, 0, 0, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush21)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush22 = QBrush(QColor(0, 0, 0, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.contrasena_incorrecta_pass_tab.setPalette(palette8)
        self.contrasena_incorrecta_pass_tab.setFont(font5)
        self.contrasena_incorrecta_pass_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta_pass_tab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.contrasena_incorrecta_pass_tab)


        self.verticalLayout_7.addWidget(self.widget_14)

        self.widget_11 = QWidget(self.frame_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(461, 51))
        self.widget_11.setMaximumSize(QSize(461, 51))
        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 10, 201, 31))
        self.label_14.setMinimumSize(QSize(201, 31))
        self.label_14.setMaximumSize(QSize(201, 31))
        self.label_14.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.newPassword_perfil_tab = QLineEdit(self.widget_11)
        self.newPassword_perfil_tab.setObjectName(u"newPassword_perfil_tab")
        self.newPassword_perfil_tab.setGeometry(QRect(220, 10, 231, 31))
        sizePolicy1.setHeightForWidth(self.newPassword_perfil_tab.sizePolicy().hasHeightForWidth())
        self.newPassword_perfil_tab.setSizePolicy(sizePolicy1)
        self.newPassword_perfil_tab.setMinimumSize(QSize(231, 31))
        self.newPassword_perfil_tab.setMaximumSize(QSize(231, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.newPassword_perfil_tab.setPalette(palette9)
        self.newPassword_perfil_tab.setFont(font4)
        self.newPassword_perfil_tab.setFocusPolicy(Qt.ClickFocus)
        self.newPassword_perfil_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPassword_perfil_tab.setEchoMode(QLineEdit.Password)
        self.newPassword_perfil_tab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.widget_11)

        self.widget_4 = QWidget(self.frame_6)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(461, 30))
        self.widget_4.setMaximumSize(QSize(461, 30))

        self.verticalLayout_7.addWidget(self.widget_4)

        self.widget_12 = QWidget(self.frame_6)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(461, 51))
        self.widget_12.setMaximumSize(QSize(461, 51))
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 10, 201, 31))
        self.label_15.setMinimumSize(QSize(201, 31))
        self.label_15.setMaximumSize(QSize(201, 31))
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.newPasswordConfirm_perfil_tab = QLineEdit(self.widget_12)
        self.newPasswordConfirm_perfil_tab.setObjectName(u"newPasswordConfirm_perfil_tab")
        self.newPasswordConfirm_perfil_tab.setGeometry(QRect(220, 10, 231, 31))
        sizePolicy1.setHeightForWidth(self.newPasswordConfirm_perfil_tab.sizePolicy().hasHeightForWidth())
        self.newPasswordConfirm_perfil_tab.setSizePolicy(sizePolicy1)
        self.newPasswordConfirm_perfil_tab.setMinimumSize(QSize(231, 31))
        self.newPasswordConfirm_perfil_tab.setMaximumSize(QSize(231, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.newPasswordConfirm_perfil_tab.setPalette(palette10)
        self.newPasswordConfirm_perfil_tab.setFont(font4)
        self.newPasswordConfirm_perfil_tab.setFocusPolicy(Qt.ClickFocus)
        self.newPasswordConfirm_perfil_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPasswordConfirm_perfil_tab.setEchoMode(QLineEdit.Password)
        self.newPasswordConfirm_perfil_tab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.frame_6)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(461, 35))
        self.widget_13.setMaximumSize(QSize(461, 35))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_17 = QSpacerItem(213, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.passDiferente_incorrecto_perfil_tab = QLabel(self.widget_13)
        self.passDiferente_incorrecto_perfil_tab.setObjectName(u"passDiferente_incorrecto_perfil_tab")
        self.passDiferente_incorrecto_perfil_tab.setMinimumSize(QSize(221, 20))
        self.passDiferente_incorrecto_perfil_tab.setMaximumSize(QSize(221, 20))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush23 = QBrush(QColor(0, 0, 0, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush24 = QBrush(QColor(0, 0, 0, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush25 = QBrush(QColor(0, 0, 0, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        self.passDiferente_incorrecto_perfil_tab.setPalette(palette11)
        self.passDiferente_incorrecto_perfil_tab.setFont(font5)
        self.passDiferente_incorrecto_perfil_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.passDiferente_incorrecto_perfil_tab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.passDiferente_incorrecto_perfil_tab)


        self.verticalLayout_7.addWidget(self.widget_13)

        self.verticalSpacer_7 = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.widget_15 = QWidget(self.frame_6)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(461, 51))
        self.widget_15.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_19 = QSpacerItem(333, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.cambioPass_perfil_bt = QPushButton(self.widget_15)
        self.cambioPass_perfil_bt.setObjectName(u"cambioPass_perfil_bt")
        sizePolicy.setHeightForWidth(self.cambioPass_perfil_bt.sizePolicy().hasHeightForWidth())
        self.cambioPass_perfil_bt.setSizePolicy(sizePolicy)
        self.cambioPass_perfil_bt.setMinimumSize(QSize(101, 41))
        self.cambioPass_perfil_bt.setMaximumSize(QSize(101, 41))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush26 = QBrush(QColor(0, 0, 0, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush26)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush27 = QBrush(QColor(0, 0, 0, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush28 = QBrush(QColor(0, 0, 0, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.cambioPass_perfil_bt.setPalette(palette12)
        self.cambioPass_perfil_bt.setFont(font1)
        self.cambioPass_perfil_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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

        self.horizontalLayout_19.addWidget(self.cambioPass_perfil_bt)


        self.verticalLayout_7.addWidget(self.widget_15)


        self.horizontalLayout_21.addWidget(self.frame_6)

        self.horizontalSpacer_23 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_23)

        self.tabWidget_perfil.addTab(self.password_tab, "")
        self.cuenta_tab = QWidget()
        self.cuenta_tab.setObjectName(u"cuenta_tab")
        self.horizontalLayout_11 = QHBoxLayout(self.cuenta_tab)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 65)
        self.horizontalSpacer_7 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.frame_8 = QFrame(self.cuenta_tab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(471, 481))
        self.frame_8.setMaximumSize(QSize(471, 481))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frameTitilo = QWidget(self.frame_8)
        self.frameTitilo.setObjectName(u"frameTitilo")
        self.frameTitilo.setMinimumSize(QSize(461, 51))
        self.frameTitilo.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_9 = QHBoxLayout(self.frameTitilo)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(121, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(self.frameTitilo)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(154, 33))
        self.label_11.setMaximumSize(QSize(154, 33))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.frameTitilo)

        self.verticalSpacer_2 = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.frame_8)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(461, 51))
        self.frame_3.setMaximumSize(QSize(461, 51))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.comboBox_selecLevel_perfil = QComboBox(self.frame_3)
        self.comboBox_selecLevel_perfil.addItem("")
        self.comboBox_selecLevel_perfil.addItem("")
        self.comboBox_selecLevel_perfil.addItem("")
        self.comboBox_selecLevel_perfil.addItem("")
        self.comboBox_selecLevel_perfil.setObjectName(u"comboBox_selecLevel_perfil")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_selecLevel_perfil.sizePolicy().hasHeightForWidth())
        self.comboBox_selecLevel_perfil.setSizePolicy(sizePolicy2)
        self.comboBox_selecLevel_perfil.setMinimumSize(QSize(159, 25))
        self.comboBox_selecLevel_perfil.setMaximumSize(QSize(176, 25))
        self.comboBox_selecLevel_perfil.setStyleSheet(u"QComboBox{\n"
"selection-background-color: rgb(72, 125, 255);\n"
"font: 15pt \"Arial\";\n"
"color: rgba(0, 0, 0, 240);\n"
"\n"
"border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
" \n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 5px;\n"
"    left: 5px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.comboBox_selecLevel_perfil)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.widget_20 = QWidget(self.frame_8)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(461, 51))
        self.widget_20.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.widget_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(130, 33))
        self.label_12.setMaximumSize(QSize(130, 33))
        self.label_12.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.horizontalSpacer_6 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.spinBox_selectSaldo_perfil = QSpinBox(self.widget_20)
        self.spinBox_selectSaldo_perfil.setObjectName(u"spinBox_selectSaldo_perfil")
        sizePolicy.setHeightForWidth(self.spinBox_selectSaldo_perfil.sizePolicy().hasHeightForWidth())
        self.spinBox_selectSaldo_perfil.setSizePolicy(sizePolicy)
        self.spinBox_selectSaldo_perfil.setMinimumSize(QSize(110, 27))
        self.spinBox_selectSaldo_perfil.setMaximumSize(QSize(110, 27))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush29 = QBrush(QColor(252, 210, 255, 0))
        brush29.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.Highlight, brush29)
        palette13.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        brush30 = QBrush(QColor(107, 176, 255, 0))
        brush30.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.Link, brush30)
        brush31 = QBrush(QColor(245, 84, 255, 0))
        brush31.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.LinkVisited, brush31)
        brush32 = QBrush(QColor(0, 0, 0, 128))
        brush32.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush32)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette13.setBrush(QPalette.Inactive, QPalette.Highlight, brush29)
        palette13.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Link, brush30)
        palette13.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush31)
        brush33 = QBrush(QColor(0, 0, 0, 128))
        brush33.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush33)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush34 = QBrush(QColor(70, 70, 70, 255))
        brush34.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Disabled, QPalette.Highlight, brush34)
        palette13.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Link, brush30)
        palette13.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush31)
        brush35 = QBrush(QColor(0, 0, 0, 128))
        brush35.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush35)
#endif
        self.spinBox_selectSaldo_perfil.setPalette(palette13)
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        font6.setKerning(True)
        self.spinBox_selectSaldo_perfil.setFont(font6)
        self.spinBox_selectSaldo_perfil.setCursor(QCursor(Qt.ArrowCursor))
        self.spinBox_selectSaldo_perfil.setMouseTracking(False)
        self.spinBox_selectSaldo_perfil.setFocusPolicy(Qt.ClickFocus)
        self.spinBox_selectSaldo_perfil.setAcceptDrops(False)
        self.spinBox_selectSaldo_perfil.setAutoFillBackground(False)
        self.spinBox_selectSaldo_perfil.setStyleSheet(u"QSpinBox{\n"
"	font: 16pt \"Arial\";\n"
"	border-radius:1px;\n"
"	border: 1px solid #000000\n"
"}")
        self.spinBox_selectSaldo_perfil.setWrapping(True)
        self.spinBox_selectSaldo_perfil.setFrame(True)
        self.spinBox_selectSaldo_perfil.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spinBox_selectSaldo_perfil.setSpecialValueText(u"")
        self.spinBox_selectSaldo_perfil.setKeyboardTracking(False)
        self.spinBox_selectSaldo_perfil.setProperty("showGroupSeparator", False)
        self.spinBox_selectSaldo_perfil.setPrefix(u"$ ")
        self.spinBox_selectSaldo_perfil.setMaximum(10000)
        self.spinBox_selectSaldo_perfil.setSingleStep(50)
        self.spinBox_selectSaldo_perfil.setValue(0)

        self.horizontalLayout_5.addWidget(self.spinBox_selectSaldo_perfil)


        self.verticalLayout_4.addWidget(self.widget_20)

        self.verticalSpacer_3 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.widget_3 = QWidget(self.frame_8)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(461, 51))
        self.widget_3.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(303, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.aceptarCuenta_perfil_bt = QPushButton(self.widget_3)
        self.aceptarCuenta_perfil_bt.setObjectName(u"aceptarCuenta_perfil_bt")
        sizePolicy.setHeightForWidth(self.aceptarCuenta_perfil_bt.sizePolicy().hasHeightForWidth())
        self.aceptarCuenta_perfil_bt.setSizePolicy(sizePolicy)
        self.aceptarCuenta_perfil_bt.setMinimumSize(QSize(101, 41))
        self.aceptarCuenta_perfil_bt.setMaximumSize(QSize(101, 41))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush36 = QBrush(QColor(0, 0, 0, 128))
        brush36.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush36)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush37 = QBrush(QColor(0, 0, 0, 128))
        brush37.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush37)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush38 = QBrush(QColor(0, 0, 0, 128))
        brush38.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush38)
#endif
        self.aceptarCuenta_perfil_bt.setPalette(palette14)
        self.aceptarCuenta_perfil_bt.setFont(font1)
        self.aceptarCuenta_perfil_bt.setLayoutDirection(Qt.LeftToRight)
        self.aceptarCuenta_perfil_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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

        self.horizontalLayout_10.addWidget(self.aceptarCuenta_perfil_bt)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.horizontalLayout_11.addWidget(self.frame_8)

        self.horizontalSpacer_28 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_28)

        self.tabWidget_perfil.addTab(self.cuenta_tab, "")
        self.delete_tab = QWidget()
        self.delete_tab.setObjectName(u"delete_tab")
        self.horizontalLayout_24 = QHBoxLayout(self.delete_tab)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, -1, -1, 65)
        self.horizontalSpacer_26 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_26)

        self.frame_7 = QFrame(self.delete_tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(471, 481))
        self.frame_7.setMaximumSize(QSize(471, 481))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_16 = QWidget(self.frame_7)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(461, 51))
        self.widget_16.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.label_6 = QLabel(self.widget_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(341, 31))
        self.label_6.setMaximumSize(QSize(341, 31))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_6)

        self.horizontalSpacer_9 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addWidget(self.widget_16)

        self.verticalSpacer_8 = QSpacerItem(20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.widget_17 = QWidget(self.frame_7)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(461, 51))
        self.widget_17.setMaximumSize(QSize(461, 51))
        self.delete_box = QCheckBox(self.widget_17)
        self.delete_box.setObjectName(u"delete_box")
        self.delete_box.setGeometry(QRect(50, 20, 121, 21))
        sizePolicy.setHeightForWidth(self.delete_box.sizePolicy().hasHeightForWidth())
        self.delete_box.setSizePolicy(sizePolicy)
        self.delete_box.setMinimumSize(QSize(121, 21))
        self.delete_box.setMaximumSize(QSize(121, 21))
        self.delete_box.setFocusPolicy(Qt.NoFocus)
        self.delete_box.setStyleSheet(u"QCheckBox{\n"
"	font: 15px \"Arial\";\n"
"	color: rgba(0, 0, 0, 240);\n"
"}\n"
"\n"
"")
        self.noCheck_delete_tab = QLabel(self.widget_17)
        self.noCheck_delete_tab.setObjectName(u"noCheck_delete_tab")
        self.noCheck_delete_tab.setGeometry(QRect(210, 20, 221, 20))
        self.noCheck_delete_tab.setMinimumSize(QSize(221, 20))
        self.noCheck_delete_tab.setMaximumSize(QSize(221, 20))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush39 = QBrush(QColor(0, 0, 0, 128))
        brush39.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush39)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush40 = QBrush(QColor(0, 0, 0, 128))
        brush40.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush40)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush41 = QBrush(QColor(0, 0, 0, 128))
        brush41.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush41)
#endif
        self.noCheck_delete_tab.setPalette(palette15)
        self.noCheck_delete_tab.setFont(font5)
        self.noCheck_delete_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe;\n"
"color: rgba(0, 0, 0, 240);")
        self.noCheck_delete_tab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.widget_17)

        self.widget_9 = QWidget(self.frame_7)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(461, 51))
        self.widget_9.setMaximumSize(QSize(461, 51))
        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 181, 31))
        self.label_10.setMinimumSize(QSize(181, 31))
        self.label_10.setMaximumSize(QSize(181, 31))
        self.label_10.setStyleSheet(u"QLabel{\n"
"	color: rgba(0, 0, 0, 240);\n"
"	font: 15px \"Arial\";\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.passwordConfirmDelete_tab = QLineEdit(self.widget_9)
        self.passwordConfirmDelete_tab.setObjectName(u"passwordConfirmDelete_tab")
        self.passwordConfirmDelete_tab.setGeometry(QRect(220, 10, 231, 31))
        self.passwordConfirmDelete_tab.setMinimumSize(QSize(231, 31))
        self.passwordConfirmDelete_tab.setMaximumSize(QSize(231, 31))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.passwordConfirmDelete_tab.setPalette(palette16)
        self.passwordConfirmDelete_tab.setFont(font4)
        self.passwordConfirmDelete_tab.setFocusPolicy(Qt.ClickFocus)
        self.passwordConfirmDelete_tab.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.passwordConfirmDelete_tab.setEchoMode(QLineEdit.Password)
        self.passwordConfirmDelete_tab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.widget_9)

        self.widget_18 = QWidget(self.frame_7)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(461, 35))
        self.widget_18.setMaximumSize(QSize(461, 35))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_24 = QSpacerItem(213, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_24)

        self.contrasena_incorrecta_delete_tab = QLabel(self.widget_18)
        self.contrasena_incorrecta_delete_tab.setObjectName(u"contrasena_incorrecta_delete_tab")
        self.contrasena_incorrecta_delete_tab.setMinimumSize(QSize(221, 20))
        self.contrasena_incorrecta_delete_tab.setMaximumSize(QSize(221, 20))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush10)
        brush42 = QBrush(QColor(0, 0, 0, 128))
        brush42.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush42)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush43 = QBrush(QColor(0, 0, 0, 128))
        brush43.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush43)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        brush44 = QBrush(QColor(0, 0, 0, 128))
        brush44.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush44)
#endif
        self.contrasena_incorrecta_delete_tab.setPalette(palette17)
        self.contrasena_incorrecta_delete_tab.setFont(font5)
        self.contrasena_incorrecta_delete_tab.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"border:Noe")
        self.contrasena_incorrecta_delete_tab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.contrasena_incorrecta_delete_tab)


        self.verticalLayout_8.addWidget(self.widget_18)

        self.verticalSpacer_9 = QSpacerItem(20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.widget_19 = QWidget(self.frame_7)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(461, 51))
        self.widget_19.setMaximumSize(QSize(461, 51))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_25 = QSpacerItem(333, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_25)

        self.aceptarPassworDelete_perfil_bt = QPushButton(self.widget_19)
        self.aceptarPassworDelete_perfil_bt.setObjectName(u"aceptarPassworDelete_perfil_bt")
        sizePolicy.setHeightForWidth(self.aceptarPassworDelete_perfil_bt.sizePolicy().hasHeightForWidth())
        self.aceptarPassworDelete_perfil_bt.setSizePolicy(sizePolicy)
        self.aceptarPassworDelete_perfil_bt.setMinimumSize(QSize(101, 41))
        self.aceptarPassworDelete_perfil_bt.setMaximumSize(QSize(101, 41))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush45 = QBrush(QColor(0, 0, 0, 128))
        brush45.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush45)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush46 = QBrush(QColor(0, 0, 0, 128))
        brush46.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush46)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush47 = QBrush(QColor(0, 0, 0, 128))
        brush47.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush47)
#endif
        self.aceptarPassworDelete_perfil_bt.setPalette(palette18)
        self.aceptarPassworDelete_perfil_bt.setFont(font1)
        self.aceptarPassworDelete_perfil_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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

        self.horizontalLayout_23.addWidget(self.aceptarPassworDelete_perfil_bt)


        self.verticalLayout_8.addWidget(self.widget_19)


        self.horizontalLayout_24.addWidget(self.frame_7)

        self.horizontalSpacer_27 = QSpacerItem(207, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_27)

        self.tabWidget_perfil.addTab(self.delete_tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_perfil)

        self.stackedWidget.addWidget(self.page_perfil)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.horizontalLayout_8 = QHBoxLayout(self.page_admin)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget = QTabWidget(self.page_admin)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"	background: rgba(87, 129, 255, 159);\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 15ex;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"	background-color: rgb(72, 107, 211);\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"	\n"
"	border-color: 1px solid rgb(255, 255, 255);\n"
"\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:select"
                        "ed {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don't want overlapping margins */\n"
"}")
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
        self.comboBox_addIndex_admin.setGeometry(QRect(370, 80, 200, 30))
        sizePolicy2.setHeightForWidth(self.comboBox_addIndex_admin.sizePolicy().hasHeightForWidth())
        self.comboBox_addIndex_admin.setSizePolicy(sizePolicy2)
        self.comboBox_addIndex_admin.setMinimumSize(QSize(142, 30))
        self.comboBox_addIndex_admin.setMaximumSize(QSize(200, 30))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.comboBox_addIndex_admin.setFont(font7)
        self.comboBox_addIndex_admin.setStyleSheet(u"QComboBox{\n"
"selection-background-color: rgb(72, 125, 255);\n"
"font: 15pt \"Arial\";\n"
"color: rgba(0, 0, 0, 240);\n"
"\n"
"border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 7em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
" \n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 5px;\n"
"    left: 5px;\n"
"}\n"
"\n"
"")
        self.comboBox_addIndex_admin.setEditable(False)
        self.comboBox_addIndex_admin.setInsertPolicy(QComboBox.InsertAtTop)
        self.aceptarAddIndex_admin_bt_tab = QPushButton(self.add_index_admin_tab)
        self.aceptarAddIndex_admin_bt_tab.setObjectName(u"aceptarAddIndex_admin_bt_tab")
        self.aceptarAddIndex_admin_bt_tab.setGeometry(QRect(490, 360, 101, 41))
        sizePolicy.setHeightForWidth(self.aceptarAddIndex_admin_bt_tab.sizePolicy().hasHeightForWidth())
        self.aceptarAddIndex_admin_bt_tab.setSizePolicy(sizePolicy)
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush48 = QBrush(QColor(0, 0, 0, 128))
        brush48.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush48)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush49 = QBrush(QColor(0, 0, 0, 128))
        brush49.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush49)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush50 = QBrush(QColor(0, 0, 0, 128))
        brush50.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush50)
#endif
        self.aceptarAddIndex_admin_bt_tab.setPalette(palette19)
        self.aceptarAddIndex_admin_bt_tab.setFont(font1)
        self.aceptarAddIndex_admin_bt_tab.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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
        self.label_7.setGeometry(QRect(290, 20, 341, 31))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(77, 125, 238);\n"
"font: 75 26pt \"Arial\";\n"
"border:Noe\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.min_frame = QFrame(self.add_index_admin_tab)
        self.min_frame.setObjectName(u"min_frame")
        self.min_frame.setGeometry(QRect(330, 250, 251, 91))
        self.min_frame.setStyleSheet(u"QCheckBox{\n"
"	font: 15px \"Arial\";\n"
"	color: rgba(0, 0, 0, 240);\n"
"}\n"
"")
        self.min_frame.setFrameShape(QFrame.StyledPanel)
        self.min_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.min_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cincoMin_box = QCheckBox(self.min_frame)
        self.cincoMin_box.setObjectName(u"cincoMin_box")

        self.gridLayout.addWidget(self.cincoMin_box, 0, 1, 1, 1)

        self.treintaMin_box = QCheckBox(self.min_frame)
        self.treintaMin_box.setObjectName(u"treintaMin_box")

        self.gridLayout.addWidget(self.treintaMin_box, 1, 0, 1, 1)

        self.unoMin_box = QCheckBox(self.min_frame)
        self.unoMin_box.setObjectName(u"unoMin_box")

        self.gridLayout.addWidget(self.unoMin_box, 0, 0, 1, 1)

        self.cuarentacincoMin_box = QCheckBox(self.min_frame)
        self.cuarentacincoMin_box.setObjectName(u"cuarentacincoMin_box")

        self.gridLayout.addWidget(self.cuarentacincoMin_box, 1, 1, 1, 1)

        self.sesentaMin_box = QCheckBox(self.min_frame)
        self.sesentaMin_box.setObjectName(u"sesentaMin_box")

        self.gridLayout.addWidget(self.sesentaMin_box, 1, 2, 1, 1)

        self.quinceMin_box = QCheckBox(self.min_frame)
        self.quinceMin_box.setObjectName(u"quinceMin_box")

        self.gridLayout.addWidget(self.quinceMin_box, 0, 2, 1, 1)

        self.daily_box = QCheckBox(self.min_frame)
        self.daily_box.setObjectName(u"daily_box")

        self.gridLayout.addWidget(self.daily_box, 2, 0, 1, 1)

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
        self.tableWidget.setStyleSheet(u"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	font: 15px \"Arial\";")
        self.aactualizar_admin_bt = QPushButton(self.usr_ajustes_admin_tab)
        self.aactualizar_admin_bt.setObjectName(u"aactualizar_admin_bt")
        self.aactualizar_admin_bt.setGeometry(QRect(510, 40, 101, 41))
        sizePolicy.setHeightForWidth(self.aactualizar_admin_bt.sizePolicy().hasHeightForWidth())
        self.aactualizar_admin_bt.setSizePolicy(sizePolicy)
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush51 = QBrush(QColor(0, 0, 0, 128))
        brush51.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush51)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush52 = QBrush(QColor(0, 0, 0, 128))
        brush52.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush52)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush53 = QBrush(QColor(0, 0, 0, 128))
        brush53.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush53)
#endif
        self.aactualizar_admin_bt.setPalette(palette20)
        self.aactualizar_admin_bt.setFont(font1)
        self.aactualizar_admin_bt.setLayoutDirection(Qt.LeftToRight)
        self.aactualizar_admin_bt.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(33, 142, 36);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush54 = QBrush(QColor(212, 0, 15, 255))
        brush54.setStyle(Qt.SolidPattern)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush54)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush54)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush54)
        brush55 = QBrush(QColor(0, 0, 0, 128))
        brush55.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush55)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush54)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush54)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush54)
        brush56 = QBrush(QColor(0, 0, 0, 128))
        brush56.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush56)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush54)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush54)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush54)
        brush57 = QBrush(QColor(0, 0, 0, 128))
        brush57.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush57)
#endif
        self.delete_admin_bt.setPalette(palette21)
        self.delete_admin_bt.setFont(font1)
        self.delete_admin_bt.setLayoutDirection(Qt.LeftToRight)
        self.delete_admin_bt.setStyleSheet(u"QPushButton{\n"
"		\n"
"	background-color: rgb(212, 0, 15);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
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

        self.horizontalLayout_8.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_admin)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_perfil.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
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
        self.aceptarUser_perfil_bt_2.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.historial_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"### RSI (Relative Strenght Index): \n"
"Indicador de tipo oscilador que refleja la fuerza relativa de los movimientos alcista en comparaci\u00f3n de los movimientos bajistas. \n"
"Es un indicador que muestra los niveles de sobrecompra y los niveles de sobreventa: \n"
"- Sobrecompra: si est\u00e1 alto hay una alta probabilidad del que precio caida ya que han habido muchas compras. \n"
"- Sobreventa: si est\u00e1 bajo, la probabilidad de que el precio suba es alta. Se ha vendido mucho, cuanto mayor sea este nivel mayor ser\u00e1 la probabilidad de que el precio revote temporalmente. \n"
"\n"
"Niveles clave: \n"
"- Sobrecompra: 70 puntos, empieza la zona de sobrecompra. Cuando mas alto sea m\u00e1s compras estan habiendo. Los que compraron en niveles bajos empezaran a cerrar operaciones haciendo que el impulso se agote llevando a que el precio baje. \n"
"- Sobreventa: 30 punto, empieza la zona de sobreventa. A medida que este numero disminuye la sobreventa aumenta. El precio pronto rebotara y dar\u00e1 un inmpuls"
                        "o al alza temporal, tependideno de mas factores sabremos si es una correcci\u00f3n para seguir caendo. ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"### MACD\n"
"Indicador tecnico que mide la fortaleza del momiviento del precio \n"
"\n"
"### Media Movil \n"
"Hay dos tipos: \n"
"- **Media movil Simple (SMA)**: realiza una media ponderada con los precios de cierre, durante un periodo que nosootros determinamos. SMA 20 coje las ultimas 20 velas y saca la media de precios. \n"
"- **Media movil exponencial (EMA)**: de la mimsa forma que la SMA saca un precio medio pero en este caso da mas importancia a los valores mas cercanos en el tiempo. \n"
"\n"
"### Volumen \n"
"Hace referencia al n\u00famero de contratos negociados en un periodo de tiempo concreto. Cuando el volumen aumenta significa que los traders tienen interes en el movimiento que el precio est\u00e1 llevando a cabo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cambiar nombre de usuario", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nuevo nombre de usuario:", None))
        self.usuarioNuevo_tab.setPlaceholderText("")
        self.existe_usuario_tab.setText("")
        self.passwordConfirm_tab.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a: ", None))
        self.contrasena_incorrecta_usr_tab.setText("")
        self.aceptarUser_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.usuario_tab), QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a de usuario", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a antigua", None))
        self.oldPasword_perfil_tab.setPlaceholderText("")
        self.contrasena_incorrecta_pass_tab.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a nueva", None))
        self.newPassword_perfil_tab.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Confirmar contrase\u00f1a ", None))
        self.newPasswordConfirm_perfil_tab.setPlaceholderText("")
        self.passDiferente_incorrecto_perfil_tab.setText("")
        self.cambioPass_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.password_tab), QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Editar cuenta", None))
        self.comboBox_selecLevel_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar nivel", None))
        self.comboBox_selecLevel_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Novato", None))
        self.comboBox_selecLevel_perfil.setItemText(2, QCoreApplication.translate("MainWindow", u"Intermedio", None))
        self.comboBox_selecLevel_perfil.setItemText(3, QCoreApplication.translate("MainWindow", u"Profesional", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Modificar saldo:", None))
        self.spinBox_selectSaldo_perfil.setSuffix("")
        self.aceptarCuenta_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.cuenta_tab), QCoreApplication.translate("MainWindow", u"Cuenta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Eliminar cuenta ", None))
        self.delete_box.setText(QCoreApplication.translate("MainWindow", u"Eliminar perfil", None))
        self.noCheck_delete_tab.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.passwordConfirmDelete_tab.setPlaceholderText("")
        self.contrasena_incorrecta_delete_tab.setText("")
        self.aceptarPassworDelete_perfil_bt.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.delete_tab), QCoreApplication.translate("MainWindow", u"Eliminar perfil", None))
        self.comboBox_addIndex_admin.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un indice", None))
        self.comboBox_addIndex_admin.setItemText(1, QCoreApplication.translate("MainWindow", u"TSLA", None))
        self.comboBox_addIndex_admin.setItemText(2, QCoreApplication.translate("MainWindow", u"COIN", None))
        self.comboBox_addIndex_admin.setItemText(3, QCoreApplication.translate("MainWindow", u"NFLX", None))
        self.comboBox_addIndex_admin.setItemText(4, QCoreApplication.translate("MainWindow", u"META", None))
        self.comboBox_addIndex_admin.setItemText(5, QCoreApplication.translate("MainWindow", u"NIO", None))
        self.comboBox_addIndex_admin.setItemText(6, QCoreApplication.translate("MainWindow", u"NVDA", None))
        self.comboBox_addIndex_admin.setItemText(7, QCoreApplication.translate("MainWindow", u"NKE", None))
        self.comboBox_addIndex_admin.setItemText(8, QCoreApplication.translate("MainWindow", u"AMZN", None))
        self.comboBox_addIndex_admin.setItemText(9, QCoreApplication.translate("MainWindow", u"BA", None))

        self.aceptarAddIndex_admin_bt_tab.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir \u00edndice", None))
        self.cincoMin_box.setText(QCoreApplication.translate("MainWindow", u"5min", None))
        self.treintaMin_box.setText(QCoreApplication.translate("MainWindow", u"30min", None))
        self.unoMin_box.setText(QCoreApplication.translate("MainWindow", u"1min", None))
        self.cuarentacincoMin_box.setText(QCoreApplication.translate("MainWindow", u"45min", None))
        self.sesentaMin_box.setText(QCoreApplication.translate("MainWindow", u"60min", None))
        self.quinceMin_box.setText(QCoreApplication.translate("MainWindow", u"15min", None))
        self.daily_box.setText(QCoreApplication.translate("MainWindow", u"daily", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_index_admin_tab), QCoreApplication.translate("MainWindow", u"Agregar indice", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.aactualizar_admin_bt.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.delete_admin_bt.setText(QCoreApplication.translate("MainWindow", u"Elimnar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usr_ajustes_admin_tab), QCoreApplication.translate("MainWindow", u"Usuarios", None))
    # retranslateUi

