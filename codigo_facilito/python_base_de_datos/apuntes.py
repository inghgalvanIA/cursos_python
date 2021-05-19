import pymysql
#libreria de variables de entorno decouple
import os
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    pasword VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) """

if __name__ =='__main__':
     

    try:

        connect = pymysql.Connect(host='127.0.0.1', 
                                port=3306,
                                user = 'usuario',
                                passwd = 'contraseña',
                                db = 'pythondb' )

        #cursor = connect.cursor()
        with connect.cursor() as cursor:

            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

        print("Conexion realizada de manera exitosa ")

    except pymysql.err.OperationalError as err:
        print("No fue posible realizar la conexiòn")
        print(err)

    finally:
        #cursor.close()
        connect.close()

        print("Conexiòn finalizada de forma exitosas")