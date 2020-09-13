from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import CelestialBodies, Landmark, User, Passenger

@app.route('/')
def hello():
    return "App is running"

@app.route('/api/v1/celestial_bodies', methods = ['GET'])
def get_bodies():
    try:
        bodies = CelestialBodies.query.all()
        return jsonify({'data': [e.serialize() for e in bodies]})
    except Exception as e:
        return(str(e))

@app.route('/api/v1/news', methods = ['GET'])
def get_api():
    try:
        response = requests.get('https://spaceflightnewsapi.net/api/v1/articles')
        return response.json()
    except Exception as response:
        return(str("Bad Request"))

@app.route('/api/v1/celestial_bodies/<id>/landmarks', methods = ['GET'])
def get_landmarks(id):
    try:
        landmarks = Landmarks.query.filter(Landmarks.celestial_body_id == id)
        return jsonify({'data': [e.serialize() for e in landmarks]})
    except Exception as e:
        return(str(e))

@app.route('/api/v1/celestial_bodies/<body_id>/landmarks/<id>', methods = ['GET'])
def get_landmark(id):
    try:
        landmark = Landmarks.query.get(id)
        return jsonify(landmark.serialize())
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()

@app.cli.command('db_seed')
def db_seed():
    mercury = CelestialBodies(name='Mercury',
                     image='https://cdn.mos.cms.futurecdn.net/GA4grWEsUYUqH58cDbRBw8.jpg',
                     celestial_body_type='Planet',
                     gravity=0.37,
                     planet_day=58.65,
                     planet_year=87.96)

    venus = CelestialBodies(name='Venus',
                     image="https://astronomy.com/-/media/Images/News%20and%20Observing/News/2020/04/Venus1__1_.jpg?mw=600",
                     celestial_body_type='Planet',
                     gravity=0.90,
                     planet_day=243.02,
                     planet_year=224.70)

    mars = CelestialBodies(name='Mars',
                     image='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSY5oCXASYgKXI1MFGmRbgs9WmSnULsnOe_fg&usqp=CAU',
                     celestial_body_type='Planet',
                     gravity=0.38,
                     planet_day=1.02,
                     planet_year=686.98)

    jupiter = CelestialBodies(name='Jupiter',
                     image='https://3.bp.blogspot.com/-JzB2ruOjBOs/WJy8tR_tJSI/AAAAAAAABdA/26gANOQ4Y4IZyMnEGS2L8X-dvhVhGL0ZQCLcB/s1600/jupiter_HD.jpg',
                     celestial_body_type='Planet',
                     gravity=2.53,
                     planet_day=0.41,
                     planet_year=4332.59)

    saturn = CelestialBodies(name='Saturn',
                     image='https://solarsystem.nasa.gov/system/resources/list_images/2490_hubblesaturn_320.png',
                     celestial_body_type='Planet',
                     gravity=1.06,
                     planet_day=0.44,
                     planet_year=10759.22)

    uranus = CelestialBodies(name='Uranus',
                     image='https://i2-prod.mirror.co.uk/science/article11370299.ece/ALTERNATES/s615/1_Uranus.jpg',
                     celestial_body_type='Planet',
                     gravity=0.90,
                     planet_day=0.72,
                     planet_year=30685.40)

    neptune = CelestialBodies(name='Neptune',
                     image='https://media.wired.com/photos/5d04045bde1abfe4e801d054/191:100/w_2292,h_1200,c_limit/Science-Neptune-FA-PIA01492_orig.jpg',
                     celestial_body_type='Planet',
                     gravity=1.14,
                     planet_day=0.67,
                     planet_year=60189.00)

    moon = CelestialBodies(name='Moon',
                     image='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSA0QNeR2YGmCWvRtZqsYN9Ft44WxYJEArbtw&usqp=CAU',
                     celestial_body_type='Moon',
                     gravity=0.16,
                     planet_day=27.32,
                     planet_year=None)

    sun = CelestialBodies(name='Sun',
                     image='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRkKZ8nFulIMZAK8MKI8kzvsfGnaa3YlqMMRA&usqp=CAU',
                     celestial_body_type='Star',
                     gravity=27.95,
                     planet_day=25.38,
                     planet_year=None)

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(mars)
    db.session.add(jupiter)
    db.session.add(saturn)
    db.session.add(uranus)
    db.session.add(neptune)
    db.session.add(moon)
    db.session.add(sun)
    db.session.commit()
    print('Database seeded!')
