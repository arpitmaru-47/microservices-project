from flask import Flask
from pymongo import MongoClient
import os 

app = Flask(__name__)

mongo_host = os.getenv("MONGO_HOST", "mongodb")
mongo_port = 27017 

client = MongoClient(
    f"mongodb://admin:password@{mongo_host}:27017/"
)
db = client["mydb"]
collection = db["users"]

@app.route("/")
def home():
    return "Flask Backend is Running!"

@app.route("/add")
def add():
    collection.insert_one({"name": "Appi"})
    return "User Added Successfully"

@app.route("/users")
def users():
    data = list(collection.find({}, {"_id": 0}))
    return data 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)