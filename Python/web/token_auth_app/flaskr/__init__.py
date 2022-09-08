from flask import Flask
from flaskr.config.utils import getenv, getconf


def create_app():
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates',
    )

    app.config.from_object(
        getconf(getenv('FLASK_APP_ENV', default='development'))
    )

    from flaskr.apis.ext import cors
    cors.init_app(app)

    from flaskr.models.ext import db, bcrypt, migrate
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    return app
