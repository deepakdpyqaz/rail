import streamlit as st
import pandas as pd
import altair as alt


def Station(df):
    st.header("Station Analysis")

    # Add dropdown to select station
    station_options = df["from_station_name"].unique()
    selected_station = st.selectbox("Select a Station", station_options)

    # Filter data by selected station
    filtered_data = df[df["from_station_name"] == selected_station]

    # Display data summary
    st.subheader("Data Summary")
    st.write(filtered_data.describe())

    # Display data visualization
    st.subheader("Data Visualization")
    st.bar_chart(filtered_data.groupby("to_station_name")["distance"].mean())
