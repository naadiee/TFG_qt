from db.db_dao import DB_DAO

class Admin():

    def __init__(self, panel):
        self.dao = DB_DAO()
        self.mainWindow = panel

        # Pagina Admin
        self.mainWindow.admin_bt.clicked.connect(
            lambda: self.mainWindow.stackedWidget.setCurrentWidget(
                self.mainWindow.page_admin))
