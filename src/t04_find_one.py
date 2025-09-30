from pymongo import MongoClient
client = MongoClient(); db = client["university"]; students = db["students"]

query_filter = {"name": "Kim"}

student = students.find_one(query_filter)

if student:
    print("found a student")
    print(student)
else:
    print("could not find a student with that name")