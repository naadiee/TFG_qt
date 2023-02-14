import mysql.connector
from mysql.connector import Error
from werkzeug.security import check_password_hash


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
                cursor.close()
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
                cursor.close()
                return resultado
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def deleteUser(self,userName):
        if self.existeUsuario(userName):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "DELETE FROM usuarios WHERE nombre= %s "
                    cursor.execute(sql, [userName])
                    self.conexion.commit() # Commit se usa para confirmar lo que estamos ejecutando
                    cursor.close()
                    print("Usuario Elimindo")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))


    def cambiarNombre(self, newName, odlName):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE usuarios SET nombre = %s WHERE nombre = %s "
                cursor.execute(sql, [newName, odlName])
                self.conexion.commit()
                cursor.close()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def cambiarPasword(self, newPass, userName):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE usuarios SET password = %s WHERE nombre = %s "
                cursor.execute(sql, [newPass, userName])
                self.conexion.commit()
                cursor.close()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def mostrarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT nombre FROM usuarios"
                cursor.execute(sql)
                resultado = cursor.fetchall()
                cursor.close()
                return resultado
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))



    # SELECT nombre FROM usuarios

    # FUNCIONES AUXILIARES
    def correct_password(self, password, userName):
        same = False
        encrypted = self.get_encryptedPassword(userName)

        if check_password_hash(encrypted,password):
            same = True

        return same

    def get_encryptedPassword(self,name):
        password = self.getUsuario(name)
        return password[1]

    def existeUsuario(self, userName):
        usuario_bd = self.getUsuario(userName)

        if usuario_bd is None:
            return False

        return True




