import streamlit as st
import pandas as pd
import altair as alt


def Train_Number(df):
    st.header("Train Number Analysis")

    # Add dropdown to select train number
    train_number_options = df["number"].unique()
    selected_train_number = st.selectbox("Select a Train Number", train_number_options)

    # Filter data by selected train number
    filtered_data = df[df["number"] == selected_train_number]

    # Display data summary
    st.subheader("Data Summary")
    st.write(filtered_data.describe())

    # Display data visualization
    st.subheader("Data Visualization")
    st.line_chart(filtered_data[["arrival", "departure"]].reset_index(drop=True))

    # Create a bar chart showing the number of trains in each zone
    chart_data = df.groupby("zone")["number"].count().reset_index()
    chart = (
        alt.Chart(chart_data)
        .mark_bar()
        .encode(x="zone", y="number")
        .properties(width=600, height=400)
    )

    # Display the chart in Streamlit
    st.altair_chart(chart)
