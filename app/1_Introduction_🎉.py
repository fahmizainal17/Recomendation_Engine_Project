import streamlit as st
from component import page_style

# Apply the page style
page_style()

# Project Title
st.title('Recommender Systems: From Basics to Advanced 🎉')

# Radio for navigating different sections
nav = st.radio("Explore different sections:", ['Introduction', 'Fundamentals of Recommender Systems', 'Advanced Techniques'])

# Introduction Section
if nav == 'Introduction':
    st.markdown("""
    ### Introduction to Recommender Systems
    Recommender systems play a pivotal role in personalizing user experiences across various platforms, from online shopping to content streaming. These systems aim to suggest relevant items to users by analyzing their preferences and behaviors, improving both user satisfaction and platform engagement.

    In this project, we dive deep into the world of recommender systems, covering foundational concepts as well as advanced techniques that are used to enhance recommendation accuracy and relevance. Whether you're new to recommender systems or looking to advance your understanding, this project provides a structured guide to mastering the topic.

    Navigate through the sections to explore both fundamental and advanced aspects of recommendation engines!
    """)

# Fundamentals Section
elif nav == 'Fundamentals of Recommender Systems':
    st.markdown("""
    ### Fundamentals of Recommender Systems
    Recommender systems are broadly classified into different types based on the methods they use to suggest items. Let’s explore the key approaches:

    1. **Content-Based Filtering**:
       - **How it works**: Recommends items based on the features of the items a user has interacted with. For example, in a movie recommender system, if a user likes action movies, the system will recommend other action movies based on the genre, actors, or directors.
       - **Advantages**: Doesn't rely on the preferences of other users, making it highly personalized.
       - **Challenges**: Limited by the available features of the items and doesn’t consider the broader tastes of similar users.

    2. **Collaborative Filtering**:
       - **How it works**: Recommends items based on the interactions of similar users (user-based) or similar items (item-based). It leverages the collective behaviors of users and finds patterns in how users interact with items.
       - **Advantages**: Can discover hidden patterns and recommend items outside the scope of the content’s features.
       - **Challenges**: Cold start problem for new users or items with no interaction history.

    3. **Hybrid Approaches**:
       - **How it works**: Combines both content-based and collaborative filtering methods for more accurate recommendations. This approach is commonly used in platforms like Netflix, which suggests content by analyzing both the user’s past preferences and patterns of similar users.
       - **Advantages**: Mitigates the drawbacks of both methods by leveraging the strengths of each.
       - **Challenges**: Increased computational complexity and requires more sophisticated algorithms to balance the two approaches.
    """)

# Advanced Techniques Section
elif nav == 'Advanced Techniques':
    st.markdown("""
    ### Advanced Techniques in Recommender Systems
    As recommender systems evolve, advanced techniques have been developed to increase accuracy, personalization, and the ability to handle massive data sets. Here are some of the advanced methods used in state-of-the-art recommendation engines:

    1. **Matrix Factorization**:
       - **How it works**: This method decomposes the user-item interaction matrix into lower-dimensional latent factors that represent hidden patterns in the data. By discovering latent relationships, matrix factorization allows for more accurate recommendations, even with sparse data.
       - **Common Techniques**: Singular Value Decomposition (SVD), Alternating Least Squares (ALS).
       - **Applications**: Widely used in collaborative filtering, especially in platforms like Amazon and Netflix.

    2. **Deep Learning Models**:
       - **Neural Collaborative Filtering**: Leverages neural networks to learn complex interaction patterns between users and items, enhancing the performance of traditional collaborative filtering models.
       - **Autoencoders**: A type of neural network used for dimensionality reduction, which can be applied to create latent representations of users and items for recommendation purposes.
       - **Recurrent Neural Networks (RNNs)**: Used for sequential data to capture the temporal dynamics in user preferences, such as the order in which users watch movies or listen to songs.
       - **Applications**: Deep learning models are used by platforms that need to process vast amounts of data and make real-time recommendations.

    3. **Context-Aware Recommender Systems**:
       - **How it works**: Considers additional contextual information like time, location, and even the device being used to make recommendations. For example, a restaurant recommender might suggest different places for breakfast, lunch, and dinner based on the time of day.
       - **Advantages**: Offers more relevant and situationally aware suggestions, enhancing user satisfaction.
       - **Challenges**: Requires more data collection and analysis, which can increase the system’s complexity and the need for real-time data processing.

    4. **Real-Time Recommendation Engines**:
       - **How it works**: These systems process user data and provide recommendations in real-time, often leveraging stream processing techniques. Real-time systems adjust recommendations based on the most recent interactions a user has had with the platform.
       - **Applications**: Streaming services, e-commerce platforms, and social media all utilize real-time recommendation systems to provide up-to-date suggestions.
       - **Challenges**: Requires efficient algorithms that can handle both the scale and speed of incoming data while maintaining accurate predictions.

    **Next Steps**:
    - Explore advanced hybrid techniques and deep learning models to create more complex and intelligent recommendation engines.
    - Experiment with different approaches to find the best recommendation strategy for your specific domain.
    """)
