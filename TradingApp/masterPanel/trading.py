from db.db_dao import DB_DAO


class Trading():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina Trading
        self.mainWindow.trading_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_trading))