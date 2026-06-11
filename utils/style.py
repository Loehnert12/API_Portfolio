"""
Custom CSS loader for the API Portfolio Streamlit app.
"""
import streamlit as st

def load_css():
    """
    Inject custom CSS into the Streamlit app (Oxanium font, card/badge styles, heading colours).
    """
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Oxanium&display=swap');

        * {
            font-family: 'Oxanium', sans-serif;
        }
        
        [data-testid="stSidebarContent"] {
            display: flex;
            flex-direction: column;
        }
        
        [data-testid="stMarkdownContainer"] hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #4482C7, transparent);
            margin: 20px 0;
        }

        .card {
            background-color: #262525;
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #4482C7;
            margin-top: 20px;
        }
                
        .badge {
            background-color: #4482C7;
            color: #FFFFFF;
            border-radius: 20px;   
            padding: 5px 12px;
            margin: 4px;
            display: inline-block;
            font-size: 0.85em;
        }
        
        h1 {
            color: #4482C7;
            text-align: center;
        }
        
        h2 {
            color: #4482C7;
        }
    </style>
    """, unsafe_allow_html=True)