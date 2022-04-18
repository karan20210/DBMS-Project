from datetime import datetime
from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.safe_load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

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
            print("Success")
            break
        else:
            print("Failure")
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
            print("Success")
            break
        else:
            print("Failure")
    mysql.connection.commit()
    cur.close()

    return render_template('login.html')

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

if(__name__ == "__main__"):
    app.run(debug = True)