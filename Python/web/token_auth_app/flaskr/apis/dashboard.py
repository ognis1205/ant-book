from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required


bp = Blueprint('dashboard', __name__)


@bp.route('/dashboard/welcome')
@jwt_required()
def welcome():
    return make_response(jsonify(
        message="Welcome! to the Data Science Learner"
    )), 200
