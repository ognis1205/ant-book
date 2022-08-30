from flask import Blueprint, render_template
from flaskr.models import db


bp = Blueprint('auth', __name__)


@bp.route('/login')
def login():
    return render_template('auth/login.html')


@bp.route('/signup')
def signup():
    return render_template('auth/signup.html')


@bp.route('/logout')
def logout():
    return 'Logout'
