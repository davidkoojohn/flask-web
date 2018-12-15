
from flask import Blueprint, render_template, flash, redirect
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, HiddenField
from wtforms.validators import DataRequired

login_view = Blueprint('login', __name__)


@login_view.route('', methods=['POST', 'GET'])
def index():
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

