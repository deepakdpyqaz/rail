import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import pandas as pd
import json
from multiprocessing import Pool
import os

with open("train.json") as f:
    data = json.load(f)

df = pd.DataFrame(data["trains"])


def getAllData(soup):
    stations = soup.find_all("a", class_="runStatStn")
    station_list = []
    delay_list = []
    for i in range(len(stations)):
        station = re.split(r"\s{2,}", stations[i].text.strip())
        station_list.append(station[0])
        delay_list.append(re.search(r"\d+", station[1]).group())
    return {"station": station_list, "delay": delay_list}


def getTrainData(train_number):
    try:
        r = requests.get("https://etrain.info/train/" + train_number + "/history")
        if r.status_code != 200:
            return pd.DataFrame()
        urls = {
            "week": r.url + "?d=1w",
            "month": r.url + "?d=1m",
            "month_3": r.url + "?d=3m",
            "month_6": r.url + "?d=6m",
            "year": r.url + "?d=1y",
        }
        data = {"station": []}
        for day, url in urls.items():
            x = requests.get(url)
            soup = BeautifulSoup(x.content, "html.parser")
            op = getAllData(soup)
            if data["station"] == []:
                data["station"] = op["station"]
            data[day] = op["delay"]

        df = pd.DataFrame(data)
        return df
    except:
        return pd.DataFrame()


def save_to_file(train_number):
    new_df = getTrainData(train_number)
    if new_df.shape[0] > 0:
        new_df.to_csv("delay2/" + train_number + ".csv", index=False)
        print(f"Done {len(os.listdir('delay2/'))}")
    else:
        print(train_number)


if __name__ == "__main__":
    p = Pool(10)
    print(f"Total {len(df['number'])}")
    p.map(save_to_file, df["number"])
