from flask import Flask
from flaskr.config.utils import getenv, getconf


def create_app():
    app = Flask(__name__)

    app.config.from_object(
        getconf(getenv('FLASK_APP_ENV', default='dev'))
    )

    from flaskr.apis.ext import cors
    cors.init_app(app)

    from flaskr.auth.ext import jwt
    jwt.init_app(app)

    from flaskr.models.ext import db, bcrypt, migrate
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from flaskr.apis.auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
