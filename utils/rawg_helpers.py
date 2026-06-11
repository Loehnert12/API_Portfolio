"""
Helper functions for searching games and fetching top-rated games via the RAWG API.
"""
from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")
BASE_URL = "https://api.rawg.io/api"

def get_game_summary(query):
    """
    Search the RAWG API for games matching a query string.

    Args:
        query: The search term (e.g. a game title or keyword).

    Returns:
        A list of dicts, each containing Name, Released, Rating, Metacritic,
        Playtime, ESRB Rating, Background Image, Genre, and Platforms,
        or None if the request fails.
    """
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
    """
    Fetch the top 10 highest-rated games from the RAWG API.

    Returns:
        A list of dicts, each containing Name, Rating, and Background Image,
        or None if the request fails.
    """
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
    """
    Render a list of game search results as side-by-side image/detail cards in the Streamlit app.

    Args:
        games: A list of dicts as returned by get_game_summary.
    """
    for game in games:

        st.divider()

        col1, col2 = st.columns([1, 2])

        with col1:
            if game["Background Image"]:
                st.image(game["Background Image"], width=300)

        with col2:
            
            st.markdown(f"### {game['Name']}")
            st.markdown(f"⭐ **Rating:** {game['Rating']}")
            st.markdown(f"🎮 **Genres:** {game['Genre']}")
            st.markdown(f"🖥️ **Platforms:** {game['Platforms']}")
            st.markdown(f"⏱️ **Playtime:** {game['Playtime']}")
            st.markdown(f"📊 **Metacritic:** {game['Metacritic']}")
            st.markdown(f"🔞 **ESRB Rating:** {game['ESRB Rating']}")

def display_top_rated(games):
    """
    Render the top-rated games as a two-row grid of cover images with captions in the Streamlit app.

    Args:
        games: A list of dicts as returned by get_top_rated_games (expects at least 10 items).
    """
    st.divider()

    row1 = st.columns(5)

    for col, game in zip(row1, games[:5]):
        with col:
            if game["Background Image"]:
                st.image(game["Background Image"], width=300)
            st.caption(game["Name"])

    row2 = st.columns(5)
    
    for col, game in zip(row2, games[5:]):
        with col:
            if game["Background Image"]:
                st.image(game["Background Image"], width=300)
            st.caption(game["Name"])
