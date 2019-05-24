from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Th1s154R4nD0mk3Y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db =SQLAlchemy(app)
bcrypt = Bcrypt(app)

from nanoBlog import routes
