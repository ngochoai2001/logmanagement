from pymongo import MongoClient
from decouple import config

MONGO_URL = config("MONGO_URL")
db_connection = MongoClient(MONGO_URL)
db = db_connection.logmanagement
user_db = db['user']
logs_db = db['logs']