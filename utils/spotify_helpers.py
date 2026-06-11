"""
Helper functions for authenticating with Spotify and fetching artist/album data.
"""
from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1"

def get_token():
    """
    Obtain a Spotify API access token via the Client Credentials flow.

    Returns:
        The access token string, or None if authentication fails.
    """
    auth = (CLIENT_ID, CLIENT_SECRET)
    data = {"grant_type": "client_credentials"}

    response = requests.post(AUTH_URL, auth=auth, data=data)

    if response.status_code != 200:
        return None

    data = response.json()

    token = data["access_token"]

    return token

def get_artist_data(artist):
    """
    Fetch an artist's profile and album list from the Spotify API.

    Searches for the top matching artist by name, then retrieves their albums.

    Args:
        artist: The artist name to search for (e.g. "Taylor Swift").

    Returns:
        A dict with keys Name, Image, Spotify URL, and Albums (list of dicts
        with Name and Image), or None if any request fails.
    """
    token = get_token()

    headers = {"Authorization": f"Bearer {token}"}

    params = {
        "q": artist,
        "type": "artist",
        "limit": 1,
        "market": "US",
    }

    response = requests.get(f"{BASE_URL}/search", headers=headers, params=params)

    if response.status_code != 200:
        return None
    
    data = response.json()

    artist_data = data["artists"]["items"][0]
    artist_id = artist_data["id"]
    name = artist_data["name"]
    images = artist_data.get("images", [])
    image = images[0]["url"] if images else None
    spotify_url = artist_data["external_urls"]["spotify"]

    track_params = {"market": "US"}

    response = requests.get(f"{BASE_URL}/artists/{artist_id}/albums", headers=headers, params=track_params)

    if response.status_code != 200:
        return None
    
    data = response.json()

    albums = data["items"]

    albums_list = []

    for album in albums:

        album_images = album.get("images", [])
        albums_list.append({
            "Name": album["name"],
            "Image": album_images[0]["url"] if album_images else None
        })

    return {
        "Name": name,
        "Image": image,
        "Spotify URL": spotify_url,
        "Albums": albums_list
    }

def display_artist(artist):
    """
    Render an artist's photo, Spotify link, and album grid in the Streamlit app.

    Args:
        artist: A dict as returned by get_artist_data.
    """
    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:

        if artist["Image"]:
            st.image(artist["Image"], width=600)
    
    with col2:

        st.markdown(f"### {artist['Name']}")
        st.markdown("*Full artist stats including followers, popularity, and genres are available on Spotify.*")
        st.markdown(f"""
                <a href="{artist['Spotify URL']}" target="_blank" style="
                    background-color: #1DB954;
                    color: #FFFFFF;
                    border-radius: 8px;
                    padding: 10px 20px;
                    text-decoration: none;
                    font-size: 1em;
                ">🎵 Open on Spotify</a>
            """, unsafe_allow_html=True
        )

    st.markdown("### Albums")
    albums = artist["Albums"]

    for i in range(0, len(albums), 4):
        cols = st.columns(4)
        for col, album in zip(cols, albums[i:i+4]):
            with col:
                if album["Image"]:
                    st.image(album["Image"], width=600)
                st.caption(album["Name"])

