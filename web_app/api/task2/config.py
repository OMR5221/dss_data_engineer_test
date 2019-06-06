import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    SQLALCHEMY_TRACK_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class QAConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_URI = os.environ.get('DATABASE_TEST_URL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProdConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_URL')


app_config = {
    'dev': DevConfig,
    'qa': QAConfig,
    'prod': ProdConfig,
}
