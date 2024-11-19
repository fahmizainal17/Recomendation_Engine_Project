import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_synthetic_jobs_data():
    """Load the synthetic job postings dataset."""
    try:
        jobs_df = pd.read_csv("datasets/Job_Dataset/Synthetic_Job_Postings_Data.csv")
        return jobs_df
    except Exception as e:
        st.error(f"Error loading synthetic job postings data: {e}")
        return None


def visualize_data(data, column, title, x_label, y_label, color="#008080"):
    """Generate a bar chart for data visualization."""
    data_count = data[column].value_counts().reset_index().head(20)
    data_count.columns = [x_label, y_label]
    fig = px.bar(
        data_count,
        x=x_label,
        y=y_label,
        title=title,
        labels={x_label: x_label, y_label: y_label},
        color_discrete_sequence=[color],
    )
    st.plotly_chart(fig)


def job_tab_1():
    """Tab 1 for exploring job opportunities."""
    st.title("Explore Job Opportunities Tailored Just for You 🌍")

    # Sidebar customization
    st.sidebar.markdown("### Visualization Options")
    color = st.sidebar.color_picker("Choose chart color", value="#008080")

    # Overview of the app
    st.markdown("""
    ### Personalized Job Search Companion
    Explore job listings tailored to your preferences.
    """)

    # Load synthetic jobs data
    with st.spinner("Loading job postings..."):
        jobs_df = load_synthetic_jobs_data()

    if jobs_df is not None:
        # Display the dataset
        st.write("#### Sample Job Listings")
        st.dataframe(jobs_df.head(50))

        # Visualize job title and location distributions
        visualize_data(
            jobs_df,
            column="Job Title",
            title="Popular Job Types",
            x_label="Job Title",
            y_label="Count",
            color=color
        )
        visualize_data(
            jobs_df,
            column="Location",
            title="Top Job Locations",
            x_label="Location",
            y_label="Count",
            color=color
        )
    else:
        st.error("Failed to load job postings.")
