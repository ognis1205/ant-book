from datetime import datetime, timedelta
from flaskr.models.ext import db


class Blacklist(db.Model):
    __tablename__ = 'blacklist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    token = db.Column(db.String(500), unique=True, nullable=False)

    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.registered_on = datetime.now()

    @staticmethod
    def check(token):
        return True if Blacklist.query.filter_by(token=token).first() else False
