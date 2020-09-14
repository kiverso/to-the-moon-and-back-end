import json
from models import CelestialBodies
from app import db

def test_hello(app):
  client = app.test_client()
  resp = client.get('/')
  data = data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert 'App is running' in data['message']

def test_it_can_return_all_celestial_bodies(app):
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

  db.session.add(mercury)
  db.session.add(venus)
  db.session.commit()

  client = app.test_client()
  resp = client.get('/api/v1/celestial_bodies')
  data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert len(data['data']) == 2
  assert (data['data'][0]['name']) == 'Mercury'
  assert (data['data'][0]['celestial_body_type']) == mercury.celestial_body_type
  assert (data['data'][0]['image']) == mercury.image
  assert (data['data'][0]['gravity']) == mercury.gravity
  assert (data['data'][0]['planet_day']) == mercury.planet_day
  assert (data['data'][0]['planet_year']) == mercury.planet_year
  assert (data['data'][0]['travel']) == mercury.travel_time()

