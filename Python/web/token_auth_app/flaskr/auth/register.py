from flask import request, make_response, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flaskr.models.ext import db
from flaskr.models import User


class Register(MethodView):
    def post(self):
        json = request.get_json()
        email = json.get('email')
        password = json.get('password')

        if user := User.query.filter_by(email=email).first():
            return make_response(jsonify(
                status='fail',
                message='User already exists. Please Log in.',
            )), 409

        try:
            user = User(
                email=email,
                password=password,
            )
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify(
                status='success',
                message='Successfully registered.',
                access_token=create_access_token(identity=email),
            )), 201
        except Exception as e:
            return make_response(jsonify(
                status='fail',
                message='Some error occurred. Please try again.',
            )), 401
