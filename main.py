
import streamlit as st
import pickle
import pandas as pd
import requests

def moviePoster(movie_id):
    result = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b9efca9e78583692b107af1d77f7b528&language=en-US'.format(movie_id))
    data = result.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(moviePoster(movie_id))
    return recommended_movies,recommended_movie_posters





movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movieName = st.selectbox(
'Enter movies',
movies['title'].values)

if st.button('Recommend'):
    movie_name, movie_poster = recommend(selected_movieName)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1 :
        # title = <p style = "font-family : Courier; font-size:20px;">movie_name[0]</p>
        st.markdown(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.markdown(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.markdown(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.markdown(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.markdown(movie_name[4])
        st.image(movie_poster[4])



