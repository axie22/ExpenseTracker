from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from bson.binary import Binary
import bcrypt
from models import users

app = Flask(__name__)
app.config.from_object('config.Config')
jwt = JWTManager(app)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": Binary(hashed_password),
        "created_at": datetime.now()
    }

    users.insert_one(user)
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.find_one({"email": data['email']})
    
    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    if not bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user['_id']))
    return jsonify(access_token=access_token), 200
