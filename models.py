from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['expense_tracker']

users = db['users']  
expenses = db['expenses']

def create_user(username, email, hash_password):
    """
    Create a new user with a username, eamil, and hashed password
    Return the id of the newly inserted value
    """
    user = {
        "username": username,
        "email": email,
        "password": hash_password,
        "created_at": datetime.now()
    }
    return users.insert_one(user).inserted_id

def delete_user(user_id):
    """
    Delete the user using the user_id
    Return 1 if succesful, 0 otherwise
    """
    return users.delete_one({"_id": ObjectId(user_id)})


def find_username(email):
    """Find the username given the email address and return it"""
    return users.find_one({"email": email})

def create_expense(user_id, category, price, date=None):
    """Create an expense given a user id
    Categorize it and also add the price and date of purchase
    Return the id of the inserted element
    """
    expense = {
        "user_id": user_id, 
        "amount": price,
        "category": category,
        "date": date if date else datetime.now()
    }
    return expenses.insert_one(expense).inserted_id

def delete_expense(user_id, category, price):
    """Delete an expense using a given user_id? Or should we use the inserted_id
    """
    return expenses.delete_one({""})
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