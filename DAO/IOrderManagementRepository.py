from abc import ABC, abstractmethod
from typing import List
from Entity.User import User
from Entity.Product import Product
from Util.DBconn import DBConnection
from Exceptions.UserExceptions import UserNotFound 
from Exceptions.OrderException import OrderNotFound

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: User, products: List[Product]):
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
    def getAllProducts(self) -> List[Product]:
        pass

    @abstractmethod
    def getOrderByUser(self, user: User) -> List[Product]:
        pass


class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        # Initialize any necessary variables or connections here
        pass

    def createOrder(self, user: User, products: List[Product]):
        # Implement createOrder method here
        pass

    def cancelOrder(self, userId: int, orderId: int):
        # Implement cancelOrder method here
        pass

    def createProduct(self, user: User, product: Product):
        # Implement createProduct method here
        pass

    def createUser(self, user: User):
        # Implement createUser method here
        pass

    def getAllProducts(self) -> List[Product]:
        # Implement getAllProducts method here
        pass

    def getOrderByUser(self, user: User) -> List[Product]:
        # Implement getOrderByUser method here
        pass
