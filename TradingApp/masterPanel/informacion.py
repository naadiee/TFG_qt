from db.db_dao import DB_DAO


class Informacion():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel
        # Pagina Información
        self.mainWindow.info_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_info))
