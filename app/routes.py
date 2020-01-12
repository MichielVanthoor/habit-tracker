from app import app

import os
import sqlalchemy as db

from flask import render_template, request
from flask_sslify import SSLify
from werkzeug.contrib.fixers import ProxyFix

# Configure HTTPS redirect
#app.wsgi_app = ProxyFix(app.wsgi_app)
#SSLify(app)

# Configure SQLAlchemy connection
engine = db.create_engine('mysql+mysqldb://miva:fbbjDPcv8wwsrhwq@35.233.54.56/habit_tracker')
connection = engine.connect()
metadata = db.MetaData()
habits = db.Table('habits', metadata, autoload=True, autoload_with=engine)

# Overview of all the routes
@app.route('/')
@app.route('/index')
def index():
    keys = habits.columns.keys()
    return render_template('index.html')
