class OrderNotFound(Exception):
    def __init__(self, Order_id):
        super().__init__(f"Order with {Order_id} is not Found")