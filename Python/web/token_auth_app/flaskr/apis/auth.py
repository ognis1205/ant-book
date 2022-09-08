from flask import Blueprint
from flaskr.auth import Login, Logout, Register


bp = Blueprint('auth', __name__)

bp.add_url_rule(
    '/auth/register',
    view_func=Register.as_view('register'),
    methods=['POST']
)

bp.add_url_rule(
    '/auth/login',
    view_func=Login.as_view('login'),
    methods=['POST']
)

bp.add_url_rule(
    '/auth/logout',
    view_func=Logout.as_view('logout'),
    methods=['POST']
)
