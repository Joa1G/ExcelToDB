import mysql.connector
from mysql.connector import Error

def conectar():

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="123", database="mydatabase")

        if connection.is_connected():
            print("Conectado ao banco de dados!")
            return connection
        else:
            print("Falha na conexão!")
            return None
    except Error as error:
         print(f"Erro ao conectar com banco mysql: {error}")
         return None

def desconectar(connection):

    if connection  and connection.is_connected():
        connection.close()
        print("Conexão com banco de dados encerrada!")