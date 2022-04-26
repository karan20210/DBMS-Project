delimiter #
create trigger add_to_Deliveries after insert on orders
for each row
begin 
	set @OID = new.order_id;
	set @DateOrder = new.date_of_order;
    select DP_ID into @dpid from Delivery_person order by rand() limit 1;
    set @DDate = date_add(@DateOrder,Interval 5 day);
	insert into deliveries(Order_ID,DP_ID,Order_Status,DateofDelivery) values(@OID,@dpid,'On the way',@DDate);
end#
delimiter ;
