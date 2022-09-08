import pytest
from datetime import datetime
from flaskr import create_app
from flaskr.models import User
from flaskr.models.ext import db
from flaskr.config.utils import getconf


@pytest.fixture()
def app():
    app = create_app()

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_encode_auth_token(app):
    with app.app_context():
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()

        assert user.id == 1
        assert user.is_admin == False
        assert isinstance(user.registered_on, datetime) == True
