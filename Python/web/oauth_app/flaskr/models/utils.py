from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def close_db(app):
    db.session.close()
    if engine := db.get_engine(app):
        engine.dispose()


def init_db(app):
    db.init_app(app)
