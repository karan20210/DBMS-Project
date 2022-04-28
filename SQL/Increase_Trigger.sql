delimiter #
create trigger increase_quantity after insert on returns
for each row
begin
	declare i INT;
	set @OID = new.order_id;
    set@rstatus = new.return_status;
    select cart_id into @cid from orders where order_id = @OID;
    select OCustomerID into @UID from orders where order_id = @OID;
    select COUNT(*) into @product_num from cart where cart_id = @cid and CCustomerID=@UID;
    
    set i =0;
    WHILE i < @product_num DO
		select product_id into @pid FROM  cart where cart_id = @CID and CCustomerID=@CustID ORDER BY product_id limit i,1 ;
        select quantity_ordered into @quantity FROM  cart where cart_id = @CID and CCustomerID=@CustID ORDER BY product_id limit 1 offset i ;
        select quantity_available+@quantity into @new_quantity from products where product_id = @pid;
		update products set quantity_available = @new_quantity;
		SET i = i + 1;
    end while;
end#
delimiter ;