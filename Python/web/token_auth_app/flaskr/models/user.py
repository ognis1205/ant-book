from datetime import datetime, timedelta
from flask import current_app
from flaskr.models.ext import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    __table_args__ = {
        'extend_existing': True
    }

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(255), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    registered_on = db.Column(db.DateTime, nullable=False)

    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password,
            current_app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.now()
        self.is_admin = is_admin
