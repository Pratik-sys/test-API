from app import db
from bson import ObjectId

class Details(db.Document):
    Name = db.StringField()
    Eamil = db.StringFiled()
    PanNumber = db.StringField()
    Dob = db.DateField()
    FatherName = db.StringField()
    ClientID = db.ObjectIdField(default=ObjectId)