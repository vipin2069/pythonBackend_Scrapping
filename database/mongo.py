from pymongo import MongoClient
from config import API_KEY

# Replace with your MongoDB connection details
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Define MongoDB collections
db = client['mydatabase']
users_collection = db['users']
posts_collection = db['posts']
