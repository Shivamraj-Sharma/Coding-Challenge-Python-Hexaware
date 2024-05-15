
from Entity.Order import Order
from Entity.Product import Product
from Entity.User import User
from DAO.IOrderManagementRepository import OrderProcessor

class MainMenu:
    order_processor = OrderProcessor()

    def order_menu(self):
        while True:
            print(
                """      
            1. Create Order
            2. Cancel Order
            3. Get Order By User  
            4. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                orderId = input("Please enter Order Id: ")
                productId = int(input("Please enter Product Id: "))
                userId = int(input("Please enter movie User Id: "))
                new_order = Order(orderId, productId, userId)
                self.order_processor.createOrder(new_order)
            elif choice == 2:
                orderId = input("Please enter Order Id: ")
                cancel_order = Order(orderId)
                self.order_processor.cancelOrder(cancel_order)
            if choice == 3:
                userId = input("Please enter User Id: ")
                get_order_by_user = Order(userId)
                self.order_processor.getOrderByUser(get_order_by_user)
            elif choice == 4:
                break

    def product_menu(self):
        while True:
            print(
                """      
            1. Add a Product
            2. View all Products
            3. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                productId = input("Please enter Product Id: ")
                productName = input("Please enter Product Name: ")
                description = input("Please enter Product Description: ")
                price = input("Please enter Product Price: ")
                quantityInStock = input("Please enter Quantity in Stock: ")
                type = input("Please enter Product type: ")
                new_product = Product(productId, productName, description, price, quantityInStock, type)
                self.order_processor.createProduct(new_product)
            elif choice == 2:
                self.order_processor.getAllProducts()
            elif choice == 3:
                break

    def user_menu(self):
        while True:
            print(
                """      
            1. Add a User
            2. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                userId = input("Please enter User Id: ")
                username = input("Please enter username: ")
                password = input("Please enter Password: ")
                role = input("Please enter User Role: ")
                new_user = User(userId, username, password, role)
                self.order_processor.createUser(new_user)
            elif choice == 2:
                break


def main():
    main_menu = MainMenu()

    while True:
        print(
            """      
            1. Order Management
            2. Product Management
            3. User Management
            4. Exit
                """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            main_menu.order_menu()
        elif choice == 2:
            main_menu.product_menu()
        elif choice == 3:
            main_menu.user_menu()
        elif choice == 4:
            main_menu.order_processor.close()
            break


if __name__ == "__main__":
    print("Welcome to the E-Order App")
    main()