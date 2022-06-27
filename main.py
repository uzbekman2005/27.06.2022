import pymysql.cursors
from config import *
import pprint

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
            sql = "CREATE TABLE IF NOT EXISTS mygroup(ID int primary key auto_increment, name varchar(100) not null," \
                  "email varchar(255) NOT NULL, password varchar(255) NOT NULL)"
            cursor.execute(sql)
        print("Jadval yaratildi")
    except Exception as ex:
        print(ex)


def insertToTable(connection, name, email, password):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO mygroup (name, email, password) " \
                  "VALUES(%s, %s, %s)"
            cursor.execute(sql, (name, email, password))
        print("Insertion added")
    except Exception as ex:
        print(ex)
    finally:
        connection.commit()

def selectFromTable(connection):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM mygroup"
            cursor.execute(sql)
            res = cursor.fetchall()
            # cursor.fetchone() # bittasinni oladi
        print("selection success")
    except Exception as ex:
        print(ex)
    finally:
        return res


def updateTable(connection, name, email,  password, id):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE mygroup set name=%s, email=%s, password=%s where id = %s"
            cursor.execute(sql, (name,email, password, id))
        print("Update success")
    except Exception as ex:
        print(ex)
    finally:
        connection.commit()

def deleteFromTable(connection, id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM mygroup WHERE ID=%s"
            cursor.execute(sql, (id,))
        print("Delete success")
    except Exception as ex:
        print(ex)
    finally:
        connection.commit()

# def dropTable(connection):
#     try:
#         with connection.cursor() as cursor:
#             sql = "DROP TABLE student"
#             cursor.execute(sql)
#         print("Drop success")
#     except Exception as ex:
#         print(ex)


# def main():
#     dbConnection()
#     while True:
#         print("1. Test1\n"
#               "2. Exit")
#         choice = int(input("> "))
#         if choice == 1:
#             print("test1")
#         elif choice == 2:
#             break


if __name__ == "__main__":
    connection = dbConnection()
    # createTable(connection)
    # insertToTable(connection)
    # updateTable(connection)
    # insertToTable(connection, 'Abbos', 'abbos@gmail.com', 'aksdj14qfq')
    # updateTable(connection, "Babur", "bobur@gmail.com", "rdq4", 9)
    # deleteFromTable(connection, 10)
    # dropTable(connection)
    result = selectFromTable(connection)
    print(result)
    connection.close()