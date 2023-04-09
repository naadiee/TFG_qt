from db.db_dao import DB_DAO


class Trading():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina Trading mostramos la pagina
        self.mainWindow.trading_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_trading))

        # cambiamos dentro de la pagina a la vista de solicitud de datos
        self.mainWindow.ventanas_trading.setCurrentWidget(
            self.mainWindow.page_solicitarDatos)

        self.mainWindow.aceptarDatos_trading_bt.clicked.connect(
            lambda: self.mainWindow.ventanas_trading.setCurrentWidget(
                self.mainWindow.page_resultados))

