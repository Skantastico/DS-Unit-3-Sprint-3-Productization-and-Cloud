from flask import Blueprint, jsonify, request, render_template #current_app

from twitoff.models import User, Tweet, db

my_routes = Blueprint("routes", __name__)


#
# ROUTING
#


@my_routes.route("/")
def index():
    # return "Hello World!"
    return render_template("homepage.html")


@my_routes.route("/about")
def about():
    return "About Me"


@my_routes.route("/users")
@my_routes.route("/users.json")
def users():
    # users = [
    #     {"id": 1, "name": "First User"},
    #     {"id": 2, "name": "Second User"},
    #     {"id": 3, "name": "Third User"}
    # ]
    # return jsonify(users)

    users = User.query.all()  # returns a list of <class 'alchemy.User'>
    # print(len(users))
    print(type(users))
    print(type(users[0]))

    users_response = []
    for u in users:
        user_dict = u.__dict__
        del user_dict["_sa_instance_state"]
        users_response.append(user_dict)

    return jsonify(users_response)


@my_routes.route("/users/create", methods=["POST"])
def create_user():
    print("CREATING A NEW USER...")
    print("FORM DATA:", dict(request.form))

    # return jsonify({"message": "CREATED OK(TODO)"})

    if "name" in request.form:
        name = request.form["name"]
        print(name)
        db.session.add(User(name=name))
        db.session.commit()
        return jsonify({"message": "CREATED OK", "name": name})
    else:
        return jsonify({"message": "OOPS PLEASE SPECIFY A NAME!"})

# Get /hello
# Get /hello?name=Polly
# Get /hello?name=Polly&country=USA


@my_routes.route("/hello")
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


@my_routes.route("/get_tweets")
def get_tweets():
    tweets = []
    # todo: actually get the tweets
    print(tweets)
    return jsonify({"message": "OK"})
