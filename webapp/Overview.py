import streamlit as st
import pandas as pd


def Overview(df):
    st.header("Overview Analysis")

    # Display data summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Display data visualization
    st.subheader("Data Visualization")
    st.line_chart(df.groupby("from_station_name")["number"].count())
