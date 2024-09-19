from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)
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

def delete_expense(expense_id):
    """Delete an expense by its ID."""
    return expenses.delete_one({"_id": ObjectId(expense_id)})

def get_expenses_by_user(user_id, filter_query=None):
    query = {"user_id": ObjectId(user_id)}
    if filter_query:
        query.update(filter_query)
    return query

def update_expense(expense_id, updated_data):
    """Update an existing expense."""
    return expenses.update_one(
        {"_id": ObjectId(expense_id)},
        {"$set": updated_data}
    )