# 🎬 Movie Recommendation and Search 🔍

This repository contains a web application that allows users to search for movies, filter results based on various criteria, and explore movie details. The app is built using **Streamlit** and the **IMDb Cinemagoer** library.

## 📚 Table of Contents

- [✨ Features](#features)
- [🚀 Demo](#demo)
- [🛠️ Installation](#installation)
- [📝 Usage](#usage)
- [🧰 Technologies Used](#technologies-used)
- [🙏 Acknowledgments](#acknowledgments)
- [🤝 Connect with Me](#connect-with-me)

---

## ✨ Features

- 🔍 **Search for Movies** by title.
- 🎛️ **Filter Results** based on:
  - **Rating Range** (0.0 to 10.0).
  - **Release Year** range.
  - **Genre** (e.g., Action, Comedy, Drama, etc.).
  - **Country of Origin** (e.g., USA, UK, India, etc.).
  - **Language** (e.g., English, Tamil, French, etc.).
  - **Cast or Crew** name.
- 🎥 **Top 250 Movies** displayed when no search query is provided.
- 📜 Links to **Wikipedia** pages for movie details.
- 💻 Simple and interactive web interface built with **Streamlit**.

## 🚀 Demo

You can try a live demo of the application to search and filter movies:

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20App-ff4b4b?style=flat&logo=streamlit)](https://movierecommendationandsearch.streamlit.app)

## 🛠️ Installation

To run this application locally, follow these steps:

### Prerequisites

Make sure you have the following installed:

- **Python 3.8 or higher**

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/movie-recommendation-search.git
    cd movie-recommendation-search
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS and Linux
    venv\Scripts\activate     # For Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

5. Open the application in your browser:

    ```
    http://localhost:8501
    ```

## 📝 Usage

1. Open the app in your browser.
2. 🔍 **Enter a movie title** in the search bar.
3. 🎛️ Apply filters such as **Rating**, **Release Year**, **Genre**, **Country**, **Language**, or **Cast/Crew**.
4. Click **Submit** to see the results.
5. Click on the movie title to visit its **Wikipedia** page.
6. If no search query is provided, the app displays the **IMDb Top 250 Movies**.

## 🧰 Technologies Used

- **🖥️ Streamlit** - For building the web application interface.
- **🎬 IMDb Cinemagoer** - For fetching movie data from IMDb.
- **🔢 Python** - For the application backend.

## 🙏 Acknowledgments

This project uses the **IMDb Cinemagoer** library for accessing movie data.

## 🤝 Connect with Me

- [![YouTube](https://img.shields.io/badge/YouTube-Channel-red?style=flat&logo=youtube)](https://www.youtube.com/@agilamlabs)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/gn-raavanan)

## Thank You
