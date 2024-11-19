import streamlit as st
import pandas as pd
import plotly.express as px

def job_tab_1():
    st.title('Explore Job Opportunities Tailored Just for You 🌍')

    # Overview and App Concept
    st.markdown("""
    ### Your Personalized Job Search Companion
    Welcome to our Job Recommender System! This platform is designed to connect you with job opportunities based on your skills, preferences, and location. Whether you're actively job-hunting or exploring options, our AI-powered recommender system ensures you're presented with jobs tailored to your profile.

    ### Features
    - **Dynamic Job Recommendations**: Get personalized job suggestions based on your resume and desired job title.
    - **Interactive Exploration**: Search for jobs by title, description, or location to discover opportunities that resonate with you.
    - **Data Visualization**: Gain insights into popular job titles, skills in demand, and location trends with interactive charts.

    """)

    # Load and Display Dataset
    jobs_df = pd.read_csv('datasets/Job_Dataset/one_per_new_df.bz2', compression='bz2')
    
    # Rename columns for clarity
    jobs_df = jobs_df.rename(columns={
        'json.schemaOrg.title': 'Title',
        'text': 'Job Description',
        'json.schemaOrg.jobLocation.address.addressLocality': 'Location'
    })

    # Display cleaned dataset
    st.write("#### Browse Job Listings (Sample Data)")
    st.dataframe(jobs_df[['Title', 'Location', 'Job Description']].head(50))

    # Visualize Job Titles
    st.markdown("### Popular Job Titles")
    title_count = jobs_df['Title'].value_counts().reset_index().head(20)
    title_count.columns = ['Job Title', 'Count']
    fig_titles = px.bar(
        title_count, 
        x='Job Title', 
        y='Count', 
        title='Most Frequent Job Titles in Listings', 
        labels={'Job Title': 'Job Title', 'Count': 'Count'},
        color_discrete_sequence=["#008080"]
    )
    st.plotly_chart(fig_titles)

    # Visualize Location Distribution
    st.markdown("### Job Locations")
    location_count = jobs_df['Location'].value_counts().reset_index().head(20)
    location_count.columns = ['Location', 'Count']
    fig_locations = px.bar(
        location_count, 
        x='Location', 
        y='Count', 
        title='Top Locations for Job Listings', 
        labels={'Location': 'Location', 'Count': 'Count'},
        color_discrete_sequence=["#008080"]
    )
    st.plotly_chart(fig_locations)

    # How to Use the Job Recommender
    st.markdown("""
    ### How It Works
    1. **Enter Your Details**: In the Job Recommender tab, input your desired job title and a summary of your skills.
    2. **Get Recommendations**: Click "Find Jobs" to see the best matches for you.
    3. **Discover Opportunities**: Explore jobs by title, location, and description to find your next career move.
    
    Start your job search journey with recommendations designed for you!
    """)
