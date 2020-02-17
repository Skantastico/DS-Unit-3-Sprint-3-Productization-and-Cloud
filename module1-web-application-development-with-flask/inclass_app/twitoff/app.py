from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["CUSTOM_VAR"] = 5 # just an example of app config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitoff_100.db"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


#
# ROUTING
#


@app.route("/")
def index():
    # return "Hello World!"
    return render_template("homepage.html")


@app.route("/about")
def about():
    return "About Me"


@app.route("/users")
@app.route("/users.json")
def users():
    users = [
        {"id": 1, "name": "First User"},
        {"id": 2, "name": "Second User"},
        {"id": 3, "name": "Third User"}
    ]
    return jsonify(users)


@app.route("/users/create", methods=["POST"])
def create_user():
    print("CREATING A NEW USER...")
    print("FORM DATA:", dict(request.form))
    #todo: create a new user
    return jsonify({"message": "CREATED OK(TODO)"})


# Get /hello
# Get /hello?name=Polly
# Get /hello?name=Polly&country=USA

@app.route("/hello")
def hello(name=None):
    print("VISITING THE HELLO PAGE")
    print("REQUEST PARAMS:", dict(request.args))

    if "name" in request.args:
        name = request.args["name"]
        message = f"Hello, {name}"
    else:
        message = "Hello World"

    # return message
    return render_template("hello.html", message=message)
