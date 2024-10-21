import streamlit as st
from component import page_style

page_style()

st.title('Welcome to the Recommender Systems Project 🎉')

st.markdown("""
### Introduction
This project demonstrates two types of recommendation systems:
1. **Movie Recommender System**: Recommends movies based on the content similarity of the movie metadata.
2. **Job Recommender System**: Provides job recommendations based on various criteria from scraped job listing data.
""")

st.markdown("""
Use the sidebar to navigate between different pages:
- **Movies Recommendation** to explore the movie recommender.
- **Jobs Recommendation** to explore the job recommender.
""")
