import streamlit as st

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