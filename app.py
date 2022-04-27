from crypt import methods
from datetime import datetime
import random
from unicodedata import category
from django.shortcuts import render
from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import yaml
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/products'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = 'karanb1809'
app.config['MYSQL_DB'] = 'PROJECT'

mysql = MySQL(app)

d = ()

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
            print("Success")
            break
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
    # ps = []
    # print(len(p))
    # for i in range(3):
    #     no = random.randint(0, len(p) - 1)
    #     ps.append(p[no])   
    
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

    mysql.connection.commit()
    cur.close()

    return render_template('sellerhomepage.html', details = d, products = p)

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
    cur.execute(s)
    p = cur.fetchall()
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

    return render_template("myprofile.html", details = d, username = u, categories = c)

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
    return render_template("product.html", details = d, product = p, category = c, reviews = r, average = avg_stars, users = review_users, categories = categories, seller = seller)

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
        print(i)
        cart_id = i[3]
        order_id = i[0]
        no_of_products = getNumberOfProducts(user_id, cart_id)
        order_date = i[2]

        order = []
        order.append(order_id)
        order.append(no_of_products)
        order.append(order_date)
        
        orders.append(order)

    s = "drop view my_orders"
    cur.execute(s)

    return render_template("myorders.html", details = d, categories = cat, orders = orders)

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
    print(dp)

    order_status = delivery[2]
    os = 0
    if(order_status == "On the way"):
        os = 1
    if(order_status == "Delivered"):
        os = 2

    return render_template("trackOrder.html", details = d, cart_price = cart_price, categories = c, order_id = order_id, delivery = delivery, dp = dp, os = os)

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

if(__name__ == "__main__"):
    app.run(debug = True)