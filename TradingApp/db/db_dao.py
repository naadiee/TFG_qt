import mysql.connector
from mysql.connector import Error


class DB_DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                db='TradingApp')
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def registrarUsuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO usuarios (nombre, password) VALUES ('{0}', '{1}')"
                cursor.execute(sql.format(str(usuario[0]), usuario[1]))
                self.conexion.commit()
                print("¡Usuario Registrado!\n")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getUsuario(self, name):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM usuarios where nombre = %s"
                cursor.execute(sql, [name])
                resultado = cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def get_encryptedPassword(self,name):
        password = self.getUsuario(name)
        return password[1]

    def existeUsuario(self, userName):
        usuario_bd = self.getUsuario(userName)

        if usuario_bd is None:
            return False

        return True

    def deleteUser(self,userName):
        if self.existeUsuario(userName):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "DELETE FROM usuarios WHERE nombre= %s "
                    cursor.execute(sql, [userName])
                    self.conexion.commit() # Commit se usa para confirmar lo que estamos ejecutando
                    print("Registro eliminado correctamente")

                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
                finally:
                    if self.conexion.is_connected():
                        self.conexion.close() # Cerramos la conexión







