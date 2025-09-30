from pymongo import MongoClient
client = MongoClient(); db = client["university"]; students = db["students"]

filter_gte = {"year": {"$gte": 2}}

print(f" --- All students in year 2 or above --- ")
for student in students.find(filter_gte):
    print(f"- {student['name']} is in year {student['year']}")