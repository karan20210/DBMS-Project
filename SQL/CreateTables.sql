CREATE DATABASE PROJECT;
use PROJECT;

CREATE TABLE `USER` (
	`Username` VARCHAR(50) NOT NULL UNIQUE,
    `Password` VARCHAR(20) NOT NULL,
    `Type` VARCHAR(10)
);

CREATE TABLE `CUSTOMER` (
  `Customer_ID` Integer NOT NULL check(Customer_ID>0),
  `Name` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(500) NOT NULL UNIQUE,
  `Contact_No` VARCHAR(15) NOT NULL,
  `Reg_Date` Date not null check(Reg_Date>20210101),
  `Address` VARCHAR(500) NOT NULL,
  `Points` Integer DEFAULT 0 check(Points>0),
  PRIMARY KEY (`Customer_ID`)
);

CREATE TABLE `CATEGORIES` (
  `Category_ID` Integer NOT NULL check(Category_ID>0),
  `Category_Name` VARCHAR(15) NOT NULL UNIQUE,
  PRIMARY KEY (`Category_ID`)
);

CREATE TABLE `SELLER` (
  `Seller_ID` Integer NOT NULL check(Seller_ID>0),
  `Name` VARCHAR(50) NOT NULL,
  `Location` VARCHAR(50) NOT NULL,
  `Contact_No` VARCHAR(15) NOT NULL,
  `Email_Id` VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (`Seller_ID`)
);

CREATE TABLE `PRODUCTS` (
  `Product_ID` Integer check(Product_ID>0),
  `Category_ID` Integer NOT NULL,
  `Name` VARCHAR (50) not null,
  `Price` Float NOT NULL check(Price>0),
  `Quantity_Available` Integer DEFAULT 0,
  `Seller_ID` Integer NOT NULL,
  `Days_to_Arrive` Integer NOT NULL check(Days_to_Arrive>0),
  `Description` VARCHAR(500) NOT NULL,
  `ImageSource` BLOB NOT NULL,
  PRIMARY KEY (`Product_ID`),
  FOREIGN KEY(Category_ID) REFERENCES CATEGORIES(Category_ID), 
FOREIGN KEY(Seller_ID) REFERENCES SELLER(Seller_ID)
);

CREATE TABLE `Reviews` (
    `Review_ID` INTEGER NOT NULL,
    `Text` VARCHAR(500),
    `Stars` INTEGER NOT NULL check(Stars>0 and Stars<=5),
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
  `Cart_ID` Integer check(Cart_ID>0),
  `Customer_ID` Integer NOT NULL,
  `Product_ID` Integer NOT NULL,
  `Quantity_Ordered` Integer DEFAULT 1,
  PRIMARY KEY (`Cart_ID`,`Customer_ID`,`Product_ID`),
FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID), 
FOREIGN KEY(Product_ID) REFERENCES PRODUCTS(Product_ID)
);

CREATE TABLE `Payment` (
  `Payment_ID` Integer NOT NULL check(Payment_ID>0),
  `Customer_ID` Integer NOT NULL,
  `Type` VARCHAR(50) NOT NULL,
  `Status` VARCHAR(15) NOT NULL check(Status='FAILED' or Status='PROCESSING' or Status='SUCCESSFUL'),
  `DatePayment` Date NOT NULL check(DatePayment>20210101),
  `Amount` Float NOT NULL,
  PRIMARY KEY (`Payment_ID`), 
FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID) 
);

CREATE TABLE `Orders` (
  `Order_ID` Integer check(Order_ID>0),
  `Customer_ID` Integer NOT NULL,
  `Date_Of_Delivery` Date NOT NULL check(Date_Of_Delivery>20210101),
  `Payment_ID` Integer NOT NULL,
  `Cart_ID` Integer NOT NULL,
  PRIMARY KEY (`Order_ID`), 
FOREIGN KEY(Customer_ID) REFERENCES Cart(Customer_ID), 
FOREIGN KEY(Payment_ID) REFERENCES Payment(Payment_ID),
FOREIGN KEY(Cart_ID) REFERENCES Cart(Cart_ID)

);

CREATE TABLE `Delivery_Person` (
  `DP_ID` Integer check(DP_ID>0),
  `Name` VARCHAR(100) NOT NULL,
  `DOJ` Date NOT NULL check(DOJ>20210101),
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
  `CC_ID` Integer check(CC_ID>0),
  `Name` VARCHAR(50) not null,
  `Contact_No` VARCHAR(15) not null,
  PRIMARY KEY (`CC_ID`)
);

CREATE TABLE `Customer_Queries` (
  `Query_ID` Integer check(Query_ID>0),
  `Customer_ID` Integer,
  `CC_ID` Integer,
  `LogTime` Timestamp ,
  `Query` VARCHAR(200),
  PRIMARY KEY (`Query_ID`),
FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID),
FOREIGN KEY(CC_ID) REFERENCES Customer_Care(CC_ID)
);

create table` Department`(`Department_ID` int check(Department_ID>0), `Department_Name` varchar(40) not null unique, primary key(department_id));
create table `Manager`(`Manager_ID` int check(manager_id>0), `Manager_Name` varchar(100) not null,`Department_ID` int, foreign key(Department_ID) references Department(Department_ID) ,primary key(Manager_Id));


