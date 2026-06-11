"""
Spotify page — lets users search for an artist and view their profile and album discography.
"""
import streamlit as st
from utils.style import load_css
from utils.spotify_helpers import (
    display_artist,
    get_artist_data,
)


st.set_page_config(
    page_title="Spotify API",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

st.markdown(
    """
    # Spotify API
    This Spotify API page allows the user to search for a specific artist and get certain information
    about that artist. Search for your favorite artist and see what their top 5 albums are along with
    a handy link that takes you right to their Spotify page.
    """
)

query = st.text_input(
    "Search for an artist",
    value="Taylor Swift",
    width=200,
    )

if st.button("Search Artist Information"):

    with st.spinner("Searching..."):

        artist_summary = get_artist_data(query)

        if artist_summary is None:
            st.error("There is an issue pulling that artist data")
        
        else:
            display_artist(artist_summary)