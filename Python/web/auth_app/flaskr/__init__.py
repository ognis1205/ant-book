import os
from dotenv import load_dotenv
from flask import Flask
from flaskr.database import init_db


load_dotenv(override=True)

config = {
    'development':  'flaskr.config.Development',
    'testing': 'flaskr.config.Testing',
    'production': 'flaskr.config.Production',
}


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.get(os.getenv('FLASK_APP_ENV', 'development')))
    init_db(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
