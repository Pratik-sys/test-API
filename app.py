from flask import Flask, jsonify,request
from flask_restx import Resource, Api
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os, random, string, json
from dotenv import load_dotenv


app = Flask(__name__)
api = Api(app)
load_dotenv(".env")
app.config["MONGODB_SETTINGS"] = {"host" : os.getenv("DB_URL")}
db = MongoEngine(app)
app.config['JWT_SECRET_KEY'] = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(16))
jwt = JWTManager(app)

class Details(db.Document):
    Name = db.StringField()
    Email = db.StringField()
    PanNumber = db.StringField()
    Dob = db.DateField()
    FatherName = db.StringField()

@api.route("/login")
class LoginUser(Resource):
    def post(self):
        record = json.loads(request.data)
        try:
            user = Details.objects(Email=record["email"]).first()
            if user.Email and user.PanNumber == record["panNumber"]:
                gen_token = create_access_token(identity=user.Email)
            return jsonify({"msg": gen_token},200)
        except Exception as ex:
            print(ex)
            return jsonify({"msg": "No such user found"},500)
@api.route("/dummydata")
class DummyData(Resource):
    def post(self):
        record = json.loads(request.data)
        try:
            details = Details(
                Name = record["name"],
                Email = record["email"],
                PanNumber = record["panNumber"],
                Dob = datetime.now(),
                FatherName = record["fatherName"]
            )
            details.save()
            return jsonify({"msg" : "Dummy Data entered!"}, 201)
        except Exception as ex:
            print(ex)
            return jsonify({"msg" : "error while entering data"}, 404)
@api.route("/<string:pan_number>/details")
class GetData(Resource):
    @jwt_required()
    def get(self, pan_number:str):
        try:
            details = Details.objects(PanNumber = pan_number).first()
            if details:
                return jsonify({"msg": details},201)
            return jsonify({"msg" : "Invalid Pan Number"},500)
        except Exception as ex:
            print(ex)
            return jsonify({"msg" : "Something went wrong"}, 404)

if __name__ == "__main__":
    app.run(debug=True)

