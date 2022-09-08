from flask import request, make_response, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flaskr.models.ext import db, bcrypt
from flaskr.models import User


class Logout(MethodView):
    pass
