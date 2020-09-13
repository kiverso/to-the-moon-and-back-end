from app import db
from sqlalchemy.dialects.postgresql import JSON
import solarsystem
import datetime

voyages = db.Table('voyages',
      db.Column('user_id', db.Integer, db.ForeignKey('users.id'),
        primary_key=True),
      db.Column('celestial_bodies_id', db.Integer,
        db.ForeignKey('celestial_bodies.id'), primary_key=True)
)

class CelestialBodies(db.Model):
    __tablename__ = 'celestial_bodies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    celestial_body_type = db.Column(db.String())
    gravity = db.Column(db.Float())
    planet_day = db.Column(db.Float())
    planet_year = db.Column(db.Float())
    landmark = db.relationship('Landmark', backref='celestial_bodies',
        lazy=True)
    user = db.relationship('User', secondary=voyages,
        back_populates='celestial_bodies')

    def __init__(self, name, image, celestial_body_type, gravity, planet_day,
        planet_year):
      self.name = name
      self.image = image
      self.celestial_body_type = celestial_body_type
      self.gravity = gravity
      self.planet_day = planet_day
      self.planet_year = planet_year

    def __repr__(self):
          return '<id {}>'.format(self.id)

    def serialize(self):
      return {
        'id': self.id,
        'name': self.name,
        'image': self.image,
        'celestial_body_type': self.celestial_body_type,
        'gravity': self.gravity,
        'planet_day': self.planet_day,
        'planet_year': self.planet_year,
        'travel': self.travel_time()
      }

    def travel_time(self):
      miles_per_au = 92955807 # Number of miles in one astronomical unit
      ship_speed = 24816 #Ship speed equal to maximum speed for manned spaceflight

      if self.name == 'Moon':
        moon_distance = 238900
        return {'distance': moon_distance, 'travel_time': moon_distance / ship_speed}
      now    = datetime.datetime.utcnow()
      now    = datetime.datetime.now(datetime.timezone.utc)
      year   = now.year
      month  = now.month
      day    = now.day
      hour   = now.hour
      minute = now.minute

      planets = solarsystem.Geocentric(year=year, month=month, day=day, hour=hour, minute=minute ).position()
      distance_au = planets[self.name][2]
      distance_miles = distance_au * miles_per_au
      travel_time = distance_miles / ship_speed
      return {'distance': distance_miles, 'travel_time': travel_time}

class Landmark(db.Model):
    __tablename__ = 'landmarks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    landmark_type = db.Column(db.String())
    image = db.Column(db.String())
    description = db.Column(db.String())
    celestial_body_id = db.Column(db.Integer,
        db.ForeignKey('celestial_bodies.id'), nullable=False)

    def __init__(self, name, landmark_type, image, description,
        celestial_body_id):
      self.name = name
      self.landmark_type = landmark_type
      self.image = image
      self.description = description
      self.celestial_body_id = celestial_body_id

    def __repr__(self):
          return '<id {}>'.format(self.id)

    def serialize(self):
      return {
        'id': self.id,
        'name': self.name,
        'image': self.image,
        'landmark_type': self.landmark_type,
        'description': self.description,
        'celestial_body_id': self.celestial_body_id
      }

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password_digest = db.Column(db.String())
    passenger = db.relationship('Passenger', backref='passengers', lazy=True)
    celestial_bodies = db.relationship('CelestialBodies', secondary=voyages,
        back_populates='user')

    def __init__(self, user_name, email, password_digest):
      self.user_name = user_name
      self.email = email
      self.password_digest = password_digest

    def __repr__(self):
            return '<id {}>'.format(self.id)

class Passenger(db.Model):
    __tablename__ = 'passengers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    weight = db.Column(db.Float())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, age, weight):
      self.name = name
      self.age = age
      self.weight = weight
      self.user_id = user_id

    def __repr__(self):
            return '<id {}>'.format(self.id)
