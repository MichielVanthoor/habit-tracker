from app import app

from flask import render_template

# Overview of all the routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
