from pymongo import MongoClient
client = MongoClient(); db = client["university"]; students = db["students"]

projection = {"name" : 1, "year": 1, "_id": 0}

print("--- Student Roster (name and year only) ---")
for student in students.find({}, projection):
    print(student)