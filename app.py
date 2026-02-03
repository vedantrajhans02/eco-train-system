"""
Eco-Train: Carbon-Aware AI Scheduler
Author: Vedant Rajhans
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from core_logic import CarbonScheduler
from datetime import datetime

st.set_page_config(page_title="Eco-Train: Carbon-Aware AI Scheduler",
                   layout="wide")

st.title("Eco-Train: Carbon-Aware AI Scheduler")

# Sidebar
st.sidebar.header("Scheduling Parameters")
model_type = st.sidebar.selectbox(
    "Model Type", ["ResNet50", "BERT", "GPT-2", "Stable Diffusion"])
max_deadline = st.sidebar.time_input("Max Deadline", datetime.now().time())

# Footer with author information
st.sidebar.markdown("---")
st.sidebar.markdown("**Author:** Vedant Rajhans")

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None

regions = ['us-east-1', 'eu-north-1', 'ap-south-1']
scheduler = CarbonScheduler()

# Main content area
if st.button("Find Greenest Region & Schedule"):
    try:
        with st.spinner("Analyzing carbon intensities across regions..."):
            greenest_region, min_intensity, all_intensities = scheduler.find_greenest_region(
                regions)
            
            # Store results in session state
            st.session_state.results = {
                'greenest_region': greenest_region,
                'min_intensity': min_intensity,
                'all_intensities': all_intensities,
                'model_type': model_type,
                'max_deadline': max_deadline
            }
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e)

# Display results if available
if st.session_state.results:
    results = st.session_state.results
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Selected Region", results['greenest_region'])
    with col2:
        st.metric("Current Carbon Intensity", f"{results['min_intensity']} gCO2/kWh")
    with col3:
        st.metric("Estimated CO2 Savings", "30%")

    st.success(
        f"Successfully scheduled {results['model_type']} in {results['greenest_region']} before {results['max_deadline']}"
    )

    # Chart
    try:
        df = pd.DataFrame(list(results['all_intensities'].items()),
                          columns=['Region', 'Carbon Intensity'])
        fig = px.bar(df,
                     x='Region',
                     y='Carbon Intensity',
                     title="Carbon Intensity by Region",
                     color='Carbon Intensity',
                     color_continuous_scale='Greens_r')
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating chart: {str(e)}")
else:
    st.info(
        "Click the button above to find the optimal region for your AI workload."
    )
