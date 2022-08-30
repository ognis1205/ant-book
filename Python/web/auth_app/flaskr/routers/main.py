from flask import Blueprint, render_template
from flaskr.models import db


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/profile')
def profile():
    return 'Profile'
