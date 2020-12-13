from flask import Flask, jsonify, make_response, request
from flask_restx import Resource, Api
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity

app = Flask(__name__)
api = Api(app)
app.config["MONGODB_SETTINGS"] = {"db": "myapp"}
db = MongoEngine(app)
app.config['JWT_SECRET_KEY'] = 'secrete-key'  
jwt = JWTManager(app)

class Details(db.Document):
    pan = db.StringField()
    name = db.StringField()
    dob = db.DateField()
    father_name = db.StringField()
    client_id = db.StringField()

    def to_json(self):
        return{
            "pan": self.pan,
            "name": self.name,
            "dob": self.dob,
            "father_name": self.father_name,
            "client_id": self.client_id
            }
# data = Details( 
#     pan = "ANRPM2537J", 
#     name = "Dinesh Kumar", 
#     dob ="1990-10-25", 
#     father_name="Hari Kumar",
#     client_id="4feb601e-2316-4dda-8d91-28c89cdb2335"
#     )
# data.save()
# print("done")

@app.route('/login', methods=['POST','GET'])
def login():
    items = Details.objects()
    username = request.json.get('username')
    password = request.json.get('password')
    for item in items:
        if username == item.name:
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

