# project/server/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(current_app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertFalse('data_test.json' in app.config['DATA_FILE'])
        self.assertTrue('data_dev.json' in app.config['DATA_FILE'])
        self.assertFalse('stats_test.json' in app.config['STATS_FILE'])
        self.assertTrue('stats_dev.json' in app.config['STATS_FILE'])


class TestTestingConfig(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue('data_test.json' in app.config['DATA_FILE'])
        self.assertFalse('data_dev.json' in app.config['DATA_FILE'])
        self.assertTrue('stats_test.json' in app.config['STATS_FILE'])
        self.assertFalse('stats_dev.json' in app.config['STATS_FILE'])


class TestProductionConfig(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertFalse(current_app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
