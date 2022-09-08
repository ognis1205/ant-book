from re import split
from flask import request, make_response, jsonify
from flask.views import MethodView
from flask_jwt_extended import decode_token
from flaskr.models.ext import db, bcrypt
from flaskr.models import Blacklist


class Logout(MethodView):
    def post(self):
        header = request.headers.get('Authorization')

        if token := split('\s+', header) if header else None:
            try:
                _ = decode_token(token)
                blacklist = Blacklist(token=token)
                db.session.add(blacklist)
                db.session.commit()
                return make_response(jsonify(
                    status='success',
                    message='Successfully logged out.'
                )), 200
            except Exception as e:
                return make_response(jsonify(
                    status='fail',
                    message=f'{type(e).__name__}, {e}',
                )), 200

        return make_response(jsonify(
            status='fail',
            message='Provide a valid auth token.'
        )), 403
