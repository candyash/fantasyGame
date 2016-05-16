import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\xbb\xed\x0e?\xcfY#8Ev\x17\x04t\x15\xa4*****************'
    USER_PER_PAGE = 20
    S3_LOCATION = 'http://ec2-52-25-146-234.us-west-2.compute.amazonaws.com/'
    S3_KEY = 'AKIAIY24N4J6SXZDDJOQ'
    S3_SECRET = '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'
    S3_UPLOAD_DIRECTORY = 'upload-picture.s3-website-us-west-2.amazonaws.com'
    S3_BUCKET = 'upload-picture'
    ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])

    if os.environ.get('DATABASE_URL') is None:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql+psycopg2://ashenafi:Uno12mazurca@localhost/fantacygame')
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

        SQLALCHEMY_RECORD_QUERIES = True
    ##print SQLALCHEMY_DATABASE_URI


class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG=False



class HerokuConfig(ProductionConfig):
    def init_app(cls,app):
        ProductionConfig.init_app(app)
        import logging
        from logging import StreamHandler
        file_handler=StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku':HerokuConfig,

    'default': DevelopmentConfig
}
