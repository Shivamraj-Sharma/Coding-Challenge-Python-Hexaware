-- seed data for Product table
INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES
(1, 'Laptop', 'High-performance laptop with SSD storage', 1200.00, 50, 'Electronics'),
(2, 'T-shirt', 'Cotton t-shirt for casual wear', 20.00, 100, 'Clothing'),
(3, 'Smartphone', 'Latest smartphone with OLED display', 800.00, 30, 'Electronics'),
(4, 'Jeans', 'Classic denim jeans', 50.00, 80, 'Clothing'),
(5, 'Headphones', 'Wireless over-ear headphones with noise cancellation', 150.00, 20, 'Electronics'),
(6, 'Dress Shirt', 'Formal shirt for business occasions', 35.00, 60, 'Clothing'),
(7, 'Tablet', '10-inch tablet with touchscreen display', 250.00, 15, 'Electronics');

-- seed data for Electronics table
INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES
(1, 'Dell', 2),
(3, 'Samsung', 1),
(5, 'Sony', 2),
(7, 'Apple', 1);

-- seed data for Clothing table
INSERT INTO Clothing (productId, size, color) VALUES
(2, 'M', 'Blue'),
(4, 'L', 'Black'),
(6, 'L', 'White');

-- seed data for Users table
INSERT INTO Users (userId, username, password, role) VALUES
(1, 'admin', 'admin123', 'admin'),
(2, 'user1', 'password1', 'customer'),
(3, 'user2', 'password2', 'customer'),
(4, 'user3', 'password3', 'customer'),
(5, 'user4', 'password4', 'customer'),
(6, 'user5', 'password5', 'customer');

-- seed data for Orders table
INSERT INTO Orders (orderId, productId, userId) VALUES
(1, 4, 2),
(2, 7, 6);

-- SELECT * FROM Product;
-- SELECT * FROM Electronics;
-- SELECT * FROM Clothing;
-- SELECT * FROM Users;
-- SELECT * FROM Orders;