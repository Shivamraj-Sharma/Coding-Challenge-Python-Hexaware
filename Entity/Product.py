class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    def getProductId(self) -> int:
        return self.productId

    def getProductName(self) -> str:
        return self.productName

    def getDescription(self) -> str:
        return self.description

    def getPrice(self) -> float:
        return self.price

    def getQuantityInStock(self) -> int:
        return self.quantityInStock

    def getType(self) -> str:
        return self.type

    def setProductId(self, productId: int):
        self.productId = productId

    def setProductName(self, productName: str):
        self.productName = productName

    def setDescription(self, description: str):
        self.description = description

    def setPrice(self, price: float):
        self.price = price

    def setQuantityInStock(self, quantityInStock: int):
        self.quantityInStock = quantityInStock

    def setType(self, type: str):
        self.type = type