from pymongo import MongoClient
client = MongoClient()


db = client["university"]

students_collection = db["students"]

new_student = {
    "name": "Kim",
    "module" : "COM517",
    "year": 4,
    "enrolled": True
}
result = students_collection.insert_one(new_student)
print(f"Sucessfully created a new student with id {result.inserted_id}")