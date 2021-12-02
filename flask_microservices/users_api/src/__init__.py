import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt


# SET ENV VARIABLE TO 
db_user     = os.environ.get('MYSQL_USER'),
db_pwd      = os.environ.get('MYSQL_PASSWORD'),
db_host     = os.environ.get('MYSQL_HOST'),
db_port     = os.environ.get('MYSQL_PORT')
db_name     = os.environ.get('MYSQL_DB')


# DATABASE_URI = f'mysql://root:root@localhost/utopia'
DATABASE_URI = f'mysql+pymysql://chuy:knowledge13@localhost:3306/utopia'


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
db.create_all()
# bcrypt = Bcrypt(app)

from src import views

