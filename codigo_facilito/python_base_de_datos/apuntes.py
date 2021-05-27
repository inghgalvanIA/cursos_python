import pymysql
#libreria de variables de entorno decouple
import os
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) """

users = [
    ("user1","password","user1@gamil.com"),
    ("user2","password","user2@gamil.com"),
    ("user3","password","user3@gamil.com"),
    ("user4","password","user4@gamil.com"),
]

if __name__ =='__main__':
     

    try:

        connect = pymysql.Connect(host='127.0.0.1', 
                                port=3306,
                                user = 'root',
                                passwd = 'Chendo2.1',
                                db = 'pythondb' )

        #cursor = connect.cursor()
        with connect.cursor() as cursor:

            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

            
            query = "INSERT INTO users(username,password,email) VALUES (%s,%s,%s)"
            #un solo insert
            #values = ("Eduardo_gpg","passwoord123","codigo@facilito.com")
            #cursor.execute(query, values)

            #multiples inserts
            # for user in users:
            #     cursor.execute(query,user)

            #otra forma de multi inserts
            cursor.executemany(query,users)
            connect.commit()

            #obtener un registro
            query = "SELECT id, username, email FROM users"
            rows = cursor.execute(query)

            for user in cursor.fetchall():
                print(user)

    except pymysql.err.OperationalError as err:
        print("No fue posible realizar la conexiòn")
        print(err)

    finally:
        #cursor.close()
        connect.close()

        print("Conexiòn finalizada de forma exitosas")