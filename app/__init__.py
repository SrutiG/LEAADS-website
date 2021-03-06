from flask import Flask

UPLOAD_FOLDER = 'app/static/images/'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
from flask_mysqldb import MySQL

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'LEAADS'
app.config['MYSQL_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key= "secretKey1"
mysql = MySQL(app)
from app import views



