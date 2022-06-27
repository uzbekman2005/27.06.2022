from PyQt6.QtWidgets import QMainWindow, QApplication
from config import *
from product import *
import sys
import pymysql.cursors
from config import *






class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_fProduct()
        self.ui.setupUi(self)
        self.dbConnection()
        self.createTable()
        self.loadDataToTable()
        self.ui.bAddProduct.clicked.connect(self.addProduct)
        self.ui.btnSearch.clicked.connect(self.searchProduct)
        # self.ui.btnAll.clicked.connect(self.allProducts)
        # self.ui.btnDel.clicked.connect(self.delProduct)
        # self.ui.leSearch.textChanged.connect(self.searchProduct)




    def dbConnection(self):
        try:
            self.connection = pymysql.connect(host=host, user=user, password=password,
                                         database=database, port=3306, charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            print("bazaga ulandi")
        except Exception as ex:
            print(ex)

    def createTable(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "CREATE TABLE IF NOT EXISTS products(ID int primary key auto_increment, name varchar(100) not null," \
                      " price DECIMAL(15, 2) NOT NULL, amount INT NOT NULL)"
                cursor.execute(sql)
            print("Jadval yaratildi")
        except Exception as ex:
            print(ex)

    # def allProducts(self):
    #     self.loadDataToTable()
    #     self.ui.leSearch.setText("")
    #
    # def delProduct(self):
    #     txtDelete = self.ui.leDelete.text()
    #
    #     if txtDelete != "":
    #
    #         for prod in products:
    #             if prod["product"] == txtDelete:
    #                 products.remove(prod)
    #         self.loadDataToTable()
    #         self.ui.leDelete.setText("")
    #
    def addProduct(self):
        try:
            textproduct = self.ui.leProduct.text()
            textprice = self.ui.lePrice.text()
            textamount= self.ui.leAmount.text()
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO products(name, price, amount) " \
                      "VALUES(%s, %s, %s)"
                cursor.execute(sql, (textproduct, textprice, textamount))
            print("Insertion added")
        except Exception as ex:
            print(ex)
        finally:
            self.connection.commit()
            self.loadDataToTable()
            self.ui.leProduct.setText("")
            self.ui.lePrice.setText("")
            self.ui.leAmount.setText("")

    def searchProduct(self):
        try:
            if self.ui.rbProduct.isChecked():
                maydon = "name"
            elif self.ui.rbPrice.isChecked():
                maydon = "price"
            else:
                maydon = "amount"
            txtSearch = self.ui.leSearch.text()
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM products where {maydon} = %s"
                cursor.execute(sql, (txtSearch,))
                products = cursor.fetchall()
                # cursor.fetchone() # bittasinni oladi
            print(products)
            row = 0
            self.ui.tProducts.setRowCount(len(products))
            for prod in products:
                self.ui.tProducts.setItem(row, 0, QtWidgets.QTableWidgetItem(prod["name"]))
                self.ui.tProducts.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod["price"])))
                self.ui.tProducts.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod["amount"])))
                row += 1
            print("selection success")

        except Exception as ex:
            print(ex)



    def loadDataToTable(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM products"
                cursor.execute(sql)
                products = cursor.fetchall()
                # cursor.fetchone() # bittasinni oladi

            row = 0
            self.ui.tProducts.setRowCount(len(products))
            for prod in products:
                self.ui.tProducts.setItem(row, 0, QtWidgets.QTableWidgetItem(prod["name"]))
                self.ui.tProducts.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod["price"])))
                self.ui.tProducts.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod["amount"])))
                row += 1
            print("selection success")
        except Exception as ex:
            print(ex)

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

