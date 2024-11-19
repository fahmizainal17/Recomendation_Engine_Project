import streamlit as st
from modules.job_tab_1 import job_tab_1
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from component_job_rec import page_style
from modules.text import text

page_style()

@st.cache_data
def load_synthetic_jobs_data():
    """Load synthetic job postings dataset."""
    return pd.read_csv("datasets/Job_Dataset/Synthetic_Job_Postings_Data.csv")


@st.cache_data
def load_vectorizers():
    """Load the pickled vectorizers."""
    with open("datasets/Job_Dataset/job_title_tfidf_vectorizer.pkl", "rb") as f:
        job_title_tfidf = pickle.load(f)
    with open("datasets/Job_Dataset/job_desc_tfidf_vectorizer.pkl", "rb") as f:
        job_desc_tfidf = pickle.load(f)
    return job_title_tfidf, job_desc_tfidf


def job_recommender_tab():
    """Tab for job recommendations."""
    st.title("Job Recommender System 🌍")
    st.markdown("Find jobs tailored to your skills and location.")

    # User inputs
    job_title = st.text_input("Enter your desired job title", "Data Analyst")
    resume = st.text_area("Enter a brief summary of your experience", text)
    user_location = st.selectbox("Select your preferred job location", ["Singapore","Kuala Lumpur, Malaysia", "George Town, Malaysia", "Shah Alam, Malaysia","Kuching, Malaysia","Seria, Brunei"])
    location_weight = st.slider("Location Weight", 0.0, 1.0, 0.2)

    if st.button("Find Jobs"):
        try:
            # Load data and vectorizers
            jobs_df = load_synthetic_jobs_data()
            job_title_tfidf, job_desc_tfidf = load_vectorizers()

            # Transform user inputs
            job_title_tfidf_user = job_title_tfidf.transform([job_title])
            job_desc_tfidf_user = job_desc_tfidf.transform([resume])

            # Transform job postings
            job_titles = jobs_df["Job Title"].values
            job_descriptions = jobs_df["Job Description"].values
            locations = jobs_df["Location"].values

            job_desc_tfidf_features = job_desc_tfidf.transform(job_descriptions)
            job_title_tfidf_features = job_title_tfidf.transform(job_titles)

            # Calculate similarity scores
            job_desc_sim = cosine_similarity(job_desc_tfidf_user, job_desc_tfidf_features)
            job_title_sim = cosine_similarity(job_title_tfidf_user, job_title_tfidf_features)

            location_weight_vector = (locations == user_location).astype(float) * location_weight
            similarity_scores = 0.4 * job_desc_sim + 0.4 * job_title_sim + location_weight_vector.reshape(1, -1)

            # Rank jobs by similarity score
            jobs_df["Similarity Score"] = similarity_scores.flatten()
            top_recommendations = jobs_df.nlargest(5, "Similarity Score")

            # Display top recommendations
            st.subheader("Top 5 Job Recommendations")
            
            # Select and display relevant columns in the DataFrame
            recommendation_df = top_recommendations[["Job Title", "Location", "Job Description", "Similarity Score"]]
            recommendation_df["Job Description"] = recommendation_df["Job Description"].str.slice(0, 200) + "..."
            
            # Show the DataFrame in Streamlit
            st.dataframe(recommendation_df)

        except Exception as e:
            st.error(f"An error occurred: {e}")


# Define the tabs
tab1, tab2 = st.tabs(["Explore Jobs 👋", "Job Recommender 🌍"])

# Tab 1: Job Exploration
with tab1:
    job_tab_1()

# Tab 2: Job Recommendations
with tab2:
    job_recommender_tab()
