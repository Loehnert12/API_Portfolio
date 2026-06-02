"""Helper functions for geocoding locations and fetching current weather from Open-Meteo."""
import requests
import streamlit as st

# Tampa's Coordinates:
# Latitude: 27.9506
# Longitude: -82.4572

BASE_URL = "https://api.open-meteo.com/v1/forecast"

####################
# GET
####################

STATE_ABBREVIATIONS = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming"
}

def get_coordinates(name):
    """Geocode a city/state string to latitude, longitude, and a display name.

    Accepts input in the format "City, ST" (e.g. "Tampa, FL"). When a state
    abbreviation is provided it is expanded to a full name for matching.

    Args:
        name: A location string, optionally including a comma-separated state abbreviation.

    Returns:
        A tuple of (latitude, longitude, display_name), or None if the location is not found.
    """
    URL = "https://geocoding-api.open-meteo.com/v1/search"

    parts = name.split(",")
    city = parts[0].strip()
    state = parts[1].strip().strip(".") if len(parts) > 1 else None

    params = {
        "name": city
    }

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        return None
    
    data = response.json()

    results = data["results"]

    if "results" not in data or len(data["results"]) == 0:
        return None
    
    
    if state:
        state_full = STATE_ABBREVIATIONS.get(state.upper(), state)
        for result in results:
            if state_full.lower() in result.get("admin1", "").lower():
                return (result["latitude"], result["longitude"], f"{result['name']}, {result['admin1']}")

    return (results[0]["latitude"], results[0]["longitude"], f"{results[0]['name']}, {results[0].get('admin1', '')}")

def get_weather_summary(latitude, longitude):
    """Fetch current weather conditions for a location from the Open-Meteo API.

    Returns data in Fahrenheit and mph. Timezone is fixed to America/New_York.

    Args:
        latitude: The location's latitude as a float.
        longitude: The location's longitude as a float.

    Returns:
        A dict with string-formatted values for Temperature, Wind Speed, Wind Gusts,
        Rain, Relative Humidity, and Apparent Temperature, or None if the request fails.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "rain",
            "wind_speed_10m",
            "wind_gusts_10m",
            "wind_direction_10m",
            "relative_humidity_2m",
            "apparent_temperature"
            ],
        "timezone": "America/New_York",
        "past_days": 0,
	    "forecast_days": 1,
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None
    
    data = response.json()

    temperature = data["current"]["temperature_2m"]
    wind_speed = data["current"]["wind_speed_10m"]
    wind_gusts = data["current"]["wind_gusts_10m"]
    rain = data["current"]["rain"]
    relative_humidity = data["current"]["relative_humidity_2m"]
    apparent_temperature = data["current"]["apparent_temperature"]


    return {
        "Temperature": f"{temperature}°F",
        "Wind Speed": f"{wind_speed} mph",
        "Wind Gusts": f"{wind_gusts} mph",
        "Rain": f"{rain} mm",
        "Relative Humidity": f"{relative_humidity}%",
        "Apparent Temperature": f"{apparent_temperature}°F",
    }

def final_weather_summary(weather, city_name):
    """Render current weather conditions as a 2-row grid of metric cards in the Streamlit app.

    Args:
        weather: A dict as returned by get_weather_summary.
        city_name: The display name for the city shown in the section heading.
    """
    st.markdown(f"### Current Weather for {city_name}")

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    col1.metric("Temperature", value=weather["Temperature"])
    col2.metric("Feels Like", value=weather["Apparent Temperature"])
    col3.metric("Humidity", value=weather["Relative Humidity"])
    col4.metric("Wind Speed", value=weather["Wind Speed"])
    col5.metric("Wind Gusts", value=weather["Wind Gusts"])
    col6.metric("Rain", value=weather["Rain"])
