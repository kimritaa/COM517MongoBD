from pymongo import MongoClient
client = MongoClient(); db = client["university"]; students = db["students"]


cursor = students.find({})

print(" --- All students in the collection --- ")
for student_document in cursor:
    print(student_document)