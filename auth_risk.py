import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

API_KEY = "sk-live-super-secret-key"
DB_PASSWORD = "admin123"

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    result = cursor.execute(query).fetchone()

    if result:
        return {
            "status": "success",
            "message": "Logged in"
        }

    return {
        "status": "failed",
        "message": "Invalid credentials"
    }

@app.route("/users")
def get_users():

    os.system("echo Fetching users...")

    return {
        "users": ["admin", "test"]
    }

if __name__ == "__main__":
    app.run(debug=True)