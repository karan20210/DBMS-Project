from datetime import datetime
import random
from unicodedata import category
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
    cur.execute("select username,password,customerID from customer_logindetails")
    
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
    cur.execute("select username,password,sellerID from seller_logindetails")
    
    records = cur.fetchall()
    print(records)

    for i in records:
        if username == i[0] and pwd == i[1]:
            l = "/sellerhomepage/" + str(i[2])
            return redirect(l)
    

@app.route("/managerlogin", methods = ['POST'])
def managerlogin():
     # Getting data from form request
    username = request.form['username']
    pwd = request.form['password']

    # Checking whether it exists in the DB or not
    cur = mysql.connection.cursor()
    cur.execute("select username,password,managerID from manager_logindetails")
    
    records = cur.fetchall()
    print(records)

    for i in records:
        if username == i[0] and pwd == i[1]:
            print("Success")
            return render_template('homepage.html')
        else:
            print("Failure")
    mysql.connection.commit()
    cur.close()

    return render_template('login.html')

@app.route("/cclogin", methods = ['POST'])
def cclogin():
     # Getting data from form request
    username = request.form['username']
    pwd = request.form['password']

    # Checking whether it exists in the DB or not
    cur = mysql.connection.cursor()
    cur.execute("select username,password,CCID from CC_LoginDetails")
    
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

@app.route("/dplogin", methods = ['POST'])
def dplogin():
     # Getting data from form request
    username = request.form['username']
    pwd = request.form['password']

    # Checking whether it exists in the DB or not
    cur = mysql.connection.cursor()
    cur.execute("select username,password,DPID from DP_LoginDetails")
    
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
    s = "INSERT INTO Customer_LoginDetails (Username, Password, CustomerID) VALUES (%s, %s, %s)"
    vals = (username, pwd, int(customerID))
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
    s = "INSERT INTO Seller_LoginDetails (Username, Password, sellerID) VALUES (%s, %s, %s)"
    vals = (username, pwd, int(sellerID))
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
    ps = []
    print(len(p))
    for i in range(3):
        no = random.randint(0, len(p) - 1)
        ps.append(p[no])   

    return render_template('homepage.html', details = d, categories = c, products = ps)

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

    s = "select username from customer_logindetails where customerId = " + str(user_id)
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

    s = "select * from cart where ccustomerid = " + str(user_id) + " and cart_id in (select max(cart_id) from cart)"
    cur.execute(s)
    c = cur.fetchall()
    # print(c)

    products_ordered_id = []
    for i in c:
        products_ordered_id.append(i[2])
    
    products_ordered = []
    for i in products_ordered_id:
        s = "select * from products where product_id = " + str(i)
        cur.execute(s)
        products_ordered.append(cur.fetchall())

    # print(products_ordered[0])

    quantity_ordered = []
    for i in c:
        quantity_ordered.append(i[3])
    # print(quantity_ordered)

    final_price = []
    total = 0
    for i in range(len(c)):
        final_price.append(quantity_ordered[i] * products_ordered[i][0][3])
        total += final_price[i]
        
    total = round(total, 2)

    s = "select * from categories";
    cur.execute(s)
    c = cur.fetchall()
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
    return render_template("product.html", details = d, product = p, category = c, reviews = r, average = avg_stars, users = review_users, categories = categories)


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
    
if(__name__ == "__main__"):
    app.run(debug = True)