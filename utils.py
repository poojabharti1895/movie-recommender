import requests
from config import TMDB_API_KEY, YOUTUBE_API_KEY

def fetch_poster(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
    data = requests.get(url).json()
    poster_path = data['results'][0]['poster_path']
    return f"https://image.tmdb.org/t/p/w500{poster_path}"

def fetch_trailer(movie_name):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie_name} trailer&key={YOUTUBE_API_KEY}"
    data = requests.get(url).json()
    video_id = data['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}"