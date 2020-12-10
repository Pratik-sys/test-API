from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route("/test")
class test(Resource):
    def get(self):
        return jsonify(
            {
                "pan": "ANRPM2537J",
                "name": "Dinesh Kumar",
                "dob": "1990-10-25",
                "father_name": "Hari Kumar",
                "client_id": "4feb601e-2316-4dda-8d91-28c89cdb2335",
            }
        )
if __name__ == "__main__":
    app.run(debug=True, port=8080)
