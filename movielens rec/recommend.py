# recommend.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 1️⃣ Load the saved matrices
ratings_matrix = pd.read_csv("ratings_matrix.csv", index_col=0)  # users × movies
movies_df = pd.read_csv("movies_df.csv")

# 2️⃣ Transpose to get movies × users for item-item similarity
movie_user_matrix = ratings_matrix.T

# 3️⃣ Compute cosine similarity between movies
movie_similarity = cosine_similarity(movie_user_matrix)
movie_similarity_df = pd.DataFrame(
    movie_similarity, 
    index=movies_df['movie_id'], 
    columns=movies_df['movie_id']
)

# 4️⃣ Function to get top N similar movies
def get_similar_movies(movie_id, top_n=5):
    if movie_id not in movie_similarity_df.index:
        return f"Movie ID {movie_id} not found."
    
    sim_scores = movie_similarity_df[movie_id].sort_values(ascending=False)
    sim_scores = sim_scores.drop(movie_id)  # remove itself
    top_movies = sim_scores.head(top_n).index.tolist()
    
    # Get movie titles
    return movies_df[movies_df['movie_id'].isin(top_movies)][['movie_id', 'title']]

# 5️⃣ Example usage
example_movie_id = 76
print(f"Top 5 movies similar to Movie ID {example_movie_id}:")
print(get_similar_movies(example_movie_id))
