import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm

# Path to the data directory
data_dir = Path("delay2")
files = list(data_dir.glob("*.csv"))
df = pd.DataFrame()

for file in tqdm(files):
    new_df = pd.read_csv(file)
    new_df["train_number"] = file.stem
    df = df.append(new_df, ignore_index=True)

df.to_csv("delay2.csv", index=False)
