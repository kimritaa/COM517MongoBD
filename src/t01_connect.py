from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


client = MongoClient("mongodb://localhost:27017/")

try:
    # The ismaster command is cheap and does not require auth.
    client.admin.command("ping")
    print("Sucess! : You are connected to MongoDB")
except ConnectionFailure:
    print("Failure! : Could not connect to MongoDB server")