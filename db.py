import os
from pymongo import MongoClient

def get_db():
    #Load Mongo URI from environment variables
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client['online_exam_system'] #Database name
    return db
