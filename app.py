from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

current_app = Flask(__name__)
current_app.config.from_object(os.environ['APP_SETTINGS'])

current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(current_app)

from models import CelestialBodies, Landmark, User, Passenger

@current_app.route('/')
def hello():
    return "App is running"

if __name__ == '__main__':
    current_app.run()

