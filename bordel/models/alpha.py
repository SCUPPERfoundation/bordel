from sqlalchemy.dialects.postgresql import JSONB

from .. import db

class ReviewDoc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blob = db.Column(JSONB)
