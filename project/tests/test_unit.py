# project/server/tests/integration/test_api.py


import os
import json
import unittest

from base import BaseTestCase

from project.server.api.utils import create_uuid, write_data

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SAMPLE_DATA = os.path.join(BASE_DIR, 'sample.json')
TEST_DATA = os.path.join(BASE_DIR, '..', 'server', 'data_test.json')


class TestUtils(BaseTestCase):

    def test_write_data(self):
        """Ensure write_data() adds data to .json file."""
        with open(TEST_DATA) as f:
            current = json.load(f)
            self.assertTrue(len(current) == 0)
        write_data(SAMPLE_DATA)
        with open(TEST_DATA) as f:
            current = json.load(f)
            self.assertTrue(len(current) == 1)

    def test_create_uuid(self):
        """Ensure uuid() is unique."""
        uuid1 = create_uuid()
        uuid2 = create_uuid()
        self.assertTrue(uuid1 is not None)
        self.assertFalse(uuid1 == uuid2)


if __name__ == '__main__':
    unittest.main()
