from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import CelestialBodies, Landmark, User, Passenger

@app.route('/')
def hello():
    return "App is running"

@app.route('/celestial_bodies')
def get_all():
    try:
        bodies = CelestialBodies.query.all()
        return jsonify({'data': [e.serialize() for e in bodies]})
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()

@app.cli.command('db_seed')
def db_seed():
    body1 = CelestialBodies(name='Earth',
                     image='Motivation',
                     celestial_body_type='Planet',
                     gravity=4.2,
                     planet_day=3.4,
                     planet_year=5.6)

    body6 = CelestialBodies(name='Mars',
                     image='Motivation',
                     celestial_body_type='Planet',
                     gravity=4.2,
                     planet_day=3.4,
                     planet_year=5.6)

    body2 = CelestialBodies(name='Venus',
                     image='Motivation',
                     celestial_body_type='Planet',
                     gravity=4.2,
                     planet_day=3.4,
                     planet_year=5.6)

    body3 = CelestialBodies(name='Neptune',
                     image='Motivation',
                     celestial_body_type='Planet',
                     gravity=4.2,
                     planet_day=3.4,
                     planet_year=5.6)

    body4 = CelestialBodies(name='Pluto',
                     image='Motivation',
                     celestial_body_type='Planet',
                     gravity=4.2,
                     planet_day=3.4,
                     planet_year=5.6)

    body5 = CelestialBodies(name='Uranus',
                     image='Motivation',
                     celestial_body_type='Planet',
                     gravity=4.2,
                     planet_day=3.4,
                     planet_year=5.6)

    db.session.add(body1)
    db.session.add(body2)
    db.session.add(body3)
    db.session.add(body4)
    db.session.add(body5)
    db.session.commit()
    print('Database seeded!')

