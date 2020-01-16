from app import app
from app import utils


import sqlalchemy as db


from flask import render_template


# Configure SQLAlchemy connection
engine = db.create_engine(
    'mysql+mysqldb://miva:fbbjDPcv8wwsrhwq@35.233.54.56/habit_tracker')
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

    results = utils.generate_output(ResultSet)
    num_dates = len(results)

    streaks = [2,2,2,2,2,2]


    return render_template('index.html', num_dates=num_dates, results=results, streaks=streaks)
