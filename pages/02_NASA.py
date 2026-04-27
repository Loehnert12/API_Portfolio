import streamlit as st
import datetime
from utils.style import load_css

from utils.nasa_helpers import (
    display_apod,
    get_apod_by_date,
)


st.set_page_config(
    page_title="NASA API",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

st.markdown(
    """
    # NASA API
    This NASA page is calling the API to display either an image or video of what
    the image/video of the day was for the specified date that the user selects
    from the box below. The image of the day is already generated below.Select a
    different date below to see what image/video was posted.
    """
)

selected_date = st.date_input(
    "Select a Date",
    value=datetime.date.today(),
    min_value=datetime.date(1995, 6, 16),
    max_value=datetime.date.today(),
    width=200,
    )

if st.button("Generate Content"):

    with st.spinner("Loading content..."):

        apod = get_apod_by_date(selected_date)
        
        if apod is None:

            st.error("No data found for this date. Please try another date.")
        
        else:
            display_apod(apod)
