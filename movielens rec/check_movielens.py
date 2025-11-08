from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the movielens database
db = client["movielens"]

# List all collections
print("Collections:", db.list_collection_names())

# Check one document from each collection
print("Sample movie:", db.movies.find_one())
print("Sample rating:", db.ratings.find_one())
print("Sample user:", db.users.find_one())
