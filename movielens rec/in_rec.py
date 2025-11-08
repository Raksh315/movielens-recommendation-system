# fuzzy_movie_recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# -----------------------------
# Step 1: Load and clean raw data
# -----------------------------
movies_columns = [
    "movie_id", "title", "release_date", "video_release_date", "imdb_url",
    "unknown","Action","Adventure","Animation","Children","Comedy","Crime","Documentary",
    "Drama","Fantasy","FilmNoir","Horror","Musical","Mystery","Romance","SciFi",
    "Thriller","War","Western"
]

movies_df = pd.read_csv("u.item", sep="|", encoding="latin-1", header=None, names=movies_columns, usecols=range(len(movies_columns)))

ratings_df = pd.read_csv("u.data", sep="\t", header=None, names=["user_id","movie_id","rating","timestamp"])

print("Movies and ratings loaded successfully!")

# -----------------------------
# Step 2: Create user-movie ratings matrix
# -----------------------------
ratings_matrix = ratings_df.pivot(index="user_id", columns="movie_id", values="rating").fillna(0)

# -----------------------------
# Step 3: Compute item-item similarity
# -----------------------------
movie_user_matrix = ratings_matrix.T
item_similarity = pd.DataFrame(cosine_similarity(movie_user_matrix),
                               index=movie_user_matrix.index,
                               columns=movie_user_matrix.index)

print("Item similarity matrix computed!")

# -----------------------------
# Step 4: Recommendation by fuzzy movie title
# -----------------------------
def recommend_by_title(movie_input, top_n=5):
    # Fuzzy match movie titles
    all_titles = movies_df['title'].tolist()
    matches = get_close_matches(movie_input, all_titles, n=3, cutoff=0.4)

    if not matches:
        print(f"No movie found matching '{movie_input}'. Try again.")
        return

    # If multiple close matches, let user select
    if len(matches) > 1:
        print("Multiple matches found:")
        for i, title in enumerate(matches):
            print(f"{i+1}. {title}")
        choice = input("Select the correct movie number (or '0' to cancel): ")
        if choice == '0':
            return
        try:
            matched_title = matches[int(choice)-1]
        except:
            print("Invalid choice.")
            return
    else:
        matched_title = matches[0]

    movie_id = movies_df.loc[movies_df['title'] == matched_title, 'movie_id'].values[0]

    sim_scores = item_similarity[movie_id].sort_values(ascending=False)
    sim_scores = sim_scores.drop(movie_id)  # exclude itself
    top_movies = sim_scores.head(top_n).index

    print(f"\nTop {top_n} movies similar to '{matched_title}':")
    print(movies_df[movies_df['movie_id'].isin(top_movies)][["title"]])

# -----------------------------
# Step 5: Interactive loop
# -----------------------------
while True:
    user_input = input("\nEnter a movie name (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    recommend_by_title(user_input)
