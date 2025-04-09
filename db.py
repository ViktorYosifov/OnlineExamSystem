import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:")
    print(e)
