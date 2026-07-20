import pandas as pd
import streamlit as st


@st.cache_data
def load_data(filepath):
    """
    Load the restaurant dataset.
    """

    df = pd.read_csv(filepath)

    return df