import streamlit as st
import pandas as pd
from recommender import recommend, movies
from utils import fetch_poster, fetch_trailer
from auth import create_user, login_user

st.set_page_config(page_title="Netflix Recommender", layout="wide")

# Sidebar Navigation
menu = ["Home", "Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- AUTH ----------------
if choice == "Signup":
    st.title("Create Account")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Signup"):
        create_user(user, pwd)
        st.success("Account created!")

elif choice == "Login":
    st.title("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        result = login_user(user, pwd)
        if result:
            st.session_state["user"] = user
            st.success("Logged in!")

# ---------------- MAIN APP ----------------
elif choice == "Home":
    st.title("🎬 Netflix Movie Recommender")

    if "user" not in st.session_state:
        st.warning("Please login first")
    else:
        movie_list = movies['title'].values
        selected_movie = st.selectbox("Search Movie", movie_list)

        if st.button("Recommend"):
            recommendations = recommend(selected_movie)

            cols = st.columns(5)
            for i, movie in enumerate(recommendations):
                with cols[i]:
                    st.image(fetch_poster(movie))
                    st.write(movie)
                    st.markdown(f"[▶ Watch Trailer]({fetch_trailer(movie)})")