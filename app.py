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

@app.route('/signup')  
def signup():  
    return render_template("signup.html")

@app.route("/customerlogin", methods = ['POST'])
def customerlogin():
    print("Customer")
    print(request.form)

    username = request.form['username']
    pwd = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("select username,password,type from user")
    
    records = cur.fetchall()

    for i in records:
        if i[2] != "Customer":
            continue
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
    print("Seller")
    print(request.form)

    username = request.form['username']
    pwd = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("select username,password,type from user")
    
    records = cur.fetchall()

    for i in records:
        if i[2] != "Seller":
            continue
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
    print("Manager")
    print(request.form)

    username = request.form['username']
    pwd = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("select username,password,type from user")
    
    records = cur.fetchall()

    for i in records:
        if i[2] != "Manager":
            continue
        if username == i[0] and pwd == i[1]:
            print("Success")
            break
        else:
            print("Failure")
    mysql.connection.commit()
    cur.close()

    return render_template('login.html')

if(__name__ == "__main__"):
    app.run(debug = True)