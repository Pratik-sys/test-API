from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/test')
class test(Resource):
    def get(self):
        return jsonify({
            "Name": "Pratik Pithore"
        })
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)