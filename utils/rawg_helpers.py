from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")
BASE_URL = "https://api.rawg.io/api"

def get_game_summary(query):

    params = {
        "search": query,
        "key": API_KEY,
    }

    response = requests.get(f"{BASE_URL}/games", params=params)

    if response.status_code != 200:
        return None
    
    data = response.json()
    games = []
    for game in data["results"]:
        esrb = game.get("esrb_rating") or {}
        games.append({
            "Name": game["name"],
            "Released": game["released"],
            "Rating": game["rating"],
            "Metacritic": game["metacritic"],
            "Playtime": game["playtime"],
            "ESRB Rating": esrb.get("name", "Not Rated"),
            "Background Image": game["background_image"],
            "Genre": ", ".join([g["name"] for g in game.get("genres", [])]),
            "Platforms": ", ".join([p["platform"]["name"] for p in game.get("platforms", [])])
        })
    return games

def get_top_rated_games():

    params = {
        "ordering": "-rating",
        "page_size": 10,
        "key": API_KEY,
    }

    response = requests.get(f"{BASE_URL}/games", params=params)

    if response.status_code != 200:
        return None
    
    data = response.json()

    games = []
    for game in data["results"]:
        games.append({
            "Name": game["name"],
            "Rating": game["rating"],
            "Background Image": game["background_image"]
        })
    return games

def display_game_results(games):
    
    for game in games:

        st.divider()

        col1, col2 = st.columns([1, 2])

        with col1:
            if game["Background Image"]:
                st.image(game["Background Image"], width="content")

        with col2:
            
            st.markdown(f"### {game['Name']}")
            st.markdown(f"⭐ **Rating:** {game['Rating']}")
            st.markdown(f"🎮 **Genres:** {game['Genre']}")
            st.markdown(f"🖥️ **Platforms:** {game['Platforms']}")
            st.markdown(f"⏱️ **Playtime:** {game['Playtime']}")
            st.markdown(f"📊 **Metacritic:** {game['Metacritic']}")
            st.markdown(f"🔞 **ESRB Rating:** {game['ESRB Rating']}")

def display_top_rated(games):
    
    st.divider()

    row1 = st.columns(5)

    for col, game in zip(row1, games[:5]):
        with col:
            if game["Background Image"]:
                st.image(game["Background Image"], width="content")
            st.caption(game["Name"])

    row2 = st.columns(5)
    
    for col, game in zip(row2, games[5:]):
        with col:
            if game["Background Image"]:
                st.image(game["Background Image"], width="content")
            st.caption(game["Name"])
