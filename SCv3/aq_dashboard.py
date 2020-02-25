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


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '< Time {} -- Value {} >'.format(self.datetime, self.value)


def get_data():
    status, body = api.measurements(city="Los Angeles", parameter="pm25")
    results = body['results']
    date_value_tuples = []
    for result in results:
        tuple = str(result['date']['utc']), result['value']
        date_value_tuples.append(tuple)
    return date_value_tuples


def get_tuples(get_data):
    for tuple in get_data:
        add_db_records = Record(datetime=tuple[0], value=tuple[1])
        DB.session.add(add_db_records)


@APP.route('/')
def root():
    """Base view."""
    records = Record.query.filter(Record.value>=10).all()
    return str(records)

    # this is the code I used for part 1 and 2, depricated
    # results = get_data()
    # return str(results)
    # # return render_template("base.html", title=results)

@APP.route('/refresh')
def refresh():
    """Pull fresh data from OpenAQ and replace existing."""
    DB.drop_all()
    DB.create_all()
    tuples = get_data()
    get_tuples(tuples)
    DB.session.commit()
    return 'Data refreshed!'
