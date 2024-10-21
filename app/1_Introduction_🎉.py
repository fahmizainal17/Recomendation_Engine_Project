import streamlit as st
from component import page_style
import streamlit.components.v1 as components
import pandas as pd
import json
import ast
import plotly.express as px

page_style()

st.title('Welcome to the Recommender Systems Project 🎉')

# Adding an interactive dataset visualization and diagrams
st.markdown("""
### Introduction
Welcome to our Recommender Systems Project! Here you will explore two amazing types of recommendation systems:

1. **Movie Recommender System**: Our AI-powered movie recommender uses the content similarity of movie metadata to find your next favorite movie! Dive into a world of personalized movie recommendations based on what you like.

2. **Job Recommender System**: Looking for the perfect job? Our job recommender provides you with job opportunities that best match your profile, scraped from the web. It helps you discover roles you are most likely to succeed in.

The navigation bar on the left allows you to explore both of these recommendation systems.
- **Movies Recommendation**: Learn more about how our movie recommendation works and get a list of movies tailored to your taste.
- **Jobs Recommendation**: Understand how jobs are recommended and explore the different job opportunities curated just for you.

### Features of Our Recommender System
- **Interactive Movie Exploration**: Hover over movie posters to see additional information, including release date, popularity, and more.
- **User-Friendly Interface**: Intuitive and simple layout that makes exploring recommendations easy and fun.
- **Real-Time Data**: Using real-time data to provide up-to-date information.

### Interactive Dataset Exploration
Below is an interactive view of the dataset used for building the recommendation system. You can filter, sort, and explore the data visually.
""")

# Load sample dataset for visualization
movies_df = pd.read_csv('datasets/tmdb_5000_movies.csv')

# Cleaning the dataset by flattening nested JSON-like columns
# Convert 'genres' column from stringified JSON to list of genre names
movies_df['genres'] = movies_df['genres'].apply(lambda x: ', '.join([i['name'] for i in ast.literal_eval(x)]) if pd.notna(x) else '')

# Convert 'keywords' column from stringified JSON to list of keyword names
movies_df['keywords'] = movies_df['keywords'].apply(lambda x: ', '.join([i['name'] for i in ast.literal_eval(x)]) if pd.notna(x) else '')

# Display cleaned dataset using Streamlit's data frame viewer
st.write("#### Movies Dataset Overview (Cleaned)")
st.dataframe(movies_df.head(50))

# Adding visualization diagram
st.markdown("""
### Understanding the Dataset
Below are some visual diagrams that will help you understand the key features of the dataset.
""")

# Create an interactive bar chart for movie genres
genre_count = movies_df['genres'].str.split(', ').explode().value_counts().reset_index()
genre_count.columns = ['Genre', 'Count']
fig_genre = px.bar(genre_count, x='Genre', y='Count', title='Movie Genres Distribution', labels={'Genre': 'Genre', 'Count': 'Count'})
st.plotly_chart(fig_genre)

# Adding documentation and tutorial for the fundamentals of recommendation systems
st.markdown("""
### Documentation
**Recommender Systems Fundamentals**

This project is designed to help you understand the fundamentals of recommendation systems. Here's what we'll cover:
1. **Content-Based Filtering**: This approach uses the content of the items (e.g., movie metadata) to make recommendations. Our movie recommender system uses this technique by analyzing the similarities in features like genre, actors, and directors.

2. **Collaborative Filtering**: Though not implemented in this version, collaborative filtering is another popular technique. It uses user behavior to recommend items that similar users enjoyed.

3. **Hybrid Approaches**: Many advanced recommender systems use a hybrid approach that combines both content-based and collaborative filtering.

**How to Use the Movie Recommender**
1. Use the sidebar to navigate to the Movie Recommender page.
2. Select a movie that you like from the dropdown menu.
3. Click on 'Show Recommendation' to get a list of recommended movies similar to your selection.
4. Hover over any movie to see additional details such as the overview, release date, and revenue.

**How to Use the Job Recommender**
1. Navigate to the Job Recommender page via the sidebar.
2. Enter your job preferences and experience details.
3. Get recommendations that are tailored to your job profile.

### Learn More
For those who want to go deeper into the technicalities of recommendation systems, we will soon release detailed notebooks and explanations on collaborative filtering, hybrid models, and even neural network-based recommenders!

Stay tuned!
""")
