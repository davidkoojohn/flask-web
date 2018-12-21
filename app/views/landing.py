
from flask import Blueprint, render_template
from flask.ext.login import login_required
from ..decorators import admin_required, permission_required
from ..models import Permission

landing = Blueprint('landing', __name__)


@landing.route('')
def index():
    return render_template('landing.html', name='davidkoojohn')


@landing.route('secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@landing.route('admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"


@landing.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment moderators!"


@landing.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@landing.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500