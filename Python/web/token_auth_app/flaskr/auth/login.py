from flask import request, make_response, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flaskr.models.ext import db, bcrypt
from flaskr.models import User


class Login(MethodView):
    def post(self):
        json = request.get_json()
        email = json.get('email')
        password = json.get('password')

        if user := User.query.filter_by(email=email).first():
            try:
                if bcrypt.check_password_hash(user.password, password):
                    return make_response(jsonify(
                        status='success',
                        message='Successfully logged in.',
                        access_token=create_access_token(identity=email),
                    )), 200
                return make_response(jsonify(
                    status='fail',
                    message='Invalid password.'
                )), 404
            except Exception as e:
                return make_response(jsonify(
                    status='fail',
                    message='Try again.'
                )), 500

        return make_response(jsonify(
            status='fail',
            message='User does not exist.',
        )), 404
