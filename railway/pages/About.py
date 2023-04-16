import streamlit as st
import base64
from utils import get_img_as_base64

# Set up the page layout
st.set_page_config(page_title="Services", page_icon=":train:", layout="wide")


delay = get_img_as_base64("img/1.png")
stats = get_img_as_base64("img/5.jpg")

# Define the information for each service
delay_prediction_info = """
Predict the delay of a train by entering its number and departure time. Our algorithm uses historical data to provide an accurate prediction.
"""

station_statistics_info = """
View statistics for a particular train station, such as the number of trains arriving and departing, the busiest times of day, and more.
"""

st.header("Features")
st.write("")
st.write("")

# Define the layout of the page
col1, col2 = st.columns(2)

# Add the services to each column
with col1:
    st.write(delay_prediction_info)
    st.markdown(
        f'<img src="data:image/png;base64,{delay}" style="width:80%;">',
        unsafe_allow_html=True,
    )

with col2:
    st.write(station_statistics_info)
    st.markdown(
        f'<img src="data:image/png;base64,{stats}" style="width:100%;">',
        unsafe_allow_html=True,
    )
