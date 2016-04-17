import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\xbb\xed\x0e?\xcfY#8Ev\x17\x04t\x15\xa4*****************'
    USER_PER_PAGE = 3
    if os.environ.get('DATABASE_URL') is None:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql+psycopg2://ashenafi:Uno12mazurca@localhost/fantacygame')
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

        SQLALCHEMY_RECORD_QUERIES = True


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG=False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
