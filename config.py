import os

# For local (.env)
from dotenv import load_dotenv
load_dotenv()

# Try Streamlit secrets first, else fallback to .env
DB_URL = os.getenv("DB_URL")

try:
    import streamlit as st
    if "DB_URL" in st.secrets:
        DB_URL = st.secrets["DB_URL"]
except:
    pass