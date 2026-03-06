import streamlit as st
import pickle
import pandas as pd
import requests

movies_list=pickle.load(open('pdict.pkl','rb'))
df = pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/ {}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index=df[df['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended = []
    recommended_posters=[]
    for i in movie_list:
        movie_id=df.iloc[i[0]].id
        #fetch poster from api
        recommended.append(df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended,recommended_posters



option = st.selectbox(
    'Which movie do you like best?',df['title'].values)

if st.button('Recommend'):
    names,posters=recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:

        st.image(posters[0])
        st.text(names[0])
    with col2:

        st.image(posters[1])
        st.text(names[1])
    with col3:

        st.image(posters[2])
        st.text(names[2])
    with col4:

        st.image(posters[3])
        st.text(names[3])
    with col5:

        st.image(posters[4])
        st.text(names[4])