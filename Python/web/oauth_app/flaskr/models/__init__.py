from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy


def get_db():
    if 'db' not in g:
        g.db = SQLAlchemy()
    return g.db
