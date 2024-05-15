from abc import ABC, abstractmethod
from typing import List
from Entity.User import User
from Entity.Product import Product
from Entity.Order import Order
from Util.DBconn import DBConnection
from Exceptions.MyExceptions import UserNotFound , OrderNotFound
from tabulate import tabulate

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: User, products: Product):
        pass

    @abstractmethod
    def cancelOrder(self, userId: int, orderId: int):
        pass

    @abstractmethod
    def createProduct(self, user: User, product: Product):
        pass

    @abstractmethod
    def createUser(self, user: User):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, user: User):
        pass


class OrderProcessor(IOrderManagementRepository,DBConnection):
    def createOrder(self, Order):
        try:
            self.cursor.execute(
                "INSERT INTO Orders (orderId, productId, userId) VALUES (?, ?, ?)",
                (Order.orderId, Order.productId, Order.userId),
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def cancelOrder(self, orderId):
        try:
            self.cursor.execute(
                "SELECT * FROM Orders WHERE orderId = ?", (orderId,)
            )
            order = self.cursor.fetchall()
            if orderId in order:
                self.cursor.execute("DELETE FROM Orders WHERE OrderId = ?", orderId)
                self.conn.commit()
            else:
                raise OrderNotFound(orderId)
        except Exception as e:
            print(e)

    def createProduct(self, Product):
        try:
            self.cursor.execute(
                "INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                (Product.productId, Product.productName, Product.description, Product.price, Product.quantityInStock, Product.type),
            )
            self.conn.commit()  
        except Exception as e:
            print(e)

    def createUser(self, User):
        try:
            self.cursor.execute(
                "INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                (User.userId, User.username, User.password, User.role),
            )
            self.conn.commit()  
        except Exception as e:
            print(e)

    def getAllProducts(self):
        try:
            self.cursor.execute("SELECT * FROM Product")
            products = self.cursor.fetchall()  
            header = [column[0] for column in self.cursor.description]
            print(tabulate(products, headers = header, tablefmt="psql"))
        except Exception as e:
            print(e)

    def getOrderByUser(self, userId):
        try:
            self.cursor.execute(
                "SELECT * FROM Orders WHERE userId = ?", (userId)
            )
            product = self.cursor.fetchall()
            if Order is None:
                raise UserNotFound(userId)
            print(product)
        except Exception as e:
            print(e)
