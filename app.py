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
        landmarks = Landmark.query.filter(Landmark.celestial_body_id == id)
        return jsonify({'data': [e.serialize() for e in landmarks]})
    except Exception as e:
        return(str(e))

@app.route('/api/v1/landmarks/<id>', methods = ['GET'])
def get_landmark(id):
    try:
        landmark = Landmark.query.get(id)
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

@app.cli.command('seed_landmark')
def seed_landmark():
    solar_core = Landmark(name="Core",
                          image="https://cdn.mos.cms.futurecdn.net/WtnoFrpeLL37TLcjpzK5A7-970-80.jpg",
                          landmark_type="Structure",
                          description="Deep in the sun's core is the beating heart of the entire solar system. It's hard to believe that so much is powered by a reaction on the atomic scale. Under pressure from the gravity of the sun being so massive, hydrogen atoms fuse into helium, providing the energy that lights up the entire solar system. It produces 1.8 billion times the energy of the largest nuclear bomb detonated on Earth... every single second!",
                          celestial_body_id=9)

    photosphere = Landmark(name="Photosphere",
                           image="https://astronomy.swin.edu.au/cms/cpg15x/albums/scaled_cache/897b42ce97bcd409a597f1392b2dd379-280x229.png",
                           landmark_type="Structure",
                           description="When you look up into the sky (but hopefully not directly!) the bright ball of the photosphere is the part of the sun you're looking at. Though often depicted as being yellow, the light from the sun is white. When it hits the Earth's atmosphere, a phenomenon called Rayleigh scattering causes it to look yellow, as well as the sky blue. The same phenomenon is responsible for the brilliant colors of both sunrises and sunsets.",
                           celestial_body_id=9)

    corona = Landmark(name="Corona",
                      image="https://media.wired.com/photos/5e62e4af2ee19f000853234b/master/w_1600%2Cc_limit/photo_space_corona_1_AFRC2017-0233-006.jpg",
                      landmark_type="Atmosphere",
                      description="Just like the Earth, the sun also has an atmosphere. The largest part of it is known as its corona. Though it is not usually visible thanks to the brightness of the photosphere, during eclipses - when the moon's orbit puts it in the right place to block out the majority of the sun's light - it becomes readily apparent. Particles stream out of the corona to create solar wind, which is responsible for phenomena such as the auroras, and comets having tails, among others.",
                      celestial_body_id=9)

    sunspots = Landmark(name="Sunspots",
                        image="https://upload.wikimedia.org/wikipedia/commons/6/67/Sunspots_1302_Sep_2011_by_NASA.jpg",
                        landmark_type="Atmosphere",
                        description="Sun spots happen when fluctuations in the sun cause areas of the surface to be not as hot as their surroundings, causing that area to look darker than the rest of the sun. Despite only appearing as spots, they can grow to a size several times our own planet's! They can last anywhere from a few days to a few months, and tend to increase and decrease in frequency based off of eleven-year cycles.",
                        celestial_body_id=9)

    solar_flare = Landmark(name="Solar Flares",
                           image="https://media1.s-nbcnews.com/j/newscms/2017_23/2030061/170608-solar-flare-mn-0850_be3b4f10ba85b1f4ef86e87522e6b26a.fit-2000w.jpg",
                           landmark_type="Atmosphere",
                           description="Solar flares are bright flashes caused by increased activity from the sun, in conjunction with a coronal mass ejection - an intense wave of energized particles that erupt from the sun and fly out into the solar system. While they are relatively common, they can cause electrical problems should the Earth be in the path of a flare, thanks to the disturbances they can cause in the atmosphere.",
                           celestial_body_id=9)

    db.session.add(solar_core)
    db.session.add(photosphere)
    db.session.add(corona)
    db.session.add(sunspots)
    db.session.add(solar_flare)
    db.session.commit()
    print('Landmarks seeded!')
