from flask import Flask, jsonify, request

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


@app.route("users/create", methods=["POST"])
def create_user():
    print("CREATING A NEW USER...")
    print("FORM DATA:", dict(request.form))
    #todo: create a new user
    return jsonify({"message": "CREATED OK(TODO)"})