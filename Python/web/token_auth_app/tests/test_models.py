import pytest
from datetime import datetime
from flaskr import create_app
from flaskr.models import User, Blacklist
from flaskr.models.ext import db


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


def test_user(app):
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


def test_blacklist(app):
    with app.app_context():
        blacklist = Blacklist(
            token='token',
        )
        db.session.add(blacklist)
        db.session.commit()

        assert blacklist.id == 1
        assert blacklist.token == 'token'
        assert isinstance(blacklist.registered_on, datetime) == True
        assert Blacklist.check('token') == True
