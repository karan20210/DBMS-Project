delimiter #
create trigger decrease_quantity after insert on orders
for each row
begin
	declare i INT;
	set @OID = new.order_id;
    set@CID = new.cart_id;
	set@CustID = new.OCustomerID;
    select COUNT(*) into @product_num from  cart where cart_id = @CID and CCustomerID=@CustID;
    
    set i =0;
    WHILE i < @product_num DO
		select product_id into @pid FROM  cart where cart_id = @CID and CCustomerID=@CustID ORDER BY product_id limit i,1 ;
        select quantity_ordered into @quantity FROM  cart where cart_id = @CID and CCustomerID=@CustID ORDER BY product_id limit 1 offset i ;
		update products set quantity_available = quantity_available-@quantity where product_id = @pid;
		SET i = i + 1;
    end while;
end#
delimiter ;