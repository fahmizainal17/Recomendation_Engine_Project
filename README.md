# **🎥 Recommendation Engine Project** [![wakatime](https://wakatime.com/badge/user/ae82a943-125e-489a-a656-e35fe84d587b/project/9ebf50ae-2f3d-47d3-ac24-6fc2598ab3e2.svg)](https://wakatime.com/badge/user/ae82a943-125e-489a-a656-e35fe84d587b/project/9ebf50ae-2f3d-47d3-ac24-6fc2598ab3e2)

<!-- Badge to Visit Project -->
<div align="center"> 
    <a href="https://recommendation-engine-project.streamlit.app/">
        <img src="https://img.shields.io/badge/Visit%20Recommendation%20Engine%20Project-brightgreen?style=for-the-badge&logo=streamlit" alt="Visit Recommendation Engine Project"/>
    </a>
</div>

---

## **📋 Overview**

The **Recommendation Engine Project** is a Streamlit-based web application that demonstrates the implementation of **content-based filtering** for recommendation systems. It showcases two key applications:  
- 🎥 **Movie Recommender System**: Recommends movies based on metadata such as genres, cast, and directors.  
- 🌍 **Job Recommender System**: Recommends jobs by analyzing textual features like job descriptions and titles.  

This project highlights the power of data-driven recommendations and provides an interactive way to explore content-based recommendation systems.

---

## **Table of Contents**

1. [🎯 Objectives](#-objectives)  
2. [🔧 Technologies Used](#-technologies-used)  
3. [🗂️ Directory Structure](#-directory-structure)  
4. [📁 Features](#-features)  
5. [🔄 Project Workflow](#-project-workflow)  
6. [🎉 Conclusion](#-conclusion)  
7. [📚 References](#-references)  
8. [📜 License](#-license)  

---

## **🎯 Objectives**

- Build an interactive platform to demonstrate **content-based filtering** in real-world applications.  
- Provide a hands-on experience for users to explore recommendation results dynamically.  
- Use metadata and textual data effectively for generating recommendations.  

---

## **🔧 Technologies Used**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)  

Other libraries:
- Pandas  
- Scikit-learn  
- Numpy  

---

## **🗂️ Directory Structure**

```plaintext
.
├── LICENSE
├── README.md
├── app
│   ├── 1_Introduction_🎉.py
│   ├── component.py
│   ├── pages
│       ├── 2_Movies_Recommendation_System_🍿.py
│       └── 3_Jobs_Recommendations_System_🌍.py
├── artifacts
│   ├── movie_list.pkl
│   └── similarity.pkl.gz
├── assets
│   ├── Job_Recommender_Background.png
│   ├── movie_background.jpg
├── datasets
│   ├── tmdb_5000_credits.csv
│   ├── tmdb_5000_movies.csv
│   ├── Synthetic_Job_Postings_Data.csv
│   └── Synthetic_Resumes_Data.csv
└── requirements.txt
```

---

## **📁 Features**

### 1. 🎥 Movie Recommender System
- Uses **content-based filtering**.  
- Recommends movies by analyzing metadata (e.g., genres, directors, cast).  
- Allows users to select a movie and receive similar recommendations.  

### 2. 🌍 Job Recommender System
- Based on **TF-IDF vectorization** of job titles and descriptions.  
- Provides job recommendations tailored to user input.  

---

## **🔄 Project Workflow**

1. **📂 Environment Setup**:
   - Install dependencies using `requirements.txt`.  

2. **🔍 Data Processing**:
   - Process datasets (TMDb movies, synthetic job postings) for feature extraction.  

3. **🧠 Model Development**:
   - Create similarity matrices using content-based techniques like cosine similarity and TF-IDF.  

4. **🚀 Web App Development**:
   - Build dynamic dashboards using Streamlit for both recommendation systems.  

5. **🌐 Deployment**:
   - Deploy the app using Streamlit's cloud services.  

---

## **🎉 Conclusion**

This project demonstrates how **content-based filtering** can be applied effectively in different domains like movies and jobs. The interactive application enables users to explore recommendations dynamically and learn about the underlying algorithms.  

---

## **📚 References**

- [Streamlit Documentation](https://docs.streamlit.io/)  
- [TMDb API Documentation](https://developers.themoviedb.org/3)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  

---

## **📜 License**

**Fahmi Zainal Custom License**  
Unauthorized copying, distribution, or modification of this project is prohibited. For inquiries, contact the project owner.