from db.db_dao import DB_DAO


class Usuario():

    def __init__(self, id):
        self.dao = DB_DAO()
        self.user_id = id

    def getUserId(self):
        return self.dao.getUsuario(self.user_id)


