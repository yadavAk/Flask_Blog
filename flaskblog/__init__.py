from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# export FLASK_APP=flaskblog.py
# export FLASK_DEBUG=1
# flask run

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ae7a2f19377000f6c12d91c84923d46'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes