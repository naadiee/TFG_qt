from db.db_dao import DB_DAO


class Historial():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina Historial
        self.mainWindow.historial_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_historial))