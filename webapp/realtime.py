import streamlit as st
import pandas as pd
import asyncio
import json
import requests
from bs4 import BeautifulSoup
import time


def get_data(train_number):
    URL = (
        f"https://www.goibibo.com/trains/app/trainstatus/results/?train={train_number}"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }
    r = requests.get(URL, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        script = soup.find("script")
        if script:
            data = json.loads(script.text.strip().split("=", 1)[1].strip(";"))
            delay = {"name": [], "delay": []}
            for station_data in data["response"]["station_data"]:
                for station in station_data["values"]:
                    delay["name"].append(station["station"]["name"])
                    delay["delay"].append(station["delay"])
            return pd.DataFrame(delay)
        else:
            return "Train not found"
    else:
        return "Invalid request"


def Realtimedata(df):
    train_number = st.text_input("Enter train number: ")
    placeholder = st.empty()
    if train_number:
        while True:
            with placeholder.container():
                time.sleep(60)
                data = get_data(train_number)
                data["time"] = time.ctime()
                st.dataframe(data)
                st.balloons()
                st.success("Train status updated")
                st.balloons()
