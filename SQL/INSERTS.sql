insert into Department(Department_ID,Department_Name) values (10, 'Seller');
insert into Department(Department_ID,Department_Name) values (20, 'Customer');
insert into Department(Department_ID,Department_Name) values (30, 'Delivery');
insert into Department(Department_ID,Department_Name) values (40, 'Product');
insert into Department(Department_ID,Department_Name) values (50, 'Order');
insert into Department(Department_ID,Department_Name) values (60, 'All');

insert into Manager(Manager_ID,Manager_Name,Department_ID) values (1,'Khwaish',10);
insert into Manager(Manager_ID,Manager_Name,Department_ID) values (2,'Karan',20);
insert into Manager(Manager_ID,Manager_Name,Department_ID) values (3,'Gautam',30);
insert into Manager(Manager_ID,Manager_Name,Department_ID) values (4,'Muskan',40);
insert into Manager(Manager_ID,Manager_Name,Department_ID) values (5,'Reddy',50);
insert into Manager(Manager_ID,Manager_Name,Department_ID) values (6,'SuperAdmin',60);

insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (1,  'Karan Baboota', 'karanbaboota@gmail.com', '7291070242', '2021-05-11', 'Amar Colony');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (2,  'Florie Giordano', 'fgiordano1@elegantthemes.com', '637-452-1702', '2021-05-11', '6182 Morningstar Way');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (3,  'Gilly Sumption', 'gsumption2@bbc.co.uk', '545-132-2618', '2022-02-24', '3 Moulton Road');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (4,  'Godfry Peppett', 'gpeppett3@bing.com', '295-885-6109', '2021-08-06', '31 Montana Parkway');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (5,  'Josh Ribbens', 'jribbens4@ftc.gov', '696-534-6271', '2021-10-19', '8307 Columbus Avenue');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (6,  'Roi Carmo', 'rcarmo5@wunderground.com', '464-359-6503', '2021-04-03', '89639 Iowa Road');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (7,  'Red Lutas', 'rlutas6@ihg.com', '138-570-4639', '2022-01-11', '8626 Fairfield Pass');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (8,  'Delcina Bluschke', 'dbluschke7@istockphoto.com', '605-933-8785', '2021-08-22', '2435 Fuller Parkway');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (9,  'Yancy Sweynson', 'ysweynson8@hexun.com', '863-260-8965', '2021-08-01', '32 Karstens Point');
insert into CUSTOMER (Customer_ID, Name, Email, Contact_No, Reg_Date, Address) values (10,  'Alberta Dimic', 'adimic9@macromedia.com', '198-883-7075', '2021-04-16', '6 Forest Place');

insert into CATEGORIES (Category_ID, Category_Name) values (1, 'Laptops');
insert into CATEGORIES (Category_ID, Category_Name) values (2, 'Washing Machine');
insert into CATEGORIES (Category_ID, Category_Name) values (3, 'Cycle');
insert into CATEGORIES (Category_ID, Category_Name) values (4, 'Shirts');
insert into CATEGORIES (Category_ID, Category_Name) values (5, 'Kurtas');
insert into CATEGORIES (Category_ID, Category_Name) values (6, 'Shoes');
insert into CATEGORIES (Category_ID, Category_Name) values (7, 'Trousers');
insert into CATEGORIES (Category_ID, Category_Name) values (8, 'Headphones');
insert into CATEGORIES (Category_ID, Category_Name) values (9, 'Mobiles');
insert into CATEGORIES (Category_ID, Category_Name) values (10, 'Refrigerator');

insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (1,  'Gerhardt Logie'      ,'1136 East Point'         , '439-650-0863', 'glogiea@globo.com'               );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (2,  'Diandra Girogetti'   , '33 Linden Pass'         , '306-219-1941', 'dgirogettib@constantcontact.com' );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (3,  'Concordia Jennings'  ,'4 Mayfield Parkway'      , '500-607-0548', 'cjenningsc@timesonline.co.uk'    );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (4,  'Darice Borthe'       , '131 Vermont Hill'       , '622-483-7736', 'dborthed@sakura.ne.jp'           );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (5,  'Jarrett Brewse'      , '61 Kennedy Center'      , '376-687-9181', 'jbrewsee@eepurl.com'             );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (6,  'Tanya Quartley'      , '29318 Kingsford Hill'   , '816-206-2782', 'tquartleyf@guardian.co.uk'       );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (7,  'Hank Goodright'      , '212 Burning Wood Pass'  , '963-350-6857', 'hgoodrightg@dot.gov'             );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (8,  'Christan Leech'      , '453 Vidon Junction'     , '120-370-7912', 'cleechh@desdev.cn'               );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (9,  'Nadine Janisson'     , '32877 Walton Place'     , '475-486-7497', 'njanissoni@odnoklassniki.ru'     );
insert into Seller (Seller_ID, Name, Location, Contact_No ,Email_ID) values (10,  'Brinn Hurworth'      , '9 Dorton Hill'          , '484-894-0621', 'bhurworthj@seesaa.net'           );

insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (1, 1, 'External Supplier', 6721.89, 37, 1, 3, '','../static/images/Carousel1.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (2, 6, 'Bread - Corn Muffaletta', 6125.82, 65, 2, 8, '','../static/images/Carousel2.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (3, 10, 'Chicken Breast Halal', 6999.88, 93, 5, 10, '','../static/images/Carousel3.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (4, 9, 'Dc Hikiage Hira Huba', 3786.98, 91, 3, 1, '','../static/images/Carousel4.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (5, 2, 'Chef Hat 25cm', 5390.37, 16, 3, 1, '','../static/images/Carousel5.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (6, 7, 'Cheese - Wine', 3568.37, 23, 6, 9, '', '../static/images/Carousel1.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (7, 5, 'Sachet', 5139.11, 22, 9, 3, '','../static/images/Carousel2.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (8, 2, 'Jam - Marmalade, Orange', 7098.2, 85, 7, 3, '','../static/images/Carousel3.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (9, 5, 'Chicken - Whole Fryers', 1320.45, 70, 8, 7, '','../static/images/Carousel4.jpg');
insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (10, 10, 'Wine - Cotes Du Rhone Parallele', 7224.63, 47, 4, 5, '','../static/images/Carousel5.jpg');

insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (1, 'Proin risus.', 3, 3, 1, '2021-03-06 05:56:39');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (2, 'Suspendisse ornare consequat lectus.', 2, 7, 5, '2022-02-16 21:22:01');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (3, 'Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.', 2, 9, 3, '2021-06-10 15:06:04');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (4, 'Nulla ut erat id mauris vulputate elementum.', 3, 1, 8, '2021-05-18 20:39:34');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (5, 'Aliquam non mauris.', 2, 8, 6, '2021-06-01 21:22:06');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (6, 'Etiam pretium iaculis justo.', 3, 7, 7, '2021-09-28 14:43:23');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (7, 'Praesent blandit.', 5, 6, 2, '2021-07-01 14:14:49');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (8, 'Vestibulum rutrum rutrum neque.', 3, 5, 4, '2021-07-10 11:01:29');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (9, 'Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc.', 2, 9, 2, '2021-08-15 00:32:16');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (10, 'Donec quis orci eget orci vehicula condimentum.', 5, 4, 3, '2022-02-09 05:05:35');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (11, 'Maecenas tincidunt lacus at velit.', 3, 5, 9, '2021-10-11 17:33:27');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (12, 'Duis aliquam convallis nunc.', 2, 6, 3, '2021-09-04 13:44:41');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (13, 'Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.', 5, 7, 9, '2021-08-28 22:38:23');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (14, 'Duis consequat dui nec nisi volutpat eleifend.', 4, 1, 3, '2021-08-15 06:17:40');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (15, 'Vivamus in felis eu sapien cursus vestibulum.', 1, 7, 9, '2021-03-07 08:19:17');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (16, 'Curabitur at ipsum ac tellus semper interdum.', 1, 6, 2, '2021-09-27 07:28:13');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (17, 'Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue.', 5, 5, 3, '2021-02-26 08:31:51');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (18, 'Ut tellus.', 4, 8, 7, '2021-10-07 16:39:19');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (19, 'Suspendisse potenti.', 4, 7, 1, '2021-07-29 16:10:01');
insert into REVIEWS (Review_ID, Text, Stars, RCustomerID, Product_ID, TimeStamp) values (20, 'Maecenas tincidunt lacus at velit.', 3, 10, 5, '2021-07-17 08:44:27');

delete from cart where Cart_ID=1 or Cart_ID=2 or Cart_ID=3;
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 1, 1, 1);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 1, 2, 2);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 1, 3, 1);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 2, 2, 3);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 2, 1, 5);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 1, 5, 4);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 3, 1, 3);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 3, 9, 2);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 2, 5, 1);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 2, 7, 2);
insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 1, 6, 2);

-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 1, 6, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 1, 8, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 1, 4, 6);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 1, 1, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 2, 3, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 2, 1, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 2, 9, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 2, 7, 4);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 2, 1, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 2, 6, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 3, 2, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 3, 1, 10);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 3, 9, 9);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 3, 1, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 3, 4, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 3, 8, 4);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 3, 2, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 3, 9, 5);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 3, 5,7);

-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 5, 4, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 5, 1, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 5, 2, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 5, 9, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 5, 12, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 5, 11, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 5, 9, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 5, 16, 6);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 5, 10, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 5, 6, 4);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 6, 12, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 6, 11, 10);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 6, 14, 1);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 6, 20, 4);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 6, 5, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 6, 3, 5);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 6, 13, 4);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 6, 11, 8);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 6, 3,3);

-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 4, 3, 5);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (1, 4, 2, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 4, 8, 8);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 4, 6, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 4, 11, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 4, 17, 2);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (2, 4, 20, 3);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 4, 18, 7);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (3, 4, 19, 4);
-- insert into CART (Cart_ID, CCustomerID, Product_ID, Quantity_Ordered) values (4, 4, 16, 3);

-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (1, 1, 'switch', true, '2021-03-25', 3242.92);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (2, 1, 'mastercard', false, '2022-01-22', 694.71);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (3, 2, 'americanexpress', true, '2021-04-15', 8359.15);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (4, 3, 'china-unionpay', false, '2021-09-07', 1203.05);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (5, 1, 'americanexpress', false, '2021-10-02', 1806.48);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (6, 2, 'jcb', false, '2021-11-03', 4149.28);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (7, 1, 'switch', true, '2021-03-02', 9460.52);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (8, 2, 'mastercard', true, '2021-07-24', 9289.25);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (9, 2, 'mastercard', true, '2021-12-31', 264.63);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (10, 3, 'jcb', true, '2021-12-07', 113.6);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (11, 3, 'jcb', false, '2021-04-25', 8750.58);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (12, 4, 'maestro', false, '2021-12-05', 1063.74);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (13, 4, 'jcb', false, '2021-08-31', 8953.43);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (14, 3, 'jcb', true, '2021-08-30', 8887.43);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (15, 3, 'visa-electron', true, '2021-05-02', 9293.07);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (16, 5, 'china-unionpay', false, '2021-11-09', 6588.15);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (17, 5, 'americanexpress', true, '2021-10-25', 9185.69);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (18, 5, 'china-unionpay', true, '2021-05-31', 7806.99);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (19, 4, 'visa-electron', true, '2021-03-20', 7974.48);
-- insert into PAYMENT (Payment_ID, PCustomerID, Type, Status, DatePayment, Amount) values (20, 4, 'jcb', true, '2021-05-19', 6408.56);

-- delete from orders where Order_id = 1 or Order_id = 2 or Order_id = 3 or Order_id = 4 or Order_id = 5 or Order_id = 6;
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (1, 1, '2022-12-03', 1,1);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (2, 1, '2022-12-03', 2,2);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (3, 2, '2022-12-03', 3,1);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (4, 3, '2022-12-03', 4,1);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (5, 1, '2022-12-03', 5,3);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (6, 2, '2022-12-03', 6,2);

-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (7, 1, '2022-12-03', 7,4);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (8, 2, '2022-12-03', 8,3);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (9, 2, '2022-12-03', 9,4);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (10, 3, '2022-12-03', 10,1);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (11, 3, '2022-12-03', 11,2);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (12, 4, '2022-12-03', 12,3);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (13, 4, '2022-12-03', 13,4);

-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (14, 10, '2022-12-03', 14,3);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (15, 3, '2022-12-03', 15,4);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (16, 5, '2022-12-03', 16,2);
-- insert into orders (Order_ID, OCustomerID, Date_of_Delivery, Payment_ID,Cart_ID) values (17, 5, '2022-12-03', 17,3);

-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (1, 'Faye Cropp'          ,  '2021-09-23',  '667-802-6236');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (2, 'Laurene Edworthie'   ,  '2021-03-30',  '711-710-6135');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (3, 'Auberta Poulney'     ,  '2021-07-22',  '974-185-0770');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (4, 'Ramsay Moiser'       ,  '2021-07-12',  '218-766-9224');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (5, 'Marcelle Flinn'      ,  '2021-05-06',  '149-283-1108');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (6, 'Palmer Paxforde'     ,  '2021-08-19',  '155-843-5360');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (7, 'Sig Bazely'          ,  '2021-10-29',   '509-203-2129');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (8, 'Caleb Bremmell'      ,  '2021-11-20', '139-502-5783');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (9, 'Jody Moger'          ,  '2021-04-02', '643-165-7876');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (10,'Jennine Angrove'     ,  '2022-02-24', '695-532-3524');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (11,'Nedi Wolseley'       ,  '2021-11-26', '809-116-4338');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (12,  'Cynthea Denyukin'  ,  '2021-08-09', '439-758-4348');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (13,  'Robb Pellissier'   ,  '2021-02-05',  '829-481-8516');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (14,  'Valerie Molloy'    ,  '2021-10-13', '588-925-4971');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (15,  'Stanleigh O'' Gara',  '2021-12-09', '197-339-6219');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (16,  'Heriberto Carbin'  ,  '2021-04-17', '659-770-9236');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (17,  'Vite Beckhurst'    ,  '2021-06-14',  '317-705-8539');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (18,  'Zena Matfield'     ,  '2021-02-08', '491-587-5673');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (19,  'Whitaker Kembery'  ,  '2021-11-03', '150-267-2238');
-- insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (20,  'Olenolin Mattholie',  '2021-11-22', '991-922-3723');

-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (1, 1, 'DISPATCHED');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (2, 1, 'Delivered');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (3, 1, 'Picked Up');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (4, 1, 'DISPATCHED');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (5, 2, 'DISPATCHED');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (6, 2, 'Delivered');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (7, 3, 'Picked Up');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (8, 3, 'DISPATCHED');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (6, 4, 'Delivered');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (8, 4, 'DISPATCHED');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (9, 5, 'DISPATCHED');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (10, 6, 'Picked Up');
-- insert into Deliveries (Order_ID, DP_ID , Order_Status) values (11, 7, 'DISPATCHED');

-- insert into Returns (Order_ID, DP_ID , Return_Status) values (12, 8, 'DISPATCHED');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (13, 8, 'Returned');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (14, 9, 'Picked Up');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (15, 10, 'Returned');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (16, 11, 'Returned');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (17, 12, 'Picked Up');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (2, 16, 'DISPATCHED');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (3, 12, 'Picked up');
-- insert into Returns (Order_ID, DP_ID , Return_Status) values (1, 13, 'Returned');

-- insert into Customer_Care (CC_ID, Name, Contact_no) values (1, 'Lucilia Okenfold',  '118-859-6762');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (2, 'Hermina Kinchington',  '822-298-9836');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (3, 'Ragnar Brayfield', '989-622-4535');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (4,  'Cami Brambley', '856-866-9487');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (5,  'Di Goldsby','969-958-5842');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (6,  'Adlai Pinkett','468-350-9111');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (7,  'Letisha Wasbrough', '370-534-3678');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (8,  'Maurene Lavalle', '577-688-1906');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (9,  'Jennifer McKeown', '174-163-7741');
-- insert into Customer_Care (CC_ID, Name, Contact_no) values (10,  'Rosabelle Leethem', '833-895-5747');

-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (1, 3, 5, '2021-09-29 16:27:18', 'cubilia curae duis faucibus accumsan odio curabitur convallis duis consequat dui nec nisi');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (2, 9, 6, '2021-06-21 08:48:41', 'massa tempor convallis nulla neque libero convallis eget eleifend luctus ultricies eu nibh quisque');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (3, 6, 2, '2021-03-29 12:25:21', 'ligula in lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu libero');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (4, 7, 8, '2022-01-18 17:21:31', 'nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (5, 1, 4, '2022-01-18 03:33:06', 'est lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien urna pretium nisl');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (6, 5, 7, '2021-10-05 22:23:50', 'vel enim sit amet nunc viverra dapibus nulla suscipit ligula in');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (7, 8, 10, '2021-09-11 07:39:58', 'nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (8, 4, 3, '2021-08-14 04:18:09', 'mi in porttitor pede justo eu massa donec dapibus duis at velit eu est congue elementum');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (9, 2, 9, '2021-05-23 20:57:50', 'orci mauris lacinia sapien quis libero nullam sit amet turpis elementum ligula vehicula consequat morbi a ipsum integer');
-- insert into Customer_Queries (Query_ID, QCustomerID, CC_ID, LogTime, Query) values (10, 10, 1, '2021-10-03 13:19:39', 'dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit');

-- insert into CC_LoginDetails (Username,Password,CCID) values ('lokenfoldk'     , 'W3mRYcFEjkzK'    ,1);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('hkinchingtonl'  , 'MBwyIZAW'        ,2);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('rbrayfieldm'    , '2PKEtZHxtRM'     ,3);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('cbrambleyn'     , 'lArcAre0r'       ,4);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('dgoldsbyo', 'fcvCyu8Bf'             ,5);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('apinkettp', 'gQjWn6AwlgH'           ,6);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('lwasbroughq', 'NQ9r9Ml'             ,7);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('mlavaller', 'XsoHBsn4Zbm'           ,8);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('jmckeowns', '067at6'                ,9);
-- insert into CC_LoginDetails (Username,Password,CCID) values ('rleethemt', 'k4gJMAm'               ,10);

-- insert into DP_LoginDetails (Username,Password,DPID) values ('fcroppu', '9TKArwtl',1);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('ledworthiev', 'F3mbpy',2);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('apoulneyw', 'SQzGaAEM',3);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('rmoiserx', 'HWhWNkLv0uI',4);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('mflinny', 'X1Ij3o', 5);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('ppaxfordez', '92Ygaha57',6);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('sbazely10', 'NfXqHwBC',7);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('cbremmell11', 'qhbScG38x',8);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('jmoger12', 'bjUKNlxLs',9);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('jangrove13', 'rK7yMH8HUC',10);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('nwolseley14', 'TN2OdIDRDYI',11);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('cdenyukin15', 'aveGi6MArTXK',12);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('rpellissier16', 'BoElS04tU',13);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('vmolloy17', '83pZaks',14);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('so18', 'p151xwJ',15);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('hcarbin19', 'ZaQ938Wf',16);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('vbeckhurst1a', 'Ex9tXmTBGI8M',17);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('zmatfield1b', 'BeFSZYpUN2',18);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('wkembery1c', 'bfuWP8lhB',19);
-- insert into DP_LoginDetails (Username,Password,DPID) values ('omattholie1d', 'NW7hZn1iuD',20);

insert into Manager_LoginDetails (Username,Password,ManagerID) values ('Khwaish11', 'Rupani',1);
insert into Manager_LoginDetails (Username,Password,ManagerID) values ('Karan22', 'Baboota',2);
insert into Manager_LoginDetails (Username,Password,ManagerID) values ('Gautam33', 'Mortala',3);
insert into Manager_LoginDetails (Username,Password,ManagerID) values ('Muskan44', 'Yadav',4);
insert into Manager_LoginDetails (Username,Password,ManagerID) values ('Reddy55', 'GRmortala',5);
insert into Manager_LoginDetails (Username,Password,ManagerID) values ('SuperAdmin66', 'Accesstoall', 6);

insert into Seller_LoginDetails (Username,Password,SellerID) values ('glogiea'     , 'IpResrpK9Uy' ,1);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('dgirogettib' , 'tehJOdYWlc8' ,2);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('cjenningsc'  , 'OzAXmbL3'    ,3);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('dborthed'    , 'UuS3CbRaTb'  ,4);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('jbrewsee'    , 'oAUbY6ET'    ,5);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('tquartleyf'  , 'r9g5Nrtw'    ,6);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('hgoodrightg' , 'atYZqT46Ca'  ,7);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('cleechh'     , 'avrfki3'     ,8);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('njanissoni'  , 'szu2ESGmo'   ,9);
insert into Seller_LoginDetails (Username,Password,SellerID) values ('bhurworthj'  , 'o1rKw5m'     ,10);

insert into Customer_LoginDetails (Username,Password,CustomerID) values ('karanbaboota'    , 'pwd'   ,1);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('fgiordano1' , 'roQVVB8pgj'  ,2);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('gsumption2' , '5AgszrP2D40' ,3);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('gpeppett3'  , 'NHs8Ug6cMi0' ,4);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('jribbens4'  , 'WMfXviF8ZV0k',5);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('rcarmo5'    , 'od5HiW'      ,6);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('rlutas6'    , 'TAgHrY4y7'   ,7);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('dbluschke7', 'YcxhwRZ9'     ,8);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('ysweynson8' , '5TIJFaOe'    ,9);
insert into Customer_LoginDetails (Username,Password,CustomerID) values ('adimic9'    , 'MZTfXOLWU'   ,10);










