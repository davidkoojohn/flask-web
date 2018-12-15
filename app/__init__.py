
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from config import DevConfig

app = Flask(__name__)
db = SQLAlchemy(app)


def create_app():
    app.config.from_object(DevConfig)

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


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column('user_name', db.String(255))
    username = db.Column(db.String(64), unique=True, index=True)
    # password = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username
