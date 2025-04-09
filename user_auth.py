from db import get_db
import bcrypt

# MongoDB collections
db = get_db()
users_collection = db['users']

# Registration logic
def register_user(username, password):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert into the database
    users_collection.insert_one({"username": username, "password": hashed_password})

# Login logic
def login_user(username, password):
    user = users_collection.find_one({"username": username})
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return user  # Successfully logged in
    else:
        return None  # Invalid credentials
