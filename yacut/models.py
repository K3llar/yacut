from datetime import datetime

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text(), nullable=False, index=True)
    short = db.Column(db.String(128), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime,
                          default=datetime.utcnow())
