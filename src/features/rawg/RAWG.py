"""
RAWG page — lets users search for video games and displays top-rated games on load.
"""
import streamlit as st
from utils.style import load_css
from utils.rawg_helpers import (
    display_game_results,
    display_top_rated,
    get_game_summary,
    get_top_rated_games,

)


st.set_page_config(
    page_title="RAWG API",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

st.markdown(
    """
    # RAWG API
    This RAWG page is allowing the user to search for a specific video game to access
    certain information about the game like Rating, Genre, Platforms and more.
    """
)

query = st.text_input(
    "Search for a game",
    width=200,
    )

if st.button("Search Game Information"):

    with st.spinner("Searching..."):

        game_summary = get_game_summary(query)

        if game_summary is None:
            st.error("There is an issue pulling that game data")
        
        else:
            display_game_results(game_summary)

st.markdown("### Top Rated Games")
top_rated = get_top_rated_games()

if top_rated:
    display_top_rated(top_rated)
