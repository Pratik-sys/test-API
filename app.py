from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_mongoengine import MongoEngine
import datetime
app = Flask(__name__)
api = Api(app)
app.config["MONGODB_SETTINGS"] = {"db": "myapp"}
db = MongoEngine(app)

class Details(db.Document):
    pan = db.StringField(required=True)
    name = db.StringField(required=True)
    dob = db.StringField(required=True)
    father_name = db.StringField(required=True)

# add = Details( pan = "ANRPM2537J", name = "Dinesh Kumar", dob ="1990-10-25", father_name="Hari Kumar"
# )
# add.save()
# print("done")

@api.route("/<string:pan_number>")
class Test(Resource):
    def get(self, pan_number):
         collect = Details.objects()
         for c in collect:
            if pan_number == c.pan :
                return jsonify(
                    {
                        "pan": c.pan,
                        "name": c.name,
                        "dob": c.dob,
                        "father_name": c.father_name,
                        "client_id": "4feb601e-2316-4dda-8d91-28c89cdb2335",
                    }
                )
            else:
                return jsonify({'message': 'error occured'})
if __name__ == "__main__":
    app.run(debug=True, port=8080)
