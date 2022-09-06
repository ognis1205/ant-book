from flask_login import UserMixin
from flaskr.models.utils import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    __table_args__ = {
        'extend_existing': True
    }

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(1000))

    email = db.Column(db.String(100), unique=True)

    thumbnail = db.Column(db.Text)
