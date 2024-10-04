import requests
import json
import os

BASE_URL = "http://127.0.0.1:5000"
TOKEN_FILE = "token.txt" 

def save_token(token):
    """Save JWT token to a file."""
    with open(TOKEN_FILE, 'w') as f:
        f.write(token)

def load_token():
    """Load the JWT token from a file."""
    try:
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def signup():
    """Sign up a new user."""
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    data = {"username": username, "email": email, "password": password}
    response = requests.post(f"{BASE_URL}/signup", json=data)

    if response.status_code == 201:
        print("Sign-up successful!")
    else:
        print("Error:", response.json())

def login():
    """Log in a user."""
    email = input("Enter email: ")
    password = input("Enter password: ")

    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/login", json=data)

    if response.status_code == 200:
        token = response.json()["access_token"]
        save_token(token)
        print("Login successful!")
    else:
        print("Error:", response.json())

def add_expense():
    token = load_token()
    category = input("Enter category (e.g., groceries, electronics, etc.): ")
    price = input("Enter amount: ")
    headers = {"Authorization": f"Bearer {token}"}
    data = {"category": category, "amount": price}
    response = requests.post(f"{BASE_URL}/expenses", json=data, headers=headers)
    
    print("Status Code:", response.status_code)
    if response.status_code == 201:
        print("Expense added successfully:")
    else:
        print("Error:", response.text)

def get_expenses():
    """Retrieve all user expenses."""
    token = load_token()
    if not token:
        print("Please log in first.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/expenses", headers=headers)

    if response.status_code == 200:
        expenses = response.json()
        print("Your Expenses:")
        for expense in expenses:
            print(f"- {expense['category']}: ${expense['amount']} (Date: {expense['date']})")
    else:
        print("Error:", response.json())

def is_logged_in():
    """Check if the user is logged in by verifying the existence of a saved token."""
    token = load_token()
    return token is not None

def logout():
    """Log the user out by deleting the saved token."""
    try:
        os.remove(TOKEN_FILE)
        print("You have been logged out.")
    except FileNotFoundError:
        print("No active session found.")

def main():
    """Main terminal interface."""
    while True:
        if is_logged_in():
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Logout")
        else:
            print("\nExpense Tracker")
            print("1. Sign Up")
            print("2. Log in")

        choice = input("Select an option: ")

        if is_logged_in():
            if choice == "1":
                add_expense()
            elif choice == "2":
                get_expenses()
            elif choice == "3":
                logout()
            else:
                print("Invalid option. Please try again.")
        else:
            if choice == "1":
                signup()
            elif choice == "2":
                login()
            else:
                print("Invalid Option. Try again")

if __name__ == "__main__":
    main()
