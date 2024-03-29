from flask import Blueprint, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
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
        id = userinfo.get('sub')
        email = userinfo.get('email')
        picture = userinfo.get('picture')
        name = userinfo.get('given_name')
    else:
        return 'User email not available or not verified by Google.', 400

    user = User(
        id=id, name=name, email=email, thumbnail=picture
    )

    if not User.query.get(id):
        db.session.add(user)
        db.session.commit()

    login_user(user)

    return redirect(url_for('main.index'))


@bp.route('/logout')
@login_required
def logout():
    user = User.query.get(current_user.get_id())
    logout_user()
    db.session.delete(user)
    db.session.commit()
    session.clear()
    return redirect(url_for('main.index'))
