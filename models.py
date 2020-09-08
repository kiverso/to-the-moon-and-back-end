from app import db
from sqlalchemy.dialects.postgresql import JSON

class CelestialBodies(db.Model):
    __tablename__ = 'celestial_bodies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    celestial_body_type = db.Column(db.String())
    gravity = db.Column(db.Integer())
    landmark = db.relationship('Landmark', backref='celestial_bodies', lazy=True)

    def __init__(self, name, image, celestial_body_type, gravity):
      self.name = name
      self.image = image
      self.celestial_body_type = celestial_body_type
      self.gravity = gravity

    def __repr__(self):
          return '<id {}>'.format(self.id)


class Landmark(db.Model):
    __tablename__ = 'landmark'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    landmark_type = db.Column(db.String())
    image = db.Column(db.String())
    description = db.Column(db.String())
    celestial_body_id = db.Column(db.Integer, db.ForeignKey('celestial_bodies.id'),
        nullable=False) 

    def __init__(self, name, landmark_type, image, description, celestial_body_id):
      self.name = name
      self.landmark_type = landmark_type
      self.image = image
      self.description = description
      self.celestial_body_id = celestial_body_id

    def __repr__(self):
          return '<id {}>'.format(self.id)