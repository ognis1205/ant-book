import os
from flask import Flask, g, session
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
from flaskr.models import User
from flaskr.config.utils import get_env, get_conf
from flaskr.models.utils import init_db


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder='static',
        template_folder='templates',
    )
    app.config.from_object(
        get_conf(get_env('FLASK_APP_ENV', default='development'))
    )


    login_manager = LoginManager()
    login_manager.init_app(app)

    init_db(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        g.oauth_client = WebApplicationClient(GOOGLE_CLIENT_ID)

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True

    return app
