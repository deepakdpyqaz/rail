import pandas as pd
import streamlit as st
import altair as alt

import streamlit as st  
import pandas as pd
import altair as alt
from utils import read_csv

# Read the CSV file
df = read_csv('data/full_data.csv')

st.header('Station Analysis')

# Add multiselect to select stations
station_options = df['station'].unique()
selected_stations = st.multiselect('Select Stations', station_options)

# Filter data by selected stations
filtered_data = df[df['station'].isin(selected_stations)]

# Display data visualization
st.subheader('Data Visualization')
st.bar_chart(filtered_data.groupby('station')['distance'].mean())



# # Calculate the number of unique trains for each station
unique_trains_per_station = df.groupby('station')['train_number'].nunique().reset_index()
unique_trains_per_station = unique_trains_per_station.sort_values('train_number', ascending=False)

# # Display the top 10 busiest train stations
st.write('Top 10 busiest train stations:')
st.table(unique_trains_per_station.head(10))

# Display a bar chart showing the number of unique trains for each station
bar_chart = alt.Chart(unique_trains_per_station).mark_bar().encode(
    x=alt.X('station', sort='-y'),
    y='train_number',
    color=alt.Color('train_number', scale=alt.Scale(scheme='reds')),
    tooltip=['station', 'train_number']
).properties(
    width=800,
    height=400,
    title='Number of Trains per Station'
)
st.write(bar_chart)


st.header('Station Delay Analysis')

# Compute average delay per station
avg_delays = df.groupby('station')['station_delay_level'].mean().reset_index()

# Create chart using Altair
chart = alt.Chart(avg_delays).mark_bar().encode(
    x=alt.X('station', sort='-y'),
    y='station_delay_level',
    tooltip=['station', 'station_delay_level']
).properties(
    width=800,
    height=500,
    title='Average Delay by Station'
)

# Display chart
st.altair_chart(chart, use_container_width=True)
