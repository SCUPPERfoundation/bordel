from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.ext.mutable import MutableDict

from .. import db

class ReviewDoc(db.model)
    id = db.Column(db.Integer, primary_key=True)
    blob = db.Column(MutableDict.as_mutable(HSTORE))
