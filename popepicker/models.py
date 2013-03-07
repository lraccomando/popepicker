import datetime
from popepicker import db


class Pope(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    photo = db.StringField(max_length=255, required=True)
    name = db.StringField(max_length=255, required=True)
    country = db.StringField(max_length=255, required=True)
    DOB = db.StringField(max_length=255, required=True)
    age = db.StringField(max_length=16, required=True)
    bio = db.StringField(max_length=255, required=False)
    rank = db.IntField(required=True, default=0)

    meta = {
        'indexes': ['-created_at', 'rank'],
        'ordering': ['rank']
    }
