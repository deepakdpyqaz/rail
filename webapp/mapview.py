import folium
from streamlit_folium import st_folium, folium_static
import pandas as pd

df = pd.read_csv("geo.csv")


def MapView():
    m = folium.Map(
        location=[df.latitude.mean(), df.longitude.mean()],
        zoom_start=5,
        control_scale=True,
    )
    for i, row in df.iterrows():
        # Setup the content of the popup
        iframe = folium.IFrame(f'{row["name"]} ({row["code"]})')

        # Initialise the popup using the iframe
        popup = folium.Popup(iframe, min_width=300, max_width=300)

        # Add each row to the map
        folium.Marker(
            location=[row["latitude"], row["longitude"]], popup=popup, c=row["name"]
        ).add_to(m)

    st_data = folium_static(m, width=700)
    # show m on streamlit
    # st_data.add_child(folium.LatLngPopup())
