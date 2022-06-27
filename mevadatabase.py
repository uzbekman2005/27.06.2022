import pymysql.cursors
from config import *


def dbConnection():
    try:
        connection = pymysql.connect(host=host, user=user, password=password,
                                     database=database, port=3306, charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        print("bazaga ulandi")
        return connection

    except Exception as ex:
        print(ex)


def createTable(connection):
    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE IF NOT EXISTS fruits(ID int primary key auto_increment, name varchar(100) not null," \
                  " price DECIMAL(15, 2) NOT NULL, navi VARCHAR(100) NOT NULL)"
            cursor.execute(sql)
        print("Jadval yaratildi")
    except Exception as ex:
        print(ex)


def insertToTable(connection, name, price, navi):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO fruits(name, price, navi) " \
                  "VALUES(%s, %s, %s)"
            cursor.execute(sql, (name, price, navi))
        print("Insertion added")
    except Exception as ex:
        print(ex)
    finally:
        connection.commit()


def selectFromTable(connection, price1 = 0, price2 = 0):
    try:
        with connection.cursor() as cursor:
            # sql = "SELECT * FROM fruits where price between %s and %s"
            sql = "SELECT * FROM fruits order by length(name) desc"
            cursor.execute(sql)
            res = cursor.fetchall()
            # cursor.fetchone() # bittasinni oladi
        print("selection success")
    except Exception as ex:
        print(ex)
    finally:
        return res


if __name__ == "__main__":
    connection = dbConnection()
    createTable(connection)
    # insertToTable(connection, "Olma", 2000, "skf")
    # insertToTable(connection, "Shaftoli", 1900, "js")
    # insertToTable(connection, "Anor", 3900, "basf")
    # insertToTable(connection, "Anjir", 2300, "as")
    # insertToTable(connection, "Olcha", 1000, "ad")
    # insertToTable(connection, "Gilos", 2200, "asdf")
    res = selectFromTable(connection)
    print(res)