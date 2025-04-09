import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
def get_db():
    # Get the MongoDB URI from the environment variable
    mongo_uri = os.getenv('MONGO_URI')

    if not mongo_uri:
        raise ValueError("Mongo URI is missing in .env file")

    # Connect to the MongoDB Atlas cluster
    client = MongoClient(mongo_uri)
    db = client['OnlineExamSystem']
    return db
