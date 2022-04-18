from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])  
def signup():  
    return render_template("signup.html")

if(__name__ == "__main__"):
    app.run(debug = True)