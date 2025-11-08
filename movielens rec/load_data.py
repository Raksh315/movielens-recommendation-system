import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["movielens"]

# Load collections into DataFrames
movies_df = pd.DataFrame(list(db.movies.find()))
ratings_df = pd.DataFrame(list(db.ratings.find()))
users_df = pd.DataFrame(list(db.users.find()))

# Drop MongoDB's automatic _id column (optional)
movies_df.drop(columns=['_id'], inplace=True)
ratings_df.drop(columns=['_id'], inplace=True)
users_df.drop(columns=['_id'], inplace=True)

# Print first 5 rows to verify
print("Movies DataFrame:\n", movies_df.head())
print("\nRatings DataFrame:\n", ratings_df.head())
print("\nUsers DataFrame:\n", users_df.head())
