"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import openaq
import requests



APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

api = openaq.OpenAQ()




def get_data():
    status, body = api.measurements(city="Los Angeles", parameter="pm25")
    results = body['results']
    date_value_tuples = []
    for result in results:
        tuple = str(result['date']['utc']), result['value']
        date_value_tuples.append(tuple)
    return date_value_tuples


@APP.route('/')
def root():
    """Base view."""
    results = get_data()
    return str(results)
    # return render_template("base.html", title=results)
