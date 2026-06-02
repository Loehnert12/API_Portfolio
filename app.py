import streamlit as st

"""
Entry point for the API Streamlit Portfolio app.

Configures the Streamlit page and sets up multi-page navigation across
the Home, Weather, NASA, RAWG, Spotify, and Pokemon feature pages.
"""
st.set_page_config(
    page_title="API Streamlit Portfolio",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation([
    st.Page("src/features/home/home_page.py", title="Home", icon="🏠"),
    st.Page("src/features/weather/Weather.py", title="Weather", icon="🌤️"),
    st.Page("src/features/nasa/NASA.py", title="NASA", icon="🚀"),
    st.Page("src/features/rawg/RAWG.py", title="RAWG", icon="🎮"),
    st.Page("src/features/spotify/Spotify.py", title="Spotify", icon="🎵"),
    st.Page("src/features/pokemon/Pokemon.py", title="Pokemon", icon="🔴"),
])
pg.run()
