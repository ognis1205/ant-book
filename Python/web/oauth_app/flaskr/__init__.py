import os
from datetime import timedelta
from flask import Flask, g, session
from flask_login import LoginManager
from werkzeug import serving
from flaskr.models import User
from flaskr.config.utils import getenv, config


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder='static',
        template_folder='templates',
    )

    app.config.from_object(
        config(getenv('FLASK_APP_ENV', default='development'))
    )

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr.oauth.ext import oauth, login_manager
    oauth.init_app(app)
    login_manager.init_app(app)

    from flaskr.models.ext import db
    db.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

    from flaskr.routers.main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    from flaskr.routers.auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
