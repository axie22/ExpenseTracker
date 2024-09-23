from flask import Flask, request, jsonify
from models import create_user, find_username
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
def signup_user(username, email, password):
    # Check if the user already exists
    if find_username(email):
        return {"error": "User already exists"}, 409 
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_id = create_user(username, email, hashed_password)
    
    return {"message": "User registered successfully!", "user_id": str(user_id)}, 201

@app.route('/login', methods=['POST'])
def login_user(email, password):
    user = find_username(email)
    if not user:
        return {"error": "Invalid email or password"}, 401

    if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return {"error": "Invalid email or password"}, 401

    access_token = create_access_token(identity=str(user['_id']))

    return {"access_token": access_token}, 200