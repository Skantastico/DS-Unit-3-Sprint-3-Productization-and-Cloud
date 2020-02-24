"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import openaq
import datetime


APP = Flask(__name__)
APP.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)
api = openaq.OpenAQ()


# CLASSES AND DEFS

def query_OpenAQ(city, param):
    status, body = api.measurements(city='city', parameter='param')
    if status == 200:
        query_dict = []
        for query in body['results']:
            query_results.append(query['date']['utc'], query['value'])
        return query_dict
    else:
        return "API Error! Something Went Wrong"


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'ID: {id}, Date: {self.datetime}, Value: {self.value}'


# ROUTES

@APP.route('/')
def root():
    """Homepage."""
    risky_values = Record.query.filter(Record.value >= 10).all()
    results = query_OpenAQ("Los Angeles", 'pm25')
    for result in results:
        time, value = result
        record = Record(datetime=str(time), value=value)
        DB.session.add(record)
    DB.session.commit()
    return render_template('homepage.html', risky_values = risky_values)


# I commented the refresh out because it kept giving me errors in refactor
# couldn't fix in time

# @APP.route('/refresh')
# def refresh():
#     """Pull fresh data from Open AQ and replace existing data."""
#     DB.drop_all()
#     DB.create_all()
#     results = query_OpenAQ("Los Angeles", 'pm25')
#     for result in results:
#         time, value = result
#         record = Record(datetime=str(time), value=value)
#         DB.session.add(record)
#     DB.session.commit()
#     return 'Data refereshed!'
