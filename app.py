# from crypt import methods
from datetime import date, datetime
import random
from unicodedata import category
from django.shortcuts import render
from flask import Flask, redirect, render_template, request, flash
from flask_mysqldb import MySQL
# from pymysql import NULL
import yaml
import os
import MySQLdb

app = Flask(__name__)

UPLOAD_FOLDER = 'static/products'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = 'karanb1809'
app.config['MYSQL_DB'] = 'PROJECT'

host = 'localhost'
mysql = MySQL(app)

d = ()

@app.route("/")
def intro():
    return render_template("intro.html"), {"Refresh": "5; url=/login"}

@app.route("/search/<user_id>", methods = ['GET', 'POST'])
def search(user_id):
    d = getDetails(user_id)
    name = request.form['name']
    print(name)
    cur = mysql.connection.cursor()
    s = "select * from products where name = '" + str(name) + "'"
    cur.execute(s)
    products = cur.fetchall()
    category = []
    category.append([1, name])
    return render_template("category.html", details = d, products = products, category = category)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        return request.form
    return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])  
def signup():  
    return render_template("signup.html")

@app.route("/customerlogin", methods = ['POST'])
def customerlogin():
    # Getting data from form request
    username = request.form['username']
    pwd = request.form['password']

    # Checking whether it exists in the DB or not
    cur = mysql.connection.cursor()
    cur.execute("select username,password,ID from logindetails where type = 'customer'")
    
    records = cur.fetchall()
    print(records)

    for i in records:
        if username == i[0] and pwd == i[1]:
            l = "/homepage/" + str(i[2])
            return redirect(l)
    mysql.connection.commit()
    cur.close()

    flash("Incorrect Username Or Password")
    return render_template('login.html')

@app.route("/sellerlogin", methods = ['POST'])
def sellerlogin():
    # Getting data from form request
    username = request.form['username']
    pwd = request.form['password']

    # Checking whether it exists in the DB or not
    cur = mysql.connection.cursor()
    cur.execute("select username,password,ID from logindetails where type = 'seller'")
    
    records = cur.fetchall()
    print(records)

    for i in records:
        if username == i[0] and pwd == i[1]:
            l = "/sellerhomepage/" + str(i[2])
            return redirect(l)
    return render_template('login.html')

@app.route("/dplogin", methods = ['POST'])
def dplogin():
     # Getting data from form request
    username = request.form['username']
    pwd = request.form['password']

    # Checking whether it exists in the DB or not
    cur = mysql.connection.cursor()
    cur.execute("select username,password,ID from logindetails where type = 'dp'")
    
    records = cur.fetchall()
    print(records)

    for i in records:
        if username == i[0] and pwd == i[1]:
            l = "/dphomepage/" + str(i[2])
            return redirect(l)
        else:
            print("Failure")
    mysql.connection.commit()
    cur.close()

    return render_template('login.html')    

@app.route("/customersignup", methods = ['POST'])
def customerSignup():
    # Gathering details from form
    username = request.form['Username']
    name = request.form['Name']
    email = request.form['Email']
    phone = request.form['Contact_Number']
    address = request.form['Address']
    pwd = request.form['Password']

    # Counting number of records
    cur = mysql.connection.cursor()
    cur.execute("select count(*) from customer")
    no_of_records = cur.fetchall()[0][0]
    customerID = no_of_records + 1

    # Getting date 
    d = datetime.today().strftime('%Y-%m-%d')

    # Inserting into Customer Table
    s = "INSERT INTO customer (Customer_ID, Name, Email, Contact_No, Reg_Date, Address, Points) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    vals = (int(customerID), name, email, phone, d, address, int(0))
    cur.execute(s, vals)

    # Inserting into Customer_LoginDetails table
    s = "INSERT INTO LoginDetails (Username, Password, Type, ID) VALUES (%s, %s, %s, %s)"
    vals = (username, pwd, 'customer', int(customerID))
    cur.execute(s, vals)

    mysql.connection.commit()
    cur.close()
    return render_template('login.html')

@app.route("/sellersignup", methods = ['POST'])
def sellerSignup():
    # Gathering details from form
    username = request.form['Username']
    name = request.form['Name']
    email = request.form['Email']
    phone = request.form['Contact_Number']
    address = request.form['Address']
    pwd = request.form['Password']

    # Counting number of records
    cur = mysql.connection.cursor()
    cur.execute("select count(*) from seller")
    no_of_records = cur.fetchall()[0][0]
    sellerID = no_of_records + 1

    # Inserting into Seller Table
    s = "INSERT INTO Seller (Seller_ID, Name, Location, Contact_No, Email_ID) VALUES (%s, %s, %s, %s, %s)"
    vals = (int(sellerID), name, address, phone, email)
    cur.execute(s, vals)

    # Inserting into Customer_LoginDetails table
    s = "INSERT INTO LoginDetails (Username, Password, Type, ID) VALUES (%s, %s, %s, %s)"
    vals = (username, pwd, 'seller', int(sellerID))
    cur.execute(s, vals)

    s = "CREATE USER '" + username + "'@'" + host + "' IDENTIFIED BY '" + pwd + "'"
    cur.execute(s)

    s = "GRANT SELECT ON seller to '" + username + "'@'localhost'"
    cur.execute(s)
    
    mysql.connection.commit()
    cur.close()
    return render_template('login.html')

@app.route("/homepage/<user_id>")
def homepage(user_id):
    cur = mysql.connection.cursor()
    d = getDetails(user_id)

    s = "select * from categories";
    cur.execute(s)
    c = cur.fetchall()

    s = "select * from products"
    cur.execute(s)
    p = cur.fetchall()
    
    cart_price = getCurrentCartPrice(user_id)

    return render_template('homepage.html', details = d, categories = c, products = p, cart_price = cart_price)

@app.route("/sellerhomepage/<seller_id>")
def sellerhomepage(seller_id):
    cur = mysql.connection.cursor()
    s = "select * from seller where seller_id = " + str(seller_id)
    cur.execute(s)
    d = cur.fetchall()[0]

    s = "select * from products where seller_id = " + str(seller_id)
    cur.execute(s)
    p = cur.fetchall()

    s = "select * from logindetails where type = 'seller' and id = " + str(seller_id)
    cur.execute(s)
    current_seller = cur.fetchall()[0]
    username = current_seller[0]
    pwd = current_seller[1]

    mysql.connection.commit()

    host = 'localhost'
    user = username
    passwd = pwd
    db = 'project'

    mysql_seller = MySQLdb.connect(host, user, passwd, db)
    seller_cursor = mysql_seller.cursor()

    s = "SELECT TABLE_SCHEMA,TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS where TABLE_SCHEMA = 'PROJECT' AND TABLE_NAME = 'my_orders_info" + str(seller_id) + "'"
    cur.execute(s)
    if(len(cur.fetchall()) == 0):
        s = "create view my_orders_info" + str(seller_id) + " as select s.seller_id, s.name as seller_name, p.name as product_name, p.price, c.quantity_ordered, c.ccustomerid as customer_id, c.cart_id as cart_id from seller s inner join products p on s.seller_id = p.seller_id inner join cart c on c.product_id = p.product_id and c.cart_id in (select cart_id from orders) where s.seller_id = " + str(seller_id)
        cur.execute(s)

    s = "GRANT SELECT ON my_orders_info" + str(seller_id) + " TO '" + username + "'@'localhost'"
    cur.execute(s)

    si = "select * from my_orders_info" + str(seller_id)
    seller_cursor.execute(si)
    # print(seller_cursor.fetchall())


    return render_template('sellerhomepage.html', details = d, products = p)

@app.route("/sellerorderinfo/<user_id>")
def seller_order_info(user_id):
    d = getSellerDetails(user_id)
    cur = mysql.connection.cursor()
    s = "select * from logindetails where type = 'seller' and id = " + str(user_id)
    cur.execute(s)
    current_seller = cur.fetchall()[0]
    username = current_seller[0]
    pwd = current_seller[1]

    mysql.connection.commit()

    host = 'localhost'
    user = username
    passwd = pwd
    db = 'project'

    mysql_seller = MySQLdb.connect(host, user, passwd, db)
    seller_cursor = mysql_seller.cursor()

    s = "select * from my_orders_info" + str(user_id)
    seller_cursor.execute(s)
    orders = seller_cursor.fetchall()
    # print(orders)

    orders_info = []
    for i in orders:
        customer_id = i[5]
        cart_id = i[6]
        s = "select * from orders where ocustomerid = " + str(customer_id) + " and cart_id = " + str(cart_id)
        cur.execute(s)
        orders_info.append(cur.fetchall()[0][0])
    
    product_images = []
    for i in orders:
        product_name = i[2]
        s = "select imagesource from products p where p.name = '" + str(product_name) + "'"
        cur.execute(s)
        product_images.append(cur.fetchall()[0][0])
    print(product_images)
    return render_template("sellerOrderInfo.html", details = d, orders = orders, orders_info = orders_info, img = product_images)

@app.route("/addproducts/<seller_id>")
def addProductsPage(seller_id):
    return render_template("addproduct.html", id = seller_id)

@app.route("/newproduct/<seller_id>", methods = ['POST'])
def newProduct(seller_id):
    name = request.form['product_name']
    category = request.form['category']
    price = request.form['price']
    quantity = request.form['quantity']
    desc = request.form['description']
    days = request.form['days_to_arrive']
    # print(request.files)

    cur = mysql.connection.cursor()
    s = "select * from Products"
    cur.execute(s)
    p = cur.fetchall()
    product_id = len(p) + 1

    s = "select category_id from categories where category_name = '" + category + "'"
    print(s)
    cur.execute(s)
    p = cur.fetchall()
    print(p)
    category_id = p[0][0]

    file = request.files['product_image']
    basedir = os.path.abspath(os.path.dirname(__file__))
    file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], file.filename))

    img_path = "../static/products/" + str(file.filename)
    s = "insert into PRODUCTS (Product_ID, Category_ID, Name, Price, Quantity_Available, Seller_ID, Days_to_Arrive, Description, ImageSource) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    v = (int(product_id), int(category_id), name, float(price), int(quantity), int(seller_id), int(days), desc, img_path)
    cur.execute(s, v)
    mysql.connection.commit()
    cur.close()

    l = "/sellerhomepage/" + seller_id
    return redirect(l)

@app.route("/myprofile/<user_id>")
def myprofile(user_id):
    cur = mysql.connection.cursor()
    d = getDetails(user_id)

    s = "select username from logindetails where Id = " + str(user_id) + " and type = 'customer'"
    cur.execute(s)
    u = cur.fetchall()[0][0]

    s = "select * from categories";
    cur.execute(s)
    c = cur.fetchall()

    cart_price = getCurrentCartPrice(user_id)

    return render_template("myprofile.html", details = d, username = u, categories = c, cart_price = cart_price)

@app.route("/cart/<user_id>")
def cart(user_id):
    cur = mysql.connection.cursor()
    s = "select * from customer where customer_ID = " + str(user_id)
    cur.execute(s)
    d = cur.fetchall()[0]

    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "select count(*) from my_carts"         # my_Carts is a view select * from carts where user_id = ccustomerid
    cur.execute(s)

    if(cur.fetchall()[0][0] == 0):
        current_cartId = 1
    else:
        s = "select max(cart_id) from my_carts"
        cur.execute(s)
        current_cartId = cur.fetchall()[0][0]
        cartOrdered = ifCartOrdered(user_id, current_cartId)
        if(cartOrdered):
            current_cartId +=1
    
    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)

    s = "select * from my_current_cart"
    cur.execute(s)

    c = cur.fetchall()
    print(c)

    products_ordered_id = []
    for i in c:
        products_ordered_id.append(i[2])
    
    products_ordered = []
    for i in products_ordered_id:
        s = "select * from products where product_id = " + str(i)
        cur.execute(s)
        products_ordered.append(cur.fetchall())


    quantity_ordered = []
    for i in c:
        quantity_ordered.append(i[3])

    final_price = []
    total = 0
    for i in range(len(c)):
        final_price.append(round(quantity_ordered[i] * products_ordered[i][0][3], 2))
        total += final_price[i]
        
    total = round(total, 2)

    s = "select * from categories";
    cur.execute(s)
    c = cur.fetchall()

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)

    return render_template("cart.html", details = d, products = products_ordered, q = quantity_ordered, p = final_price, t = total, categories = c)

@app.route("/<user_id>/products/<product_id>")
def productPage(user_id, product_id):
    d = getDetails(user_id)

    p = getProductDetails(product_id)

    categories = getAllCategories()

    c = getCategoryFromProduct(product_id)

    r = getReviewsOfProduct(product_id)
    total_stars = 0
    for i in r:
        total_stars += i[2]
    if(len(r)!=0):
        avg_stars = total_stars/len(r)
    else:
        avg_stars = 0

    review_users = []
    for i in r:
        review_users.append(getDetails(i[3]))
    
    seller_id = p[5]

    avg_stars = round(avg_stars, 2)

    cur = mysql.connection.cursor()
    s = "select * from seller where seller_id = "  + str(seller_id)
    cur.execute(s)
    seller = cur.fetchall()[0]

    cart_price = getCurrentCartPrice(user_id)
    return render_template("product.html", details = d, product = p, category = c, reviews = r, average = avg_stars, users = review_users, categories = categories, seller = seller, cart_price = cart_price)

@app.route("/<user_id>/addtocart/<product_id>", methods = ['GET', 'POST'])
def addToCart(user_id, product_id):
    cur = mysql.connection.cursor()
    q = request.form
    quantity = 1
    for i in q:
        quantity = request.form[i]

    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "select count(*) from my_carts"         # my_Carts is a view select * from carts where user_id = ccustomerid
    cur.execute(s)
    
    if(cur.fetchall()[0][0] == 0):
        current_cartId = 1
    else:
        s = "select max(cart_id) from my_carts"
        cur.execute(s)
        current_cartId = cur.fetchall()[0][0]
        cartOrdered = ifCartOrdered(user_id, current_cartId)
        if(cartOrdered):
            current_cartId +=1
        #  Add a check for whether cart is checked out or not when making changes in the DB
    
    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)
    
    s = "select * from my_current_cart where product_id = " + str(product_id)
    cur.execute(s)
    if(len(cur.fetchall()) == 0):
        s = "Insert into cart values (%s, %s, %s, %s)"
        vals = (int(current_cartId), int(user_id), int(product_id), int(quantity))
        cur.execute(s, vals)
        mysql.connection.commit()
    else:
        s = "UPDATE my_current_cart SET quantity_ordered = quantity_ordered + " + str(quantity) + " where product_id = " + str(product_id)
        cur.execute(s)
        mysql.connection.commit()

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)
    l = "/cart/" + str(user_id)
    return redirect(l)

@app.route("/<user_id>/addquantity/<product_id>")
def addQuantity(user_id, product_id):
    cur = mysql.connection.cursor()

    current_cartId = getCurrentCartId(user_id)

    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)
    
    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)
    
    s = "UPDATE my_current_cart SET quantity_ordered = quantity_ordered + 1 where product_id = " + str(product_id)
    cur.execute(s)
    mysql.connection.commit()

    s = "drop view my_current_cart"
    cur.execute(s)

    s = "drop view my_carts"
    cur.execute(s)

    l = "/cart/" + str(user_id)
    return redirect(l)

@app.route("/<user_id>/reducequantity/<product_id>")
def reduceQuantity(user_id, product_id):
    cur = mysql.connection.cursor()

    current_cartId = getCurrentCartId(user_id)

    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)
    
    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)
    
    s = "UPDATE my_current_cart SET quantity_ordered = quantity_ordered - 1 where product_id = " + str(product_id)
    cur.execute(s)
    mysql.connection.commit()

    s = "select quantity_ordered from my_current_cart where product_id = " + str(product_id)
    cur.execute(s)
    if(cur.fetchall()[0][0] == 0):
        s = "SET FOREIGN_KEY_CHECKS=0"
        cur.execute(s)
        s = "delete from my_current_cart where product_id = " + str(product_id)
        cur.execute(s)
        s = "SET FOREIGN_KEY_CHECKS=1"
        cur.execute(s)
        mysql.connection.commit()

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)

    l = "/cart/" + str(user_id)
    return redirect(l)

@app.route("/checkout/<user_id>")
def checkout(user_id):
    d = getDetails(user_id)
    c = getAllCategories()
    price = getCurrentCartPrice(user_id)
    return render_template('checkout.html', details = d, categories = c, t = price)

@app.route("/placeorder/<user_id>/<payment_type>")
def placeOrder(user_id, payment_type):
    cur = mysql.connection.cursor()
    d = getDetails(user_id)
    cat = getAllCategories()

    current_cartId = getCurrentCartId(user_id)
    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)

    s = "select * from my_current_cart"
    cur.execute(s)

    c = cur.fetchall()
    print(c)

    products_ordered_id = []
    for i in c:
        products_ordered_id.append(i[2])
    
    products_ordered = []
    for i in products_ordered_id:
        s = "select * from products where product_id = " + str(i)
        cur.execute(s)
        products_ordered.append(cur.fetchall())
    
    quantity_ordered = []
    for i in c:
        quantity_ordered.append(i[3])
    
    final_price = []
    total = 0
    for i in range(len(c)):
        final_price.append(round(quantity_ordered[i] * products_ordered[i][0][3], 2))
        total += final_price[i]
        
    total = round(total, 2)

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)

    s = "select count(*) from orders"
    cur.execute(s)
    orderId = cur.fetchall()[0][0] + 1

    date = datetime.today().strftime('%Y-%m-%d')

    payment_type = payment_type.capitalize()

    return render_template("orderPlaced.html", details = d, categories = cat, products = products_ordered, q = quantity_ordered, p = final_price, t = total, orderId = orderId, date = date, payment_type = payment_type)

@app.route("/confirmorder/<user_id>/<payment_type>")
def orderConfirmed(user_id, payment_type):
    cur = mysql.connection.cursor()
    d = getDetails(user_id)
    cat = getAllCategories()

    current_cartId = getCurrentCartId(user_id)
    print("Current cart: ", current_cartId)
    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)

    s = "select * from my_current_cart"
    cur.execute(s)

    c = cur.fetchall()
    print(c)

    products_ordered_id = []
    for i in c:
        products_ordered_id.append(i[2])
    
    products_ordered = []
    for i in products_ordered_id:
        s = "select * from products where product_id = " + str(i)
        cur.execute(s)
        products_ordered.append(cur.fetchall())
    
    quantity_ordered = []
    for i in c:
        quantity_ordered.append(i[3])
    
    final_price = []
    total = 0
    for i in range(len(c)):
        final_price.append(round(quantity_ordered[i] * products_ordered[i][0][3], 2))
        total += final_price[i]
        
    total = round(total, 2)

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)

    s = "select count(*) from orders"
    cur.execute(s)
    orderId = cur.fetchall()[0][0] + 1

    date = datetime.today().strftime('%Y-%m-%d')

    s = "Insert into orders values (%s, %s, %s, %s)"
    vals = (int(orderId), int(user_id), date, int(current_cartId))
    cur.execute(s,vals)
    mysql.connection.commit()

    s = "select count(*) from payment"
    cur.execute(s)
    paymentId = cur.fetchall()[0][0] + 1

    type = payment_type
    status = "SUCCESSFUL"
    
    s = "Insert into payment values (%s, %s, %s, %s, %s, %s)"
    vals = (int(paymentId), int(orderId), type, status, date, float(total))
    cur.execute(s, vals)
    mysql.connection.commit()

    s = "select * from deliveries where order_id = " + str(orderId)
    cur.execute(s)
    delivery = cur.fetchall()[0]

    # Reduce quantity of products ordered, link payment to the order and assign this order to a delivery person and add it to deliveries table

    return render_template("orderConfirmed.html", details = d, categories = cat, products = products_ordered, q = quantity_ordered, p = final_price, t = total, orderId = orderId, date = date, delivery = delivery, payment_type = type)
    
@app.route("/myorders/<user_id>")
def myOrders(user_id):
    cur = mysql.connection.cursor()
    d = getDetails(user_id)
    cat = getAllCategories()

    s = "create view my_orders as select * from orders where ocustomerid = " + str(user_id)
    cur.execute(s)

    s = "select * from my_orders"
    cur.execute(s)
    orders = []
    for i in cur.fetchall():
        cart_id = i[3]
        order_id = i[0]
        no_of_products = getNumberOfProducts(user_id, cart_id)
        order_date = i[2]

        s = "select order_status from deliveries where order_id = " + str(order_id)
        cur.execute(s)
        status = cur.fetchall()[0][0]

        order = []
        order.append(order_id)
        order.append(no_of_products)
        order.append(order_date)
        order.append(status)
        orders.append(order)

    s = "drop view my_orders"
    cur.execute(s)

    cart_price = getCurrentCartPrice(user_id)

    return render_template("myorders.html", details = d, categories = cat, orders = orders, cart_price = cart_price)

@app.route("/orderinfo/<order_id>/<user_id>")
def orderInfo(order_id, user_id):
    cur = mysql.connection.cursor()
    d = getDetails(user_id)
    cat = getAllCategories()

    s = "select cart_id from orders where order_id = " + str(order_id)
    cur.execute(s)
    current_cartId = cur.fetchall()[0][0]

    print("Current cart: ", current_cartId)
    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)

    s = "select * from my_current_cart"
    cur.execute(s)

    c = cur.fetchall()
    print(c)

    products_ordered_id = []
    for i in c:
        products_ordered_id.append(i[2])
    
    products_ordered = []
    for i in products_ordered_id:
        s = "select * from products where product_id = " + str(i)
        cur.execute(s)
        products_ordered.append(cur.fetchall())
    
    quantity_ordered = []
    for i in c:
        quantity_ordered.append(i[3])
    
    final_price = []
    total = 0
    for i in range(len(c)):
        final_price.append(round(quantity_ordered[i] * products_ordered[i][0][3], 2))
        total += final_price[i]
        
    total = round(total, 2)

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)

    date = datetime.today().strftime('%Y-%m-%d')

    s = "select * from deliveries where order_id = " + str(order_id)
    cur.execute(s)
    delivery = cur.fetchall()[0]

    s = "select type from payment where orderid = " + str(order_id)
    cur.execute(s)
    type = cur.fetchall()[0][0]

    return render_template("orderConfirmed.html", details = d, categories = cat, products = products_ordered, q = quantity_ordered, p = final_price, t = total, orderId = order_id, date = date, delivery = delivery, payment_type = type)


@app.route("/<user_id>/addreview/<product_id>")
def addReview(user_id, product_id):
    d = getDetails(user_id)
    p = product_id
    return render_template("addReview.html", details = d, productid = p)

@app.route("/<user_id>/newreview/<product_id>", methods = ['POST'])
def newReview(user_id, product_id):
    print(request.form)
    stars = request.form['stars']
    text= request.form['write-a-review']

    cur = mysql.connection.cursor()
    s = "select count(*) from reviews"
    cur.execute(s)
    review_id = cur.fetchall()[0][0] + 1
    d = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    s = "Insert into reviews values (%s, %s, %s, %s, %s, %s)"
    vals = (int(review_id), text, int(stars), int(user_id), int(product_id), d)
    cur.execute(s, vals)
    mysql.connection.commit()
    l = "/" + str(user_id) + "/addreview/" + str(product_id)
    return redirect(l)

@app.route("/track/<user_id>/<order_id>")
def track(user_id, order_id):
    d = getDetails(user_id)
    cart_price = getCurrentCartPrice(user_id)
    c = getAllCategories()

    cur = mysql.connection.cursor()
    s = "select * from deliveries where order_id = " + str(order_id)
    cur.execute(s)
    delivery = cur.fetchall()[0]

    dp_id = delivery[1]
    s = "select * from delivery_person where dp_id = " + str(dp_id)
    cur.execute(s)
    dp = cur.fetchall()[0]
    order_status = delivery[2]

    dod = delivery[3]
    cur_date= date.today()
    days_till_recieving = (dod-cur_date).days
    if(days_till_recieving <= 0):
        order_status = "Delivered"
        s = "update deliveries set order_status = 'Delivered' where order_id = " + str(order_id)
        cur.execute(s)
        mysql.connection.commit()
    
    os = 0
    if(order_status == "On the way"):
        os = 1
    if(order_status == "Delivered"):
        os = 2

    return render_template("trackOrder.html", details = d, cart_price = cart_price, categories = c, order_id = order_id, delivery = delivery, dp = dp, os = os)

@app.route("/category/<category_id>/<user_id>")
def categoryPage(category_id, user_id):
    d = getDetails(user_id)
    categories = getAllCategories()
    
    cur = mysql.connection.cursor()
    s = "select * from products where category_id = " + str(category_id)
    cur.execute(s)
    products = cur.fetchall()

    s = "select * from categories where category_id = " + str(category_id)
    cur.execute(s)
    category = cur.fetchall()

    cart_price = getCurrentCartPrice(user_id)
    return render_template("category.html", details = d, categories = categories, products = products, category = category, cart_price = cart_price)

@app.route("/<category_id>/<user_id>/lowtohigh")
def categoryPageLowToHigh(category_id, user_id):
    d = getDetails(user_id)
    categories = getAllCategories()
    
    cur = mysql.connection.cursor()
    s = "select * from products where category_id = " + str(category_id) + " order by price"
    cur.execute(s)
    products = cur.fetchall()

    s = "select * from categories where category_id = " + str(category_id)
    cur.execute(s)
    category = cur.fetchall()

    return render_template("category.html", details = d, categories = categories, products = products, category = category)

@app.route("/<category_id>/<user_id>/hightolow")
def categoryPageHightoLow(category_id, user_id):
    d = getDetails(user_id)
    categories = getAllCategories()
    
    cur = mysql.connection.cursor()
    s = "select * from products where category_id = " + str(category_id) + " order by price desc"
    cur.execute(s)
    products = cur.fetchall()

    s = "select * from categories where category_id = " + str(category_id)
    cur.execute(s)
    category = cur.fetchall()

    return render_template("category.html", details = d, categories = categories, products = products, category = category)

@app.route("/<category_id>/<user_id>/<stars>")
def categoryPageStars(category_id, user_id, stars):
    d = getDetails(user_id)
    categories = getAllCategories()
    
    cur = mysql.connection.cursor()
    # s = "select * from products where category_id = " + str(category_id)
    # cur.execute(s)
    # products = cur.fetchall()

    s = "select p.product_id, avg(stars) as average from products p inner join reviews r on p.product_id = r.product_id and p.category_id = " + str(category_id) + " group by product_id having average > " + str(stars)
    cur.execute(s)
    
    products = []
    for i in cur.fetchall():
        pid = i[0]
        s = "select * from products where product_id = " + str(pid)
        cur.execute(s)
        products.append(cur.fetchall()[0])


    s = "select * from categories where category_id = " + str(category_id)
    cur.execute(s)
    category = cur.fetchall()

    return render_template("category.html", details = d, categories = categories, products = products, category = category)

@app.route("/dphomepage/<dp_id>")
def dp_homepage(dp_id):
    cur = mysql.connection.cursor()
    s = "select name from delivery_person where dp_id = " + str(dp_id)
    cur.execute(s)
    name = cur.fetchall()[0][0]

    s = "select * from logindetails where type = 'dp' and id = " + str(dp_id)
    cur.execute(s)
    current_seller = cur.fetchall()[0]
    username = current_seller[0]
    pwd = current_seller[1]

    mysql.connection.commit()

    host = 'localhost'
    user = username
    passwd = pwd
    db = 'project'

    mysql_seller = MySQLdb.connect(host, user, passwd, db)
    dp_cursor = mysql_seller.cursor()

    dates = []
    order_ids = []
    s = "select * from deliveries d where d.order_status = 'On the Way' and d.dp_id = " + str(dp_id)
    cur.execute(s)
    for i in cur.fetchall():
        dates.append(i[3])
        order_ids.append(i[0])
    
    user_details = []
    s = "SELECT TABLE_SCHEMA,TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS where TABLE_SCHEMA = 'PROJECT' AND TABLE_NAME = 'dp_pending_orders" + str(dp_id) + "'"
    cur.execute(s)
    if(len(cur.fetchall()) == 0):
        s = "create view dp_pending_orders" + str(dp_id) + " as select customer_id, address from customer where customer_id in (select ocustomerid from orders o where o.order_id in (select order_id from deliveries d where d.order_status = 'On the Way' and d.dp_id = " + str(dp_id) + "))"
        cur.execute(s)

    s = "GRANT SELECT ON dp_pending_orders" + str(dp_id) + " TO '" + username + "'@'localhost'"
    cur.execute(s)

    s = "select * from dp_pending_orders" + str(dp_id)
    dp_cursor.execute(s)
    for i in dp_cursor.fetchall():
        user_details.append(i)
    

    return render_template("dphomepage.html", name = name, dates = dates, user_details = user_details, dp_id = dp_id, orders = order_ids)

@app.route("/dpreturns/<dp_id>")
def dp_returns(dp_id):
    cur = mysql.connection.cursor()
    s = "select name from delivery_person where dp_id = " + str(dp_id)
    cur.execute(s)
    name = cur.fetchall()[0][0]

    s = "select * from logindetails where type = 'dp' and id = " + str(dp_id)
    cur.execute(s)
    current_seller = cur.fetchall()[0]
    username = current_seller[0]
    pwd = current_seller[1]

    mysql.connection.commit()

    host = 'localhost'
    user = username
    passwd = pwd
    db = 'project'

    mysql_seller = MySQLdb.connect(host, user, passwd, db)
    dp_cursor = mysql_seller.cursor()

    dates = []
    order_ids = []
    s = "select * from returns r where r.dp_id = " + str(dp_id)
    cur.execute(s)
    for i in cur.fetchall():
        dates.append(i[3])
        order_ids.append(i[0])
    
    user_details = []
    s = "SELECT TABLE_SCHEMA,TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS where TABLE_SCHEMA = 'PROJECT' AND TABLE_NAME = 'dp_pending_returns" + str(dp_id) + "'"
    cur.execute(s)
    if(len(cur.fetchall()) == 0):
        s = "create view dp_pending_returns" + str(dp_id) + " as select customer_id, address from customer where customer_id in (select ocustomerid from orders o where o.order_id in (select order_id from returns r where r.dp_id = " + str(dp_id) + "))"
        cur.execute(s)

    s = "GRANT SELECT ON dp_pending_returns" + str(dp_id) + " TO '" + username + "'@'localhost'"
    cur.execute(s)

    s = "select * from dp_pending_returns" + str(dp_id)
    dp_cursor.execute(s)
    for i in dp_cursor.fetchall():
        user_details.append(i)
    print(user_details)
    
    return render_template("dpreturns.html", name = name, dates = dates, user_details = user_details, dp_id = dp_id, orders = order_ids)

@app.route("/deliveryhistory/<dp_id>")
def deliveryhistory(dp_id):
    cur = mysql.connection.cursor()
    s = "select name from delivery_person where dp_id = " + str(dp_id)
    cur.execute(s)
    name = cur.fetchall()[0][0]

    s = "select * from logindetails where type = 'dp' and id = " + str(dp_id)
    cur.execute(s)
    current_seller = cur.fetchall()[0]
    username = current_seller[0]
    pwd = current_seller[1]

    mysql.connection.commit()

    host = 'localhost'
    user = username
    passwd = pwd
    db = 'project'

    mysql_seller = MySQLdb.connect(host, user, passwd, db)
    dp_cursor = mysql_seller.cursor()

    dates = []
    order_ids = []
    s = "select * from deliveries d where d.order_status = 'Delivered' and d.dp_id = " + str(dp_id)
    cur.execute(s)
    for i in cur.fetchall():
        dates.append(i[3])
        order_ids.append(i[0])
    
    user_details = []
    s = "SELECT TABLE_SCHEMA,TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS where TABLE_SCHEMA = 'PROJECT' AND TABLE_NAME = 'dp_order_history" + str(dp_id) + "'"
    cur.execute(s)
    if(len(cur.fetchall()) == 0):
        s = "create view dp_order_history" + str(dp_id) + " as select customer_id, address from customer where customer_id in (select ocustomerid from orders o where o.order_id in (select order_id from deliveries d where d.order_status = 'Delivered' and d.dp_id = " + str(dp_id) + "))"
        cur.execute(s)

    s = "GRANT SELECT ON dp_order_history" + str(dp_id) + " TO '" + username + "'@'localhost'"
    cur.execute(s)

    s = "select * from dp_order_history" + str(dp_id)
    dp_cursor.execute(s)
    for i in dp_cursor.fetchall():
        user_details.append(i)
    print(user_details)
    print(dates)

    return render_template("dphistory.html", name = name, dates = dates, user_details = user_details, dp_id = dp_id, orders = order_ids)

@app.route("/return/<order_id>/<user_id>")
def return_item(order_id, user_id):
    cur = mysql.connection.cursor()
    s = "select count(*) from delivery_person"
    cur.execute(s)
    no = cur.fetchall()[0][0]

    dp_id = random.randint(1, no)

    date = datetime.today().strftime('%Y-%m-%d')

    s = "Insert into returns values(%s, %s, %s, %s)"
    vals = (int(order_id), int(dp_id), "Returned", date)
    cur.execute(s,vals)
    mysql.connection.commit()

    s = "update deliveries set order_status = 'Returned' where order_id = " + str(order_id)
    cur.execute(s)
    mysql.connection.commit()

    s = "select amount from payment where orderid = " + str(order_id)
    cur.execute(s)
    price = cur.fetchall()[0][0]

    s = "update customer set points = points + " + str(price) + " where customer_id = " + str(user_id) 
    cur.execute(s)
    mysql.connection.commit()
    return "Returned"

@app.route("/admin")
def admin():
    cur = mysql.connection.cursor()

    s = "select count(*) from customer"
    cur.execute(s)
    customers = cur.fetchall()[0][0]

    s = "select count(*) from seller"
    cur.execute(s)
    sellers = cur.fetchall()[0][0]

    s = "select count(*) from orders"
    cur.execute(s)
    orders = cur.fetchall()[0][0]

    s = "select sum(amount) from payment"
    cur.execute(s)
    earned = cur.fetchall()[0][0]
    earned = int(earned)

    s = "select p.product_id, p.name, sum(c.quantity_ordered * p.price) as total, sum(c.quantity_ordered) from cart c inner join products p on c.product_id = p.product_id where c.cart_id in (select cart_id from orders) and c.ccustomerid in (select ocustomerid from orders o where o.cart_id = c.cart_id) group by c.product_id order by total desc;"
    cur.execute(s)
    product_wise_money = cur.fetchall()

    s = "select c.name, sum(p.Amount) from payment p, customer c where c.customer_id in (select o.ocustomerid from orders o where p.orderid = o.order_id) group by c.name"
    cur.execute(s)
    customer_info = cur.fetchall()

    s = "Select type, SUM(Amount) from payment group by type"
    cur.execute(s)
    payment_info = cur.fetchall()
    
    payment_type_percentage = []
    cnt = 0
    for i in payment_info:
        payment_type_percentage.append(int(i[1])/int(earned) * 100)
        cnt+=1
    
    for i in range(4-cnt):
        payment_type_percentage.append(0)
    
    payment_info = {'Card': payment_type_percentage[0], 'UPI': payment_type_percentage[1], 'COD': payment_type_percentage[2], 'Points': payment_type_percentage[3]}
    print(payment_info)
    

    return render_template("admin.html", customers = customers, orders = orders, sellers = sellers, earned = earned, pwm = product_wise_money, ci = customer_info, ptp = payment_type_percentage, data = payment_info)

# Helper functions
def getDetails(user_id):
    cur = mysql.connection.cursor()
    s = "select * from customer where customer_id = " + str(user_id)
    cur.execute(s)
    return cur.fetchall()[0]

def getProductDetails(product_id):
    cur = mysql.connection.cursor()
    s = "select * from products where product_id = " + str(product_id)
    cur.execute(s)
    return cur.fetchall()[0]

def getCategoryFromProduct(product_id):
    cur = mysql.connection.cursor()
    s = "select * from categories where category_id in (select category_id from products where product_id = " + str(product_id) + ")"
    cur.execute(s)
    return cur.fetchall()[0]

def getReviewsOfProduct(product_id):
    cur = mysql.connection.cursor()
    s = "select * from reviews where product_id = " + str(product_id)
    cur.execute(s)
    return cur.fetchall()

def getAllCategories():
    cur = mysql.connection.cursor()
    s = "select * from categories"
    cur.execute(s)
    return cur.fetchall()

def ifCartOrdered(user_id, cart_id):
    cur = mysql.connection.cursor()
    s = "select * from orders where OCustomerID = " + str(user_id) + " and Cart_ID = " + str(cart_id)
    cur.execute(s)
    if(len(cur.fetchall()) == 0):
        return False
    return True

def getCurrentCartPrice(user_id):
    cur = mysql.connection.cursor()
    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "select count(*) from my_carts"         # my_Carts is a view select * from carts where user_id = ccustomerid
    cur.execute(s)
    
    if(cur.fetchall()[0][0] == 0):
        current_cartId = 1
    else:
        s = "select max(cart_id) from my_carts"
        cur.execute(s)
        current_cartId = cur.fetchall()[0][0]
        cartOrdered = ifCartOrdered(user_id, current_cartId)
        if(cartOrdered):
            current_cartId +=1
    
    s = "create view my_current_cart as select * from my_carts where cart_id = " + str(current_cartId)
    cur.execute(s)

    s = "select * from my_current_cart"
    cur.execute(s)

    c = cur.fetchall()
    print(c)

    products_ordered_id = []
    for i in c:
        products_ordered_id.append(i[2])
    
    products_ordered = []
    for i in products_ordered_id:
        s = "select * from products where product_id = " + str(i)
        cur.execute(s)
        products_ordered.append(cur.fetchall())


    quantity_ordered = []
    for i in c:
        quantity_ordered.append(i[3])

    final_price = []
    total = 0
    for i in range(len(c)):
        final_price.append(round(quantity_ordered[i] * products_ordered[i][0][3], 2))
        total += final_price[i]
        
    total = round(total, 2)

    s = "drop view my_current_cart"
    cur.execute(s)
    s = "drop view my_carts"
    cur.execute(s)

    return total

def getCurrentCartId(user_id):
    cur = mysql.connection.cursor()
    s = "select * from customer where customer_ID = " + str(user_id)
    cur.execute(s)
    d = cur.fetchall()[0]

    s = "create view my_carts as select * from cart where ccustomerid = " + str(user_id)
    cur.execute(s)

    s = "select count(*) from my_carts"         # my_Carts is a view select * from carts where user_id = ccustomerid
    cur.execute(s)

    if(cur.fetchall()[0][0] == 0):
        current_cartId = 1
    else:
        s = "select max(cart_id) from my_carts"
        cur.execute(s)
        current_cartId = cur.fetchall()[0][0]
        cartOrdered = ifCartOrdered(user_id, current_cartId)
        if(cartOrdered):
            current_cartId +=1
    
    s = "drop view my_carts"
    cur.execute(s)

    return current_cartId

def getNumberOfProducts(user_id, cart_id):
    cur = mysql.connection.cursor()

    s = "select * from cart where cart_id = " + str(cart_id) + " and ccustomerid = " + str(user_id)
    cur.execute(s)
    return len(cur.fetchall())

def getSellerDetails(user_id):
    cur = mysql.connection.cursor()

    s = "select * from seller where seller_id = " + str(user_id)
    cur.execute(s)
    return cur.fetchall()[0]

if(__name__ == "__main__"):
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True)