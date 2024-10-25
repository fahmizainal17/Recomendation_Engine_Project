import pickle
import streamlit as st
import requests
from component import page_style
import streamlit.components.v1 as components
from modules.backend import fetch_poster, shorten_overview, shorten_overview, recommend
from modules.movie_tab_1 import movies_tab_1

# Apply the page style using a function from your components module
page_style()

# Load movie list and similarity matrix from pickle files
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Define the tabs
tab1, tab2 = st.tabs(["About👋", "Movies Recommendation App🍿"])

# Content for Tab 1
with tab1:
    movies_tab_1()

# Content for Tab 2
with tab2:
    st.title('Movie Recommender System Using Machine Learning 🍿')
    st.markdown("<style>div.stButton > button {color: white; background-color: #ff6347; border-radius: 8px;}</style>", unsafe_allow_html=True)

    # Dropdown to select a movie
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    # Show recommendations when button is clicked
    if st.button('Show Recommendation'):
        recommended_movie_ids, recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        num_recommendations = 15  # Total recommendations to display
        cols_per_row = 5

        # Loop to display recommended movie posters
        for row in range(0, num_recommendations, cols_per_row):
            cols = st.columns(cols_per_row, gap="small")
            for i, col in enumerate(cols):
                index = row + i
                if index < num_recommendations:
                    with col:
                        # Fetch movie details for hover
                        movie_id = recommended_movie_ids[index]
                        poster_url = recommended_movie_posters[index]
                        movie_details = fetch_metrics_for_hover(movie_id)

                        # Prepare the HTML for the movie poster with expanded hover pop-up
                        html_string = f'''
                        <div class="movie-container">
                            <img src="{poster_url}" alt="{recommended_movie_names[index]}" class="movie-poster">
                            <div class="hover-info">
                                <h3>{movie_details['Movie Name']}</h3>
                                <p><strong>Overview:</strong> {movie_details['Overview']}</p>
                                <p><strong>Popularity:</strong> {movie_details['Popularity']}</p>
                                <p><strong>Vote Average:</strong> {movie_details['Vote Average']}</p>
                                <p><strong>Revenue:</strong> ${movie_details['Revenue']:,}</p>
                                <p><strong>Release Date:</strong> {movie_details['Release Date']}</p>
                                <p><strong>Adult Content:</strong> {movie_details['Adult']}</p>
                            </div>
                        </div>
                        <style>
                            .movie-container {{
                                position: relative;
                                display: inline-block;
                                cursor: pointer;
                                margin: 0;
                            }}
                            .movie-poster {{
                                width: 100%;
                                border-radius: 15px;
                                transition: transform 0.3s ease, box-shadow 0.3s ease;
                            }}
                            .movie-container:hover .movie-poster {{
                                transform: scale(1.05);
                                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
                            }}
                            .hover-info {{
                                position: absolute;
                                top: 0;
                                left: 0;
                                width: 100%;
                                min-height: 100%;
                                background: rgba(34, 34, 34, 0.95);
                                color: white;
                                opacity: 0;
                                transition: opacity 0.4s ease;
                                padding: 15px;
                                overflow-y: auto;
                                border-radius: 15px;
                                text-align: left;
                            }}
                            .movie-container:hover .hover-info {{
                                opacity: 1;
                            }}
                            .hover-info h3 {{
                                margin-top: 0;
                                font-family: 'Arial', sans-serif;
                            }}
                            .hover-info p {{
                                margin-bottom: 8px;
                                line-height: 1.5;
                                font-size: 0.9em;
                            }}
                        </style>
                        '''
                        
                        # Render the HTML with components.html()
                        components.html(html_string, height=400)
