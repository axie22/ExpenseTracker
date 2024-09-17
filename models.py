from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['expense_tracker']

users = db['users']  
expenses = db['expenses']

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
