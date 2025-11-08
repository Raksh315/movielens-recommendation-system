import pandas as pd

# Column names for movies (u.item)
movie_columns = [
    'movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url',
    'unknown','Action','Adventure','Animation','Children','Comedy','Crime','Documentary',
    'Drama','Fantasy','FilmNoir','Horror','Musical','Mystery','Romance','SciFi',
    'Thriller','War','Western'
]

# Read the MovieLens data files
movies_df = pd.read_csv("u.item", sep='|', names=movie_columns, encoding='latin-1')
ratings_df = pd.read_csv("u.data", sep="\t", names=['user_id','movie_id','rating','timestamp'])
users_df = pd.read_csv("u.user", sep="|", names=['user_id','age','gender','occupation','zip_code'])

# Create user-item ratings matrix
ratings_matrix = ratings_df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

# Print to check
print("Movies DataFrame:")
print(movies_df.head())
print("\nRatings DataFrame:")
print(ratings_df.head())
print("\nUsers DataFrame:")
print(users_df.head())
print("\nRatings Matrix:")
print(ratings_matrix.head())

# Save ratings matrix and movies DataFrame for later use
ratings_matrix.to_csv("ratings_matrix.csv")
movies_df.to_csv("movies_df.csv", index=False)

print("Matrices saved: ratings_matrix.csv and movies_df.csv")
