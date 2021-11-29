from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate
import os
# from flask_bcrypt import Bcrypt

# GET ENV VARIABLES from .env
config = {
    'host': os.environ.get('MYSQL_HOST'),
    'port': os.environ.get('MYSQL_PORT'),
    'user': os.environ.get('MYSQL_USER'),
    'password': os.environ.get('MYSQL_PASSWORD'),
    'database': os.environ.get('MYSQL_DB'),
}

# SET ENV VARIABLE TO 
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('ENV_VAR')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
db.create_all()
# bcrypt = Bcrypt(app)

from src import views

