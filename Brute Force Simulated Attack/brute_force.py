import requests
import time
import random

url = "http://127.0.0.1:5001"

users = ["admin", "test", "user", "guest", "root"]
passwords = ["123", "password", "admin", "test123", "wrong", "letmein"]

while True:
    user = random.choice(users)
    pwd = random.choice(passwords)

    try:
        requests.post(url, data={"user": user, "pass": pwd})
        print(f"Attempted: {user}:{pwd}")
    except Exception as e:
        print(e)

    time.sleep(1)
