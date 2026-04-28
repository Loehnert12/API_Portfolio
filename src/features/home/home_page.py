import streamlit as st
from utils.style import load_css

load_css()

col1, col2 = st.columns([1, 3])

with col1:
    st.image("src/assets/images/profile.jpg", width=300)

with col2:
    st.markdown(
        """
        ## Daniel Loehnert API Portfolio
        ### Data Analyst | Full-Stack Data Dev
        A collection of 5 Python-powered API integrations built to demonstrate real-world data fetching, processing, and visualization skills.
        """
    )

st.divider()

st.markdown(
    """
    ### About This Project
    I built this app as part of my journey transitioning from Data Analyst to a more developer-focused role.
    Each page connects to a real-world API, handles live data, and presents it through an interactive Streamlit interface.
    The goal was to sharpen my Python skills while building something that reflects both my technical and creative interests.
    """
)

st.divider()
st.markdown("### Explore the Apps")

row1 = st.columns(3)
row2 = st.columns(3)

with row1[0]:
    st.markdown(
        """
        <div class="card">
        <h4> 🌤️ Weather</h4>
        <p>Enter a city and state to get live current weather conditions.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row1[1]:
    st.markdown(
        """
        <div class="card">
        <h4> 🚀 NASA</h4>
        <p>Pick any date and view NASA's Astronomy Picture of the Day with its full description.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row1[2]:
    st.markdown(
        """
        <div class="card">
        <h4> 🎮 RAWG</h4>
        <p>Search any video game by name and pull up detailed information from the RAWG database.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row2[0]:
    st.markdown(
        """
        <div class="card">
        <h4> 🎵 Spotify</h4>
        <p>Search any artist and explore their stats and discography pulled live from Spotify.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row2[1]:
    st.markdown(
        """
        <div class="card">
        <h4> 🔴 Pokémon</h4>
        <p>Look up any Pokémon by name and view their base stats displayed as a bar chart.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("### Tech Stack")

st.markdown(
    """
    <span class="badge">Python</span>
    <span class="badge">Streamlit</span>
    <span class="badge">OpenWeather API</span>
    <span class="badge">NASA API</span>
    <span class="badge">RAWG API</span>
    <span class="badge">Spotify API</span>
    <span class="badge">Poké API</span>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    """
    <a href="https://github.com/Loehnert12" target="_blank" style="
        background-color: #121212;
        color: #FFFFFF;
        border: 1px solid #4482C7;
        border-radius: 8px;
        padding: 10px 20px;
        text-decoration: none;
        font-size: 1em;
    ">
    View My GitHub</a>
    """,
    unsafe_allow_html=True
)
