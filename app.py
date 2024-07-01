import streamlit as st
import pickle


st.markdown(
    """
    <style>
    .stApp{
        background: linear-gradient( #F5F7FA , #A3D5FF, #FFC3A0) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(enumerate(how_much_similar[index]), reverse=True, key=lambda x: x[1])
    recommended=[]
    for i in distance[1:6]:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

how_much_similar=pickle.load(open('similarity.pkl','rb'))

movies = pickle.load(open('movies.pkl','rb'))
movie_list=movies['title'].values

st.title("Movie Recommendation System")
selected_movie = st.selectbox(
    "How would you like to be contacted?",
    (movie_list))

st.write("You selected:", selected_movie)
if st.button("Recommend", type="primary"):
   suggested=recommend(selected_movie)
   for i in suggested:
      st.write(i)