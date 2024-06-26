from abc import ABC, abstractmethod
from Util.DBconn import DBConnection
from Entity.User import User
from Entity.Product import Product
from Entity.Order import Order
from Exceptions.MyExceptions import UserNotFound , OrderNotFound
from tabulate import tabulate

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, Order):
        pass

    @abstractmethod
    def cancelOrder(self, orderId):
        pass

    @abstractmethod
    def createProduct(self, Product):
        pass

    @abstractmethod
    def createUser(self, User):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, User):
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
            order = self.cursor.fetchall()
            header = [column[0] for column in self.cursor.description]
            if order is None:
                raise UserNotFound(userId)
            print(tabulate(order, headers = header, tablefmt="psql"))
        except Exception as e:
            print(e)
