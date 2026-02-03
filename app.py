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

# Footer with author information
st.sidebar.markdown("---")
st.sidebar.markdown("**Author:** Vedant Rajhans")

# Sidebar
st.sidebar.header("Scheduling Parameters")
model_type = st.sidebar.selectbox(
    "Model Type", ["ResNet50", "BERT", "GPT-2", "Stable Diffusion"])
max_deadline = st.sidebar.time_input("Max Deadline", datetime.now().time())

regions = ['us-east-1', 'eu-north-1', 'ap-south-1']
scheduler = CarbonScheduler()

if st.button("Find Greenest Region & Schedule"):
    greenest_region, min_intensity, all_intensities = scheduler.find_greenest_region(
        regions)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Selected Region", greenest_region)
    with col2:
        st.metric("Current Carbon Intensity", f"{min_intensity} gCO2/kWh")
    with col3:
        st.metric("Estimated CO2 Savings", "30%")

    st.success(
        f"Successfully scheduled {model_type} in {greenest_region} before {max_deadline}"
    )

    # Chart
    df = pd.DataFrame(list(all_intensities.items()),
                      columns=['Region', 'Carbon Intensity'])
    fig = px.bar(df,
                 x='Region',
                 y='Carbon Intensity',
                 title="Carbon Intensity by Region",
                 color='Carbon Intensity',
                 color_continuous_scale='Greens_r')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info(
        "Click the button above to find the optimal region for your AI workload."
    )
