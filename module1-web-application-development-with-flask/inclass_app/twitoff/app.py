from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


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
