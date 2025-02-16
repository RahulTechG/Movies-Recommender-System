import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

new_df=pickle.load(open("new_df.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

def featch_poster(movie_id):

    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ef288f8808f394143c3bd2fcd89e17ff&language=en-US".format(movie_id))

    data=response.json()
    
    return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommand(movie):


    recommended_movies=[]
    recommended_movies_path=[]

    movie_index=new_df[new_df["title_x"]==movie.lower()].index[0]

    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movies_list:

        movie_id=new_df.iloc[i[0]].movie_id
        
        
        recommended_movies.append((new_df.iloc[i[0]].title_x))

        # featching the poster

        recommended_movies_path.append(featch_poster(movie_id))

    return recommended_movies,recommended_movies_path



new_df_values=new_df["title_x"].values

st.title("Movies Recommender System")

selected_movie_name=st.selectbox("How would you like to choose",new_df_values)

if st.button("Recommend"):

    
    
    recommended_movie_names,recommended_movie_posters = recommand(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
            
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:

        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
    with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
    with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
