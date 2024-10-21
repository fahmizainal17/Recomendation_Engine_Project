import pickle
import streamlit as st
import requests
from component import page_style
import streamlit.components.v1 as components

# Apply the page style using a function from your components module
page_style()

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

# Streamlit app title
st.title('Movie Recommender System Using Machine Learning 🍿')
st.markdown(
    "<style>div.stButton > button {color: black; background-color: #FFEA00; border-radius: 8px;}</style>", 
    unsafe_allow_html=True
)

# Load movie list and similarity matrix from pickle files
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

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
