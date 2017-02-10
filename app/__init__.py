from flask import Flask
<<<<<<< HEAD
#from flask_mysqldb import MySQL
=======
>>>>>>> fd8c8ef40f9c975d988f9c6b70fef947a3e0e6ce

app = Flask(__name__)
from app import views
app.secret_key= "secretKey1"

