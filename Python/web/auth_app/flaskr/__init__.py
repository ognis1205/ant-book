import os
from dotenv import load_dotenv
from flask import Flask
from flaskr.models import init_db


load_dotenv(override=True)

config = {
    'development':  'flaskr.config.Development',
    'testing': 'flaskr.config.Testing',
    'production': 'flaskr.config.Production',
}


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder='static',
        template_folder='templates',
    )
    app.config.from_object(config.get(os.getenv('FLASK_APP_ENV', 'development')))
    init_db(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr.routers.auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from flaskr.routers.main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
