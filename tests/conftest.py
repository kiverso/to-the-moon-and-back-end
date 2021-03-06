import pytest
from app import create_app, db

@pytest.fixture
def app():
  app = create_app()
  app.config.from_object('config.TestingConfig')
  with app.app_context():   
    db.create_all()
    yield app
    db.session.close()
    db.drop_all()

