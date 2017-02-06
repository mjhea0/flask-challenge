# project/server/tests/test_api.py


import os
import json
import unittest
import pandas as pd

from base import BaseTestCase

from project.server import app

basedir = os.path.abspath(os.path.dirname(__file__))
SAMPLE_DATA = os.path.join(basedir, 'sample.json')


class TestAPIBlueprint(BaseTestCase):

    def test_ping(self):
        """Ensure Flask is setup."""
        resp = self.client.get('/api/v1/ping')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.headers['Content-Type'], 'application/json')
        self.assertEquals(resp.json['status'], '200')
        self.assertEquals(resp.json['data'], 'pong!')

    def test_ensure_content_type(self):
        """Ensure 'content_type' is 'application/json'."""
        resp = self.client.post(
            '/api/v1/stats',
            data=json.dumps(dict(foo='bar'))
        )
        self.assertEquals(resp.status_code, 400)
        self.assertEquals(resp.headers['Content-Type'], 'application/json')
        self.assertEquals(resp.json['status'], '400')
        self.assertEquals(resp.json['error'], 'Not found')

    def test_ensure_invalid_payload(self):
        """Ensure invalid payload throws an error."""
        resp = self.client.post(
            '/api/v1/stats',
            data=json.dumps(dict(foo='bar')),
            content_type='application/json'
        )
        self.assertEquals(resp.status_code, 400)
        self.assertEquals(resp.headers['Content-Type'], 'application/json')
        self.assertEquals(resp.json['status'], '400')
        self.assertEquals(resp.json['error'], 'Invalid payload')
        with open(app.config['DATA_FILE']) as file:
            self.assertEquals(len(json.load(file)), 0)

    def test_ensure_valid_payload(self):
        """Ensure valid payload."""
        with open(SAMPLE_DATA) as f:
            resp = self.client.post(
                '/api/v1/stats',
                data=json.dumps(json.load(f)),
                content_type='application/json'
            )
            self.assertEquals(resp.status_code, 200)
            self.assertEquals(resp.headers['Content-Type'], 'application/json')
            self.assertEquals(resp.json['status'], '200')
            self.assertEquals(resp.json['data'], 'Data added')
            with open(app.config['DATA_FILE']) as file:
                self.assertEquals(len(json.load(file)), 1)

    def test_ensure_more_than_one_row(self):
        """Ensure file conatins more than one row."""
        with open(SAMPLE_DATA) as f:
            self.client.post(
                '/api/v1/stats',
                data=json.dumps(json.load(f)),
                content_type='application/json'
            )
        with open(SAMPLE_DATA) as f:
            resp = self.client.post(
                '/api/v1/stats',
                data=json.dumps(json.load(f)),
                content_type='application/json'
            )
            self.assertEquals(resp.status_code, 200)
            self.assertEquals(resp.headers['Content-Type'], 'application/json')
            self.assertEquals(resp.json['status'], '200')
            self.assertEquals(resp.json['data'], 'Data added')
            with open(app.config['DATA_FILE']) as file:
                self.assertEquals(len(json.load(file)), 2)

    def test_ensure_all_stats(self):
        """Ensure all stats."""
        resp = self.client.get('/api/v1/stats')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.headers['Content-Type'], 'application/json')
        self.assertEquals(resp.json['status'], '200')
        self.assertEquals(resp.json['data'], [])

    def test_ensure_single_stat_is_none(self):
        """Ensure single stat is none."""
        resp = self.client.get('/api/v1/stats/test')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.headers['Content-Type'], 'application/json')
        self.assertEquals(resp.json['status'], '200')
        self.assertEquals(resp.json['data'], None)

    def test_ensure_single_stat_is_not_none(self):
        """Ensure single stat is not none."""
        with open(SAMPLE_DATA) as f:
            self.client.post(
                '/api/v1/stats',
                data=json.dumps(json.load(f)),
                content_type='application/json'
            )
        with open(app.config['STATS_FILE']) as file:
            resp = self.client.get('/api/v1/stats/{0}'.format(
                json.load(file)[0]['uuid']))
            self.assertEquals(resp.status_code, 200)
            self.assertEquals(resp.headers['Content-Type'], 'application/json')
            self.assertEquals(resp.json['status'], '200')
            self.assertEquals(len(resp.json['data']), 3)
            self.assertEquals(resp.json['data']['name'], 'event_duration')

    def test_404(self):
        resp = self.client.get('/404')
        self.assert404(resp)
        self.assertEquals(resp.headers['Content-Type'], 'application/json')
        self.assertEquals(resp.json['status'], '404')
        self.assertEquals(resp.json['error'], 'Not Found')


if __name__ == '__main__':
    unittest.main()
