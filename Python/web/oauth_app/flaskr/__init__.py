import os
from flask import Flask
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

    init_db(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
