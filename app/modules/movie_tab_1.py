import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import ast
import plotly.express as px

def movies_tab_1():
    st.title('Explore Movies Tailored Just for You 🍿')

    # Overview and App Concept
    st.markdown("""
    ### Your Personalized Movie Adventure
    Dive into a curated movie experience! Our Movie Recommender System is designed to find movies you'll love based on the genres, keywords, and other metadata of films you enjoy. Just select a movie, and our AI will instantly recommend a collection of films with similar themes and styles. This app is your guide to discovering hidden gems and popular hits tailored to your taste.

    ### Features
    - **Dynamic Movie Recommendations**: Get personalized movie lists based on what you already like.
    - **Interactive Exploration**: Hover over movie posters to reveal details like release dates, popularity, revenue, and a brief overview.
    - **Data Visualization**: Explore trends in movie genres and keywords with interactive charts that provide insights into popular themes across our collection.

    """)

    # Load and Display Dataset
    movies_df = pd.read_csv('datasets/tmdb_5000_movies.csv')
    
    # Process nested columns for visualization
    movies_df['genres'] = movies_df['genres'].apply(lambda x: ', '.join([i['name'] for i in ast.literal_eval(x)]) if pd.notna(x) else '')
    movies_df['keywords'] = movies_df['keywords'].apply(lambda x: ', '.join([i['name'] for i in ast.literal_eval(x)]) if pd.notna(x) else '')

    # Display cleaned dataset
    st.write("#### Browse Our Movies Collection")
    st.dataframe(movies_df.head(50))

    # Visualize Genre Distribution
    st.markdown("### Genre Distribution")
    genre_count = movies_df['genres'].str.split(', ').explode().value_counts().reset_index()
    genre_count.columns = ['Genre', 'Count']
    fig_genre = px.bar(genre_count, x='Genre', y='Count', title='Popular Movie Genres', labels={'Genre': 'Genre', 'Count': 'Count'})
    st.plotly_chart(fig_genre)

    # Visualization: Top Keywords
    st.markdown("### Popular Keywords in Movies")
    keyword_count = movies_df['keywords'].str.split(', ').explode().value_counts().reset_index().head(20)
    keyword_count.columns = ['Keyword', 'Count']
    fig_keywords = px.bar(keyword_count, x='Keyword', y='Count', title='Top Keywords in Movies', labels={'Keyword': 'Keyword', 'Count': 'Count'})
    st.plotly_chart(fig_keywords)

    # How to Use the Movie Recommender
    st.markdown("""
    ### How It Works
    1. **Select a Movie**: In the Movie Recommender tab, choose a movie you like.
    2. **Discover Similar Movies**: Click "Show Recommendation" to reveal movies with similar themes, genres, or keywords.
    3. **Hover for Details**: Get a deeper insight into each recommendation, including an overview and additional movie metrics.
    
    Experience movies in a whole new way with tailored recommendations just for you!
    """)
