import streamlit as st
import pandas as pd
import numpy as np


RELEASES_URL = "https://api.github.com/repos/ibis-project/ibis/releases"


@st.cache_data
def load_data():
    data = pd.read_json(RELEASES_URL)
    return data


st.title("Ibis Project Releases Dashboard")
data = load_data()
st.subheader("Releases")
st.write(data)
