# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowBQmyda.ui'
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
        self.verticalLayout_4 = QVBoxLayout(self.page_perfil)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget_perfil = QTabWidget(self.page_perfil)
        self.tabWidget_perfil.setObjectName(u"tabWidget_perfil")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_perfil.sizePolicy().hasHeightForWidth())
        self.tabWidget_perfil.setSizePolicy(sizePolicy)
        self.tabWidget_perfil.setMaximumSize(QSize(921, 16777215))
        self.tabWidget_perfil.setStyleSheet(u"color: rgba(0, 0, 0, 240);\n"
"border-radius:10px;")
        self.tabWidget_perfil.setTabPosition(QTabWidget.North)
        self.tabWidget_perfil.setTabShape(QTabWidget.Rounded)
        self.usuario_tab = QWidget()
        self.usuario_tab.setObjectName(u"usuario_tab")
        self.frame = QFrame(self.usuario_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(210, 39, 297, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 13pt \"Arial\";")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.usuarioNuevo_tb = QLineEdit(self.frame)
        self.usuarioNuevo_tb.setObjectName(u"usuarioNuevo_tb")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(180, 180, 180, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(107, 107, 107, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.usuarioNuevo_tb.setPalette(palette1)
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.usuarioNuevo_tb.setFont(font1)
        self.usuarioNuevo_tb.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.usuarioNuevo_tb.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.usuarioNuevo_tb)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 13pt \"Arial\";")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.passwordConfirm_tb = QLineEdit(self.frame)
        self.passwordConfirm_tb.setObjectName(u"passwordConfirm_tb")
        self.passwordConfirm_tb.setMaximumSize(QSize(16777215, 16777200))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.passwordConfirm_tb.setPalette(palette2)
        self.passwordConfirm_tb.setFont(font1)
        self.passwordConfirm_tb.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.passwordConfirm_tb.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.passwordConfirm_tb)

        self.tabWidget_perfil.addTab(self.usuario_tab, "")
        self.password_tab = QWidget()
        self.password_tab.setObjectName(u"password_tab")
        self.frame_2 = QFrame(self.password_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 60, 391, 101))
        self.frame_2.setStyleSheet(u"border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 13pt \"Arial\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.oldPassword_tb = QLineEdit(self.frame_2)
        self.oldPassword_tb.setObjectName(u"oldPassword_tb")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.oldPassword_tb.setPalette(palette3)
        self.oldPassword_tb.setFont(font1)
        self.oldPassword_tb.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.oldPassword_tb.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.oldPassword_tb)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 13pt \"Arial\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.newPassword_tb = QLineEdit(self.frame_2)
        self.newPassword_tb.setObjectName(u"newPassword_tb")
        self.newPassword_tb.setMaximumSize(QSize(16777215, 16777200))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.newPassword_tb.setPalette(palette4)
        self.newPassword_tb.setFont(font1)
        self.newPassword_tb.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPassword_tb.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.newPassword_tb)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgba(64, 64, 64, 254);\n"
"font: 13pt \"Arial\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.newPasswordConfirm_tb = QLineEdit(self.frame_2)
        self.newPasswordConfirm_tb.setObjectName(u"newPasswordConfirm_tb")
        self.newPasswordConfirm_tb.setMaximumSize(QSize(16777215, 16777200))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.newPasswordConfirm_tb.setPalette(palette5)
        self.newPasswordConfirm_tb.setFont(font1)
        self.newPasswordConfirm_tb.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius:10px;\n"
"border:Noe; ")
        self.newPasswordConfirm_tb.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.newPasswordConfirm_tb)

        self.tabWidget_perfil.addTab(self.password_tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget_perfil)

        self.botones_frame = QFrame(self.page_perfil)
        self.botones_frame.setObjectName(u"botones_frame")
        self.botones_frame.setMaximumSize(QSize(921, 61))
        self.botones_frame.setFrameShape(QFrame.StyledPanel)
        self.botones_frame.setFrameShadow(QFrame.Raised)
        self.aceptar_bt_pg = QPushButton(self.botones_frame)
        self.aceptar_bt_pg.setObjectName(u"aceptar_bt_pg")
        self.aceptar_bt_pg.setGeometry(QRect(600, 10, 101, 41))
        palette6 = QPalette()
        brush6 = QBrush(QColor(33, 142, 36, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        self.aceptar_bt_pg.setPalette(palette6)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.aceptar_bt_pg.setFont(font2)
        self.aceptar_bt_pg.setStyleSheet(u"QPushButton{\n"
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
"	background-color: rgb(43, 105, 23);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.cancelar_bt_pg = QPushButton(self.botones_frame)
        self.cancelar_bt_pg.setObjectName(u"cancelar_bt_pg")
        self.cancelar_bt_pg.setGeometry(QRect(710, 10, 101, 41))
        palette7 = QPalette()
        brush7 = QBrush(QColor(200, 1, 17, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.cancelar_bt_pg.setPalette(palette7)
        self.cancelar_bt_pg.setFont(font2)
        self.cancelar_bt_pg.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgb(200, 1, 17);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #ffffff;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"		\n"
"	\n"
"	background-color: rgb(132, 1, 11);\n"
"	font: 75 14pt \"Arial\";\n"
"	border: 2px solid #000000;\n"
"	border-radius:10px;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.botones_frame)

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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nuevo nombre de usuario", None))
        self.usuarioNuevo_tb.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.passwordConfirm_tb.setPlaceholderText("")
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.usuario_tab), QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a antigua", None))
        self.oldPassword_tb.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a nueva", None))
        self.newPassword_tb.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Confirmar contrase\u00f1a ", None))
        self.newPasswordConfirm_tb.setPlaceholderText("")
        self.tabWidget_perfil.setTabText(self.tabWidget_perfil.indexOf(self.password_tab), QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.aceptar_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.cancelar_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.admin_bt_pg.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
    # retranslateUi

