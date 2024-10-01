from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from auth import signup_user, login_user 
from models import create_expense, get_expenses_by_user, delete_expense, update_expense
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET')  
jwt = JWTManager(app)

# --- Auth Routes ---

@app.route('/signup', methods=['POST'])
def signup():
    """
    User signup endpoint.
    Expected JSON: {"username": "example", "email": "example@example.com", "password": "examplepass"}
    """
    data = request.get_json()

    # Pass data to signup_user function in auth.py
    result, status_code = signup_user(data['username'], data['email'], data['password'])

    return jsonify(result), status_code


@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint.
    Expected JSON: {"email": "example@example.com", "password": "examplepass"}
    """
    data = request.get_json()

    # Pass data to login_user function in auth.py
    result, status_code = login_user(data['email'], data['password'])

    return jsonify(result), status_code


# --- Expense Routes ---

@app.route('/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    """
    Create a new expense.
    Expected JSON: {"category": "groceries", "price": 50.0, "date": "2024-01-01"} (date is optional)
    """
    user_id = get_jwt_identity()  # Get the user ID from JWT token
    data = request.get_json()

    # Create expense using the create_expense function in models.py
    expense_id = create_expense(user_id, data['category'], data['amount'], data.get('date'))
    
    return jsonify({"message": "Expense added successfully!", "expense_id": str(expense_id)}), 201


@app.route('/expenses', methods=['GET'])
@jwt_required()
def get_user_expenses():
    """
    Get all expenses for the authenticated user.
    Optionally, filter by date range using query params: start_date, end_date.
    """
    user_id = get_jwt_identity()  # Get the user ID from JWT token
    
    # Retrieve expenses for the user
    expenses = get_expenses_by_user(user_id)
    
    return jsonify(expenses), 200


@app.route('/expenses/<expense_id>', methods=['DELETE'])
@jwt_required()
def delete_user_expense(expense_id):
    """
    Delete a specific expense for the authenticated user by expense_id.
    """
    user_id = get_jwt_identity()

    # Delete the expense using the delete_expense function in models.py
    result = delete_expense(expense_id)

    if result:
        return jsonify({"message": "Expense deleted successfully"}), 200
    else:
        return jsonify({"error": "Expense not found"}), 404


@app.route('/expenses/<expense_id>', methods=['PUT'])
@jwt_required()
def update_user_expense(expense_id):
    """
    Update a specific expense for the authenticated user.
    Expected JSON: {"category": "groceries", "price": 75.0}
    """
    user_id = get_jwt_identity()
    data = request.get_json()

    result = update_expense(expense_id, data)

    if result:
        return jsonify({"message": "Expense updated successfully"}), 200
    else:
        return jsonify({"error": "Expense not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
