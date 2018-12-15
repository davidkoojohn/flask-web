
from flask import Blueprint, render_template

landing_view = Blueprint('landing', __name__)


@landing_view.route('')
def index():
    return render_template('landing.html', name='davidkoojohn')
