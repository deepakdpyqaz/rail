import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("Railway Data Analysis Dashboard")

# Display the dataframe
st.write(df)

# Create interactive filters
st.sidebar.title("Filters")
from_station = st.sidebar.multiselect("From Station", df["from_station_name"].unique())
to_station = st.sidebar.multiselect("To Station", df["to_station_name"].unique())
train_type = st.sidebar.selectbox("Train Type", df["type"].unique())

# Apply the filters to the dataframe
filtered_df = df[
    (df["from_station_name"].isin(from_station))
    & (df["to_station_name"].isin(to_station))
    & (df["type"] == train_type)
]

# Display the filtered dataframe
st.write(filtered_df)

# Add data visualizations
st.subheader("Data Visualizations")
st.bar_chart(df.groupby("type")["distance"].sum())
