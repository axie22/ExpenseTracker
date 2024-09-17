from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['expense_tracker']

users = db['users']  
expenses = db['expenses']

def create_user(username, email, hash_password):
    user = {
        "username": username,
        "email": email,
        "password": hash_password,
        "created_at": datetime.now()
    }
    return users.insert_one(user).inserted_id

def delete_user(user_id):
    # returns 1 if successful, 0 otherwise
    return users.delete_one({"_id": ObjectId(user_id)})

def find_username(email):
    return users.find_one({"email": email})

'''

users.insert_one({
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "hashed_password",
    "created_at": datetime.now()
})

expenses.insert_one({
    "user_id": "mongo_user_id",
    "amount": 50.0,
    "category": "Groceries",
    "date": datetime.now(),
})

'''