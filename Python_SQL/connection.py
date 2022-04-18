from colorama import Cursor
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

cursor= mydb.cursor()
cursor.execute("use project")
cursor.execute("Select Count(*) from Customer")
result= cursor.fetchall()
no = result[0]
value = no[0]
print(value)
# ,customer_queries,payment,cart

'''
This loop below lets us create views for each customer containing data for a particular user and the access to each view will be given to only that particular user
THis can be extended to sellers and managers and delivery person and customer care people using joins which is I couldn't get working
run the customer insert before trying to fix this query below
'''
for i in range(1,value+1):
  name =(i,)
  query= "create view customer"+str(i)+"View as select * [except OCustomerID,[RCustomerID]]  from Customer INNERJOIN Orders on customer.customer_id=Orders.ocustomerid INNERJOIN reviews on customer.customer_id=reviews.rcustomerid"
  cursor.execute(query)
  mydb.commit()


# for i in range(1,value+1):
#   name =(i,)
#   query= "drop view customer"+str(i)+"View"
#   cursor.execute(query)
#   mydb.commit()


cursor.execute("show tables")
result= cursor.fetchall()
print(result)