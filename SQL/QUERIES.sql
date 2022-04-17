use PROJECT;
select name from products p where p.product_id in (select product_id from cart c, orders o where o.cart_id= c.cart_id AND c.user_id = 1);

select order_status from deliveries d where d.order_id in (select o.order_id from orders o where o.user_id = 1);

select p.product_id, p.Name, p.Price from products p
order by p.price;

select DP.Name, DP.Contact from DELIVERY_PERSON DP where DP.DP_ID in(select DP_ID from deliveries d where d.order_id in (select o.order_id from orders o where o.user_id = 1) AND d.order_id = 7);

Select * from reviews where product_id =13 and stars>=4;

select location from seller where seller_id in(
select seller_id from products where product_id = 1);

select c.product_id, sum(c.quantity_ordered), p.price, sum(c.quantity_ordered) * p.price as revenue from cart c, products p where c.cart_id in 
(select cart_id from orders)
and p.product_id = c.product_id
group by c.product_id;

select cc.name, cc.Contact_no from CUSTOMER_CARE cc where cc.CC_ID in
(select CC_ID from CUSTOMER_QUERIES cq where cq.user_id = 13);

(select ca.Category_Name, p.category_id, count(p.category_id) as no_of_products from products p, categories ca where p.product_id in 
(select product_id from cart c, orders o where o.cart_id= c.cart_id AND c.user_id = 1)
and ca.category_id = p.category_id
group by category_id
order by no_of_products desc);

select d.dp_id, dp.name, count(d.dp_id) as No_of_deliveries_made from deliveries d, delivery_person dp where d.dp_id = dp.dp_id group by d.dp_id;











