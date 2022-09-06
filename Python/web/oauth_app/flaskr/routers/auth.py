from flask import Blueprint, redirect, url_for
from flask_login import login_user, logout_user
from flaskr.models import User
from flaskr.oauth.ext import redirect_authorize, get_userinfo, external_url_for
from flaskr.models.ext import db


bp = Blueprint('auth', __name__)


@bp.route('/login')
def login():
    return redirect_authorize(
        external_url_for('auth.callback', _external=True, _scheme='https')
    )


@bp.route('/login/callback')
def callback():
    userinfo = get_userinfo()

    if userinfo.get('email_verified'):
        unique_id = userinfo.get('sub')
        users_email = userinfo.get('email')
        picture = userinfo.get('picture')
        users_name = userinfo.get('given_name')
    else:
        return 'User email not available or not verified by Google.', 400

    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    if not User.query.get(int(unique_id)):
        db.session.add(user)
        db.session.commit()

    login_user(user)

    return redirect(url_for('main.index'))
