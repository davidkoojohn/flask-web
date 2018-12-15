
from flask import Flask, render_template, flash, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, HiddenField
from wtforms.validators import DataRequired


from config import DevConfig

app = Flask(__name__)
db = SQLAlchemy(app)


def create_app():
    app.config.from_object(DevConfig)

    return app


@app.route('/')
def index():
    return render_template('index.html', name='koo')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' +
              form.openid.data + '", remember_me='
              + str(form.remember_me.data))
        form.openid.data = ''
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


class LoginForm(Form):
    hidden_tag = HiddenField()
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


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
