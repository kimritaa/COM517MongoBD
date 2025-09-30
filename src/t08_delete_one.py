from pymongo import MongoClient
client = MongoClient(); db = client["university"]; students = db["students"]

delete_filter = {"name":"Kim"}
result = students.delete_one(delete_filter)

print(f"Deleted {result.deleted_count} document(s) matching the filter {delete_filter}")