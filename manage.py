import os
import pytest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the Test Suite"""
    pytest.main(["-s", "./tests"])


if __name__ == '__main__':
    manager.run()

