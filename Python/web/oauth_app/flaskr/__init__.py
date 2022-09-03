import os
from flask import Flask
from flaskr.config import getenv, getconf
from flaskr.models import get_db


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder='static',
        template_folder='templates',
    )

    app.config.from_object(getconf(getenv('FLASK_APP_ENV')))
    with app.app_context():
        db = get_db()
        db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
