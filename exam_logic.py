from db import get_db

# MongoDB collections
db = get_db()
exams_collection = db['exams']

# Example function to store exam results
def store_exam_result(user_id, score):
    exams_collection.insert_one({
        "user_id": user_id,
        "score": score,
        "exam_taken_at": time.time()
    })
