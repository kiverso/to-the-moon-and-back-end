from flask import Blueprint, Flask, request, jsonify
from models import CelestialBodies, Landmark, User, Passenger

main  = Blueprint('main', __name__)
@main.route('/')
def hello():
    return jsonify({'message': "App is running"})

@main.route('/api/v1/celestial_bodies', methods = ['GET'])
def get_bodies():
    try:
        bodies = CelestialBodies.query.all()
        return jsonify({'data': [e.serialize() for e in bodies]})
    except Exception as e:
        return(str(e))

@main.route('/api/v1/celestial_bodies/<id>', methods = ['GET'])
def get_one_body(id):
    try:
        celestial_body = CelestialBodies.query.get(id)
        return jsonify(celestial_body.serialize())
    except Exception as e:
        return(str(e))

@main.route('/api/v1/news', methods = ['GET'])
def get_api():
    try:
        response = requests.get('https://spaceflightnewsapi.net/api/v1/articles')
        return response.json()
    except Exception as response:
        return(str("Bad Request"))

@main.route('/api/v1/celestial_bodies/<id>/landmarks', methods = ['GET'])
def get_landmarks(id):
    try:
        landmarks = Landmark.query.filter(Landmark.celestial_body_id == id)
        return jsonify({'data': [e.serialize() for e in landmarks]})
    except Exception as e:
        return(str(e))

@main.route('/api/v1/landmarks/<id>', methods = ['GET'])
def get_landmark(id):
    try:
        landmark = Landmark.query.get(id)
        return jsonify(landmark.serialize())
    except Exception as e:
        return(str(e))
