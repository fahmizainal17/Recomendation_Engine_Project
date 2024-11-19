import streamlit as st
from component_job_rec import page_style

page_style()

st.title('Job Recommender System 🌍')

st.markdown("""
This page will feature a job recommender system that scrapes job listings from various platforms, and provides personalized job recommendations based on user inputs.
""")

# Placeholder content until recommendation logic is ready
st.write("Job recommendation system coming soon!")

# Add placeholders for user input and job recommendations
job_title_input = st.text_input("Enter a job title to get recommendations:")
if job_title_input:
    st.write(f"Showing recommendations for: {job_title_input}")
    # Recommendation logic will go here in the future
