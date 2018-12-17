import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_MIGRATE_REPO = SQLALCHEMY_MIGRATE_REPO
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True,
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = 'flask-web'
    FLASKY_MAIL_SENDER = 'Flask Admin <davidkoojohn@163.com>'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'data.sqlite'))


class DevConfig(Config):
    DEBUG = True
    CSRF_ENABLED = True
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'data-test.sqlite'))


config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'production': ProdConfig,
    'default': DevConfig
}
