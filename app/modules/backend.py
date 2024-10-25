import streamlit as st
import pickle
import requests
from component import page_style
import pandas as pd
import json
import ast
import plotly.express as px

# Function to fetch movie poster URL
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url).json()
    poster_path = response.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return None

# Function to shorten the overview to a maximum of 22 words
def shorten_overview(overview, max_words=22):
    words = overview.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + "..."
    return overview

# Function to fetch additional movie details for the hover pop-up
def fetch_metrics_for_hover(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    # Extracting details to display in hover pop-up
    overview = data.get("overview", "N/A")
    shortened_overview = shorten_overview(overview) if overview != "N/A" else "N/A"
    return {
        "Movie Name": data.get("original_title", "N/A"),
        "Overview": shortened_overview,
        "Popularity": data.get("popularity", "N/A"),
        "Vote Average": data.get("vote_average", "N/A"),
        "Revenue": data.get("revenue", "N/A"),
        "Release Date": data.get("release_date", "N/A"),
        "Adult": "Yes" if data.get("adult") else "No"
    }

# Recommendation function to get movie details
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_ids = []
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:16]:  # Fetch top 15 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_ids.append(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_ids, recommended_movie_names, recommended_movie_posters