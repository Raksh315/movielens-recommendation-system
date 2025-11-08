# MovieLens Recommendation System 🎬

## About this project

This project is a **Movie Recommendation System** built using the **MovieLens 100K dataset**, **Python**, and **MongoDB**.  
It allows users to get personalized movie recommendations using **item-based collaborative filtering**, providing an interactive experience where users can search by movie name.

---

## Features

- Store MovieLens data in MongoDB
- Load and process data using Python and Pandas
- Create a user-item rating matrix for recommendations
- Interactive recommendations by movie name

---

## Project Structure

movielens-recommendation-system/
│
├─ check_movielens.py      # Inspect data in MongoDB
├─ create_matrix.py        # Build user-item ratings matrix
├─ in_rec.py               # Interactive recommendation system
├─ load_data.py            # Load CSVs into Python
├─ recommend.py            # Recommend movies by movie ID
├─ movies.csv              # Cleaned movie dataset
├─ ratings_matrix.csv      # User-item rating matrix
└─ README.md               # Project description

---

## Getting Started

### Prerequisites

- Python 3.x  
- MongoDB (optional if using CSVs only)

### Install Dependencies

pip install pandas pymongo

### How to Run

1. Load data into Python:
python load_data.py

2. Create the ratings matrix:
python create_matrix.py

3. Recommend movies by ID:
python recommend.py

4. Get interactive recommendations by movie name:
python in_rec.py

---

## Dataset

MovieLens 100K dataset includes:  

- u.item → Movie information  
- u.data → User ratings  
- u.user → User information  

---

## Key Learnings

- Data cleaning and preprocessing are essential  
- MongoDB is useful for storing data, but Pandas simplifies data analysis  
- Item-based collaborative filtering is a simple and effective recommendation approach  
- User-friendly interactive input improves system usability

---

