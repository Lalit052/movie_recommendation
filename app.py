import streamlit as st
import pandas as pd
import pickle
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)), reverse=True,key=lambda x:x[1])[1:6]

    recommended=[]
    recommended_movie_poster=[]

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended,recommended_movie_poster



movies_dict=pickle.load(open("movie_dict.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
select_movie_name=st.selectbox(
    'Enter The Movie Name To Search',
movies['title'].values)
if st.button("Recommend"):
    names,posters=recommend(select_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0],width=120)
    with col2:
        st.text(names[1])
        st.image(posters[1],width=120)
    with col3:
        st.text(names[2])
        st.image(posters[2],width=120)
    with col4:
        st.text(names[3])
        st.image(posters[3],width=120)
    with col5:
        st.text(names[4])
        st.image(posters[4],width=120)

