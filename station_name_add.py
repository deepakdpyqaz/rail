import pandas as pd
analysis = pd.read_csv("railway/data/analysis.csv")
geo = pd.read_csv("railway/data/geo.csv")

analysis = analysis.merge(geo[["code","name"]], left_on="station_code", right_on="code", how="left")
station = analysis["name"]
analysis.drop(["code","name"], axis=1, inplace=True)
analysis["station"] = station
analysis.to_csv("railway/data/full_data.csv", index=False)