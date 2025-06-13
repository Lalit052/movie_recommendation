import streamlit as st
import pandas as pd
import pickle
import requests
import os
import gdown

# Download the pickle files if not already downloaded
if not os.path.exists("movie_dict.pkl"):
    url = "https://drive.google.com/uc?id=1qbNl4GpA3DsfxRmQOekG6owRkVW22OVS"
    gdown.download(url, "movie_dict.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1qaWFXWnD5eZzeBTWhORuZvpeUlzGME1b"
    gdown.download(url, "similarity.pkl", quiet=False)

# ✅ Load the pickles AFTER they're guaranteed to exist
with open("movie_dict.pkl", "rb") as f:
    movies_dict = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies_dict)

def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    recommended_movie_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended, recommended_movie_poster

# Streamlit UI
st.title('Movie Recommender System')

select_movie_name = st.selectbox(
    'Enter The Movie Name To Search',
    movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(select_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i], width=120)
