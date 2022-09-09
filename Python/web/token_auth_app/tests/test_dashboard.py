import json
import time
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


def _request_dashboard(client, access_token=None):
    if access_token:
        return client.get(
            '/dashboard/welcome',
            headers=dict(
                Authorization='Bearer ' + access_token
            )
        )
    return client.get('/dashboard/welcome')


def test_authorized_request(client):
    with client:
        resp = _register_user(client, 'john@gmail.com', 'password')
        data = json.loads(resp.data.decode())

        assert data['status'] == 'success'
        assert data['message'] == 'Successfully registered.'
        assert data['access_token']
        assert resp.content_type == 'application/json'
        assert resp.status_code == 201

        resp = _login_user(client, 'john@gmail.com', 'password')
        data = json.loads(resp.data.decode())

        assert data['status'] == 'success'
        assert data['message'] == 'Successfully logged in.'
        assert data['access_token']
        assert resp.content_type == 'application/json'
        assert resp.status_code == 200

        resp = _request_dashboard(client, data['access_token'])
        data = json.loads(resp.data.decode())

        assert data['message'] == 'Welcome! to the Data Science Learner'
        assert resp.content_type == 'application/json'
        assert resp.status_code == 200


def test_unauthorized_request(client):
    with client:
        resp = _request_dashboard(client)
        data = json.loads(resp.data.decode())

        assert data['msg'] == 'Missing Authorization Header'
        assert resp.content_type == 'application/json'
        assert resp.status_code == 401
