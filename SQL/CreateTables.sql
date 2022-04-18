CREATE DATABASE PROJECT;
use PROJECT;

CREATE TABLE `USER` (
	`Username` VARCHAR(50) NOT NULL UNIQUE,
    `Password` VARCHAR(20) NOT NULL,
    `Type` VARCHAR(10)
);

CREATE TABLE `CUSTOMER` (
  `Customer_ID` Integer NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(500) NOT NULL UNIQUE,
  `Contact_No` VARCHAR(15) NOT NULL,
  `Reg_Date` Date,
  `Address` VARCHAR(50) NOT NULL,
  `Points` Integer DEFAULT 0,
  PRIMARY KEY (`Customer_ID`)
);

CREATE TABLE `CATEGORIES` (
  `Category_ID` Integer NOT NULL,
  `Category_Name` VARCHAR(15) NOT NULL UNIQUE,
  PRIMARY KEY (`Category_ID`)
);

CREATE TABLE `SELLER` (
  `Seller_ID` Integer NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `Location` VARCHAR(50) NOT NULL,
  `Contact_No` VARCHAR(15) NOT NULL,
  `Email_Id` VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (`Seller_ID`)
);

CREATE TABLE `PRODUCTS` (
  `Product_ID` Integer,
  `Category_ID` Integer NOT NULL,
  `Name` VARCHAR (50),
  `Price` Float NOT NULL,
  `Quantity_Available` Integer DEFAULT 0,
  `Seller_ID` Integer NOT NULL,
  `Days_to_Arrive` Integer NOT NULL,
  `Description` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`Product_ID`),
  FOREIGN KEY(Category_ID) REFERENCES CATEGORIES(Category_ID), 
FOREIGN KEY(Seller_ID) REFERENCES SELLER(Seller_ID)
);

CREATE TABLE `Reviews` (
    `Review_ID` INTEGER NOT NULL,
    `Text` VARCHAR(500),
    `Stars` INTEGER NOT NULL,
    `Customer_ID` INTEGER NOT NULL,
    `Product_ID` INTEGER NOT NULL,
    `TimeStamp` TIMESTAMP NOT NULL,
    PRIMARY KEY (`Review_ID`),
    FOREIGN KEY (Customer_ID)
        REFERENCES CUSTOMER (Customer_ID),
    FOREIGN KEY (Product_ID)
        REFERENCES PRODUCTS (Product_ID)
);

CREATE TABLE `Cart` (
  `Cart_ID` Integer,
  `Customer_ID` Integer NOT NULL,
  `Product_ID` Integer NOT NULL,
  `Quantity_Ordered` Integer DEFAULT 1,
  PRIMARY KEY (`Cart_ID`,`Customer_ID`,`Product_ID`),
FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID), 
FOREIGN KEY(Product_ID) REFERENCES PRODUCTS(Product_ID)
);

CREATE TABLE `Payment` (
  `Payment_ID` Integer NOT NULL,
  `Customer_ID` Integer NOT NULL,
  `Type` VARCHAR(50) NOT NULL,
  `Status` VARCHAR(15) NOT NULL,
  `Date` Date NOT NULL,
  `Amount` Float NOT NULL,
  PRIMARY KEY (`Payment_ID`), 
FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID) 
);

CREATE TABLE `Orders` (
  `Order_ID` Integer,
  `Customer_ID` Integer NOT NULL,
  `Date_Of_Delivery` Date NOT NULL,
  `Payment_ID` Integer NOT NULL,
  `Cart_ID` Integer NOT NULL,
  PRIMARY KEY (`Order_ID`), 
FOREIGN KEY(Customer_ID) REFERENCES Cart(Customer_ID), 
FOREIGN KEY(Payment_ID) REFERENCES Payment(Payment_ID),
FOREIGN KEY(Cart_ID) REFERENCES Cart(Cart_ID)

);

CREATE TABLE `Delivery_Person` (
  `DP_ID` Integer,
  `Name` VARCHAR(100) NOT NULL,
  `DOJ` Date NOT NULL,
  `Contact` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`DP_ID`)
);

CREATE TABLE `Deliveries` (
  `Order_ID` Integer NOT NULL,
  `DP_ID` Integer NOT NULL,
  `Order_Status` VARCHAR(50) NOT NULL,
FOREIGN KEY(Order_ID) REFERENCES ORDERS(ORDER_ID),
FOREIGN KEY(DP_ID) REFERENCES Delivery_Person(DP_ID)
);

CREATE TABLE `Returns` (
  `Order_Id` Integer NOT NULL,
  `DP_ID` Integer NOT NULL,
  `Return_Status` VARCHAR(50) NOT NULL, 
FOREIGN KEY(Order_ID) REFERENCES ORDERS(ORDER_ID),
FOREIGN KEY(DP_ID) REFERENCES Delivery_Person(DP_ID)
);

CREATE TABLE `Customer_Care` (
  `CC_ID` Integer,
  `Name` VARCHAR(50),
  `Contact_No` VARCHAR(15),
  PRIMARY KEY (`CC_ID`)
);

CREATE TABLE `Customer_Queries` (
  `Query_ID` Integer,
  `Customer_ID` Integer,
  `CC_ID` Integer,
  `Time` Timestamp,
  `Query` VARCHAR(200),
  PRIMARY KEY (`Query_ID`),
FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID),
FOREIGN KEY(CC_ID) REFERENCES Customer_Care(CC_ID)
);

