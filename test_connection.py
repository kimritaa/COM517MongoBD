from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient('localhost', 27017)

try:
    client.admin.command('ping')
    print("Connection is working")
except ConnectionFailure:
    print("Connection failed")