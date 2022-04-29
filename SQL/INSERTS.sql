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

insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (1, 'Faye Cropp'          ,  '2021-09-23',  '667-802-6236');
insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (2, 'Laurene Edworthie'   ,  '2021-03-30',  '711-710-6135');
insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (3, 'Auberta Poulney'     ,  '2021-07-22',  '974-185-0770');
insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (4, 'Ramsay Moiser'       ,  '2021-07-12',  '218-766-9224');
insert into Delivery_Person (DP_ID, Name , DOJ, Contact) values (5, 'Marcelle Flinn'      ,  '2021-05-06',  '149-283-1108');

insert into logindetails values('Faye Cropp', 'pwd', 'dp', 1);
insert into logindetails values('Laurene Edworthie', 'pwd', 'dp', 2);
insert into logindetails values('Auberta Poulney', 'pwd', 'dp', 3);
insert into logindetails values('Ramsay Moiser', 'pwd', 'dp', 4);
insert into logindetails values('Marcelle Flinn', 'pwd', 'dp', 5);

CREATE USER 'Faye Cropp'@'localhost' IDENTIFIED BY 'pwd';
CREATE USER 'Laurene Edworthie'@'localhost' IDENTIFIED BY 'pwd';
CREATE USER 'Auberta Poulney'@'localhost' IDENTIFIED BY 'pwd';
CREATE USER 'Ramsay Moiser'@'localhost' IDENTIFIED BY 'pwd';
CREATE USER 'Marcelle Flinn'@'localhost' IDENTIFIED BY 'pwd';

GRANT SELECT ON delivery_person to 'Faye Cropp'@'localhost';
GRANT SELECT ON delivery_person to 'Laurene Edworthie'@'localhost';
GRANT SELECT ON delivery_person to 'Auberta Poulney'@'localhost';
GRANT SELECT ON delivery_person to 'Ramsay Moiser'@'localhost';
GRANT SELECT ON delivery_person to 'Marcelle Flinn'@'localhost';

use project;
show tables;