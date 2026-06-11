"""
Weather page — geocodes a user-entered city and displays current weather conditions.
"""
import streamlit as st
from utils.style import load_css
from utils.weather_helpers import (
    final_weather_summary,
    get_coordinates,
    get_weather_summary,
)


st.set_page_config(
    page_title="Weather API",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

st.markdown(
    """
    # Weather API
    This weather page demonstrates how I am utilizing the API call to pull together
    a summary of the current weather in a city that you choose. Fill out the city name
    in the block below and click the button "Current Weather Summary" to see the:
    - Temperature
    - Wind Speed
    - Wind Gusts
    - Rain
    - Relative Humidity
    - Apparent Temperature
    """
)

city = st.text_input(
    "Enter a city name to get the current weather",
    value="Tampa, FL",
    width=200,
    )

if st.button("Current Weather Summary"):
    coordinates = get_coordinates(city.strip())

    if coordinates is None:
        st.error("City not found. Please try again.")

    else:
        lat, lon, city_name = coordinates
        weather = get_weather_summary(lat, lon)

        if weather is None:
            st.error("Could not retrieve weather data. Please try again.")

        else:
            final_weather_summary(weather, city_name)