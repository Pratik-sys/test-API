from flask import Flask, jsonify, make_response, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'ce93c0d66f7ea57ff4c6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db' # set the congif where you want to save the db 
app.config["MONGODB_SETTINGS"] = {"db": "myapp"}
db = MongoEngine(app)
app.config['JWT_SECRET_KEY'] = 'secrete-key'  
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pan = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    father_name = db.Column(db.String(60), nullable=False)
    client_id = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f'{self.pan}, {self.name},{self.father_name},{self.client_id}'

class Details(db.Document):
    pan = db.StringField(unquie=True, required=True)
    name = db.StringField(unquie=True, required=True)
    dob = db.DateField()
    father_name = db.StringField()
    client_id = db.StringField()

# data = Details( 
#     pan = "RTUNNHMJ890", 
#     name = "green", 
#     dob ="1889-10-07", 
#     father_name="star",
#     client_id="77uikilo-yhybvft-juygjh-vrhtt-hthtthh"
#     )
# data.save()
# print("done")
# data = Details( 
#     pan = "YHNMKIOL0908", 
#     name = "rock", 
#     dob ="2000-10-07", 
#     father_name="lee",
#     client_id="uimik87-uhgbuyj-989bgyv-ikm90opl"
#     )
# data.save()
# print("done")

@app.route('/login', methods=['POST','GET'])
def login():
    items = Details.objects.all()
    username = request.json.get('username')
    print(username)
    password = request.json.get('password')
    for item in items:
        if username == item.name:
            print(item.name)
            access_token = create_access_token(identity=username)
        else:
            return jsonify({"msg": "Invalid  user "})
    return jsonify({"access_token":access_token},200)

@api.route("/<string:pan_number>")
class GetData(Resource):
    @jwt_required
    def get(self, pan_number):
        retrive = Details.objects()
        for i in retrive:
            if pan_number != i.pan:
                return jsonify({"msg": "Error, no such pan in the database"},403)
            else:
                return jsonify({
                    "pan": i.pan,
                    "name": i.name,
                    "dob":i.dob.strftime("%Y-%m-%d"),
                    "father_name": i.father_name,
                    "client_id": i.client_id
                }, 201)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

