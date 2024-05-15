class UserNotFound(Exception):
    def __init__(self, UserId):
        super().__init__(f"User with {UserId} is not Found")

class ProductNotFound(Exception):
    def __init__(self, productId):
        super().__init__(f"Product with {productId} is not Found")

class OrderNotFound(Exception):
    def __init__(self, OrderId):
        super().__init__(f"Order with {OrderId} is not Found")