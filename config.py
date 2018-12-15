import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')


class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_MIGRATE_REPO = SQLALCHEMY_MIGRATE_REPO
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
