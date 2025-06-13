# 🎬 Movie Recommendation App

Hey there! 👋  
This is a simple and fun Movie Recommender System I built using Python and Streamlit. Just select a movie from the dropdown, and it’ll show you 5 similar movies along with their posters.

##  How it Works

- I used a pre-processed dataset of movies.
- The app loads a similarity matrix to find and suggest movies that are similar to the one you choose.
- Movie posters are fetched using TMDB API.
- The app is deployed on **Streamlit Cloud**, so you can access it from anywhere!

## 🔗 Live Demo

Click here to try the app --> (https://movierecommendation-8abagj3ztbbumaknpkfra5.streamlit.app/)

## 🛠 Tech Stack

- Python 
- Pandas & NumPy
- Streamlit
- TMDB API for posters
- Google Drive (via `gdown`) for loading large `.pkl` files

## How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/your-username/movie_recommendation.git
cd movie_recommendation
