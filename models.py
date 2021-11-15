from app import db
from bson import ObjectId

class Details(db.Document):
    name = db.StringField()
    password = db.StringField()
    pan = db.StringField()
    dob = db.DateField()
    father_name = db.StringField()
    client_id = db.ObjectIdField(default=ObjectId)