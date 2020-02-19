

import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twitoff.models import db, User, Tweet, migrate
from twitoff.routes import my_routes
from twitoff.twitter_service import twitter_api_client

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

def create_app():
    app = Flask(__name__)
    app.config["CUSTOM_VAR"] = 5  # just an example of app config
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["TWITTER_API_CLIENT"] = twitter_api_client()

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(my_routes)

    return app
