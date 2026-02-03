"""
Entry point for running the Eco-Train Streamlit app.
Author: Vedant Rajhans

You can launch the app with:
    streamlit run main.py

This file simply imports `app.py`, which builds the Streamlit UI.
"""

try:
    # Importing app.py executes its top-level Streamlit code and renders the UI.
    import app  # noqa: F401
except ImportError as e:
    import streamlit as st
    st.error(f"Failed to import app module: {e}")
    st.exception(e)
except Exception as e:
    import streamlit as st
    st.error(f"An error occurred: {e}")
    st.exception(e)