from pymongo import MongoClient


db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.logmanagement
user_db = db['user']
logs_db = db['logs']