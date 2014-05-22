import os
import sqlite3
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir

DATABASE = '/opt/love-story/app.db'
STORYDIR = '/opt/love-story/app/stories/'
app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)
from app import views