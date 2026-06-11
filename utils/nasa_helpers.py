"""
Helper functions for fetching and displaying NASA's Astronomy 
Picture of the Day (APOD).
"""
from dotenv import load_dotenv
import os
import requests
import streamlit as st
import time

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")
BASE_URL = "https://api.nasa.gov/planetary/apod"

def get_apod_by_date(date):
    """
    Fetch NASA's Astronomy Picture of the Day for a given date.

    Retries up to 3 times on 503 errors before giving up.

    Args:
        date: A date object or string in YYYY-MM-DD format.

    Returns:
        A dict with keys Title, Date, Copyright, URL, Explanation, and Media Type,
        or None if the request fails.
    """
    date = str(date)

    param = {
        "date": date,
        "api_key": API_KEY
    }

    for attempt in range(3):
        response = requests.get(BASE_URL, params=param)
        if response.status_code == 200:
            break
        elif response.status_code == 503:
            time.sleep(2)
        else:
            return None
    
    if response.status_code != 200:
        return None

    data = response.json()

    title = data["title"]
    date = data["date"]
    copyright = data.get("copyright", "No copyright listed")
    url = data["url"]
    explanation = data["explanation"]
    media_type = data["media_type"]

    return{
        "Title": title,
        "Date": date,
        "Copyright": copyright,
        "URL": url,
        "Explanation": explanation,
        "Media Type": media_type,
    }

def display_apod(apod):
    """
    Render APOD content (image or video) and its metadata in the Streamlit app.

    Args:
        apod: A dict as returned by get_apod_by_date, containing URL, Media Type,
              Title, Date, Copyright, and Explanation.
    """
    _, col2, _ = st.columns([1, 3, 1])

    with col2:

        if apod["Media Type"] == "image":

            st.subheader(apod["Title"])
            st.image(
                image=apod["URL"],
                width=600,
            )

        else:

            st.video(apod["URL"], autoplay=True, muted=False)

    st.markdown(f"""
        <div class="card">
            <p>📅 {apod['Date']} | © {apod['Copyright']}</p>
            <p>{apod["Explanation"]}</p>
        </div>""",
        unsafe_allow_html=True,
    )
