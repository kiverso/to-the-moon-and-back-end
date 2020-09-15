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

@app.route('/api/v1/celestial_bodies/<id>', methods = ['GET'])
def get_one_body(id):
    try:
        celestial_body = CelestialBodies.query.get(id)
        return jsonify(celestial_body.serialize())
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
                        landmark_type="Surface",
                        description="Sun spots happen when fluctuations in the sun cause areas of the surface to be not as hot as their surroundings, causing that area to look darker than the rest of the sun. Despite only appearing as spots, they can grow to a size several times our own planet's! They can last anywhere from a few days to a few months, and tend to increase and decrease in frequency based off of eleven-year cycles.",
                        celestial_body_id=9)

    solar_flare = Landmark(name="Solar Flares",
                           image="https://media1.s-nbcnews.com/j/newscms/2017_23/2030061/170608-solar-flare-mn-0850_be3b4f10ba85b1f4ef86e87522e6b26a.fit-2000w.jpg",
                           landmark_type="Atmosphere",
                           description="Solar flares are bright flashes caused by increased activity from the sun, in conjunction with a coronal mass ejection - an intense wave of energized particles that erupt from the sun and fly out into the solar system. While they are relatively common, they can cause electrical problems should the Earth be in the path of a flare, thanks to the disturbances they can cause in the atmosphere.",
                           celestial_body_id=9)

    apollodorus = Landmark(name="Apollodorus",
                           image="https://www.nasa.gov/sites/default/files/thumbnails/image/messenger-12-apollodorus_pantheon_2015_0.png",
                           landmark_type="Crater",
                           description="This crater, located within the Pantheon Fossae, is remarkable because of the long troughs that radiate out from the center. When first discovered, it was nicknamed the Spider because of the web like shape. It is still uncertain if the impact caused them, or whether the asteroid that caused the crater merely landed in the center of a pre-existing formation.",
                           celestial_body_id=1)

    caloris = Landmark(name="Caloris Basin",
                       image="https://cdn.britannica.com/75/145475-050-916827A9/Caloris-Basin-Mercury-spacecraft-Messenger-2008.jpg",
                       landmark_type="Crater",
                       description="The Caloris basin is one of the largest impact craters in the Solar System, measuring at over 900 miles wide. The asteroid that created the impact was likely at least 60 miles wide, larger than the one theorized to have caused the dinosaurs' extinction. The impact was so violent that it caused deformations in the terrain on the exact opposite side of the planet (the antipode).",
                       celestial_body_id=1)

    mercury_pole = Landmark(name="Poles",
                            image="https://api.hub.jhu.edu/factory/sites/default/files/styles/hub_medium/public/mercury_ice.jpg?itok=1baACeWG",
                            landmark_type="Structure",
                            description="Despite being the planet closest to the sun, Mercury can get quite cold. At the poles of the planet, hidden perpetually from the sun in the shadows of craters, there's ample evidence that there is large amounts of ice lying frozen. Though a fraction of what exists on Earth's polar regions, it is still enough to be at least a couple miles deep.",
                            celestial_body_id=1)

    debussy = Landmark(name="Debussy",
                       image="https://live.staticflickr.com/6170/6176086738_3a98b804a4_b.jpg",
                       landmark_type="Crater",
                       description="Named after the French composer, this crater, along with a similar one named Hakusai, are prominent enough to be detected from Earth using radio telescopes. It has a very noticeable ray pattern stretching out from the impact center, which indicates that it's relatively new. It was one of the first things photographed by the MESSENGER probe, sent to orbit the planet from 2011 to 2015.",
                       celestial_body_id=1)

    tolstoj = Landmark(name="Tolstoj",
                       image="https://upload.wikimedia.org/wikipedia/commons/b/b1/Tolstoj_crater_EW0227961993G.jpg",
                       landmark_type="Crater",
                       description="The Tolstoj crater is notable for its well-preserved ejecta blanket and the reflective material that has settled into the crater plain, leaving it an easy to spot bright patch on the planet's surface. It is one of the oldest craters on Mercury, being estimated to be nearly 4 billion years old.",
                       celestial_body_id=1)

    venus_atmo = Landmark(name="Atmosphere",
                          image="https://cdn.mos.cms.futurecdn.net/B8WfkaJZWrsms27RGsTu63.jpg",
                          landmark_type="Atmosphere",
                          description="The thick atmosphere of Venus means despite being further away from the sun than Mercury, it's actually the hottest planet in the system with a surface temperature of 870 degrees Fahrenheit. It's caused by a runaway greenhouse effect - since it's made of nearly 96% carbon dioxide. The atmosphere is also so dense that the pressure is 90 times that of Earth. Oh, and the clouds and rain are made of sulfuric acid.",
                          celestial_body_id=2)

    terra = Landmark(name="Terra",
                     image="https://media.sciencephoto.com/r3/34/00/21/r3340021-800px-wm.jpg",
                     landmark_type="Surface",
                     description="While there are no oceans on Venus - water is incompatible with such harsh conditions - areas of highland terrain that rise up above the volcanic plains make up the rough landmasses of Venus. These are known as terra, and there are three - the two major ones, Aphrodite Terra (around the size of South America) and Ishtar Terra (somewhere between the continental US and Australia), as well as a smaller one, Lada Terra, at Venus's south pole.",
                     celestial_body_id=2)

    regio = Landmark(name="Regio",
                     image="https://p0.pikist.com/photos/78/602/venus-planet-surface-space-solar-system-alpha-regio.jpg",
                     landmark_type="Surface",
                     description="Regio are large plateaus that rise above Venus's surface. They are composed of some of the most intriguing tectonic features of Venus, such as the highly deformed tesserae terrain in the Alpha Regio, or the large Devana Chasma rift zone that cuts through the Beta Regio. These were some of the first regions of the surface to be detected by radar, as the cloud cover made telescopic observation impossible.",
                     celestial_body_id=2)

    maxwell = Landmark(name="Maxwell Montes",
                       image="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Maxwell_Montes_of_planet_Venus.jpg/1280px-Maxwell_Montes_of_planet_Venus.jpg",
                       landmark_type="Mountain",
                       description="Maxwell Montes is the highest mountain on Venus, standing at about 35,000 feet tall. Rising from the Ishtar Terra on the northern half of the planet, the mountain is one of just three features not named after women or ancient goddesses on the entire surface of the planet, having been grandfathered in before the International Astronomical Union made the decision on nomenclature for further discoveries.",
                       celestial_body_id=2)

    maat = Landmark(name="Maat Mons",
                    image="https://media.pixcove.com/F/8/2/Maat-Mons-Planet-Venus-Surface-Free-Image-Space-So-6947.jpg",
                    landmark_type="Mountain",
                    description="Named for the Egyptian goddess of truth, Maat Mons is the largest volcano on Venus and the second highest on the planet. Venus is the most volcanically active planet in the entire solar system, with over 1600 major volcanoes across the surface. Indeed, there's evidence that the entire planet is periodically resurfaced in floods of lava.",
                    celestial_body_id=2)

    sea_tranquility = Landmark(name="Sea of Tranquility",
                               image="https://ca-times.brightspotcdn.com/dims4/default/df8dc29/2147483647/strip/true/crop/600x338+0+31/resize/1200x675!/quality/90/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F69%2Fd5%2Ffb72584f2cbca5a528892bcfa45c%2F11-apollo-fevbd1gy",
                               landmark_type="Surface",
                               description="Mare, or seas, are dark features most common on the near side of the moon - where volcanic eruptions have covered these regions in basalt, which reflects less of the sun's light. Generally wide and flat, the most famous of these is the Sea of Tranquility, where on July 20, 1969, Apollo 11 became the first manned lunar landing.",
                               celestial_body_id=8)

    tycho = Landmark(name="Tycho",
                     image="https://skyandtelescope.org/wp-content/uploads/Tycho-closeup-at-full-Frank-Barrett.jpg",
                     landmark_type="Crater",
                     description="Perhaps the most notable crater on the near side of the moon thanks to its distinctive rays that spread out across the southern side. It is a relatively young crater by the standards of the moon, having impacted roughly 108 million years ago, which means unlike other prominent craters, it has yet to be malformed by further impacts.",
                     celestial_body_id=8)

    aitken = Landmark(name="Aitken Basin",
                      image="https://i.insider.com/5cfeb3856fc920079c630e49?width=1100&format=jpeg&auto=webp",
                      landmark_type="Crater",
                      description="The largest impact crater on the moon, and one of the largest in the entire solar system is located on the South Pole, creating the South Pole-Aitken Basin. Mostly visible from the far side of the moon, the crater is 1600 miles wide, and 4 to 5 miles deep. On the near side visible from Earth, only the outer ring of the basin, known as the Leibnitz mountains, can be seen.",
                      celestial_body_id=8)

    oceanus = Landmark(name="Oceanus Procellarum",
                       image="https://upload.wikimedia.org/wikipedia/commons/1/19/Oceanus_Procellarum_%28LRO%29.png",
                       landmark_type="Surface",
                       description="Of all the dark spots that splotch the near side of the moon, only Procellarum, the largest by some stretch, was given the title Oceanus - or ocean, in comparison to the mare, or seas, that are defined elsewhere. It covers 10% of the entire lunar surface, and has been visited by a series of probes - the Soviet Luna 9 and 13, and the American Surveyor 1 and 3. Apollo 12 would land close to the Surveyor 3 site, returning parts of the probe home with them, the only time this was ever done.",
                       celestial_body_id=8)

    orientale = Landmark(name="Mare Orientale",
                         image="https://apod.nasa.gov/apod/image/1103/orientale_lro_crop800.jpg",
                         landmark_type="Crater",
                         description="Though the name means Eastern Sea, it is so called because it appears on the east from Earth - it is actually on the west side of the moon. Though difficult to see because it lies on the boundary of what is visible, satellite imagery in the 1960s revealed it to have a striking set of concentric circles, making almost a target bullseye on the moon. The inner ring of mountains is known as the Montes Rook, while the outer ring are known as the Montes Cordillera.",
                         celestial_body_id=8)

    olympus = Landmark(name="Olympus Mons",
                          image="https://cdn.mos.cms.futurecdn.net/XNRcoHujh5mZHmPQZzYbgH.jpg",
                          landmark_type="Mountain",
                          description="The largest mountain on any planet in the solar system, the volcano Olympus Mons towers over the Martian surface, rising 85,000 feet from the surrounding terrain. It is, in fact, so tall that it almost rises above the Martian atmosphere, close to sticking out all the way into space. At two and a half times the size of Mount Everest, were it to be placed in the deepest part of the Pacific Ocean, it would still rise higher than most commercial jetliners fly.",
                          celestial_body_id=3)

    marineris = Landmark(name="Valles Marineris",
                         image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/VallesMarinerisHuge.jpg/800px-VallesMarinerisHuge.jpg",
                         landmark_type="Surface",
                         description="The Valles Marineris is a noticeable scar on the Martian surface, a canyon that would dwarf the Earth's Grand Canyon, at four times the depth, a dozen times the length and over ten times the Grand Canyon's maximum width. The most likely reason for its formation is a tectonic crack in the planet's surface, widened over time via erosion and collapses of the rift walls.",
                         celestial_body_id=3)

    borealis = Landmark(name="Borealis Basin",
                        image="https://scx2.b-cdn.net/gfx/news/2017/swriledteamd.jpg",
                        landmark_type="Structure",
                        description="Most of the north of Mars lies in a very wide basin that covers 40% of the entire planet. The basin is considerably smoother than the rest of the planet's surface and is mostly flat, though the volcanic Tharsis Bulge rises above it in the planet's western hemisphere. Speculation abounds as to why the north and south of the planet are so different - whether it be a large asteroid impact (if so, the basin would be the largest crater in the Solar System by a fourfold margin) or perhaps a vast ocean in Mars' distant past.",
                        celestial_body_id=3)

    hellas = Landmark(name="Hellas Planitia",
                      image="https://upload.wikimedia.org/wikipedia/commons/2/21/Hellas_Planitia_by_the_Viking_orbiters.jpg",
                      landmark_type="Crater",
                      description="This crater impact site is not quite the largest on Mars, but is noticeable for being incredibly deep - over thirty thousand feet lower than the surrounding terrain. The crater is so deep that it causes changes to the Martian atmosphere, and the air pressure at the bottom of the crater is double what it is elsewhere on the Martian surface. In fact, it's one of the few places on Mars that has sufficient pressure to sustain liquid water, were the temperature to stay warm enough.",
                      celestial_body_id=3)

    phobos_deimos = Landmark(name="Phobos and Deimos",
                             image="https://mars.nasa.gov/system/content_pages/main_images/65_moons.jpg",
                             landmark_type="Moon",
                             description="The two moons of Mars are tiny - Phobos is less than 15 miles long, with Deimos being less than 10. They are still visible from the Martian surface, however, thanks to orbiting much closer to the planet. They are named after twin sons of the Greek god Ares, who is the analogue to the Roman god Mars. Though it is not known for certain, the most likely scenario is that Mars captured these moons from the asteroid belt.",
                             celestial_body_id=3)

    db.session.add(solar_core)
    db.session.add(photosphere)
    db.session.add(corona)
    db.session.add(sunspots)
    db.session.add(solar_flare)
    db.session.add(apollodorus)
    db.session.add(caloris)
    db.session.add(mercury_pole)
    db.session.add(debussy)
    db.session.add(tolstoj)
    db.session.add(venus_atmo)
    db.session.add(terra)
    db.session.add(regio)
    db.session.add(maxwell)
    db.session.add(maat)
    db.session.add(sea_tranquility)
    db.session.add(tycho)
    db.session.add(oceanus)
    db.session.add(orientale)
    db.session.add(olympus)
    db.session.add(marineris)
    db.session.add(borealis)
    db.session.add(hellas)
    db.session.add(phobos_deimos)
    db.session.commit()
    print('Landmarks seeded!')
