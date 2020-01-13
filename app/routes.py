from app import app

import datetime
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
    query = db.select([habits]).where(habits.columns.user_id == 'miva')
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    total_results = []
    for date in ResultSet:
      daily_results = []

      # Detect the date
      formatted_date = date[1].strftime("%a, %b %d")

      daily_results.append(formatted_date)

      # Detect 'snoozed'
      if date[2] == 0:
        daily_results.append('warning')
      else:
        daily_results.append('danger')

      # Detect 'water_drank'
      if date[7] == 1:
        daily_results.append('warning')
      else:
        daily_results.append('danger')

      # Detect 'teeth_brushed_am'
      if date[3] == 1:
        daily_results.append('warning')
      else:
        daily_results.append('danger')

      # Detect 'www_used_am'
      if date[5] == 0:
        daily_results.append('warning')
      else:
        daily_results.append('danger')

      # Detect 'teeth_brushed_pm'
      if date[4] == 1:
        daily_results.append('warning')
      else:
        daily_results.append('danger')

      # Detect 'www_used_pm'
      if date[6] == 0:
        daily_results.append('warning')
      else:
        daily_results.append('danger')

      total_results.append(daily_results)


    num_dates = len(total_results)
    print(ResultSet)

    return render_template('index.html', num_dates = num_dates, results = total_results)
