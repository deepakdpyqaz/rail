import numpy as np
import pandas as pd
import json
from pathlib import Path
from tqdm import tqdm

trains = list(Path("trains2").glob("*.json"))

geo = {"code": [], "name": [], "latitude": [], "longitude": []}
for train in tqdm(trains):
    with open(train, "r") as f:
        data = json.load(f)
    try:
        for station_data in data["response"]["station_data"]:
            for station in station_data["values"]:
                code = station["station"]["code"]
                latitude = station["station"]["latitude"]
                longitude = station["station"]["longitude"]
                name = station["station"]["name"]
                geo["code"].append(code)
                geo["latitude"].append(latitude)
                geo["longitude"].append(longitude)
                geo["name"].append(name)
    except:
        pass
df = pd.DataFrame(geo)
# Remove duplicates
df = df.drop_duplicates(subset="code", keep="first")
df.to_csv("geo2.csv", index=False)
