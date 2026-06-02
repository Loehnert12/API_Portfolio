"""Helper functions for fetching Pokémon data from PokéAPI and rendering it in Streamlit."""
import pandas as pd
import plotly.express as px
import requests
import streamlit as st

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_summary(name):
    """Fetch summary data for a Pokémon by name or ID from the PokéAPI.

    Args:
        name: The Pokémon's name (e.g. "charizard") or numeric ID.

    Returns:
        A dict with keys Name, ID, Height, Weight, Base Experience, Type, Sprite,
        and Stats, or None if the Pokémon is not found.
    """
    response = requests.get(f"{BASE_URL}/pokemon/{name}")

    if response.status_code != 200:
        return None
    
    data = response.json()

    types = ", ".join([t["type"]["name"] for t in data["types"]])

    return{
        "Name": data["name"],
        "ID": data["id"],
        "Height": data["height"],
        "Weight": data["weight"],
        "Base Experience": data.get("base_experience", "N/A"),
        "Type": types,
        "Sprite": data["sprites"]["other"]["official-artwork"]["front_default"] or data["sprites"]["front_default"],
        "Stats": {stat["stat"]["name"].replace("-", " ").title(): stat["base_stat"] for stat in data["stats"]},
    }

def display_pokemon(pokemon):
    """Render a Pokémon's sprite, info, and a horizontal base-stats bar chart in the Streamlit app.

    Args:
        pokemon: A dict as returned by get_pokemon_summary.
    """
    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:
        if pokemon["Sprite"]:
            st.image(pokemon["Sprite"], width=300)

    with col2:
        
        st.markdown(f"### {pokemon['Name']}")
        st.markdown(f"**ID**: {pokemon['ID']}")
        st.markdown(f"**Type**: {pokemon['Type']}")
        st.markdown(f"**Height**: {pokemon['Height']}")
        st.markdown(f"**Weight**: {pokemon['Weight']}")
        st.markdown(f"**Base Experience**: {pokemon['Base Experience']}")


    st.markdown("### Base Stats")
    df = pd.DataFrame.from_dict(
        pokemon["Stats"],
        orient="index",
        columns=["Base Stat"]
    )
    df["Color"] = ["#4482C7", "#E74C3C", "#2ECC71", "#F39C12", "#9B59B6", "#1ABC9C"]
    fig = px.bar(
    df,
    x="Base Stat",
    y=df.index,
    orientation="h",
    text_auto=True,
    color="Color",
    color_discrete_map={c: c for c in df["Color"]}
    )
    fig.update_layout(
        showlegend=False,
        yaxis_title=None,
        xaxis_title="Base Stat Value",
        font=dict(size=20),
        height=500,
        bargap=0,
    )
    fig.update_traces(
        width=0.8,
        textfont_size=16,
        textfont_color="black",
        textfont=dict(size=16, color="black", weight="bold"),
        textposition="inside",
        insidetextanchor="middle",
    )
    st.plotly_chart(fig, use_container_width=True)
