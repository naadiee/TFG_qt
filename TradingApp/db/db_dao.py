import mysql.connector
from mysql.connector import Error
from werkzeug.security import check_password_hash
from datetime import datetime


class DB_DAO:

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

    def deleteUser(self, userName):
        if self.existeUsuario(userName):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "DELETE FROM usuarios WHERE nombre= %s "
                    cursor.execute(sql, [userName])
                    self.conexion.commit()
                    cursor.close()
                    print("Usuario Eliminado")
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

    # FUNCIONES AUXILIARES
    def correct_password(self, password, userName):
        same = False
        encrypted = self.get_encryptedPassword(userName)

        if check_password_hash(encrypted, password):
            same = True

        return same

    def get_encryptedPassword(self, name):
        password = self.getUsuario(name)
        return password[1]

    def existeUsuario(self, userName):
        usuario_bd = self.getUsuario(userName)

        if usuario_bd is None:
            return False

        return True

    def registrarActivo(self, nombre, tiempos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO asset (nombre, 1min, 5min, 15min, 30min, 45min, 60min, daily) VALUES ('{0}', '{1}', '{2}', '{3}','{4}', '{5}', '{6}', '{7}')"
                cursor.execute(sql.format(str(nombre), tiempos[0], tiempos[1], tiempos[2], tiempos[3], tiempos[4], tiempos[5], tiempos[6]))
                self.conexion.commit()
                cursor.close()
                print("¡added asset!\n")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def setSaldo(self, cantidad, userName):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE usuarios SET saldo = '{0}' WHERE nombre = '{1}' "
                cursor.execute(sql.format(cantidad, str(userName)))
                self.conexion.commit()
                cursor.close()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def setExperiencia(self, exp, userName):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE usuarios SET experiencia = '{0}' WHERE nombre = '{1}' "
                cursor.execute(sql.format(exp, str(userName)))
                self.conexion.commit()
                cursor.close()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarOperacion(self, idUsuario, tipoOperacion, activo, precio,cantidad, fechaOperacion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO historial (id_usuario, tipo_operacion, activo, precio,cantidad, fecha_operacion) VALUES (%s, %s, %s, %s ,%s, %s)"
                datos = (idUsuario, tipoOperacion, activo, precio,cantidad, fechaOperacion)
                cursor.execute(sql, datos)
                self.conexion.commit()
                cursor.close()
               # print("¡added operation!\n")
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def getHistorial(self, idUsuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM historial WHERE id_usuario = %s"
                cursor.execute(sql, [idUsuario])
                resultado = cursor.fetchall()
                cursor.close()
                return resultado
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
