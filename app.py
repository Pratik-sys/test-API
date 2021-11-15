from flask import Flask, jsonify, make_response, request
from flask_restx import Resource, Api
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
import os, random, string
from dotenv import load_dotenv
from models import Details


app = Flask(__name__)
api = Api(app)
load_dotenv(".env")
app.config["MONGODB_SETTINGS"] = {"host" : os.getenv("URI")}
db = MongoEngine(app)
app.config['JWT_SECRET_KEY'] = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(16))
jwt = JWTManager(app)

@api.route("/login")
class LoginUser(Resource):
    def post():
        try:
            pass
        except:
            pass

@api.route("/dummydata")
class DummyData(Resource):
    def post():
        try: 
            pass
        except: 
            pass
@api.route("/<string:pan_number>")
class GetData(Resource):
    @jwt_required
    def get(self, pan_number):
        try:
            pass
        except:
            pass


if __name__ == "__main__":
    app.run(debug=True, port=8080)

