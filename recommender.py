import pickle

movies = pickle.load(open('data/movies.pkl', 'rb'))
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies