# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
# import re
# URL = "https://www.google.com/search"
# exp = re.compile(r"(\d+\.\d+)")
# session = HTMLSession()

# def get_google(station_code):
#     r = session.get(URL, params={"q": f"{station_code} railway station latitude and longitude"})
#     soup = BeautifulSoup(r.html.html, "html.parser")
#     return re.findall(exp, soup.find("div",class_="Z0LcW t2b5Cf").text)

import pandas as pd

df = pd.read_csv("analysis2.csv")
import json

with open("train.json", "r") as f:
    tn = json.load(f)
train = pd.DataFrame(tn["trains"])
train["number"] = pd.to_numeric(train["number"])
print(df.dtypes)
analysis = pd.merge(df, train, left_on="train_number", right_on="number", how="left")
print(analysis[["train_number", "name"]].head())
b = analysis[["train_number", "name"]].drop_duplicates()
b.to_csv("railway/data/train.csv", index=False)
