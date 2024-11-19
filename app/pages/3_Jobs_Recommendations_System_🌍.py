import streamlit as st
from component_job_rec import page_style
from modules.job_tab_1 import job_tab_1
import pickle
import bz2
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Apply custom page styling
page_style()

# Define the tabs
tab1, tab2 = st.tabs(["About 👋", "Job Recommender System 🌍"])

# Content for Tab 1
with tab1:
    st.title("Welcome to the Job Recommender System!")
    st.markdown("""
    This project leverages machine learning models to recommend jobs based on user input. 
    Start exploring by navigating to the 'Job Recommender System 🌍' tab.
    """)
    job_tab_1()

# Content for Tab 2
with tab2:
    st.title("Job Recommender System 🌍")

    st.markdown("""
    Find jobs tailored to your skills, preferences, and location using this interactive job recommender.
    """)

    # User Inputs
    job_title = st.text_input("Enter your desired job title", "Data Scientist")
    resume = st.text_area("Enter a brief summary of your experience", "Experienced data scientist with a PhD in statistics")
    user_location = st.selectbox("Select your preferred job location", options=["New York", "San Francisco", "Seattle"])

    if st.button("Find Jobs"):
        try:
            # Load vectorizer objects
            with open("datasets/Job_Dataset/job_desc_tfidf_vectorizer.pkl", "rb") as f:
                job_desc_tfidf = pickle.load(f)
            with open("datasets/Job_Dataset/job_title_tfidf_vectorizer.pkl", "rb") as f:
                job_title_tfidf = pickle.load(f)

            # Transform user inputs
            job_title_tfidf_user = job_title_tfidf.transform([job_title])
            job_desc_tfidf_user = job_desc_tfidf.transform([resume])

            # Load dataset
            with bz2.BZ2File('datasets/Job_Dataset/one_per_new_df.bz2', 'r') as f:
                new_df = pd.read_csv(f)

            # Rename columns for clarity
            new_df = new_df.rename(columns={
                'json.schemaOrg.title': 'Title',
                'text': 'Job Description',
                'json.schemaOrg.jobLocation.address.addressLocality': 'Location'
            })

            # Extract job features
            job_titles = new_df["Title"].values
            job_descriptions = new_df["Job Description"].values
            locations = new_df['Location'].values

            # Generate feature vectors
            job_desc_tfidf_features = job_desc_tfidf.transform(job_descriptions)
            job_title_tfidf_features = job_title_tfidf.transform(job_titles)

            # Calculate similarity scores
            job_desc_cosine_similarities = cosine_similarity(job_desc_tfidf_user, job_desc_tfidf_features)
            job_title_cosine_similarities = cosine_similarity(job_title_tfidf_user, job_title_tfidf_features)
            similarity_scores = 0.4 * job_desc_cosine_similarities + 0.4 * job_title_cosine_similarities

            # Add location as a weighted feature
            location_weight = np.zeros(len(locations))
            location_weight[locations == user_location] = 0.2
            similarity_scores += location_weight.reshape(1, -1)

            # Rank jobs by similarity score
            new_df['Similarity Score'] = similarity_scores.reshape(-1)
            top_recommendations = new_df.sort_values('Similarity Score', ascending=False).head(5)

            # Display recommendations
            st.subheader("Top 5 Job Recommendations")
            for _, row in top_recommendations.iterrows():
                st.markdown(f"**Title**: {row['Title']}")
                st.markdown(f"**Location**: {row['Location']}")
                st.markdown(f"**Description**: {row['Job Description'][:200]}...")
                st.markdown(f"**Score**: {row['Similarity Score']:.2f}")
                st.markdown("---")
        except Exception as e:
            st.error(f"An error occurred: {e}")

