from pymongo import MongoClient
client = MongoClient(); db = client["university"]; students = db["students"]

student_filter = {"name":"Kim"}

update_action = {"$set":{"year":2}, "$set":{"login_count":1}}

result = students.update_one(student_filter, update_action)

print(f"Documents matched: {result.matched_count}, Documents modified: {result.modified_count}")