"""
Pokémon page — allows users to search any Pokémon and view its stats and sprite.
"""
import streamlit as st
from utils.style import load_css
from utils.pokemon_helpers import (
    display_pokemon,
    get_pokemon_summary,
)


st.set_page_config(
    page_title="Pokémon API",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

st.markdown(
    """
    # Pokemon API
    This Pokemon API page allows the user to search for a specific pokemon and see
    the different stats. This can be helpful when learning about new pokemon and
    planning out how you can best use them in a fight.
    """
)

query = st.text_input(
    "Search for a pokemon",
    value="charizard",
    width=200
    )

if st.button("Search Pokemon"):

    with st.spinner("Searching..."):

        pokemon_summary = get_pokemon_summary(query)

        if pokemon_summary is None:
            st.error("There is an issue pulling that pokemon data")
        
        else:
            display_pokemon(pokemon_summary)