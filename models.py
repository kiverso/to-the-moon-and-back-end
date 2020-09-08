from app import db
from sqlalchemy.dialects.postgresql import JSON

class CelestialBodies(db.Model):
    __tablename__ = 'celestial_bodies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    celestial_body_type = db.Column(db.String())
    gravity = db.Column(db.Integer())

    def __init__(self, name, image, celestial_body_type, gravity):
      self.name = name
      self.image = image
      self.celestial_body_type = celestial_body_type
      self.gravity = gravity

    def __repr__(self):
          return '<id {}>'.format(self.id)