import json
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


def _register_user(client, email, password):
    return client.post(
        '/auth/register',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )


def _login_user(client, email, password):
    return client.post(
        '/auth/login',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )


def test_register(client):
    with client:
        resp = _register_user(client, 'john@gmail.com', 'password')
        data = json.loads(resp.data.decode())

        assert data['status'] == 'success'
        assert data['message'] == 'Successfully registered.'
        assert data['access_token']
        assert resp.content_type == 'application/json'
        assert resp.status_code, 201
