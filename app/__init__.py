
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

from config import config, DevConfig

app = Flask(__name__)
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from views import landing_view, login_view

    app.register_blueprint(landing_view, url_prefix='/')
    app.register_blueprint(login_view, url_prefix='/login')

    return app


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __init__(self, name):
        self.username = name

    def __repr__(self):
        return '<Role %r>' % self.name
