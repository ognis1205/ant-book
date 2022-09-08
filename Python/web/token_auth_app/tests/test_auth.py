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


def test_register(client):
    with client:
        resp = _register_user(client, 'john@gmail.com', 'password')
        data = json.loads(resp.data.decode())

        assert data['status'] == 'success'
        assert data['message'] == 'Successfully registered.'
        assert data['access_token']
        assert resp.content_type == 'application/json'
        assert resp.status_code == 201


def test_register_with_already_registered_user(app, client):
    with app.app_context():
        user = User(
            email='john@gmail.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()

    with client:
        resp = _register_user(client, 'john@gmail.com', 'password')
        data = json.loads(resp.data.decode())

        assert data['status'] == 'fail'
        assert data['message'] == 'User already exists. Please Log in.'
        assert resp.content_type == 'application/json'
        assert resp.status_code == 409


def test_registered_user_login(client):
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


def test_non_registered_user_login(client):
    with client:
        resp = _login_user(client, 'john@gmail.com', 'password')
        data = json.loads(resp.data.decode())

        assert data['status'] == 'fail'
        assert data['message'] == 'User does not exist.'
        assert resp.content_type == 'application/json'
        assert resp.status_code == 404


def test_valid_logout(client):
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

        resp = client.post(
            '/auth/logout',
            headers=dict(
                Authorization='Bearer ' + json.loads(resp.data.decode())['access_token']
            )
        )
        data = json.loads(resp.data.decode())

        assert data['status'] == 'success'
        assert data['message'] == 'Successfully logged out.'
        assert resp.status_code == 200


def test_invalid_logout(client):
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

        time.sleep(6)
        resp = client.post(
            '/auth/logout',
            headers=dict(
                Authorization='Bearer ' + json.loads(resp.data.decode())['access_token']
            )
        )
        data = json.loads(resp.data.decode())

        assert data['status'] == 'fail'
        assert data['message'] == 'ExpiredSignatureError, Signature has expired'
        assert resp.status_code == 401
