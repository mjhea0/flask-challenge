# project/server/tests/base.py


import json

from flask_testing import TestCase

from project.server import app


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def setUp(self):
        with open(app.config['DATA_FILE'], mode='w') as file:
            file.write(json.dumps([], indent=2))
        with open(app.config['STATS_FILE'], mode='w') as file:
            file.write(json.dumps([], indent=2))

    def tearDown(self):
        with open(app.config['DATA_FILE'], mode='w') as file:
            file.write(json.dumps([], indent=2))
        with open(app.config['STATS_FILE'], mode='w') as file:
            file.write(json.dumps([], indent=2))
