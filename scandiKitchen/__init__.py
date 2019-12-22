import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import Loginmanager

app = Flask(__name__)

#setup database
basedir = os.path.abspath(os.path.dirname(__file__))
#set up connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK+MODIFICATIONS'] = False

#create database
db = SQLAlchemy(app)
#connect app to database
Migrate(app,db)

#setup login configurations
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from scandiKitchen.core.views import core
app.register_blueprint(core)
