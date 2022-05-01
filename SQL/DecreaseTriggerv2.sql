delimiter #
create trigger decrease_quantity after insert on orders
for each row
begin
	declare i INT;
	set @OID = new.order_id;
    set@CID = new.cart_id;
	set@CustID = new.OCustomerID;
    select COUNT(*) into @product_num from cart where cart_id = @CID and CCustomerID=@CustID;
    
    set i =0;
    WHILE i < @product_num DO
		select product_id into @pid FROM  cart where cart_id = @CID and CCustomerID=@CustID ORDER BY product_id limit i,1 ;
        select quantity_ordered into @quantity FROM  cart where cart_id = @CID and CCustomerID=@CustID ORDER BY product_id limit 1 offset i ;        
        select quantity_available into @available from products where product_id = @pid;
		update products set quantity_available = quantity_available-@quantity where product_id = @pid;
        select quantity_available into @available_after_order from products where product_id = @pid;
        if(@available_after_order<0) then
			update products set quantity_available = 0 where product_id = @pid;
            update cart set quantity_ordered = @available where product_id = @pid and cart_id = @CID;
		end if;
		SET i = i + 1;
        -- end if;
    end while;
end#
delimiter ;

-- drop trigger decrease_quantity;


