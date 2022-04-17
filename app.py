from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return "Login :)"

if(__name__ == "__main__"):
    app.run(debug = True)