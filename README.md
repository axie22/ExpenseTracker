# Expense Tracker | Backend

## Table of Contents

- [Expense Tracker | Backend](#expense-tracker--backend)
  - [Table of Contents](#table-of-contents)
  - [Introduction ](#introduction-)
  - [Features ](#features-)
  - [Setup ](#setup-)
  - [Usage ](#usage-)
  - [Terminal Interface ](#terminal-interface-)
    - [Menu Options](#menu-options)

## Introduction <a name="introduction"></a>

The Expense Tracker is a backend system for tracking personal expenses. It allows users to sign up, log in, and manage their expenses through a secure API built using Flask and MongoDB. The app uses JSON Web Tokens (JWT) for authentication, ensuring that each user can securely manage their data. This project also features a terminal-based user interface that allows users to interact with the backend API directly.

## Features <a name="features"></a>

1. **User Authentication**: 
   - Users can sign up and log in using their email and password.
   - Passwords are securely hashed using bcrypt.
   - JWT-based authentication for secure access to API routes.

2. **Expense Management**:
   - **Add Expense**: Users can add expenses, including category and amount.
   - **View Expenses**: Users can view all their expenses with an option to filter by date.
   - **Delete Expense**: Users can delete any of their recorded expenses.
   - **Update Expense**: Users can update details of an existing expense (e.g., category, amount).

3. **State-based User Interface**:
   - The terminal interface changes its available options based on whether the user is logged in or not.
   - Logged-out users can only sign up or log in, while logged-in users can add/view expenses or sign out.

## Setup <a name="setup"></a>

1. **Create a virtual environment**

   Mac: 
   ```bash
   python3 -m venv venv
   ```

   Windows:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   Mac:
   ```bash
   source venv/bin/activate
   ```

   Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies**

   After activating the virtual environment, install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root and set the following variables:

   ```bash
   MONGODB_URI=<your_mongodb_uri>
   JWT_SECRET=<your_jwt_secret_key>
   ```

5. **Run the application**

   To start the Flask server, run the following command:

   ```bash
   python app.py
   ```

   The server will run on `http://127.0.0.1:5000` by default.

## Usage <a name="usage"></a>

Once the application is running, you can use a tool like [Postman](https://www.postman.com/) or cURL to interact with the API, or you can use the provided terminal interface to log in and manage your expenses.

- The terminal interface provides a menu-based system where you can log in, add expenses, view expenses, and more.
  
- Users must first sign up and log in to obtain a JWT token before they can perform any operations on expenses.

## Terminal Interface <a name="terminal-interface"></a>

The terminal interface allows users to interact with the Expense Tracker API without needing a web browser or other tools. 

### Menu Options

- **Sign Up**: Creates a new user account.
- **Log In**: Logs in an existing user and stores the JWT token for future requests.
- **Add Expense**: Allows the logged-in user to add a new expense by entering the category and amount.
- **View Expenses**: Displays all expenses associated with the logged-in user.
- **Sign Out**: Logs the user out by removing the stored JWT token.
- **Quit**: Exits the application.
