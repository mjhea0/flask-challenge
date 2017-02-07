# project/server/config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    DATA_FILE = os.path.join(BASE_DIR, 'data_dev.json')
    STATS_FILE = os.path.join(BASE_DIR, 'stats_dev.json')


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DATA_FILE = os.path.join(BASE_DIR, 'data_test.json')
    STATS_FILE = os.path.join(BASE_DIR, 'stats_test.json')


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
