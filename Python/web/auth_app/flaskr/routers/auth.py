import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flaskr.models import db
from flaskr.models.user import User


bp = Blueprint('auth', __name__)


@bp.route('/login')
def login():
    return render_template('auth/login.html')


@bp.route('/signup')
def signup():
    return render_template('auth/signup.html')


@bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method='sha256'),
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    session.permanent = True

    return redirect(url_for('main.profile'))
