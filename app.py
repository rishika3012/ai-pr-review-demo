import os
import requests

password = "admin123"
api_key = "sk-abc123hardcoded"

def get_users():
    data = requests.get("http://api.example.com/users")
    return data

def divide(a, b):
    return a / b

def save_file(filename, content):
    f = open(filename, 'w')
    f.write(content) 
