import streamlit as st
import pandas as pd
import altair as alt
from Overview import Overview
from TrainNumber import Train_Number
from visulization import Visualization
from station import Station
from predict import predict_duration
from realtime import Realtimedata
from mapview import MapView

# Load data
df = pd.read_csv("data.csv")

# Set app title
st.title("Railway Data Analysis Dashboard")

st.set_option("deprecation.showPyplotGlobalUse", False)

# Add sidebar to select analysis type
st.sidebar.title("Select an Analysis Type")
analysis_type = st.sidebar.radio(
    "",
    [
        "Overview",
        "Train Number",
        "Station",
        "Visual Analysis",
        "Predict Duration of Train Journey",
        "Real time data",
        "Map View",
    ],
)

# If the user selects the 'Predict Duration of Train Journey' task, display the model
if analysis_type == "Predict Duration of Train Journey":
    st.sidebar.title("Predict the Duration of a Train Journey")
    distance = st.sidebar.number_input("Distance (in km)")
    train_type = st.sidebar.selectbox(label="Train Type", options=df["type"].unique())
    predict_button = st.sidebar.button("Predict")
    if predict_button:
        prediction = predict_duration(distance, train_type)
        st.sidebar.write("Predicted duration of journey: %.2f hours" % prediction)

# If the user selects any other task, display the appropriate analysis
else:
    st.sidebar.title("Select an analysis")
    if analysis_type == "Overview":
        st.sidebar.write("Displaying overview analysis")
        Overview(df)
    elif analysis_type == "Train Number":
        st.sidebar.write("Displaying train number analysis")
        Train_Number(df)
    elif analysis_type == "Station":
        st.sidebar.write("Displaying station analysis")
        Station(df)
    elif analysis_type == "Visual Analysis":
        st.sidebar.write("Displaying visual analysis")
        Visualization(df)
    elif analysis_type == "Real time data":
        st.sidebar.write("Displaying real time data")
        Realtimedata(df)
    elif analysis_type == "Map View":
        st.sidebar.write("Displaying map view")
        MapView()
