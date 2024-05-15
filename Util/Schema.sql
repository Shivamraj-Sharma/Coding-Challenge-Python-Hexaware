CREATE DATABASE OrderManagementSystem;
USE OrderManagementSystem;

-- Creating a product table
CREATE TABLE Product (
    productId INT PRIMARY KEY,
    productName VARCHAR(255),
    description VARCHAR(255),
    price FLOAT, 
    quantityInStock INT,
    type VARCHAR(50)
);

-- creating a electronics table ( sub-table of product)
CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(255),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- creating a clothing table ( sub-table of product)
CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(50),
    color VARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- creating a user table
CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(50)
);

-- creating a orders table
CREATE TABLE Orders (
	orderId INT PRIMARY KEY,
	productId INT,
	UserId INT,
	FOREIGN KEY (productId) REFERENCES Product(productId),
	FOREIGN KEY (userId) REFERENCES Users(userId)
);