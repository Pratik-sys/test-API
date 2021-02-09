from flask import Flask, jsonify, make_response, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'ce93c0d66f7ea57ff4c6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pan.db' # set the congif where you want to save the db 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'secrete-key'  
jwt = JWTManager(app)

class Pan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pan = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    father_name = db.Column(db.String(60), nullable=False)
    client_id = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'{self.pan}, {self.name},{self.father_name},{self.client_id}'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.username}'

@app.route('/add', methods=['POST','GET'])
def add():
    pan = request.json.get('pan')
    name = request.json.get('name')
    father_name = request.json.get('father_name')
    client_id = request.json.get('client_id')
    details = Pan(pan=pan, name=name , father_name=father_name, client_id=client_id)
    db.session.add(details)
    db.session.commit()
    return jsonify({"msg": "details added"})

@app.route('/signup', methods=['POST','GET'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username,password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg":"user added"},200)

@app.route('/login', methods=['POST','GET'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password,password):
        access_token = create_access_token(identity=username)
    else:
        return jsonify({"msg": "Invalid  user "})
    return jsonify({"access_token":access_token},200)

@api.route("/<string:pan_number>")
class GetData(Resource):
    @jwt_required
    def get(self, pan_number):
        details = Pan.query.filter_by(pan=pan_number).first()
        try:
            if details.pan == pan_number:
                return  jsonify({
                "pan": details.pan,
                "name": details.name,
                "father_name": details.father_name,
                "client_id": details.client_id
                }, 201)
        except:
            return jsonify({"msg":"error"})

if __name__ == "__main__":
    app.run(debug=True, port=8080)


